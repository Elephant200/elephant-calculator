#!/bin/bash

# Ensure Python 3.12.5+ is installed
PYTHON=$(which python3)
VERSION=$($PYTHON --version 2>&1 | awk '{print $2}')
REQUIRED="3.12"

if [[ "$VERSION" < "$REQUIRED" ]]; then
    echo "Python 3.12.5 or higher is required. Current version: $VERSION"
    exit 1
fi

# Create a virtual environment
echo "Creating virtual environment..."
$PYTHON -m venv .venv

# Activate the virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate 2>/dev/null || .venv\Scripts\activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create necessary folders
echo "Setting up folder structure..."
mkdir -p reviews
touch reviews/ratings.txt reviews/reviews.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating empty .env file..."
    touch .env
fi

echo "Setup complete! Activate the virtual environment and run the project."
