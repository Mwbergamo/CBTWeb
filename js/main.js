// CodeBlue Technology — shared site behavior (no framework, no build step)

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
});
