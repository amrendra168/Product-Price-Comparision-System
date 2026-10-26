# Online Product Price Comparison System

## 1. Introduction
The Online Product Price Comparison System is a beginner-level Python project. It helps a user compare sample prices of the same product from different stores and identify the cheapest offer.

## 2. Problem Statement
A product may be listed at different prices in different stores. Comparing each price manually takes time. This program organizes sample offers in one place and makes comparison easier.

## 3. Objectives
- Read product data from a CSV file.
- Search for products by name.
- Compare offers from different stores.
- Find the lowest price.
- Filter offers by category.
- Save offers and price history in an SQLite database.
- Optionally display a bar chart.

## 4. Technologies Used
- Python
- CSV file handling
- SQLite (`sqlite3`)
- Matplotlib (optional, for charts)
- `unittest` (for tests)

## 5. Main Python Concepts
- Variables and data types
- Lists and dictionaries
- `if-else` conditions
- `for` loops
- Functions and modules
- File handling
- Exception handling
- SQL queries and database operations
- Unit testing

## 6. How the System Works
1. The program reads offers from `products.csv`.
2. The user selects an option from the menu.
3. The program searches, filters, or compares the loaded offers.
4. The user can manually add or update an offer.
5. The user can save offers to SQLite and review saved price history.
6. A chart can be displayed if Matplotlib is installed.

## 7. Sample Data
The CSV contains product name, store, price, category, and a sample URL. The values and URLs are illustrative only and do not represent live shopping prices.

## 8. Testing
Run the tests from the project folder:
```powershell
python -m unittest discover -s tests -v
```
The tests check product search, cheapest-price selection, empty input, category filtering, and sorting.

## 9. Limitations
- Prices are sample values and must be updated manually.
- The program does not fetch live prices from shopping websites.
- The interface is command-line based.
- Charts require the optional Matplotlib package.

## 10. Future Scope
- Add permitted live-price data sources.
- Build a graphical interface if required.
- Add price alerts and more detailed price-history analysis.

## 11. Conclusion
The project demonstrates how basic Python, CSV handling, functions, error handling, and SQLite can be used to create a simple product price comparison tool.
