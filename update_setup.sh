#!/bin/bash

# Name of the virtual environment directory
VENV_DIR="python_course"

# Remove the virtual environment if it exists
if [ -d "$VENV_DIR" ]; then
    echo "Removing existing virtual environment..."
    rm -rf "$VENV_DIR"
else
    echo "No existing virtual environment found. A new one will be created."
fi

# Create a new virtual environment
echo "Creating a new virtual environment..."
python3 -m venv "$VENV_DIR"

# Activate the virtual environment
echo "Activating the virtual environment..."
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
    echo "Virtual environment is ready and dependencies are installed."
else
    echo "Error: requirements.txt file not found"
    deactivate
    exit 1
fi
