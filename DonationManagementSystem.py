import os

# File name for storing donations
donation_file = "donations.txt"

# Static Dataset of Donations
donations = {
    1: {'donor': 'Alice Johnson', 'amount': 100, 'date': '2025-02-25', 'purpose': 'Charity'},
    2: {'donor': 'Bob Smith', 'amount': 50, 'date': '2025-02-26', 'purpose': 'Education'},
    3: {'donor': 'Charlie Brown', 'amount': 200, 'date': '2025-02-25', 'purpose': 'Medical'},
    4: {'donor': 'David Lee', 'amount': 150, 'date': '2025-02-26', 'purpose': 'Charity'},
    5: {'donor': 'Frank White', 'amount': 120, 'date': '2025-02-27', 'purpose': 'Medical'}
}


# Function 1: Save Donations to File
def save_static_donations():
    """
    Saves the static dataset of donations to the file.
    """
    # Overwrite file with static donations (no duplicates)
    with open(donation_file, 'w') as file:
        for donation_id, donation_data in donations.items():
            file.write(f"{donation_id}|{donation_data}\n")

    return donations


# Function 2: Check If Frank White Donated
def check_frank_white_donated():
    """
    Checks if Frank White has made any donations.
    """
    for donation in donations.values():
        # Case insensitive check for donor name
        if donation['donor'].lower() == 'frank white':
            return True
    return False


# Function 3: Calculate Total Donations
def calculate_total_donations():
    """
    Calculates the total amount donated by all donors.
    """
    total_amount = 0

    # Calculate total donations using Dictionaries and if-else Control Flow
    for donation in donations.values():
        if 'amount' in donation:
            total_amount += donation['amount']
        else:
            total_amount += 0  # If amount is missing, add 0

    return total_amount


# Main Function to Execute and Display Results
def main():
    # Save static donations to file
    print("\n--- Saving Static Donations ---")
    saved_donations = save_static_donations()
    print("Static Donations Saved.")

    # Display all donations
    print("\n--- All Donations ---")
    for donation_id, donation in saved_donations.items():
        print(f"ID: {donation_id}, Details: {donation}")

    # Check if Frank White donated
    print("\n--- Check If Frank White Donated ---")
    frank_donated = check_frank_white_donated()
    if frank_donated:
        print("Yes, Frank White has donated.")
    else:
        print("No, Frank White has not donated.")

    # Calculate total donations
    print("\n--- Calculate Total Donations ---")
    total_amount = calculate_total_donations()
    print(f"Total Amount Donated: ₹{total_amount}")


if __name__ == "__main__":
    main()
