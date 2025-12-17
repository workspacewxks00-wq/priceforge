from config_loader import load_targets
from scraper import scrape_target
from exporters import export_results

def main():
    targets = load_targets()
    results = []

    for target in targets:
        result = scrape_target(target)
        if result:
            results.append(result)

    if results:
        export_results(results)
        print("Scraping completed. Files saved to output/")
    else:
        print("No data scraped.")

if __name__ == "__main__":
    main()
