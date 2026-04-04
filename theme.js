(function () {
  const html = document.documentElement;
  const btn = document.getElementById('themeToggle');
  const icon = document.getElementById('themeIcon');
  const mediaQuery = window.matchMedia ? window.matchMedia('(prefers-color-scheme: light)') : null;

  function applyTheme(theme, options) {
    const persist = options && options.persist;
    html.setAttribute('data-theme', theme);

    if (icon) {
      icon.textContent = theme === 'light' ? '☀️' : '🌙';
    }

    if (btn) {
      const nextModeLabel = theme === 'light' ? '切换为暗色模式' : '切换为亮色模式';
      btn.setAttribute('aria-label', nextModeLabel);
      btn.setAttribute('title', nextModeLabel);
      btn.setAttribute('aria-pressed', String(theme === 'light'));
    }

    if (persist) {
      localStorage.setItem('portal-theme', theme);
    }
  }

  const savedTheme = localStorage.getItem('portal-theme');
  const initialTheme = savedTheme || (mediaQuery && mediaQuery.matches ? 'light' : 'dark');
  applyTheme(initialTheme, { persist: false });

  if (btn) {
    btn.addEventListener('click', function () {
      const currentTheme = html.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
      const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
      applyTheme(nextTheme, { persist: true });
    });
  }

  if (mediaQuery) {
    const syncWithSystem = function (event) {
      if (!localStorage.getItem('portal-theme')) {
        applyTheme(event.matches ? 'light' : 'dark', { persist: false });
      }
    };

    if (typeof mediaQuery.addEventListener === 'function') {
      mediaQuery.addEventListener('change', syncWithSystem);
    } else if (typeof mediaQuery.addListener === 'function') {
      mediaQuery.addListener(syncWithSystem);
    }
  }
})();
