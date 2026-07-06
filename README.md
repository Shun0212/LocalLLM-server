# LocalLLM-server

ローカル環境で vLLM の OpenAI 互換サーバーを起動し、Python からチャット補完 API を呼び出すための最小構成プロジェクトです。

デフォルトでは `nvidia/Qwen3.6-27B-NVFP4` を vLLM で配信し、`main.py` から `http://localhost:8000/v1` にリクエストします。

## 構成

```text
.
├── main.py          # OpenAI SDK を使った動作確認用クライアント
├── pyproject.toml   # Python プロジェクト設定と依存関係
├── README.md
└── vllm_server.sh   # vLLM サーバー起動スクリプト
```

## 前提条件

- Python 3.10 以上
- NVIDIA GPU と CUDA が利用できる環境
- 対象モデルを実行できる十分な GPU メモリ
- `uv`

`pyproject.toml` では vLLM 0.24.0 向けの CUDA 12.9 wheel index を指定しています。

## セットアップ

依存関係をインストールします。

```bash
uv sync
```

## サーバーの起動

vLLM サーバーを起動します。

```bash
bash vllm_server.sh
```

起動スクリプトの内容は以下の設定になっています。

```bash
vllm serve nvidia/Qwen3.6-27B-NVFP4 \
    --host 0.0.0.0 \
    --port 8000 \
    --max-model-len 8192 \
    --max-num-seqs 128 \
    --gpu-memory-utilization 0.90
```

サーバーは OpenAI 互換 API として `http://localhost:8000/v1` で待ち受けます。

## 動作確認

別のターミナルでクライアントを実行します。

```bash
uv run python main.py
```

`main.py` は次の内容でチャット補完 API を呼び出します。

- API ベース URL: `http://localhost:8000/v1`
- モデル: `nvidia/Qwen3.6-27B-NVFP4`
- プロンプト: `日本語で自己紹介して`
- 最大生成トークン数: `1000`

## モデルや設定を変更する

別のモデルを使う場合は、以下の2箇所を同じモデル名に変更してください。

- `vllm_server.sh` の `vllm serve ...`
- `main.py` の `model=...`

ポートを変更する場合は、以下の2箇所を合わせて変更してください。

- `vllm_server.sh` の `--port`
- `main.py` の `base_url`

## トラブルシューティング

### `Connection refused` が出る

vLLM サーバーが起動していない、または `main.py` の `base_url` とサーバーのポートが一致していない可能性があります。

### GPU メモリ不足で起動できない

`vllm_server.sh` の以下の値を調整してください。

- `--max-model-len`
- `--max-num-seqs`
- `--gpu-memory-utilization`

より小さいモデルに変更することも検討してください。

### 認証について

現在の `main.py` では `api_key="dummy"` を指定しています。vLLM 側で API キー認証を有効にしていない場合、この値は任意です。
