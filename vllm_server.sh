vllm serve nvidia/Qwen3.6-27B-NVFP4 \
    --host 0.0.0.0 \
    --port 8000 \
    --max-model-len 8192 \
    --max-num-seqs 128 \
    --gpu-memory-utilization 0.90