import { FsLightbox } from "fslightbox";
import { CountUp } from "countup.js";

console.log("Created with Hugo and Tailwind CSS");

document.addEventListener("DOMContentLoaded", () => {
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
