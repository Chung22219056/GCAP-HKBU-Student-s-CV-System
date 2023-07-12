from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, base64


def sendEmail(to, email_content, subject=None):
    print()
    content = MIMEMultipart()  
    if subject != None:
        content["subject"] = "subject"  

    content["from"] = "gcap3055hkbu@gmail.com"  
    content['Subject'] = "InterView"
    #content["to"] = "22219056@life.hkbu.edu.hk" 
    content["to"] = to
    content.attach(MIMEText(email_content, "html"))  

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  
        try:
            smtp.ehlo()
            smtp.starttls()
            #smtp.login("gcap3055hkbu@gmail.com", "smfakeaptgbotnqc")
            smtp.login("gcap3055bu@gmail.com","")
            smtp.send_message(content)
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)