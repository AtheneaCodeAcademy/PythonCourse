#!/bin/bash

echo "Starting installation process..."

# Switch to the master branch and pull the latest changes
git checkout main
git pull

# Create a virtual environment named 'python_course' if it doesn't exist
if [ ! -d "venv_course" ]; then
  echo "Creating virtual environment 'venv_course'..."
  python3 -m venv venv_course
else
  echo "Virtual environment 'venv_course' already exists."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv_course/bin/activate

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
  echo "Installing dependencies from requirements.txt..."
  pip install -r requirements.txt
  echo "Virtual environment has been created."
else
  echo "requirements.txt file not found."
fi