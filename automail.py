import os
import yagmail
def mail(file):
    receiver = "reciver mail @gmail.com"  # receiver email address
    body = "Attendance file"  # email body
    filename = "Attendance"+os.sep+str(file)  # attach the file

# mail information
    yag = yagmail.SMTP("sender mail******@gmail.com", "pasword********")

# sent the mail
    yag.send(
        to=receiver,
        subject="Attendance report is ready !",  # email subject
        contents=body,  # email body
        attachments=filename,  # file attached
    )
