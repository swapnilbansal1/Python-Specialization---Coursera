import smtplib


host = "smtp.gmail.com"
port= 587
username= "testingpyemail@gmail.com"
password ="8977152909"

from_email = username
to_list = ["swapnil.bansal1@gmail.com"]
msg="Sample test message"


email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()

try:
	email_conn.login(username,password)
	email_conn.sendmail(from_email,to_list,msg)
except:
	print("error occured try again")

email_conn.quit()
