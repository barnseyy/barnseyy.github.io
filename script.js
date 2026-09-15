document.getElementById("year").textContent = new Date().getFullYear();

const revealEls = document.querySelectorAll(".reveal");

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      }
    },
    { threshold: 0.15 }
  );

  revealEls.forEach((el) => observer.observe(el));
} else {
  revealEls.forEach((el) => el.classList.add("is-visible"));
}

// ---------- Carousel Logic ----------
const carouselTrack = document.getElementById('projectCarousel');
const navDots = document.querySelectorAll('.nav-dot');

if (carouselTrack && navDots.length > 0) {
  const cards = carouselTrack.querySelectorAll('.card');
  let activeIndex = 0;
  let autoplayTimer = null;
  let isInteracting = false;
  let interactionTimeout = null;
  const AUTOPLAY_INTERVAL = 8000;

  // Update active dot based on intersection
  const observerOptions = {
    root: carouselTrack,
    threshold: 0.6
  };

  const carouselObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const index = Array.from(cards).indexOf(entry.target);
        navDots.forEach(d => d.classList.remove('active'));
        if (navDots[index]) {
          navDots[index].classList.add('active');
          activeIndex = index;
        }
      }
    });
  }, observerOptions);

  cards.forEach(card => carouselObserver.observe(card));

  // Click nav dot to scroll to card
  navDots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
      pauseAutoplay();
      cards[index].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    });
  });

  // Autoplay function
  const startAutoplay = () => {
    if (autoplayTimer) clearInterval(autoplayTimer);
    autoplayTimer = setInterval(() => {
      if (!isInteracting) {
        let nextIndex = activeIndex + 1;
        
        // If we are at the last card, or can't scroll further right, loop back
        const maxScroll = carouselTrack.scrollWidth - carouselTrack.clientWidth;
        if (nextIndex >= cards.length || carouselTrack.scrollLeft >= maxScroll - 5) {
          nextIndex = 0;
        }
        
        cards[nextIndex].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
      }
    }, AUTOPLAY_INTERVAL);
  };

  // Pause on interaction
  const pauseAutoplay = () => {
    isInteracting = true;
    if (interactionTimeout) clearTimeout(interactionTimeout);
    interactionTimeout = setTimeout(() => {
      isInteracting = false;
    }, AUTOPLAY_INTERVAL); // Resume normal checking after 8s of no interaction
  };

  // Listen for manual swipe/scroll/touch
  carouselTrack.addEventListener('touchstart', pauseAutoplay, { passive: true });
  carouselTrack.addEventListener('mousedown', pauseAutoplay, { passive: true });
  carouselTrack.addEventListener('wheel', pauseAutoplay, { passive: true });
  carouselTrack.addEventListener('scroll', pauseAutoplay, { passive: true });

  // Initialize
  startAutoplay();
}
