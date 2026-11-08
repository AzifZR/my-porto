with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace button in nav
old_nav_button = """ <a href="mailto:contact@azifzr.dev" class="flex items-center gap-2 bg-brand-dark hover:bg-brand-navy text-brand-surface px-4 py-1.5 rounded-full text-xs font-medium transition-all group shadow-sm">
 <span class="w-2 h-2 rounded-full bg-brand-steel group-hover:scale-125 transition-transform animate-ping"></span>
 <span class="relative -ml-3 w-2 h-2 rounded-full bg-brand-steel"></span>
 <span>Let's Talk →</span>
 </a>"""

new_nav_button = """ <div class="flex items-center gap-3">
 <!-- Minimal Theme Switcher -->
 <button onclick="toggleTheme()" id="theme-toggle-btn" title="Toggle Clean Light / Cyber Dark"
 class="px-2.5 py-1 rounded-full text-xs font-mono border border-brand-ice text-brand-navy hover:text-brand-steel hover:border-brand-steel transition-all flex items-center gap-1.5 bg-brand-surface">
 <span id="theme-indicator" class="w-2 h-2 rounded-full bg-brand-steel"></span>
 <span id="theme-label" class="text-[11px] font-semibold">LIGHT</span>
 </button>

 <a href="mailto:contact@azifzr.dev" class="flex items-center gap-2 bg-brand-dark hover:bg-brand-navy text-brand-surface px-4 py-1.5 rounded-full text-xs font-medium transition-all group shadow-sm">
 <span class="w-2 h-2 rounded-full bg-brand-steel group-hover:scale-125 transition-transform animate-ping"></span>
 <span class="relative -ml-3 w-2 h-2 rounded-full bg-brand-steel"></span>
 <span>Let's Talk →</span>
 </a>
 </div>"""

if old_nav_button in text:
    text = text.replace(old_nav_button, new_nav_button)
    print("Direct nav button replaced!")
else:
    import re
    text = re.sub(
        r'<a href="mailto:contact@azifzr\.dev" class="[^"]*">[\s\S]*?<span>Let\'s Talk →</span>\s*</a>',
        new_nav_button.strip(),
        text
    )
    print("Regex nav button replaced!")

with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved!")
