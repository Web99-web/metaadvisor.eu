// MetaAdvisor – manual GA4 page tracking (geo-safe)
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

  // --- DELAYED initial page_view (CRITICAL FOR GEO) ---
  let initialSent = false;

  function sendInitialPageView() {
    if (initialSent) return;
    initialSent = true;
    sendPageView();
  }

  // wait for page to be visible + small delay
  function geoSafeInit() {
    if (document.visibilityState === 'visible') {
      setTimeout(sendInitialPageView, 120);
    } else {
      document.addEventListener('visibilitychange', () => {
        if (document.visibilityState === 'visible') {
          setTimeout(sendInitialPageView, 120);
        }
      }, { once: true });
    }
  }

  geoSafeInit();

  // --- SPA navigation tracking ---
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

    if (scrolled > 0.05) {
      scrollSent = true;

      gtag('event', 'scroll_05', {
        event_category: 'engagement',
        event_label: location.pathname
      });
    }
  }, { passive: true });

})();

function showCopyNotice() {
  const notice = document.getElementById("copyNotice");
  if (!notice) return;
  notice.style.opacity = "1";
  setTimeout(() => {
    notice.style.opacity = "0";
  }, 1500);
}
function copyArticleLink(url) {

  function trackCopy() {
    if (typeof gtag === "function") {
      gtag('event', 'share_copy', {
        event_category: 'engagement',
        event_label: url
      });
    }
  }

  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(url).then(() => {
      showCopyNotice();
      trackCopy();
    }).catch(() => {
      fallbackCopy(url);
    });
  } else {
    fallbackCopy(url);
  }

  function fallbackCopy(text) {
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.style.position = "fixed";
    textarea.style.left = "-9999px";
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);

    showCopyNotice();
    trackCopy();
  }
}

