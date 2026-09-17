// POST /api/contact — emails the form submission.
// Requires two environment variables in Vercel:
//   RESEND_API_KEY  — from resend.com (free tier is fine)
//   CONTACT_TO      — where the message should land, e.g. marfarooqui@gmail.com
// Until a verified sending domain is set up, "from" must stay onboarding@resend.dev.

import { Resend } from 'resend';

const esc = (s = '') =>
  String(s).slice(0, 4000).replace(/[<>&]/g, (c) => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;' }[c]));

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Use POST.' });
  }

  const { name, email, topic, message, company_website } = req.body || {};

  if (company_website) return res.status(200).json({ ok: true }); // honeypot
  if (!name || !email || !message) {
    return res.status(400).json({ error: 'Name, email, and details are required.' });
  }
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
    return res.status(400).json({ error: 'That email address is not valid.' });
  }

  try {
    const resend = new Resend(process.env.RESEND_API_KEY);
    await resend.emails.send({
      from: 'mofarooqui.com <onboarding@resend.dev>',
      to: process.env.CONTACT_TO,
      replyTo: email,
      subject: `New enquiry — ${esc(topic || 'General')} — ${esc(name)}`,
      html: `
        <h2>New enquiry from mofarooqui.com</h2>
        <p><strong>Name:</strong> ${esc(name)}</p>
        <p><strong>Email:</strong> ${esc(email)}</p>
        <p><strong>Topic:</strong> ${esc(topic || 'Not specified')}</p>
        <p><strong>Details:</strong></p>
        <p>${esc(message).replace(/\n/g, '<br>')}</p>
      `
    });
    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('contact form failed:', err);
    return res.status(500).json({ error: 'Send failed.' });
  }
}
