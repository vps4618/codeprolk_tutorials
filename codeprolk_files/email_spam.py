import smtplib,datetime

from email.message import EmailMessage
print(datetime.datetime.today())
print("--------------------------------")
print("Welcome to Vishwa's email bot !")
print("--------------------------------")
my_mail=str(input("Enter your gmail account : "))
my_mail_password=str(input("Enter your gmail account's password : "))
def sendmail(receiver,subject,message):
    print("Your email is composing.Please wait...")
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo() #authentication
    server.starttls() #authentication
    server.ehlo() #authentication
    
    server.login(my_mail,my_mail_password)
    mail=EmailMessage()
    mail["From"]=my_mail
    mail["To"]=receiver
    mail["Subject"]=subject
    mail.set_content(message)

    server.send_message(mail)
    server.close()
    print("Email sent successfully ",receiver)
    print("-------------------------------------------------")

receiver=str(input("Enter receiver's email : "))    
print("-------------------------------")  
subject=str(input("Enter subject : "))
message1=str(input("Enter message : "))
print("---------------------------------------------------")
sendmail(receiver,subject,message1)

input("Programme finished.Press Enter key to end up this programme.")


