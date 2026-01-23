// MetaAdvisor – manual GA4 page tracking
(function () {

  window.maTrackingLoaded = true;

  if (typeof gtag !== 'function') return;


  function sendPageView() {
    gtag('event', 'page_view', {
      page_location: window.location.href,
      page_path: window.location.pathname,
      page_title: document.title
    });
  }

  // initial
  sendPageView();

  let lastPath = location.pathname;

  const observer = new MutationObserver(() => {
    if (location.pathname !== lastPath) {
      lastPath = location.pathname;
      sendPageView();
    }
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true
  });

    // --- simple scroll tracking (once per page) ---
  let scrollSent = false;

  window.addEventListener('scroll', () => {
    if (scrollSent) return;

    const scrolled =
      (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight;

    if (scrolled > 0.5) { // 50% scroll
      scrollSent = true;

      gtag('event', 'scroll_50', {
        event_category: 'engagement',
        event_label: location.pathname
      });
    }
  }, { passive: true });

})();
