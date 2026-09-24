# ml-foundations

A Python-based study project for learning ML powered by Jupyter Notebooks and managed with **uv**.

## Features
* **Fast Dependency Management**: Built using `uv` for lightning-fast installation and reproducible environments.
* **Jupyter Integration**: Pre-configured for seamless development in Jupyter Lab / Notebooks.
* **Isolated Environment**: Clean separation of development and production dependencies.

## Prerequisites

Before running the project, ensure you have `uv` installed. If you don't have it yet, install it via curl (macOS/Linux) or PowerShell (Windows):

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Getting Started

Follow these steps to clone the repository, set up the environment, and launch the Jupyter server.

### 1. Clone the Repository
```bash
git clone https://github.com/miroshnichenkoai/ml-foundations.git
cd ml-foundations
```

### 2. Install Dependencies
Initialize the virtual environment and install all required packages using `uv`:
```bash
uv sync
```

### 3. Launch Jupyter Lab
Run Jupyter Lab directly within the project's virtual environment:
```bash
uv run --with jupyter jupyter lab
```

Alternatively, if you prefer the classic Jupyter Notebook interface:
```bash
uv run --with jupyter jupyter notebook
```