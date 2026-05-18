(function () {
  function goPrev() {
    const prev = document.querySelector("link[rel='prev']")?.href;
    if (prev) window.location.href = prev;
  }

  function goNext() {
    const next = document.querySelector("link[rel='next']")?.href;
    if (next) window.location.href = next;
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") goPrev();
    if (e.key === "ArrowRight") goNext();
  });

  // Swipe navigation
  let startX = 0;
  let startY = 0;
  let startTime = 0;
  const distanceThreshold = 80;
  const horizontalRatioThreshold = 1.8;
  const velocityThreshold = 0.25;

  document.addEventListener("touchstart", (e) => {
    startX = e.changedTouches[0].clientX;
    startY = e.changedTouches[0].clientY;
    startTime = performance.now();
  }, { passive: true });

  document.addEventListener("touchend", (e) => {
    const endX = e.changedTouches[0].clientX;
    const endY = e.changedTouches[0].clientY;
    const endTime = performance.now();
    const dx = endX - startX;
    const dy = endY - startY;
    const dt = endTime - startTime;

    if (Math.abs(dx) < distanceThreshold) return;
    if (Math.abs(dx) < horizontalRatioThreshold*Math.abs(dy)) return;
    if (Math.abs(dx) < velocityThreshold * dt) return;

    if (dx > 0) goPrev();
    else goNext();
  }, { passive: true });
})();