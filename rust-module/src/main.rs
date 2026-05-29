use axum::{
    routing::{get, post},
    http::StatusCode,
    Json, Router,
};
use serde::{Serialize, Deserialize};
use std::net::SocketAddr;

#[derive(Serialize, Deserialize)]
struct ComputeResult {
    result: i64,
    computation_time: String,
}

#[derive(Serialize, Deserialize)]
struct BoolResult {
    result: bool,
    computation_time: String,
}

fn fibonacci(n: u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let mut a = 0;
            let mut b = 1;
            for _ in 2..=n {
                let c = a + b;
                a = b;
                b = c;
            }
            b
        }
    }
}

fn factorial(n: u32) -> u64 {
    (1..=n).product()
}

fn is_prime(n: u64) -> bool {
    if n <= 1 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    let sqrt_n = (n as f64).sqrt() as u64;
    (3..=sqrt_n).step_by(2).all(|i| n % i != 0)
}

async fn handle_fibonacci(path: axum::extract::Path<u32>) -> (StatusCode, Json<ComputeResult>) {
    let n = path.0;
    let start = std::time::Instant::now();
    let result = fibonacci(n);
    let duration = start.elapsed();
    
    (
        StatusCode::OK,
        Json(ComputeResult {
            result: result as i64,
            computation_time: format!("{:?}", duration),
        }),
    )
}

async fn handle_factorial(path: axum::extract::Path<u32>) -> (StatusCode, Json<ComputeResult>) {
    let n = path.0;
    let start = std::time::Instant::now();
    let result = factorial(n);
    let duration = start.elapsed();
    
    (
        StatusCode::OK,
        Json(ComputeResult {
            result: result as i64,
            computation_time: format!("{:?}", duration),
        }),
    )
}

async fn handle_is_prime(path: axum::extract::Path<u64>) -> (StatusCode, Json<BoolResult>) {
    let n = path.0;
    let start = std::time::Instant::now();
    let result = is_prime(n);
    let duration = start.elapsed();
    
    (
        StatusCode::OK,
        Json(BoolResult {
            result,
            computation_time: format!("{:?}", duration),
        }),
    )
}

async fn health_check() -> &'static str {
    "OK"
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(health_check))
        .route("/compute/fibonacci/:n", get(handle_fibonacci))
        .route("/compute/factorial/:n", get(handle_factorial))
        .route("/compute/is_prime/:n", get(handle_is_prime));

    let addr = SocketAddr::from(([0, 0, 0, 0], 8081));
    println!("Rust compute service running on http://{}", addr);
    
    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}