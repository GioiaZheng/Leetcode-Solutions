import generate_catalog
import generate_topics
import update_stats


def main():
    generate_catalog.main()
    generate_topics.main()
    metrics = update_stats.collect_metrics()
    update_stats.update_readme(metrics)

    print("Updated README metrics:")
    for name, count in metrics.items():
        print(f"- {name}: {count}")


if __name__ == "__main__":
    main()
