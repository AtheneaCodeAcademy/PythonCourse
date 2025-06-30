#!/bin/bash

echo "Starting installation process..."

# Switch to the master branch and pull the latest changes
git checkout main
git pull

# Create a virtual environment named 'python_course' if it doesn't exist
if [ ! -d "python_course" ]; then
  echo "Creating virtual environment 'python_course'..."
  python3 -m venv python_course
else
  echo "Virtual environment 'python_course' already exists."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source python_course/bin/activate

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
  echo "Installing dependencies from requirements.txt..."
  pip install --upgrade pip
  pip install -r requirements.txt
else
  echo "requirements.txt file not found."
fi