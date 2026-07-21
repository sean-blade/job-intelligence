from pathlib import Path

ROOT = Path(__file__).parent.parent
README = ROOT / "README.md"


def generate_tree(path: Path, prefix="") -> list[str]:
    lines = []

    items = sorted(
        [
            item
            for item in path.iterdir()
            if item.name
            not in {
                ".venv",
                ".git",
                "__pycache__",
                ".pytest_cache",
                "job_intelligence.egg-info",
                ".vscode",
                ".mypy_cache",
                ".ruff_cache",
            }
        ],
        key=lambda x: (x.is_file(), x.name.lower()),
    )

    for index, item in enumerate(items):
        connector = "└── " if index == len(items) - 1 else "├── "

        if item.is_dir():
            lines.append(f"{prefix}{connector}{item.name}/")
            lines.extend(
                generate_tree(
                    item, prefix + ("    " if index == len(items) - 1 else "│   ")
                )
            )
        else:
            lines.append(f"{prefix}{connector}{item.name}")

    return lines


def update_readme(tree_text: str):
    readme_text = README.read_text(encoding="utf-8")
    start_marker = "<!-- PROJECT_STRUCTURE_START -->"

    if start_marker not in readme_text:
        raise ValueError("README markers not found")
    end_marker = "<!-- PROJECT_STRUCTURE_END -->"

    start = readme_text.index(start_marker) + len(start_marker)
    end = readme_text.index(end_marker)

    new_readme = readme_text[:start] + "\n\n" + tree_text + "\n\n" + readme_text[end:]

    README.write_text(new_readme, encoding="utf-8")


def main():
    tree = ["```text", f"{ROOT.name}/", *generate_tree(ROOT), "```"]

    tree_text = "\n".join(tree)

    update_readme(tree_text)

    print("README updated successfully.")


if __name__ == "__main__":
    main()
