from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import re
import numpy as np

def scrape_flipkart_reviews(url, product_name):
    # Initialize the WebDriver for Safari
    browser = webdriver.Safari()

    # Open the provided URL
    browser.get(url)

    # Lists to store all data
    all_data = []
    total_reviews_loaded = 0  # Track total reviews loaded
    current_page = 1  # Track current page number

    try:
        # Loop through each page
        while True:
            try:
                # Click all "READ MORE" links to expand the reviews
                read_more_links = browser.find_elements(By.XPATH, "//span[contains(text(),'READ MORE')]")
                for link in read_more_links:
                    try:
                        browser.execute_script("arguments[0].click();", link)
                        time.sleep(1)  # Add a small delay to ensure the content loads

                        # Ensure the review content is expanded and doesn't contain "READ MORE"
                        expanded_reviews = WebDriverWait(browser, 10).until(
                            EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'ZmyHeo') and not(contains(text(), 'READ MORE'))]"))
                        )
                    except Exception as e:
                        print(f"Error clicking 'READ MORE': {e}")

                # Extract all review elements using your provided XPath
                review_elements = browser.find_elements(By.XPATH, "//div[contains(@class, 'ZmyHeo')]")

                # Extract all rating elements using your provided XPath
                rating_elements = browser.find_elements(By.XPATH, "//div[contains(@class, 'XQDdHH')]")

                # Extract all dislikes using your provided XPath
                dislikes_elements = browser.find_elements(By.XPATH, "//div[contains(@class, '_6kK6mk') and contains(@class, 'aQymJL')]//span[contains(@class, 'tl9VpF')]")

                # Extract all likes using your provided XPath
                likes_elements = browser.find_elements(By.XPATH, "//div[contains(@class, '_6kK6mk') and not(contains(@class, 'aQymJL'))]//span[contains(@class, 'tl9VpF')]")

                # Debug: Print number of elements found
                print(f"Page {current_page}: Found {len(review_elements)} reviews")

                # Loop through each review, rating, likes, and dislikes element on the current page
                reviews_loaded_on_page = 0  # Track reviews loaded per page
                for review, rating, likes, dislikes in zip(review_elements, rating_elements, likes_elements, dislikes_elements):
                    try:
                        # Handle possible missing or non-integer values for likes and dislikes
                        likes_text = likes.text.replace(',', '') if likes else '0'
                        dislikes_text = dislikes.text.replace(',', '') if dislikes else '0'
                        likes_count = int(likes_text) if likes_text.isdigit() else 0
                        dislikes_count = int(dislikes_text) if dislikes_text.isdigit() else 0

                        # Append the extracted data to the list
                        all_data.append({
                            'Product Name': product_name,
                            'Rating': rating.text if rating else 'N/A',
                            'Review': review.text.strip().replace('READ MORE', ''),  # Remove 'READ MORE' and trim extra spaces
                            'Likes': likes_count,
                            'Dislikes': dislikes_count
                        })
                        reviews_loaded_on_page += 1
                        total_reviews_loaded += 1
                    except Exception as e:
                        print(f"Error processing review data: {e}")

                # Print reviews loaded on the current page
                print(f"Page {current_page}: Reviews loaded: {reviews_loaded_on_page}")

                # Check if there's a "Next" button and navigate to the next page
                try:
                    next_button = WebDriverWait(browser, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]"))
                    )
                    # Use JavaScript to click the "Next" button to avoid the interception issue
                    browser.execute_script("arguments[0].click();", next_button)
                    current_page += 1
                    time.sleep(3)  # Adding a delay to ensure the next page loads
                except Exception as e:
                    print(f"An error occurred while navigating to the next page: {e}")
                    break

            except Exception as e:
                print(f"An error occurred on page {current_page}: {e}")
                break

    finally:
        # Close the browser
        browser.quit()

        # Create a DataFrame from the collected data
        if all_data:
            df = pd.DataFrame(all_data)

            # Data Cleaning
            # Clearing the Special Character
            pattern = re.compile(r'[^\x00-\x7F]+')
            df["Review"] = df["Review"].replace({pattern: ' '}, regex=True)
            # Trim spaces from the values in the Review column
            df['Review'] = df['Review'].str.strip()
            # Replace empty strings with NaN
            df['Review'] = df['Review'].replace({'': np.nan})
            # Drop rows where Review is NaN
            df = df.dropna(subset=['Review'])
            # Optionally, reset the index if you want a clean DataFrame without gaps in the index
            df = df.reset_index(drop=True)

            # Save the DataFrame to a CSV file
            csv_filename = f"{product_name.replace(' ', '_')}_reviews.csv"
            df.to_csv(csv_filename, index=False)
            print(f"Total reviews loaded: {total_reviews_loaded}")
            print(f"Reviews saved to {csv_filename}")
        else:
            print("No reviews found. Please check the XPaths and ensure the page is loaded correctly.")

# Example usage
product_url_1 = "https://www.flipkart.com/oneplus-11r-5g-galactic-silver-256-gb/product-reviews/itmd8344a066fd54?pid=MOBGN3BQGU5BRTHZ&lid=LSTMOBGN3BQGU5BRTHZWFOUVK&marketplace=FLIPKART"  # Replace with the actual product link
product_name_1 = "OnePlus 11R 5G (Galactic Silver, 256 GB)"  # Replace with the actual product name

scrape_flipkart_reviews(product_url_1, product_name_1)
