# FileSystem Project

This project contains a Python script (`fileSystem.py`) designed to create a large-scale file system with a specified directory structure and file content. The script is intended for testing purposes, allowing you to simulate the creation of 1 billion files in a nested directory structure. This README provides instructions on how to set up, run, and test the script both locally and inside a Docker container.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Script Locally](#running-the-script-locally)
- [Running the Script in Docker](#running-the-script-in-docker)
- [Code Quality and Style Checking with Flake8](#code-quality-and-style-checking-with-flake8)
- [Generating Documentation with Sphinx](#generating-documentation-with-sphinx)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.8 or higher
- Docker (if running in a container)
- [Flake8](https://flake8.pycqa.org/en/latest/) for code style checking
- [Sphinx](https://www.sphinx-doc.org/en/master/) for generating documentation

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/olaeben/filesystem-project.git
   cd filesystem-project
   
2. **Install Python Dependencies**

   #### Install Flake8:
   ```bash
   pip install flake8
   ```
   #### Install Sphinx:

   ```bash
   pip install flake8
   ```

## Running the Script Locally
   To run the script locally:

   Navigate to the directory where fileSystem.py is located.
   Run the script:
   ```bash
   python3 fileSystem.py
   ```

## Running the Script in Docker
   Build the Docker Image:
   ```bash 
   docker build -t filesystem-loader .
   ```
   Run the Docker Container:
   ```bash 
   docker run -it --rm filesystem-loader
   ```
This command will execute the script inside the Docker container.

## Code Quality and Style Checking with Flake8
   Run Flake8:
   ```bash
   flake8 fileSystem.py
   ```

## Generating Documentation with Sphinx
   This project uses Sphinx to generate documentation.
   Generate HTML Documentation after Sphinx has been installed
   
   **Navigate to the docs directory and build the HTML documentation**
   ```bash
   cd docs
   make html
   ```

   The generated documentation will be available as `index.html` file in the  `_build/html` directory.

   Open it in a browser:
   ```bash 
   open _build/html/index.html  # macOS
   xdg-open _build/html/index.html  # Linux
   start _build/html/index.html  # Windows
   ```

   ## Contributing
   If you want to contribute to this project, please fork the repository, create a new branch, make your changes, and submit a pull request. Contributions are welcome!

   ## License
   This project is licensed under the MIT License. 