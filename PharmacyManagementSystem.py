# Static Dataset of Medicines
medicines = {
    101: {'name': 'Paracetamol', 'category': 'Painkiller', 'price': 10, 'stock': 100},
    102: {'name': 'Amoxicillin', 'category': 'Antibiotic', 'price': 50, 'stock': 25},
    103: {'name': 'Cetirizine', 'category': 'Antihistamine', 'price': 15, 'stock': 60},
    104: {'name': 'Ibuprofen', 'category': 'Painkiller', 'price': 20, 'stock': 80},
    105: {'name': 'Metformin', 'category': 'Antidiabetic', 'price': 30, 'stock': 40}
}


# Function 1: Count Number of Unique Medicines
def count_number_of_unique_medicines():
    """
    Counts the number of unique medicines available.
    """
    unique_medicines = set()

    # Collect all unique medicine names
    for details in medicines.values():
        unique_medicines.add(details['name'])

    # Count the number of unique medicines
    total_unique_medicines = len(unique_medicines)

    return total_unique_medicines


# Function 2: Calculate Total Stock Value
def calculate_total_stock_value():
    """
    Calculates the total stock value of all medicines.
    """
    total_value = 0

    # Calculate stock value for each medicine
    for details in medicines.values():
        stock_value = details['price'] * details['stock']
        total_value += stock_value

    return total_value


# Function 3: Find Medicine with Lowest Stock
def find_medicine_with_lowest_stock():
    """
    Identifies the medicine with the lowest stock quantity.
    """
    lowest_stock = float('inf')
    medicine_name = None

    # Find the medicine with the lowest stock
    for details in medicines.values():
        if details['stock'] < lowest_stock:
            lowest_stock = details['stock']
            medicine_name = details['name']

    return (medicine_name, lowest_stock)


# Main Function to Execute and Display Results
def main():
    # Count number of unique medicines
    print("\n--- Count Number of Unique Medicines ---")
    total_unique_medicines = count_number_of_unique_medicines()
    print(f"Total Unique Medicines: {total_unique_medicines}")

    # Calculate total stock value
    print("\n--- Calculate Total Stock Value ---")
    total_stock_value = calculate_total_stock_value()
    print(f"Total Stock Value: ₹{total_stock_value}")

    # Find the medicine with the lowest stock quantity
    print("\n--- Medicine with Lowest Stock ---")
    lowest_stock = find_medicine_with_lowest_stock()
    print(f"Medicine with Lowest Stock: {lowest_stock[0]} ({lowest_stock[1]} units)")


if __name__ == "__main__":
    main()
