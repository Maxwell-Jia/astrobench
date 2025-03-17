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