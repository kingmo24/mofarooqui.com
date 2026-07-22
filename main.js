/* Reveals, active-section nav, year, contact form. */
(function () {
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var items = document.querySelectorAll('.rise');

  if (reduce || !('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -10% 0px' });
    items.forEach(function (el) { io.observe(el); });
    requestAnimationFrame(function () {
      document.querySelectorAll('.hero .rise').forEach(function (el) { el.classList.add('in'); });
    });
  }

  /* --- mobile menu --- */
  var toggle = document.getElementById('nav-toggle');
  var menu = document.getElementById('nav-menu');
  var scrim = document.getElementById('nav-scrim');

  if (toggle && menu) {
    var open = false;

    var setMenu = function (next) {
      open = next;
      toggle.setAttribute('aria-expanded', String(open));
      if (open) {
        menu.setAttribute('data-open', '');
        scrim.hidden = false;
        requestAnimationFrame(function () { scrim.classList.add('show'); });
        document.body.style.overflowY = 'hidden';
      } else {
        menu.removeAttribute('data-open');
        scrim.classList.remove('show');
        setTimeout(function () { if (!open) scrim.hidden = true; }, 300);
        document.body.style.overflowY = '';
      }
    };

    toggle.addEventListener('click', function () { setMenu(!open); });
    scrim.addEventListener('click', function () { setMenu(false); });

    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) setMenu(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && open) { setMenu(false); toggle.focus(); }
    });

    // rotating the phone from portrait to desktop width should not leave it stuck
    window.addEventListener('resize', function () {
      if (open && window.innerWidth >= 960) setMenu(false);
    });
  }

  var form = document.getElementById('contact-form');
  if (!form) return;
  var status = document.getElementById('form-status');

  function set(state, text) { status.dataset.state = state; status.textContent = text; }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var data = Object.fromEntries(new FormData(form).entries());
    if (data.company_website) return;
    if (!data.name || !data.email || !data.message) {
      set('error', 'Add your name, email, and a few details so I can reply.');
      return;
    }
    set('', 'Sending…');
    fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function () { form.reset(); set('ok', 'Sent. I reply within one business day.'); })
      .catch(function () { set('error', 'That did not send. Email marfarooqui@gmail.com directly and it will reach me.'); });
  });
})();
