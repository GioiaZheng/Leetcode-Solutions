from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "CATALOG.md"

PROBLEM_DIR_RE = re.compile(r"^(\d{4,})-(.+)$")
TAGS_RE = re.compile(r"^\*\*Tags:\*\*\s*(.+?)\s*$", re.MULTILINE)


def problem_directories():
    return sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir()
        and (match := PROBLEM_DIR_RE.match(path.name))
        and int(match.group(1)) > 0
    )


def title_from_slug(slug):
    return " ".join(word.capitalize() for word in slug.split("-"))


def escape_table_cell(value):
    return value.replace("|", r"\|")


def topics_from_readme(directory):
    readme = directory / "README.md"
    if not readme.is_file():
        return ""

    match = TAGS_RE.search(readme.read_text(encoding="utf-8"))
    if not match:
        return ""

    topics = match.group(1).strip()
    topics = re.sub(r"\s*,\s*", "; ", topics)
    return topics.strip(" .")


def catalog_rows():
    rows = []
    for directory in problem_directories():
        match = PROBLEM_DIR_RE.match(directory.name)
        problem_id, slug = match.groups()
        rows.append(
            {
                "id": problem_id,
                "title": title_from_slug(slug),
                "directory": directory.name,
                "topics": topics_from_readme(directory),
            }
        )
    return rows


def render_catalog(rows):
    lines = [
        "# Problem Catalog",
        "",
        "Generated from problem directories by `python scripts/generate_catalog.py`.",
        "Directory naming follows `problem-id-kebab-case-title` (all lowercase).",
        "",
        f"**Total problems:** {len(rows)}",
        "",
        "| ID | Problem | Directory | Topics |",
        "|---:|---|---|---|",
    ]

    for row in rows:
        directory = row["directory"]
        lines.append(
            "| {id} | {title} | [`{directory}/`]({directory}/) | {topics} |".format(
                id=row["id"],
                title=escape_table_cell(row["title"]),
                directory=directory,
                topics=escape_table_cell(row["topics"]),
            )
        )

    return "\n".join(lines) + "\n"


def main():
    rows = catalog_rows()
    CATALOG.write_text(render_catalog(rows), encoding="utf-8")
    print(f"Generated CATALOG.md with {len(rows)} problem entries.")


if __name__ == "__main__":
    main()
