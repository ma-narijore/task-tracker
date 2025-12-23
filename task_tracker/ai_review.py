import os
import subprocess

# -------------------------
# 1️⃣ Set repo root
# -------------------------
repo_root = os.path.dirname(os.path.abspath(__file__))  # location of this script
os.chdir(repo_root)

# -------------------------
# 2️⃣ Get list of changed files
# -------------------------
changed_files = subprocess.getoutput("git diff --name-only origin/main").splitlines()

if not changed_files:
    print("No changed files detected.")
    exit()

# -------------------------
# 3️⃣ Process each Python file
# -------------------------
for file_path in changed_files:
    # Remove leading folder if needed
    if file_path.startswith("task_tracker/"):
        file_path = file_path[len("task_tracker/"):]

    if not file_path.endswith(".py"):
        continue

    if not os.path.isfile(file_path):
        print(f"Skipping non-existent file: {file_path}")
        continue

    with open(file_path, encoding="utf-8") as f:
        code = f.read()

    # -------------------------
    # 4️⃣ Mock AI Review (free version)
    # -------------------------
    review_text = f"""
[MOCK AI REVIEW]
File: {file_path}

- This is a mock review for testing purposes.
- The script detected {len(code.splitlines())} lines of code.
- Suggestions, best practices, and security checks would appear here if using the real OpenAI API.
"""

    print(f"\n--- AI Review for {file_path} ---\n")
    print(review_text)
