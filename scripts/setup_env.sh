#!/bin/bash
# Setup Python virtual environment

echo ">>> Setting up Python environment..."

# Create virtual environment
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install base dependencies
pip install numpy scipy scikit-learn torch torchvision matplotlib

echo ">>> Environment setup complete."
