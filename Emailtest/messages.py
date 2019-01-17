import datetime
from smtplib import SMTP, SMTPException, SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

host = "smtp.gmail.com"
port= 587
username= "testingpyemail@gmail.com"
password ="8977152909"
from_email = username

class MessageUser():
    user_details = []
    messages = []
    email_messages=[]

    def get_templete_path(path):
        file_path = os.path.join(os.getcwd(),path)
        if not os.path.isfile(file_path):
            raise Exception("Not a valid path %s"%(file_path))
        return file_path

    file_ = 'desktop\\emailtest\\templetes\\email_message.html'

    def get_templete(path):
        file_path=get_templete_path(path)
        return open(file_path).read()

    def render_context(templete_string, context):
        return templete_string.format(**context)

    base_message=get_templete(file_)

    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower() 
        amount = "%.2f" %(amount)
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail = {
            "name": name,
            "amount": amount,
            "date" : date_text
        } 
        if email is not None:
            detail["email"] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                new_msg = self.base_message.format(
                    name=detail["name"],
                    date=detail["date"],
                    total=detail["amount"]
                )
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                        }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_msg)     
            return self.messages
        return []
    def send_email(self):
        self.make_messages()
        if len(self.email_messages)>0:
            for user_data in self.email_messages:
                user_email = user_data['email']
                user_message = user_data['message']
                try:
                    msg=MIMEMultipart("Sample test message")
                    msg['Subject'] = "Billing Update"
                    msg["From"] = from_email
                    msg["To"] = user_email
                    part_1 = MIMEText(user_message,'html')
                    msg.attach(part_1)
                    email_conn = SMTP(host,port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username,password)
                    email_conn.sendmail(from_email,[user_email],msg.as_string())
                    email_conn.quit()
                except SMTPAuthenticationError :
                    print("error login try again")
                except:
                    print("error occuredtry again")
            return True
        return False

obj = MessageUser()
obj.add_user("Justin", 123.32, email='testingpyemail@gmail.com')
obj.add_user("jOhn", 94.23, email='testingpyemail@gmail.com')
obj.add_user("Sean", 93.23, email='testingpyemail@gmail.com')
obj.add_user("Emilee", 193.23, email='testingpyemail@gmail.com')
obj.add_user("Marie", 13.23, email='testingpyemail@gmail.com')
obj.get_details()
obj.send_email()
