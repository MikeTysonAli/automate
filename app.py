import requests
import os

BASE_URL = "http://127.0.0.1:5000"  # Change this if your Flask app runs on a different server

# Function to get email details
def get_email_details():
    print("\n=== Email Sending Automation ===")
    sender_email = input("Enter your sender email: ").strip()
    sender_name = input("Enter your name: ").strip()
    receiver_emails = input("Enter receiver emails (comma-separated): ").strip()
    email_subject = input("Enter the email subject (press Enter for 'No Subject'): ").strip() or "No Subject"
    email_body = input("Enter the email body: ").strip()
    is_html = input("Send as HTML? (yes/no): ").strip().lower() == "yes"

    if not sender_email or not sender_name or not receiver_emails or not email_body:
        print("Error: Missing required parameters.")
        return None

    return {
        "sender_email": sender_email,
        "sender_name": sender_name,
        "receiver_emails": receiver_emails,
        "email_subject": email_subject,
        "email_body": email_body,
        "is_html": str(is_html).lower()
    }

# Function to organize files
def get_organize_files_details():
    print("\n=== File Organizer ===")
    path = input("Enter the directory path to organize: ").strip()

    if not path or not os.path.exists(path):
        print("Error: Invalid directory path.")
        return None

    return {"path": path}

# Function to convert PNG to JPG
def get_png_to_jpg_details():
    print("\n=== PNG to JPG Converter ===")
    folder_path = input("Enter the folder path containing PNG files: ").strip()

    if not folder_path or not os.path.exists(folder_path):
        print("Error: Invalid directory path.")
        return None

    return {"folder_path": folder_path}

# Function to convert CSV to Excel
def get_csv_to_excel_details():
    print("\n=== CSV to Excel Converter ===")
    csv_files = input("Enter CSV filenames (comma-separated): ").strip()
    separator = input("Enter separator (default is ','): ").strip() or ","
    excel_name = input("Enter output Excel filename (with .xlsx extension): ").strip()

    if not csv_files or not excel_name:
        print("Error: Missing required parameters.")
        return None

    return {"csv_files": csv_files, "separator": separator, "excel_name": excel_name}

# Function to send a request to the Flask API
def send_request(endpoint, params):
    print(f"\nProcessing request for {endpoint}...")
    response = requests.get(f"{BASE_URL}/{endpoint}", params=params)

    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.json())

# Main Menu
def main():
    while True:
        print("\n=== Automation Tools ===")
        print("1. Send Email")
        print("2. Organize Files")
        print("3. Convert PNG to JPG")
        print("4. Convert CSV to Excel")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            params = get_email_details()
            if params:
                send_request("send-email", params)
        elif choice == "2":
            params = get_organize_files_details()
            if params:
                send_request("organize-files", params)
        elif choice == "3":
            params = get_png_to_jpg_details()
            if params:
                send_request("convert-png-to-jpg", params)
        elif choice == "4":
            params = get_csv_to_excel_details()
            if params:
                send_request("csv-to-excel", params)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
