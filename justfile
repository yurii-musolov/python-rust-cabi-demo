set shell := ["bash", "-cu"]

build:
    cd rustlib && cargo build --release

demo: build
    python3 python/main.py

clean:
    rm -rf rustlib/target