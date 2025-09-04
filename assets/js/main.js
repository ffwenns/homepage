import Swiper from "swiper";
import { Navigation } from "swiper/modules";

const swiper = new Swiper(".swiper", {
  modules: [Navigation],
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  enabled: false,
  spaceBetween: 16,
  grabCursor: true,
  breakpoints: {
    768: {
      slidesPerView: 2,
      enabled: true,
    },
    1280: {
      slidesPerView: 3,
      enabled: true,
    },
  },
});
