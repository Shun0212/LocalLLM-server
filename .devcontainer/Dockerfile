# CUDA 12.9.2 + cuDNN8 ベース（Ubuntu 22.04）
FROM nvidia/cuda:12.9.2-cudnn-devel-ubuntu22.04

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip git openmpi-bin libopenmpi-dev curl unzip&& \
    rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# uv のパスを通す
ENV PATH="/root/.local/bin:${PATH}"

# uv が コピーを使う
ENV UV_LINK_MODE=copy

# pip management tools
RUN pip3 install --upgrade pip packaging
RUN uv pip install vllm \
    --extra-index-url https://wheels.vllm.ai/0.24.0/cu129 \
    --extra-index-url https://download.pytorch.org/whl/cu129 \
    --index-strategy unsafe-best-match
    
