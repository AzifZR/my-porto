with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Tambahkan CSS Theme Transition & Dark Palette Variables
theme_css = """
    /* Theme Transition & Cyber Matrix / Dark Mode Palette */
    html {
      transition: background-color 0.4s ease, color 0.4s ease;
    }
    html.dark-theme {
      background-color: #070D19 !important;
      color: #F6FAFD !important;
    }
    html.dark-theme body {
      background-color: #070D19 !important;
      color: #F6FAFD !important;
    }
    html.dark-theme .bg-white {
      background-color: #070D19 !important;
    }
    html.dark-theme .bg-brand-surface {
      background-color: #0D1B2E !important;
      border-color: #1A3D63 !important;
    }
    html.dark-theme .text-brand-dark {
      color: #F6FAFD !important;
    }
    html.dark-theme .text-brand-navy {
      color: #B3CFE5 !important;
    }
    html.dark-theme .border-brand-ice {
      border-color: #1A3D63 !important;
    }
    html.dark-theme .border-brand-ice\\/70,
    html.dark-theme .border-brand-ice\\/80,
    html.dark-theme .border-brand-ice\\/60 {
      border-color: #1A3D63 !important;
    }
"""

text = text.replace('  </style>', theme_css + '\n  </style>')

# 2. Tambahkan Toggle Theme Switcher Button di Navbar (Sebelum status Let\'s Talk)
old_nav_end = """      <a href="mailto:contact@azifzr.dev" class="flex items-center gap-2 bg-brand-dark hover:bg-brand-navy text-brand-surface px-4 py-1.5 rounded-full text-xs font-medium transition-all group shadow-sm">
        <span class="w-2 h-2 rounded-full bg-brand-steel group-hover:scale-125 transition-transform animate-ping"></span>
        <span class="relative -ml-3 w-2 h-2 rounded-full bg-brand-steel"></span>
        <span>Let's Talk →</span>
      </a>"""

new_nav_end = """      <div class="flex items-center gap-3">
        <!-- Minimal Theme Switcher -->
        <button onclick="toggleTheme()" id="theme-toggle-btn" title="Toggle Clean Light / Cyber Dark"
                class="px-2.5 py-1 rounded-full text-xs font-mono border border-brand-ice text-brand-navy hover:text-brand-steel hover:border-brand-steel transition-all flex items-center gap-1.5">
          <span id="theme-indicator" class="w-2 h-2 rounded-full bg-brand-steel"></span>
          <span id="theme-label" class="text-[11px] font-semibold">LIGHT</span>
        </button>

        <a href="mailto:contact@azifzr.dev" class="flex items-center gap-2 bg-brand-dark hover:bg-brand-navy text-brand-surface px-4 py-1.5 rounded-full text-xs font-medium transition-all group shadow-sm">
          <span class="w-2 h-2 rounded-full bg-brand-steel group-hover:scale-125 transition-transform animate-ping"></span>
          <span class="relative -ml-3 w-2 h-2 rounded-full bg-brand-steel"></span>
          <span>Let's Talk →</span>
        </a>
      </div>"""

text = text.replace(old_nav_end, new_nav_end)

# 3. Tambahkan Theme Script
theme_js = """
  <!-- Minimal Theme Switcher Script -->
  <script>
    function applyTheme(isDark) {
      const htmlEl = document.documentElement;
      const themeLabel = document.getElementById('theme-label');
      const themeIndicator = document.getElementById('theme-indicator');

      if (isDark) {
        htmlEl.classList.add('dark-theme');
        if (themeLabel) themeLabel.textContent = 'DARK';
        if (themeIndicator) {
          themeIndicator.classList.remove('bg-brand-steel');
          themeIndicator.classList.add('bg-emerald-400');
        }
        localStorage.setItem('azifzr-theme', 'dark');
      } else {
        htmlEl.classList.remove('dark-theme');
        if (themeLabel) themeLabel.textContent = 'LIGHT';
        if (themeIndicator) {
          themeIndicator.classList.remove('bg-emerald-400');
          themeIndicator.classList.add('bg-brand-steel');
        }
        localStorage.setItem('azifzr-theme', 'light');
      }
    }

    function toggleTheme() {
      const isDark = document.documentElement.classList.contains('dark-theme');
      applyTheme(!isDark);
    }

    // Auto restore preference
    window.addEventListener('DOMContentLoaded', () => {
      const saved = localStorage.getItem('azifzr-theme');
      if (saved === 'dark') {
        applyTheme(true);
      }
    });
  </script>
"""

text = text.replace('</body>', theme_js + '\n</body>')

with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Stage 4 Theme Switcher injected successfully!')
