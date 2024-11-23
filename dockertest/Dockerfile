# Use the latest Alpine image
FROM alpine:3.20.3

# Set the working directory
WORKDIR /root

# Install necessary packages
RUN apk update && apk add --no-cache \
    git \
    nodejs \
    npm \
    python3 \
    neovim \
    ripgrep \
    build-base \
    wget \
    bash

# Clone Nvim configuration
RUN git clone https://github.com/reymaa19/nvim.git ~/.config/nvim

# Set the entrypoint to start Neovim
ENTRYPOINT ["nvim"]
