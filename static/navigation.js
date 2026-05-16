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
  const threshold = 60;

  document.addEventListener("touchstart", (e) => {
    startX = e.changedTouches[0].clientX;
  }, { passive: true });

  document.addEventListener("touchend", (e) => {
    const endX = e.changedTouches[0].clientX;
    const diff = endX - startX;

    if (Math.abs(diff) < threshold) return;

    if (diff > 0) goPrev();
    else goNext();
  }, { passive: true });
})();