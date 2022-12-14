const hamburger = document.querySelector("#hamburger");
const overlay = document.querySelector("#overlay");
const nav = document.querySelector("#nav");

const toggleMenu = () => {
  hamburger.classList.toggle("is-active");
  overlay.classList.toggle("is-visible");
  nav.classList.toggle("is-open");
};

hamburger.addEventListener("click", toggleMenu);
overlay.addEventListener("click", toggleMenu);
nav.addEventListener("click", toggleMenu);