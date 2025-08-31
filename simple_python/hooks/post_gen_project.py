import subprocess

def run_command():
    commands = [
        ["git", "init"],
        ["git", "branch", "-M", "main"],
        ["uv", "sync"],
        ["git", "add", "-A"],
        ["git", "commit", "-m", "Initial commit"],
        ["git", "log", "--oneline"]
    ]
    for cmd in commands:
        subprocess.run(cmd, check=True)
    print("\n\n\nSuccessfully activated virtual environment using python version {{ cookiecutter.python_version }}.")
    print("Performed uv sync to retreive all the dependencies.")
    print("Initialized Git and created the local main branch. Staged and committed all changes to local git repository.")
    print("\nTo push changes to a remote repository:")
    print("git remote add origin git@github.com:user/repo.git")
    print("git push -u origin main")

if __name__ == "__main__":
    run_command()