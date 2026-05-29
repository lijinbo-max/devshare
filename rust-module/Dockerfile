FROM rust:1.74 AS builder
WORKDIR /app
COPY Cargo.toml .
COPY Cargo.lock .
COPY src ./src
RUN cargo build --release

FROM debian:bookworm-slim
WORKDIR /app
COPY --from=builder /app/target/release/rust-module .
EXPOSE 8081
CMD ["./rust-module"]