# Library App

A Django-based web application for searching library books and retrieving call numbers.

## Features

- **Search for Books**: Users can search for books by entering keywords.
- **Multiple Keyword Search**: Supports searching for multiple books at once by separating keywords with commas (e.g., `Book1, Book2, Book3`).
- **Web Scraping**: Retrieves book data (title, call number, library location, and availability status) from the Yeosu Library website.
- **Error Handling**: Displays user-friendly error messages if no keywords are provided or if an issue occurs during the scraping process.
- **Responsive UI**: Search results are displayed in a clean and organized format.

## How It Works

1. **Search Form**:
   - Users enter one or more keywords in the search form.
   - Keywords are separated by commas for multiple searches.

2. **Data Retrieval**:
   - The application sends a request to the Yeosu Library website using the provided keywords.
   - Book details are scraped using BeautifulSoup.

3. **Display Results**:
   - The retrieved book data is displayed on the results page, including:
     - Title
     - Call Number
     - Library Location
     - Availability Status

4. **Error Handling**:
   - If no keywords are entered, an error message prompts the user to provide input.
   - If an error occurs during the scraping process (e.g., website issues), an error message is displayed.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd library_app
