import re
from collections import defaultdict
from pathlib import Path

from generate_catalog import catalog_rows, escape_table_cell

TOPICS = Path(__file__).resolve().parent.parent / "TOPICS.md"

CATEGORY_ALIASES = {
    "Array": "Arrays & Matrices",
    "Matrix": "Arrays & Matrices",
    "Grid": "Arrays & Matrices",
    "String": "Strings",
    "Parsing": "Strings",
    "Pattern Matching": "Strings",
    "String Validation": "Strings",
    "Hash Table": "Hashing",
    "Hash Map": "Hashing",
    "Hash Set": "Hashing",
    "Hashing": "Hashing",
    "Two Pointers": "Two Pointers & Sliding Window",
    "Sliding Window": "Two Pointers & Sliding Window",
    "Binary Search": "Binary Search",
    "Feasibility Check": "Binary Search",
    "Sorting": "Sorting & Heap",
    "Bucket Sort": "Sorting & Heap",
    "Heap": "Sorting & Heap",
    "Heap (Priority Queue)": "Sorting & Heap",
    "Greedy": "Greedy",
    "Dynamic Programming": "Dynamic Programming",
    "Knapsack": "Dynamic Programming",
    "Memoization": "Dynamic Programming",
    "State Machine": "Dynamic Programming",
    "Stock Trading": "Dynamic Programming",
    "Subsequence": "Dynamic Programming",
    "Tree DP": "Dynamic Programming",
    "Graph": "Graph & Tree",
    "BFS": "Graph & Tree",
    "BFS / Simulation": "Graph & Tree",
    "Breadth-First Search": "Graph & Tree",
    "DFS": "Graph & Tree",
    "Depth-First Search": "Graph & Tree",
    "Tree": "Graph & Tree",
    "Binary Tree": "Graph & Tree",
    "Lowest Common Ancestor": "Graph & Tree",
    "Math": "Math & Counting",
    "Combinatorics": "Math & Counting",
    "Counting": "Math & Counting",
    "Modular Arithmetic": "Math & Counting",
    "Modulo": "Math & Counting",
    "Number Theory": "Math & Counting",
    "Parity": "Math & Counting",
    "Pigeonhole Principle": "Math & Counting",
    "Geometry": "Geometry",
    "Prefix Area": "Geometry",
    "Sweep Line": "Geometry",
    "Backtracking": "Backtracking & Search",
    "Brute Force": "Backtracking & Search",
    "Enumeration": "Backtracking & Search",
    "Simulation": "Simulation",
    "Timeline Processing": "Simulation",
    "Stack": "Stack & Monotonic Structures",
    "Monotonic Stack": "Stack & Monotonic Structures",
    "Prefix Sum": "Prefix & Difference Techniques",
    "Prefix Min/Max": "Prefix & Difference Techniques",
    "Prefix/Suffix Frequency": "Prefix & Difference Techniques",
    "Consecutive Segment Counting": "Prefix & Difference Techniques",
    "Linked List": "Linked Lists",
    "Segment Tree": "Advanced Data Structures",
    "Caching": "Other Techniques",
    "Divide and Conquer": "Other Techniques",
    "Partitioning": "Other Techniques",
}

CATEGORY_ORDER = [
    "Arrays & Matrices",
    "Strings",
    "Hashing",
    "Two Pointers & Sliding Window",
    "Binary Search",
    "Sorting & Heap",
    "Greedy",
    "Dynamic Programming",
    "Graph & Tree",
    "Math & Counting",
    "Geometry",
    "Backtracking & Search",
    "Simulation",
    "Stack & Monotonic Structures",
    "Prefix & Difference Techniques",
    "Linked Lists",
    "Advanced Data Structures",
    "Other Techniques",
    "Untagged",
]


def category_for(topic):
    return CATEGORY_ALIASES.get(topic, "Other Techniques")


def slug(value):
    value = value.lower()
    value = re.sub(r"[^a-z0-9 -]", "", value)
    value = re.sub(r"\s+", "-", value.strip())
    return value


def topic_groups(rows):
    groups = defaultdict(list)
    for row in rows:
        topics = [topic.strip() for topic in row["topics"].split(";") if topic.strip()]
        if not topics:
            topics = ["Untagged"]

        row_categories = {category_for(topic) for topic in topics}
        for category in row_categories:
            groups[category].append(row)

    ordered = {}
    for category in CATEGORY_ORDER:
        if category in groups:
            ordered[category] = sorted(groups[category], key=lambda item: int(item["id"]))
    return ordered


def render_topics(groups):
    lines = [
        "# Topic Index",
        "",
        (
            "Generated from `metadata.json` and problem directories by "
            "`python scripts/generate_topics.py`."
        ),
        "Problems can appear in multiple sections when their metadata has multiple topics.",
        "",
        "## Major Topics",
        "",
    ]

    for topic, rows in groups.items():
        anchor = slug(topic)
        lines.append(f"- [{topic}](#{anchor}) ({len(rows)})")

    for topic, rows in groups.items():
        lines.extend(
            [
                "",
                f"## {topic}",
                "",
                "| ID | Problem | Difficulty | Status | Directory | Original Topics |",
                "|---:|---|---|---|---|---|",
            ]
        )
        for row in rows:
            directory = row["directory"]
            lines.append(
                (
                    "| {id} | {title} | {difficulty} | {status} | "
                    "[`{directory}/`]({directory}/) | {topics} |"
                ).format(
                    id=row["id"],
                    title=escape_table_cell(row["title"]),
                    difficulty=escape_table_cell(row["difficulty"]),
                    status=escape_table_cell(row["status"]),
                    directory=directory,
                    topics=escape_table_cell(row["topics"] or "Untagged"),
                )
            )

    return "\n".join(lines) + "\n"


def main():
    groups = topic_groups(catalog_rows())
    TOPICS.write_text(render_topics(groups), encoding="utf-8")
    print(f"Generated TOPICS.md with {len(groups)} topic sections.")


if __name__ == "__main__":
    main()
