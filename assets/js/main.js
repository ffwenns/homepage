import { FsLightbox } from "fslightbox";
import { CountUp } from "countup.js";
import Swiper from "swiper";
import { Mousewheel, Navigation } from "swiper/modules";

console.log("Created with Hugo and Tailwind CSS");

document.addEventListener("DOMContentLoaded", () => {
  const swiper = new Swiper(".swiper", {
    modules: [Mousewheel, Navigation],
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    enabled: false,
    spaceBetween: 16,
    mousewheel: true,
    grabCursor: true,
    breakpoints: {
      640: {
        slidesPerView: 2,
        enabled: true,
      },
      1280: {
        slidesPerView: 3,
        enabled: true,
      },
    },
  });

  const counters = document.querySelectorAll(".counter");

  counters.forEach((counter, index) => {
    const targetCount = parseInt(counter.textContent);
    const countUp = new CountUp(counter, targetCount, {
      startVal: 0,
      duration: 10,
      separator: ".",
      enableScrollSpy: true,
      scrollSpyOnce: true,
      scrollSpyDelay: 100,
    });

    countUp.start();
  });
});
