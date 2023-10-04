import subprocess


def lint_code(file_path):
    """Lints a Python file."""
    subprocess.run(["flake8", file_path])


def format_code(file_path):
    """Formats a Python file."""
    subprocess.run(["black", file_path])


if __name__ == "__main__":
    file_path = input("Enter the path to the Python file: ")
    lint_code(file_path)
    format_code(file_path)
