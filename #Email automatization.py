#Email automatization 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def authenticate_email(username, password):
    try:
        # Establish a secure session with Gmail's outgoing SMTP server using your gmail account
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Log in with your email credentials
        server.login(username, password)
        
        print("Logged in successfully")
        return server
    except Exception as e:
        print(f"Failed to log in: {e}")
        return None

# Replace with your email and app-specific password
username = "your_email@gmail.com"
password = "your_password"

server = authenticate_email(username, password)

if server:
    # You can now use the server object to send emails
    server.quit()