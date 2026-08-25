import requests
from pathlib import Path


API_URL = "https://anapioficeandfire.com/api/houses"
PAGE_SIZE = 100
OUTPUT_FILE = Path(__file__).parent.parent / "output" / "houses.txt"


def fetch_houses():
    """Fetch all houses from the API using pagination."""
    all_houses = []
    page = 1

    while True:
        response = requests.get(
            API_URL,
            params={
                "page": page,
                "pageSize": PAGE_SIZE
            },
            timeout=10
        )

        response.raise_for_status()

        houses = response.json()

        if not isinstance(houses, list):
            raise ValueError("API response is not a list.")

        if not houses:
            break

        all_houses.extend(houses)
        page += 1

    return all_houses


def extract_house_data(houses):
    """Extract valid house names and regions from API data."""
    house_list = []

    for house in houses:
        if not isinstance(house, dict):
            continue

        house_name = house.get("name")
        region = house.get("region", "")

        if not isinstance(house_name, str):
            continue

        if not isinstance(region, str):
            region = str(region)

        house_name = house_name.strip()
        region = region.strip()

        if house_name:
            house_list.append((house_name, region))

    return house_list


def sort_houses(house_list):
    """Sort houses alphabetically by house name."""
    return sorted(house_list, key=lambda house: house[0].casefold())


def save_to_file(house_list):
    """Save the sorted house data to the output text file."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for house_name, region in house_list:
            file.write(f"{house_name} - {region}\n")


def main():
    """Run the complete Houses of Ice and Fire workflow."""
    print("=" * 55)
    print("           HOUSES OF ICE AND FIRE")
    print("=" * 55)

    try:
        print("\nFetching house data from the API...")

        houses = fetch_houses()

        if not houses:
            raise ValueError("The API returned no house data.")

        print(f"✓ Successfully fetched {len(houses)} houses.")

        house_list = extract_house_data(houses)

        if not house_list:
            raise ValueError("No valid house records were found.")

        print(f"✓ Extracted {len(house_list)} house records.")

        sorted_houses = sort_houses(house_list)

        print("✓ Sorted houses alphabetically.")

        save_to_file(sorted_houses)

        print("✓ Saved results to output/houses.txt.")
        print("\nProcess completed successfully.")
        print("=" * 55)

    except requests.exceptions.Timeout:
        print("\n✗ API request timed out.")

    except requests.exceptions.ConnectionError:
        print("\n✗ Could not connect to the API.")

    except requests.exceptions.HTTPError as error:
        print(f"\n✗ API returned an HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"\n✗ API request failed: {error}")

    except ValueError as error:
        print(f"\n✗ Data validation error: {error}")

    except OSError as error:
        print(f"\n✗ File operation failed: {error}")

    except Exception as error:
        print(f"\n✗ An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()