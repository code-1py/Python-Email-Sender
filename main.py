from smtplib import SMTP 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_mail(reciever_mail):
    sender_mail = "<<Sender's Email>>" # Replace With Your Email.
    password = "<<Password>>" # Replace With Your Password (Use app Password for Gmail).

    subject = f"<<Subject>>" # Replace With Subject Of Email
    body = f"<<Body>>" # Replace With Body Of Email

    email = MIMEMultipart()
    email["From"] = sender_mail
    email["To"] = reciever_mail
    email["Subject"] = subject
    email.attach(MIMEText(body,"plain"))

    try: # Replace smtp.gmail.com and 587 with your email service's Smtp address and port.
        with SMTP("smtp.gmail.com",587) as server: 
            server.starttls() # For Secure Connection at first
            server.login(sender_mail,password)
            server.send_message(email)
            print(f"✅ Email sent successfully to {reciever_mail}\n")
    except Exception as e:            
        print(f"Error Occured : {e}") # For Any Error It Will Get Printed


send_mail("Email") # Replace "Email" with email address of reciever
