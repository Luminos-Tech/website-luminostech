/* ===========================
   LUMINOS TECH — Main JS
   =========================== */

// Mobile nav toggle
const mobileToggle = document.getElementById('mobileToggle');
const navLinks = document.getElementById('navLinks');

mobileToggle.addEventListener('click', () => {
  navLinks.classList.toggle('open');
  mobileToggle.classList.toggle('active');
});

// Close mobile nav when a link is clicked
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    mobileToggle.classList.remove('active');
  });
});

// Scroll reveal — staggered animation
const revealMap = [
  { sel: '.tag-label, .section-label', cls: 'reveal', delay: 0 },
  { sel: '.hero-heading, .hero-sub, .hero-buttons, .ticker-wrap', cls: 'reveal', delay: 0 },
  { sel: '.vp-left, .vp-right', cls: 'reveal', delay: 0 },
  { sel: '.vp-bullets li', cls: 'reveal', delay: 80 },
  { sel: '.card', cls: 'reveal', delay: 80 },
  { sel: '.product-card', cls: 'reveal', delay: 100 },
  { sel: '.stat-card', cls: 'reveal', delay: 80 },
  { sel: '.process-step', cls: 'reveal', delay: 100 },
  { sel: '.case-card', cls: 'reveal', delay: 60 },
  { sel: '.section-heading, .callout-line', cls: 'reveal', delay: 0 },
  { sel: '.footer-cta .big-heading, .footer-cta .footer-cta-sub, .footer-cta .btn-primary', cls: 'reveal', delay: 0 },
];

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, {
  threshold: 0.1,
  rootMargin: '0px 0px -48px 0px'
});

revealMap.forEach(({ sel, cls, delay }) => {
  document.querySelectorAll(sel).forEach((el, i) => {
    el.classList.add(cls);
    if (delay > 0) {
      el.style.transitionDelay = `${i * delay}ms`;
    }
    observer.observe(el);
  });
});

// Navbar — use class toggle
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
}, { passive: true });
