import os
import subprocess

def run_command():
    # Example: Run a shell command in the generated project directory
    subprocess.run(["echo", "Hello from post_gen_project!"], check=True)

if __name__ == "__main__":
    run_command()