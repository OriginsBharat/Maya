#!/bin/bash

echo "🚀 Starting Maya AI..."
echo "This is the ONLY script you ever need to run"

# Create directories
mkdir -p maya_data/memories
mkdir -p maya_data/content
mkdir -p maya_data/logs

# Install requirements
pip install -r requirements.txt

# Run auto test
python cloud/auto_test.py

echo "✅ Maya is initialized!"
echo "📓 Now go to Google Colab and run maya_brain.ipynb"
echo "🌐 Maya will handle everything else automatically"
