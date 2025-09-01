import subprocess
import sys


def check_tool(name, command):
    try:
        subprocess.run(command + ["--version"], check=True, capture_output=True)
        print(f"Validation of environment successful: {name} is available.")
    except subprocess.CalledProcessError:
        print(f"Error: {name} is not installed or not available.")
        sys.exit(1)


def check_python_versions():
    try:
        result = subprocess.run(
            ["uv", "python", "list"], check=True, capture_output=True, text=True
        )
    except subprocess.CalledProcessError:
        print("Error: Failed to list Python versions via uv.")
        sys.exit(1)

    installed_versions = result.stdout
    required_versions = ["3.10", "3.11", "3.12", "3.13"]
    missing_versions = [v for v in required_versions if v not in installed_versions]
    if missing_versions:
        print(f"Error: Python versions missing: {', '.join(missing_versions)}")
        sys.exit(1)
    print("Validation successful: Python versions (3.10-3.13) are available via uv.")


def main():
    tools = [
        ("uv", ["uv"]),
        ("ruff", ["ruff"]),
        ("pre-commit", ["pre-commit"]),
        ("git", ["git"]),
    ]
    for name, cmd in tools:
        check_tool(name, cmd)

    check_python_versions()


if __name__ == "__main__":
    main()
