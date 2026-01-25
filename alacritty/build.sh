docker build -t alacritty-dev .

docker run -it --rm \
    -v $(pwd):/workspace \
    alacritty-dev \
    bash -c "
        git clone --depth 1 --branch v0.16.1 https://github.com/alacritty/alacritty.git &&
        cd alacritty &&
        cargo build --release
    "
