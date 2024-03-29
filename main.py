from src.scraper import WikipediaScraper
from time import perf_counter  # For performance measurement
import threading

# Recording the start time of the program execution
start_time = perf_counter()  

if __name__ == "__main__":
    # Create an instance of WikipediaScraper
    wiki_scraper = WikipediaScraper()

    # Refresh the cookie
    wiki_scraper.refresh_cookie()

    # Get leaders for each country and extract first paragraph from Wikipedia URL
    wiki_scraper.get_leaders()

    # Loop over the leaders data and extract details
    threads = []
    for country, leaders in wiki_scraper.leaders_data.items():
        for leader in leaders:
            thread = threading.Thread(target=wiki_scraper.get_first_paragraph, args=(leader['wikipedia_url'], leader))
            thread.start()
            threads.append(thread)
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Save the data to a JSON file
    wiki_scraper.to_json_file("leaders_data.json")

    # Printing the total execution time
    print(f"\nTime spent inside the loop: {perf_counter() - start_time} seconds.")
