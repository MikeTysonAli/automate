import requests
from bs4 import BeautifulSoup
import pandas as pd
import smtplib

# Step 1: User Inputs
sender_email = input("Enter your email: ")
sender_password = input("Enter your email password: ")  # Use environment variables for security
url = input("Enter the website URL to scrape leads: ")
filename = input("Enter the filename to save leads (e.g., leads.xlsx): ")

# Step 2: Scrape Business Leads
def scrape_leads(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    leads = []
    for lead in soup.find_all("div", class_="lead-info"):
        name = lead.find("h2").text.strip()
        email = lead.find("a", href=True).text.strip()
        leads.append({"Name": name, "Email": email})
    
    return leads

# Step 3: Save Leads in Excel
def save_to_excel(leads, filename):
    df = pd.DataFrame(leads)
    df.to_excel(filename, index=False)
    print(f"Leads saved to {filename}")

# Step 4: Send Automated Emails
def send_email(sender_email, sender_password, to_email, name):
    subject = "Special Offer for You!"
    body = f"Hello {name},\n\nWe are excited to connect with you. Let's discuss how we can collaborate.\n\nBest Regards,\nYour Company"

    message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message)
        server.quit()
        print(f"Email sent to {name} ({to_email})")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Step 5: Run the Automation
def main():
    leads = scrape_leads(url)

    if leads:
        save_to_excel(leads, filename)
        
        # Ask if user wants to send emails
        send_emails = input("Do you want to send emails to the scraped leads? (yes/no): ").strip().lower()
        if send_emails == "yes":
            for lead in leads:
                send_email(sender_email, sender_password, lead["Email"], lead["Name"])
        else:
            print("Emails were not sent.")
    else:
        print("No leads found.")

# Run the script
if __name__ == "__main__":
    main()
