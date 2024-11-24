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



SMTP_SERVER = 'smtp-mail.outlook.com' 
SMTP_PORT = 587  
SENDER_EMAIL = EMAIL 
SENDER_PASSWORD = PASS   


def send_email(to_email, body,service, member):
     
    # Create a MIME message
    message = MIMEMultipart()
    message['From'] = to_email
    message['To'] = EMAIL
    message['Subject'] = service + ": " + member
    message['Subject'] = 'Booking Request'  

    
    message.attach(MIMEText(body, 'plain'))

    try:
       
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls() 
        server.login(SENDER_EMAIL, SENDER_PASSWORD) 
        server.sendmail(SENDER_EMAIL, to_email, message.as_string()) 
        server.quit() 
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

@app.route('/booking', methods=['POST'])
def booking():
  
    service = request.form['service']
    member = request.form['member']
    user_email = request.form['email']
    message = request.form['message']

  
    email_body = f"Service: {service}\nTeam Member: {member}\nUser Email: {user_email}\nMessage:\n{message}"

   
    to_email = user_email 

  
    if send_email(to_email, email_body, service, member):
        return "Form submitted successfully! We'll get back to you soon."
    else:
        return "Failed to send email. Please try again later."

if __name__ == '__main__':
    app.run(debug=True)
