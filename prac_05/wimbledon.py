"""
Emma Naumann
CP1404 Practical 5

Read and display data about the champions and countries of Wimbledon

Estimate: 30 minutes
Actual: 49 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    """Get records from file and store as a list of lists."""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Create dictionary of champions and set of countries from records."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champions and countries."""
    print("wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print(f"These {len(countries)} countries have won Wimbledon:")
    # print(", ".join(country for country in sorted(countries)))
    print(", ".join(sorted(countries)))


main()
