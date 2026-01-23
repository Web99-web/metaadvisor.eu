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
})();
