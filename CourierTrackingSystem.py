# Static Dataset of Shipments
shipments = {
    "TRK1001": {
        "sender": "Alice Johnson",
        "recipient": "Bob Smith",
        "current_location": "New York",
        "status": "In Transit"
    },
    "TRK1002": {
        "sender": "Charlie Brown",
        "recipient": "David Lee",
        "current_location": "Chicago",
        "status": "Delivered"
    },
    "TRK1003": {
        "sender": "Eve Miller",
        "recipient": "Frank White",
        "current_location": "San Francisco",
        "status": "Out for Delivery"
    },
    "TRK1004": {
        "sender": "George Harris",
        "recipient": "Helen Young",
        "current_location": "Los Angeles",
        "status": "In Transit"
    },
    "TRK1005": {
        "sender": "Ian Scott",
        "recipient": "Jane Clark",
        "current_location": "Boston",
        "status": "Delivered"
    }
}


# Function 1: List All Shipments
def list_all_shipments():
    """
    Lists all shipments with their details.
    """
    shipment_list = []

    for tracking_number, details in shipments.items():
        shipment = {
            "tracking_number": tracking_number,
            "sender": details["sender"],
            "recipient": details["recipient"],
            "current_location": details["current_location"],
            "status": details["status"]
        }
        shipment_list.append(shipment)

    return shipment_list


# Function 2: Check Shipment Status
def check_shipment_status(tracking_number):
    """
    Checks the status of a specific shipment using the tracking number.
    """
    if tracking_number in shipments:
        return shipments[tracking_number]["status"]
    else:
        return f"Tracking Number {tracking_number} not found."


# Function 3: Count Shipments by Status
def count_shipments_by_status():
    """
    Returns a dictionary counting the number of shipments per status.
    Example: {'In Transit': 2, 'Delivered': 2, 'Out for Delivery': 1}
    """
    status_counts = {}
    for details in shipments.values():
        status = details["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
    return status_counts


# Optional: Main function to demonstrate functionality
def main():
    # List all shipments
    print("\n--- List of All Shipments ---")
    all_shipments = list_all_shipments()
    for shipment in all_shipments:
        print(shipment)

    # Check shipment status for a specific tracking number
    tracking_number = "TRK1003"
    print(f"\n--- Shipment Status for {tracking_number} ---")
    status = check_shipment_status(tracking_number)
    print(f"Status: {status}")

    # Count shipments by status
    print("\n--- Shipment Count by Status ---")
    status_counts = count_shipments_by_status()
    print(status_counts)


if __name__ == "__main__":
    main()
