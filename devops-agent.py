import os
import subprocess
import sys
from glob import glob

def run_cmd(cmd, exit_on_fail=True):
    print(f"\n➡️ {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Failed: {cmd}")
        if exit_on_fail:
            sys.exit(1)

def find_main_file():
    # Auto-detect a Python entrypoint (fallback: app.py)
    py_files = [f for f in os.listdir('.') if f.endswith('.py') and not f.startswith('devops-agent')]
    if not py_files:
        print("❌ No Python entrypoint (e.g. app.py) found.")
        sys.exit(1)
    return py_files[0]

def check_file(filename):
    if not os.path.exists(filename):
        print(f"❌ Missing: {filename}")
        sys.exit(1)

def setup_git(github_repo):
    if not os.path.isdir(".git"):
        run_cmd("git init")
        run_cmd(f"git remote add origin {github_repo}")
    run_cmd("git add .")
    run_cmd('git commit -m "Auto commit from DevOps Agent"')
    run_cmd("git branch -M main")
    run_cmd("git push -u origin main")

def docker_login():
    print("\n🔐 Docker Login (you'll be prompted once)")
    run_cmd("docker login")

def build_and_push_docker(image_name):
    run_cmd(f"docker build -t {image_name} .")
    run_cmd(f"docker push {image_name}")

def run_container(image_name):
    run_cmd(f"docker run -d -p 5000:5000 {image_name}", exit_on_fail=False)

def main():
    print("🧠 DevOps Agent: GitHub & Docker Automation")

    github_repo = input("🔗 Enter your GitHub repo URL: ").strip()
    docker_image = input("🐳 Enter Docker image name (username/repo): ").strip()
    run_container_flag = input("🚀 Run container after push? (y/n): ").strip().lower() == "y"

    # Check for required files
    check_file("Dockerfile")
    entry = find_main_file()
    print(f"✅ Found entrypoint: {entry}")

    # Run pipeline
    setup_git(github_repo)
    docker_login()
    build_and_push_docker(docker_image)

    if run_container_flag:
        run_container(docker_image)

    print("\n✅ All done. Your code is live and containerized.")

if __name__ == "__main__":
    main()