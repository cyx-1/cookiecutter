import os
import subprocess

def run_command():
    # activate virtual environment, git and establish local main branch
    subprocess.run(["cmd", "/c", "echo activating git, git local main branch, and uv library installation"], check=True)
    subprocess.run(["cmd", "/c", "cd {{ cookiecutter.project_name }}; git init; git branch -M main; uv sync"], check=True)

if __name__ == "__main__":
    run_command()