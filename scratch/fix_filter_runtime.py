with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Pasang data-category dan class project-card ke tiap kartu
card1_old = '<!-- Big Bento Hero Card (7 Cols) -> JagaJiwa Project -->\n <div class="lg:col-span-7 bg-brand-surface'
card1_new = '<!-- Big Bento Hero Card (7 Cols) -> JagaJiwa Project -->\n <div data-category="web ai-nlp security" class="project-card lg:col-span-7 bg-brand-surface'

card2_old = '<!-- Bento Card 2 (5 Cols - JiwaBot AI & Anon Community) -->\n <div class="lg:col-span-5 bg-brand-surface'
card2_new = '<!-- Bento Card 2 (5 Cols - JiwaBot AI & Anon Community) -->\n <div data-category="web ai-nlp" class="project-card lg:col-span-5 bg-brand-surface'

card3_old = '<!-- Lower Bento Card 3: Backend & Systems Architecture -->\n <div class="lg:col-span-6 bg-brand-surface'
card3_new = '<!-- Lower Bento Card 3: Backend & Systems Architecture -->\n <div data-category="security web" class="project-card lg:col-span-6 bg-brand-surface'

card4_old = '<!-- Lower Bento Card 4: High Performance Rust Tooling -->\n <div class="lg:col-span-6 bg-brand-surface'
card4_new = '<!-- Lower Bento Card 4: High Performance Rust Tooling -->\n <div data-category="systems" class="project-card lg:col-span-6 bg-brand-surface'

text = text.replace(card1_old, card1_new)
text = text.replace(card2_old, card2_new)
text = text.replace(card3_old, card3_new)
text = text.replace(card4_old, card4_new)

# Update fungsi filterProjects agar robust
old_filter_func = """    // Project Category Filtering
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
    }"""

new_filter_func = """    // Project Category Filtering
    function filterProjects(category) {
      const cards = document.querySelectorAll('.project-card');
      const buttons = document.querySelectorAll('.filter-btn');

      buttons.forEach(btn => {
        if (btn.getAttribute('data-filter') === category) {
          btn.className = "filter-btn active-filter px-4 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-brand-dark text-brand-surface shadow-sm";
        } else {
          btn.className = "filter-btn px-4 py-1.5 rounded-full text-xs font-mono font-medium transition-all bg-brand-surface text-brand-navy border border-brand-ice hover:border-brand-steel";
        }
      });

      cards.forEach(card => {
        const cats = card.getAttribute('data-category') || '';
        if (category === 'all' || cats.includes(category)) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    }"""

text = text.replace(old_filter_func, new_filter_func)

with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Filter fixed with display toggle and project-card selector!')
