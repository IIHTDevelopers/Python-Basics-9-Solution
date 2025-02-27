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

    # Collect all shipment details
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
        status = shipments[tracking_number]["status"]
        return status
    else:
        return f"Tracking Number {tracking_number} not found."




# Main Function to Execute and Display Results
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


if __name__ == "__main__":
    main()
