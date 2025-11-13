#!/bin/bash

# Colores ANSI
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
RESET="\e[0m"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo -e "${BLUE}Windows Setup Shell Script${RESET}"
echo -e "${YELLOW} > Starting installation process...${RESET}"

# Switch to the master branch and pull the latest changes
git checkout main
git pull

# Create a virtual environment named 'python_course' if it doesn't exist
if [ ! -d "venv_course" ]; then
  echo -e "${YELLOW} > Creating virtual environment 'venv_course'...${RESET}"
  python -m venv venv_course
else
  echo -e "${GREEN} > Virtual environment 'venv_course' already exists${RESET}"
fi

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then

  # Activate the virtual environment
  echo -e "${YELLOW} > Activating virtual environment...${RESET}"
  source venv_course/Scripts/activate

  # Install dependencies
  echo -e "${YELLOW} > Installing dependencies from requirements.txt...${RESET}"
  pip install -r requirements.txt
  echo -e "${GREEN} > Virtual environment created successfully${RESET}"
else
  echo -e "${RED} > requirements.txt file not found.${RESET}"
fi
