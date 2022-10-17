import PhotoSwipeLightbox from "photoswipe/lightbox";
import PhotoSwipe from "photoswipe";
import "photoswipe/style.css";

const hamburger = document.querySelector("#hamburger");
const overlay = document.querySelector("#overlay");
const nav = document.querySelector("#nav");

const toggleMenu = () => {
  hamburger.classList.toggle("is-active");
  overlay.classList.toggle("is-visible");
  nav.classList.toggle("is-open");
};

const lightbox = new PhotoSwipeLightbox({
  gallery: ".gallery",
  children: "a",
  pswpModule: PhotoSwipe,
});

hamburger.addEventListener("click", toggleMenu);
overlay.addEventListener("click", toggleMenu);
nav.addEventListener("click", toggleMenu);

lightbox.init();
