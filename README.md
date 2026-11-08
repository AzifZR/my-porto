# Muhammad Azif Zain Rizky (AzifZR) — Personal Portfolio

> High-performance personal portfolio web application engineered with Rust, Axum, Askama, and Tailwind CSS.

---

## ⚡ Tech Stack & Architecture

- **Backend:** [Axum 0.7](https://github.com/tokio-rs/axum) with [Tokio](https://tokio.rs/) async runtime.
- **Templating:** [Askama 0.12](https://github.com/djc/askama) (Type-safe, compile-time HTML rendering with zero runtime overhead).
- **Styling:** Tailwind CSS with modern, dark-navy & clean-ice color scheme.
- **Static Assets:** Tower-HTTP static file service.

---

## 🚀 Quick Start

### Prerequisites
- [Rust & Cargo](https://www.rust-lang.org/tools/install) (1.80+)

### Running Locally
```bash
git clone https://github.com/AzifZR/my-porto.git
cd my-porto

cargo run
```

Buka di browser: `http://localhost:8080`

---

## 📂 Project Structure
```text
.
├── Cargo.toml               # Rust dependencies configuration
├── src/
│   └── main.rs              # Axum HTTP server entry point & template router
├── templates/
│   └── index.html           # Modern clean responsive portfolio UI
└── static/                  # Static assets & optimized images
    ├── avatar.jpg
    ├── profile.jpg
    ├── jagajiwa-dashboard.png
    └── jagajiwa-bot.png
```

---

## 👨‍💻 Author
**Muhammad Azif Zain Rizky (AzifZR)**  
Mahasiswa D3 Manajemen Informatika • Politeknik Negeri Malang (POLINEMA) PSDKU Kediri  
- GitHub: [@AzifZR](https://github.com/AzifZR)
