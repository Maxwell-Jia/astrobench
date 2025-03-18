# astrobench

## Installation

### Using uv (Recommended)

For installing with [uv](https://github.com/astral-sh/uv), follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/astrobench.git
cd astrobench

# Create and activate venv environment
uv venv . --python 3.11
source .venv/bin/activate

# Install dependencies with uv
uv pip install .

# Install flash-attn (Optional, recommended for better performance)
uv pip install flash-attn --no-build-isolation
```

For uv installation instructions, refer to the [official documentation](https://github.com/astral-sh/uv#installation).

### Using conda

```bash
# Clone the repository
git clone https://github.com/yourusername/astrobench.git
cd astrobench

# Create and activate conda environment
conda create -n astrobench python=3.11
conda activate astrobench

# Install the package
pip install .

# Install flash-attn (Optional, recommended for better performance)
pip install flash-attn --no-build-isolation
```

## Results

| Model | Astrobench-MCQ | GPQA-astro | SuperGPQA-astro |
| --- | --- | --- | --- |
| deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B | 51.9 | 38.1 | 16.5 |
| Qwen/Qwen2.5-72B-Instruct | 81.0 | 40.5 | 40.0 |
| Qwen/Qwen2-72B-Instruct | 78.4 | 31.0 | 30.1 |
| AstroOne/Qwen2-72B-tianwen-48b-cpt-sft | 76.1 | 21.4 | 25.7 |
| openai/gpt-4o | - | 45.2 | 42.2 |
| openai/chatgpt-4o-latest (2025.03) | - | 66.7 | 52.1 |