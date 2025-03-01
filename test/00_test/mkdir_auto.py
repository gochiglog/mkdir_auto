import os

# 基本ディレクトリ
base_dirs = [
    "bin",
    "data",
    "discard",
    "docs",
    "logs",
    "resources",
    "src",
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
        with open(file, "w") as f:
            pass  # 空のファイルを作成

    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
