# wikipedia-scraper

[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 📒 Description

The Wikipedia Scraper is a Python program designed to scrape data from Wikipedia for country leaders. It retrieves data from a custom API endpoint that provides information about leaders of various countries. The program then extracts the first paragraph from the Wikipedia page of each leader and stores this information alongside the leader's data in a json file.

## 📦 Repo structure
.
├── src/
│ └── scraper.py
├── main.py
└── README.md

## 🎮 Usage

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command in your terminal:

    ```
    pip install -r requirements.txt
    ```

3. Run the `main.py` file to execute the scraper:

    ```
    python main.py
    ```

4. The program will retrieve data about country leaders from the custom API endpoint and then scrape the first paragraph from the Wikipedia page of each leader. The resulting data will be saved to a JSON file named "leaders_data.json" in the root directory.

5. The total execution time will be displayed in the terminal upon completion, estimated at ~50seconds.

## ⏱️ Timeline

The development of this project took 2.5 days for completion.

## 📌 Personal Situation

This project was completed as part of a coding exercise or for personal learning purposes.

Connect with me on [LinkedIn](https://www.linkedin.com/in/bear-revels/) for more information.