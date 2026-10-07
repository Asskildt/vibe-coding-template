(function () {
  var storageKey = 'theme';
  var cycle = ['system', 'light', 'dark'];
  var labels = { system: 'System', light: 'Light', dark: 'Dark' };
  var toggle = document.querySelector('.theme-toggle');
  var label = toggle.querySelector('.theme-label');

  function systemTheme() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function apply(choice) {
    var effective = choice === 'system' ? systemTheme() : choice;
    document.documentElement.setAttribute('data-theme', effective);
    localStorage.setItem(storageKey, choice);
    label.textContent = labels[choice];
  }

  apply(localStorage.getItem(storageKey) || 'system');

  toggle.addEventListener('click', function () {
    var current = localStorage.getItem(storageKey) || 'system';
    apply(cycle[(cycle.indexOf(current) + 1) % cycle.length]);
  });

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
    if ((localStorage.getItem(storageKey) || 'system') === 'system') apply('system');
  });
})();

(function () {
  document.querySelectorAll('.prompt-expand').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var prompt = btn.closest('.prompt');
      var open = prompt.classList.toggle('open');
      btn.textContent = open ? 'Collapse' : 'Expand';
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  document.querySelectorAll('.copy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var pre = document.getElementById(btn.getAttribute('data-copy'));
      if (!pre) return;
      var text = pre.textContent;
      function done() {
        var original = btn.textContent;
        btn.textContent = 'Copied';
        btn.classList.add('copied');
        setTimeout(function () {
          btn.textContent = original;
          btn.classList.remove('copied');
        }, 1600);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done).catch(fallback);
      } else {
        fallback();
      }
      function fallback() {
        var r = document.createRange();
        r.selectNodeContents(pre);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(r);
        try { document.execCommand('copy'); done(); } catch (e) { /* no-op */ }
        sel.removeAllRanges();
      }
    });
  });
})();
