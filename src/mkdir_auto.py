import os
import shutil

# 基本ディレクトリ
base_dirs = [
    "bin",
    "data",
    "discard",
    "docs",
    "logs",
    "resources",
    "src",
    "test",
    "lib",
    "venv"
]

# サブディレクトリ
sub_dirs = [
    "data/cache"
]

# 作成するファイル
files = [
    "docs/architecture.md",
    ".gitignore",
    "README.md"
]

# Git管理対象から除外するディレクトリ・ファイル
gitignore_content = """\
# バイナリや一時ファイル
bin/
data/
discard/
logs/
resources/
test/
lib/
venv/

# 一時ファイル
*.log
*.tmp
"""

def create_project_structure():
    """ディレクトリとファイルを適切に作成する"""

    # 基本ディレクトリの作成
    for directory in base_dirs:
        os.makedirs(directory, exist_ok=True)

    # サブディレクトリの作成
    for sub_dir in sub_dirs:
        os.makedirs(sub_dir, exist_ok=True)
        
    # ファイルの作成
    for file in files:
        with open(file, "w", encoding='utf-8') as f:
            pass  # 空のファイルを作成
        
     # .gitignoreにデフォルトで追加"
    gitignore_path = ".gitignore"
    with open(gitignore_path, "w", encoding="utf-8") as f:
        f.write(gitignore_content + "\n")  # 改行を追加しながら追記する

    script_src = "mkdir_auto"
    script_dest = "./bin/mkdir_auto"
    if os.path.exists(script_src):
        shutil.move(script_src, script_dest)
        print(f"Moved {script_src} to {script_dest}")

    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
