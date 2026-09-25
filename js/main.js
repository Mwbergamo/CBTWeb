// CodeBlue Technology - shared site behavior (no framework, no build step)

document.addEventListener("DOMContentLoaded", function () {
  // Mobile nav toggle
  var toggle = document.querySelector(".nav-toggle");
  var mobileNav = document.querySelector(".nav-mobile");
  if (toggle && mobileNav) {
    toggle.addEventListener("click", function () {
      var open = mobileNav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // "Talk to a rep" 3-field micro-forms (there may be more than one per page)
  var repForms = document.querySelectorAll(".rep-form form");
  repForms.forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var wrapper = form.closest(".rep-form");
      // TODO: wire to real lead-capture endpoint (see mail/send-quote.php
      // pattern used on SolutionsHub) once staging backend is ready.
      if (wrapper) wrapper.classList.add("submitted");
    });
  });

  // Scroll-reveal: fade/rise elements marked .reveal as they enter view.
  // Elements are visible by default (see CSS). Only once we know the
  // observer is live do we "arm" them (add .reveal-armed, which is what
  // actually hides them pending .in). This guarantees content is never
  // stuck invisible if this script fails to load or errors out.
  var revealTargets = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealTargets.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
    );
    revealTargets.forEach(function (el) {
      el.classList.add("reveal-armed");
      io.observe(el);
    });
  }
});
