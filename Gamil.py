import smtplib
import getpass
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
identity = input("Please enter your email ID - ")
password = getpass.getpass('Password:')
s.login(identity, password)
password = 0
message = input("Please what you would like to send - ")
sender = identity
r =input("Please enter your recipients address - ")
s.sendmail(sender, r, message) 
print("Succesful")
s.quit() 
