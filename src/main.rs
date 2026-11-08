use askama::Template;
use axum::{
    response::{Html, IntoResponse},
    routing::get,
    Router,
};
use std::env;
use std::net::SocketAddr;
use std::path::PathBuf;
use tower_http::services::ServeDir;

#[derive(Template)]
#[template(path = "index.html")]
struct IndexTemplate;

async fn index_handler() -> impl IntoResponse {
    let template = IndexTemplate;
    match template.render() {
        Ok(html) => Html(html).into_response(),
        Err(err) => (
            axum::http::StatusCode::INTERNAL_SERVER_ERROR,
            format!("Template error: {}", err),
        )
            .into_response(),
    }
}

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt::init();

    // Port and host from environment or default
    let port: u16 = env::var("PORT")
        .ok()
        .and_then(|p| p.parse().ok())
        .unwrap_or(8080);

    let host = env::var("HOST").unwrap_or_else(|_| "0.0.0.0".to_string());

    // Detect static directory relative to current working directory or binary location
    let static_dir = env::var("STATIC_DIR")
        .map(PathBuf::from)
        .unwrap_or_else(|_| {
            let pwd_static = PathBuf::from("static");
            if pwd_static.exists() {
                pwd_static
            } else if let Ok(exe_path) = env::current_exe() {
                if let Some(exe_dir) = exe_path.parent() {
                    let relative_to_exe = exe_dir.join("static");
                    if relative_to_exe.exists() {
                        relative_to_exe
                    } else {
                        PathBuf::from("/home/gwolf/projects/azifzr-portfolio/static")
                    }
                } else {
                    PathBuf::from("static")
                }
            } else {
                PathBuf::from("static")
            }
        });

    println!("📁 Serving static files from: {:?}", static_dir);

    let app = Router::new()
        .route("/", get(index_handler))
        .nest_service("/static", ServeDir::new(static_dir));

    let addr: SocketAddr = format!("{}:{}", host, port)
        .parse()
        .unwrap_or_else(|_| SocketAddr::from(([0, 0, 0, 0], port)));

    println!("🦀 AzifZR Portfolio Server running on http://{}", addr);

    let listener = tokio::net::TcpListener::bind(addr)
        .await
        .unwrap_or_else(|e| panic!("Failed to bind to {}: {}", addr, e));

    axum::serve(listener, app)
        .await
        .expect("Server failed to run");
}
