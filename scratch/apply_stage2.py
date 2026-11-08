with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Filter buttons HTML
filter_buttons_html = """    <!-- Interactive Category Filter Tabs -->
    <div class="flex flex-wrap items-center gap-2 mb-8">
      <button onclick="filterProjects('all')" data-filter="all" class="filter-btn active-filter px-4 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-brand-dark text-brand-surface shadow-sm">
        [All Projects]
      </button>
      <button onclick="filterProjects('web')" data-filter="web" class="filter-btn px-4 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-brand-surface text-brand-navy border border-brand-ice hover:border-brand-steel">
        / Fullstack & Web
      </button>
      <button onclick="filterProjects('ai-nlp')" data-filter="ai-nlp" class="filter-btn px-4 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-brand-surface text-brand-navy border border-brand-ice hover:border-brand-steel">
        / AI & NLP
      </button>
      <button onclick="filterProjects('security')" data-filter="security" class="filter-btn px-4 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-brand-surface text-brand-navy border border-brand-ice hover:border-brand-steel">
        / Cryptography & Security
      </button>
      <button onclick="filterProjects('systems')" data-filter="systems" class="filter-btn px-4 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-brand-surface text-brand-navy border border-brand-ice hover:border-brand-steel">
        / Rust & Systems
      </button>
    </div>"""

# Replace in index.html right before <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
target_grid_header = '    <!-- Asymmetrical Bento Grid with Glow Cards -->\n    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">'
replacement_grid_header = '    <!-- Asymmetrical Bento Grid with Glow Cards -->\n' + filter_buttons_html + '\n    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8" id="projects-grid">'

text = text.replace(target_grid_header, replacement_grid_header)

# Tambahkan data-category ke setiap card
text = text.replace(
    '<!-- Big Bento Hero Card (7 Cols) -> JagaJiwa Project -->\n      <div class="lg:col-span-7',
    '<!-- Big Bento Hero Card (7 Cols) -> JagaJiwa Project -->\n      <div data-category="web ai-nlp security" class="project-item lg:col-span-7'
)

text = text.replace(
    '<!-- Bento Card 2 (5 Cols - JiwaBot AI & Anon Community) -->\n      <div class="lg:col-span-5',
    '<!-- Bento Card 2 (5 Cols - JiwaBot AI & Anon Community) -->\n      <div data-category="web ai-nlp" class="project-item lg:col-span-5'
)

text = text.replace(
    '<!-- Lower Bento Card 3: Backend & Systems Architecture -->\n      <div class="lg:col-span-6',
    '<!-- Lower Bento Card 3: Backend & Systems Architecture -->\n      <div data-category="security web" class="project-item lg:col-span-6'
)

text = text.replace(
    '<!-- Lower Bento Card 4: High Performance Rust Tooling -->\n      <div class="lg:col-span-6',
    '<!-- Lower Bento Card 4: High Performance Rust Tooling -->\n      <div data-category="systems" class="project-item lg:col-span-6'
)

