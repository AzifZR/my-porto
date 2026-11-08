with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

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
    </div>

    <!-- Asymmetrical Bento Grid with Glow Cards -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8" id="projects-grid">"""

import re
text = re.sub(
    r'<!-- Asymmetrical Bento Grid with Glow Cards -->\s*<div class="grid grid-cols-1 lg:grid-cols-12 gap-8">',
    filter_buttons_html,
    text
)

with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('SUCCESS!')
