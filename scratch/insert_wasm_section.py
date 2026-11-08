with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

wasm_section_html = """
  <!-- 02.5 / LIVE RUST WEBASSEMBLY PLAYGROUND -->
  <section id="wasm-lab" class="max-w-6xl mx-auto px-6 py-16 border-t border-brand-ice/70">
    <div class="bg-brand-surface border border-brand-steel/40 rounded-2xl p-7 md:p-9 shadow-sm relative overflow-hidden">
      <div class="absolute -top-12 -right-12 w-48 h-48 bg-brand-steel/15 rounded-full blur-2xl pointer-events-none"></div>

      <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-6 mb-8">
        <div>
          <div class="text-xs font-mono font-semibold text-brand-steel uppercase tracking-widest flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>Live WebAssembly Engine</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-brand-dark tracking-tight mt-1">
            Rust WASM in Browser: Live Benchmark
          </h2>
          <p class="text-brand-navy text-sm mt-1 max-w-xl">
            Modul biner Rust murni (<code class="text-brand-steel">wasm_core.wasm</code>, 21 KB) yang dieksekusi langsung oleh browser client tanpa runtime overhead.
          </p>
        </div>

        <div class="flex items-center gap-2 bg-brand-dark text-brand-surface px-4 py-2 rounded-xl text-xs font-mono border border-brand-navy shadow-inner">
          <span class="text-emerald-400 font-bold">[WASM]</span>
          <span id="wasm-status-text">Module Ready • wasm32-unknown</span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center bg-white p-6 rounded-xl border border-brand-ice/80">
        <div class="space-y-4">
          <div class="text-xs font-mono text-brand-steel uppercase font-semibold">Test Workload: Sieve Prime Computation</div>
          <p class="text-xs text-brand-navy leading-relaxed">
            Hitung jumlah bilangan prima hingga batas tertentu menggunakan algoritma deterministik yang sama antara <strong>Rust WASM</strong> vs <strong>JavaScript V8</strong>.
          </p>
          
          <div class="flex items-center gap-3">
            <label class="text-xs font-mono text-brand-dark font-medium">Batas Limit:</label>
            <select id="wasm-limit" class="bg-brand-surface border border-brand-ice rounded-lg px-3 py-1.5 text-xs font-mono text-brand-dark focus:outline-none focus:border-brand-steel">
              <option value="50000">50,000 Angka</option>
              <option value="100000" selected>100,000 Angka</option>
              <option value="200000">200,000 Angka</option>
            </select>
          </div>

          <div class="pt-2 flex flex-wrap gap-3">
            <button onclick="runWasmBenchmark()" id="wasm-bench-btn" class="bg-brand-dark hover:bg-brand-navy text-brand-surface px-5 py-2.5 rounded-lg text-xs font-mono font-medium transition-all shadow-sm flex items-center gap-2">
              <span>▶ Run Benchmark</span>
            </button>
            <button onclick="calcFibonacci()" class="bg-brand-surface hover:border-brand-steel border border-brand-ice text-brand-dark px-4 py-2.5 rounded-lg text-xs font-mono font-medium transition-all">
              Hitung Fibonacci (n=90)
            </button>
          </div>
        </div>

        <div class="bg-brand-dark rounded-xl p-5 border border-brand-navy font-mono text-xs text-brand-surface space-y-3 min-h-[160px] flex flex-col justify-center">
          <div class="flex items-center justify-between border-b border-brand-navy pb-2 text-[11px] text-brand-ice/70">
            <span>benchmark_results.log</span>
            <span class="text-emerald-400 font-bold" id="bench-indicator">IDLE</span>
          </div>

          <div id="wasm-results" class="space-y-1.5 text-[11.5px]">
            <div class="text-brand-ice/80">Klik tombol <span class="text-amber-300 font-bold">"Run Benchmark"</span> untuk menguji kecepatan Rust WASM langsung di browser Anda.</div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# Sisipkan tepat sebelum <!-- 03 / ABOUT ME -->
target_anchor = "  <!-- 03 / ABOUT ME -->"
if target_anchor in text:
    text = text.replace(target_anchor, wasm_section_html + "\n\n" + target_anchor)
    print("Injected before target anchor!")
else:
    import re
    text = re.sub(r'(\s*<!-- 03 / ABOUT ME -->)', wasm_section_html + r'\n\1', text)
    print("Injected via regex!")

with open('/home/gwolf/projects/azifzr-portfolio/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("File written successfully!")
