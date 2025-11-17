#!/bin/bash

# Maya AI Launcher Script

echo "🚀 Starting Maya AI..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt -q

# Run Maya
echo "Starting Maya..."
python main.py

# Deactivate on exit
deactivate
