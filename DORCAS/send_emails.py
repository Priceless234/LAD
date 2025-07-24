import smtplib
import pymysql

# Database Connection
conn = pymysql.connect(host='localhost', user='root', password='', database='ShoppingMallDB')
cursor = conn.cursor()

# Fetch Pending Orders
cursor.execute("SELECT ProductID, QuantityOrdered, SupplierEmail FROM Orders WHERE Status = 'Pending'")
orders = cursor.fetchall()

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "ajiboyedorcasmercy123@gmail.com"
EMAIL_PASSWORD = "Afolake@1506"

for order in orders:
    product_id, quantity, supplier_email = order
    
    subject = "New Order for Product ID: {}".format(product_id)
    body = "Hello,\n\nA new order has been placed for Product ID {}. Please supply {} units.\n\nThank you.".format(product_id, quantity)
    email_text = "Subject: {}\n\n{}".format(subject, body)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, supplier_email, email_text)
            print(f"Email sent to {supplier_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

conn.close()