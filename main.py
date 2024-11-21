
import json

from backend.webScraping.source.googleMaps import fetch_business_data

if __name__ == "__main__":
    search_query = "Restaurante em Guarapari"
    scroll_limit = 4

    # Fetch business data
    business_results = fetch_business_data(search_query, scroll_limit)

    # Save results to a JSON file
    with open("business_data.json", "w", encoding="UTF-8") as file:
        json.dump(business_results, file, indent=6, ensure_ascii=False)

    print("Process completed. Results saved in 'business_data.json'.")
