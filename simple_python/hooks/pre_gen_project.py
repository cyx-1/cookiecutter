import subprocess
import sys

def main():
    try:
        subprocess.run(['uv', '--version'], check=True, capture_output=True)
        print("Validation of environment successful: uv is available.")
    except subprocess.CalledProcessError:
        print("Error: uv is not installed or not available.")
        sys.exit(1)

    try:
        subprocess.run(['ruff', '--version'], check=True, capture_output=True)
        print("Validation of environment successful: ruff is available.")
    except subprocess.CalledProcessError:
        print("Error: ruff is not installed or not available.")
        sys.exit(1)

    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True)
        print("Validation of environment successful: git is available.")
    except subprocess.CalledProcessError:
        print("Error: git is not installed or not available.")
        sys.exit(1)

    try:
        result = subprocess.run(['uv', 'python', 'list'], check=True, capture_output=True, text=True)
        installed_versions = result.stdout
        required_versions = ['3.10', '3.11', '3.12', '3.13']
        missing_versions = [v for v in required_versions if v not in installed_versions]
        if missing_versions:
            print(f"Error: The following Python versions are not installed via uv: {', '.join(missing_versions)}")
            sys.exit(1)
        print("Validation of environment successful: All required Python versions (3.10, 3.11, 3.12, 3.13) are available via uv.")
    except subprocess.CalledProcessError:
        print("Error: Failed to list Python versions via uv.")
        sys.exit(1)

if __name__ == "__main__":
    main()