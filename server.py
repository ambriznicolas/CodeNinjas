from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

load_dotenv()

EMAIL =os.getenv("COMPANY_EMAIL")
PASS =os.getenv("EMAIL_PASS")
    
@app.route('/')
def index():
    return render_template('index.html') 
 
@app.route('/about')
def about():
    return render_template('about.html')  

@app.route('/booking')
def book():
    return render_template('booking.html') 
 
@app.route('/contact')
def contact():
    return render_template('contact.html')  

@app.route('/team')
def team():
    return render_template('team.html') 
 
@app.route('/shifa')
def shifa_wp():
    return render_template('members/shifa/personalwebpage.html') 
 
@app.route('/chasitty')
def chassity_wp():
    return render_template('/members/chasitty/personalwebpage.html') 
@app.route('/chasitty-contact')
def chasitty_contact():
    return render_template('/members/chasitty/contact.html') 
 
@app.route('/nicolas')
def nico_wp():
    return render_template('members/nicolas/Personal-Webpage-WP.html')  
@app.route('/muhammad')
def muhammad_wp():
    return render_template('members/muhammad/webpage.html')  

# engineers = {
#     "Nicolas Ambriz": ,
#     "Shifa Maknojia": "shifa@gator.uhd.edu",
#     "Chassity Ayala": "chas@gator.uhd.edu",
#     "Muhammad Admin": "muhammad@gator.uhd.edu",
    
# }

# @app.route('/booking', methods=['POST'])
# def submit_booking():
#     # Get values from the form
#     service = request.form.get('service')
#     member = request.form.get('member')
#     email = request.form.get('email')  # User's email (optional in this case)
#     message = request.form.get('message')

#     print(engineers[member])

#     # Ensure the member is in the engineers dictionary
#     if member not in engineers:
#         return f"Error: {member} is not a valid team member."

#     # Log the booking information
#     print(f"Service: {service}, Member: {member}, Email: {email}, Message: {message}")
    
#     # Set email subject and content
#     email_subject = f"New Booking for {service}"
#     email_content = f"Service: {service}\nTeam Member: {member}\nMessage: {message}"

#     # Get the recipient's email address
#     email_recipient = engineers[member]  # Replace with the recipient's email address

#     # Send the email via SendGrid
#     email_status = send_email_via_sendgrid(email_recipient, email_subject, email_content)

#     # Respond to the user
#     return f"Form submitted successfully! {email_status}"

# # Function to send an email using SendGrid API
# def send_email_via_sendgrid(to_email, subject, content):
#     url = "https://api.sendgrid.com/v3/mail/send"
#     headers = {
#         "Authorization": f"Bearer {SENDGRID_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "personalizations": [
#             {
#                 "to": [{"email": to_email}],
#                 "subject": subject
#             }
#         ],
#         "from": {"email": to_email},  # Your sender email
#         "content": [{"type": "text/plain", "value": content}]
#     }

#     # Send the email using a POST request to SendGrid API
#     try:
#         response = requests.post(url, headers=headers, data=json.dumps(payload))
        
#         # Check if the email was sent successfully
#         if response.status_code == 202:
#             return "Email sent successfully!"
#         else:
#             return f"Failed to send email: {response.status_code} - {response.text}"
    
#     except requests.exceptions.RequestException as e:
#         return f"An error occurred while sending the email: {str(e)}"

SMTP_SERVER = 'smtp-mail.outlook.com'  # Outlook SMTP server
SMTP_PORT = 587  # Port for TLS (587 is for secure SMTP)
SENDER_EMAIL = EMAIL  # Your Outlook email
SENDER_PASSWORD = PASS  # Your Outlook email password or App Password   

 #Function to send email using Outlook's SMTP server
def send_email(to_email, body,service, member):
     
    # Create a MIME message
    message = MIMEMultipart()
    message['From'] = to_email
    message['To'] = EMAIL
    message['Subject'] = service + ": " + member
    message['Subject'] = 'Booking Request'  # Default subject if you don't want to specify one

    # Attach the email body
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the Outlook SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection using TLS
        server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to your Outlook account
        server.sendmail(SENDER_EMAIL, to_email, message.as_string())  # Send the email
        server.quit()  # Close the connection
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

@app.route('/booking', methods=['POST'])
def booking():
    # Get form data
    service = request.form['service']
    member = request.form['member']
    user_email = request.form['email']
    message = request.form['message']

    # Construct email body
    email_body = f"Service: {service}\nTeam Member: {member}\nUser Email: {user_email}\nMessage:\n{message}"

    # Send email to the team or your email
    to_email = user_email # Replace with your team or recipient email address

    # Send email using the send_email function
    if send_email(to_email, email_body, service, member):
        return "Form submitted successfully! We'll get back to you soon."
    else:
        return "Failed to send email. Please try again later."

if __name__ == '__main__':
    app.run(debug=True)