# Modal HTML & Filter JS
modal_and_filter_js = """
  <!-- Interactive Architecture Modal (JagaJiwa Deep-Dive) -->
  <div id="arch-modal" class="fixed inset-0 z-50 bg-brand-dark/70 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="bg-brand-surface border border-brand-steel/50 rounded-2xl max-w-2xl w-full p-6 shadow-2xl space-y-4 max-h-[90vh] overflow-y-auto font-sans" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between border-b border-brand-ice pb-3">
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <h3 class="font-bold text-base text-brand-dark font-mono">JagaJiwa / Architecture & Data Pipeline</h3>
        </div>
        <button onclick="closeModal()" class="text-brand-navy hover:text-brand-steel p-1 rounded-md text-sm font-mono">[close ×]</button>
      </div>

      <div class="space-y-3 text-xs leading-relaxed text-brand-navy font-mono">
        <div class="p-3 bg-brand-dark text-brand-surface rounded-xl space-y-2 border border-brand-navy">
          <div class="text-emerald-400 font-semibold">[FLOW 1] Zero-Knowledge Journal Encryption:</div>
          <div class="pl-2 border-l border-brand-steel/40 text-[11px] text-brand-ice/90">
            User Input (Mood & Diary) ➔ Client-side AES-256 (crypto-js) ➔ Express 5 API ➔ PostgreSQL (Supabase RLS). Server & database never store plain diary text.
          </div>
        </div>

        <div class="p-3 bg-brand-dark text-brand-surface rounded-xl space-y-2 border border-brand-navy">
          <div class="text-cyan-300 font-semibold">[FLOW 2] JiwaBot AI & Sentiment Analysis:</div>
          <div class="pl-2 border-l border-brand-steel/40 text-[11px] text-brand-ice/90">
            User Chat ➔ sastrawijs Indonesian Stemmer ➔ Token Sentiment Scoring ➔ OpenAI SDK Streaming Endpoint ➔ Realtime UI Render (Vite 8 + React 19).
          </div>
        </div>

        <div class="p-3 bg-brand-dark text-brand-surface rounded-xl space-y-2 border border-brand-navy">
          <div class="text-amber-300 font-semibold">[FLOW 3] Security & 2FA Verification:</div>
          <div class="pl-2 border-l border-brand-steel/40 text-[11px] text-brand-ice/90">
            Google OAuth / Passport ➔ JWT Stateless Session ➔ otplib TOTP Generation & QR Verification.
          </div>
        </div>
      </div>

      <div class="pt-3 border-t border-brand-ice flex justify-between items-center text-xs">
        <span class="text-brand-steel font-mono">Stack: React 19 • Express 5 • Supabase • Vitest</span>
        <button onclick="closeModal()" class="bg-brand-dark text-brand-surface hover:bg-brand-navy px-4 py-1.5 rounded-lg font-mono text-xs">Tutup Detail</button>
      </div>
    </div>
  </div>

  <script>
    // Project Category Filtering
    function filterProjects(category) {
      const items = document.querySelectorAll('.project-item');
      const buttons = document.querySelectorAll('.filter-btn');

      buttons.forEach(btn => {
        if (btn.getAttribute('data-filter') === category) {
          btn.className = "filter-btn active-filter px-4 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-brand-dark text-brand-surface shadow-sm";
        } else {
          btn.className = "filter-btn px-4 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-brand-surface text-brand-navy border border-brand-ice hover:border-brand-steel";
        }
      });

      items.forEach(item => {
        const itemCats = item.getAttribute('data-category') || '';
        if (category === 'all' || itemCats.includes(category)) {
          item.classList.remove('hidden');
          item.classList.add('flex');
        } else {
          item.classList.add('hidden');
          item.classList.remove('flex');
        }
      });
    }

    // Modal controls
    function openModal() {
      const modal = document.getElementById('arch-modal');
      modal.classList.remove('hidden');
    }
    function closeModal() {
      const modal = document.getElementById('arch-modal');
      modal.classList.add('hidden');
    }
    document.getElementById('arch-modal').addEventListener('click', closeModal);
  </script>
"""

# Tambahkan tombol "Inspect Architecture" di JagaJiwa card
inspect_btn = """          <div class="pt-2">
            <button onclick="openModal()" class="inline-flex items-center gap-1.5 text-xs font-mono text-brand-steel hover:text-brand-dark transition-colors font-medium underline underline-offset-4">
              <span>[+] Inspect System Architecture & Data Flow</span>
            </button>
          </div>"""

text = text.replace(
    'Platform terpadu kesehatan mental berbasis Artificial Intelligence',
    inspect_btn + '\n          <p class="text-brand-navy text-sm leading-relaxed">\n            Platform terpadu kesehatan mental berbasis Artificial Intelligence'
)

# Append modal and scripts before </body>
text = text.replace('</body>', modal_and_filter_js + '\n</body>')

with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Stage 2 interactive filters and modal injected successfully!')
