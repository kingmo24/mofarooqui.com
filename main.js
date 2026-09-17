/* mofarooqui.com — daylight interactions */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---- scroll progress bar ---- */
  var bar = document.getElementById('progress');
  if (bar) {
    var ticking = false;
    var update = function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      var p = max > 0 ? h.scrollTop / max : 0;
      bar.style.transform = 'scaleX(' + p + ')';
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* ---- nav shadow on scroll ---- */
  var nav = document.querySelector('.nav');
  if (nav) {
    var navScroll = function () {
      if (window.scrollY > 8) nav.setAttribute('data-scrolled', '');
      else nav.removeAttribute('data-scrolled');
    };
    window.addEventListener('scroll', navScroll, { passive: true });
    navScroll();
  }

  /* ---- reveal: rise, stagger, and hero line clip ---- */
  var revealTargets = document.querySelectorAll('.rise, .stagger, .hero');
  if (reduce || !('IntersectionObserver' in window)) {
    revealTargets.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.05 });
    revealTargets.forEach(function (el) { io.observe(el); });
    // hero fires immediately so the headline animates on load
    requestAnimationFrame(function () {
      document.querySelectorAll('.hero').forEach(function (el) { el.classList.add('in'); });
    });
  }

  /* ---- magnetic buttons (pointer only, respects reduced motion) ---- */
  if (!reduce && window.matchMedia('(hover:hover) and (pointer:fine)').matches) {
    document.querySelectorAll('.btn').forEach(function (btn) {
      var strength = 0.28;
      btn.addEventListener('pointermove', function (e) {
        var r = btn.getBoundingClientRect();
        var x = e.clientX - r.left - r.width / 2;
        var y = e.clientY - r.top - r.height / 2;
        btn.style.transform = 'translate(' + x * strength + 'px,' + y * strength + 'px)';
      });
      btn.addEventListener('pointerleave', function () { btn.style.transform = ''; });
    });

    /* ---- card pointer-tracked glow ---- */
    document.querySelectorAll('.card').forEach(function (card) {
      card.addEventListener('pointermove', function (e) {
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100) + '%');
        card.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100) + '%');
      });
    });
  }

  /* ---- mobile menu ---- */
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
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && open) { setMenu(false); toggle.focus(); } });
    window.addEventListener('resize', function () { if (open && window.innerWidth >= 960) setMenu(false); });
  }

  /* ---- contact form ---- */
  var form = document.getElementById('contact-form');
  if (!form) return;
  var status = document.getElementById('form-status');
  var set = function (s, t) { status.dataset.state = s; status.textContent = t; };
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var data = Object.fromEntries(new FormData(form).entries());
    if (data.company_website) return;
    if (!data.name || !data.email || !data.message) { set('error', 'Add your name, email, and a few details so I can reply.'); return; }
    set('', 'Sending…');
    fetch('/api/contact', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function () { form.reset(); set('ok', 'Sent. I reply within one business day.'); })
      .catch(function () { set('error', 'That did not send. Email marfarooqui@gmail.com directly and it will reach me.'); });
  });
})();
