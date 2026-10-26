# Online Product Price Comparison System

A beginner-friendly Python command-line project that compares product prices from sample CSV data.

## Features
- View all available product offers
- Search products by name
- Compare prices across stores
- Show the cheapest offer (including ties)
- Filter products by category
- Add or update an offer in the CSV file
- Save offers and price history to an SQLite database
- Optionally create a simple price comparison chart

**Note:** The included prices and store names are sample data for learning. They are not live prices. Live collection from shopping websites is not included in this basic version.

## Requirements
- Python 3.10 or newer
- VS Code (recommended)
- Matplotlib is optional and only needed for charts

## Run on Windows 11
1. Extract the ZIP file.
2. Open the `online_product_price_comparison` folder in VS Code.
3. Open Terminal > New Terminal.
4. Check Python:
   ```powershell
   python --version
   ```
5. Run the program:
   ```powershell
   python main.py
   ```

## Optional charts
Install Matplotlib:
```powershell
python -m pip install -r requirements.txt
```
Then select the chart option in the program.

## Files
- `main.py`: menu and program flow
- `comparison.py`: search, sorting, and cheapest-price logic
- `data_loader.py`: reads and writes the CSV file
- `data_collector.py`: adds or updates sample offers manually
- `database.py`: saves offers and price history in SQLite
- `analytics.py`: optional chart
- `products.csv`: sample product data
- `tests/test_comparison.py`: basic automated tests
- `project_report.md`: project report draft
- `viva_questions.md`: viva questions and answers

The SQLite database (`prices.db`) is created automatically when you save data to it.
