# Python Linting and Testing

This repository is set up to automate Python code linting using [flake8](https://flake8.pycqa.org/en/latest/) and includes a basic Python script for testing.

## Table of Contents

- [Workflow](#workflow)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
    - [Running the Linter](#running-the-linter)
    - [Running the Test](#running-the-test)
    - [Workflow Usage](#workflow-usage)
- [Contributing](#contributing)

## Workflow

This repository is configured with GitHub Actions to run linting on every push to the `main` branch and on every pull request to the `main` branch. The linting workflow checks your Python code for `PEP8` compliance using `flake8`.

If the linting checks fail, the workflow will indicate that there are `PEP8` violations in the code, and the pull request or push will be marked as failed.

## Getting Started

### Prerequisites

Before you get started, make sure you have the following prerequisites installed:

- Python 3.10.12
- pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```
2. Install Python 3.10.12 if you haven't already.

3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Linter

To manually run the `flake8` linter on your Python code, use the following command:

```bash
flake8 .
```

This will check your code for `PEP8` compliance and report any violations.

### Running the test

To manually run the basic Python script for testing, use the following command:

```bash
python linter.py
```

This script will prompt you to enter the path to a Python file, and it will then run the `flake8` linter on that file.

### Workflow Usage

The linting workflow (`lint.yml`) is configured to run automatically when you push code to the `main` branch or create a pull request to the `main` branch. It checks your Python code for `PEP8` compliance and fails the workflow if any violations are found. You can review the workflow status in the GitHub Actions tab of your repository.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to your forked repository on GitHub.
6. Create a pull request to merge your changes into the main branch of the original repository.
