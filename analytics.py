def show_price_chart(products):
    """Display a simple bar chart. Matplotlib must be installed for this feature."""
    if not products:
        print("No matching products to display.")
        return
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Charts need Matplotlib. Install it with: python -m pip install matplotlib")
        return

    store_names = []
    prices = []

    for product in products:
        store_names.append(product["store"])
        prices.append(product["price"])

    plt.bar(store_names, prices)
    plt.title("Price Comparison: " + products[0]["name"])
    plt.xlabel("Store")
    plt.ylabel("Price (Rs.)")
    plt.tight_layout()
    plt.show()
