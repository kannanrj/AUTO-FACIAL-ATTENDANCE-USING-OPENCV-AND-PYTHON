import os
import yagmail

def get_most_recent_file(dir):
    files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    files.sort(key=lambda x: os.path.getctime(os.path.join(dir, x)))
    return files[-1]

def mail(file):
    receiver = "reciver mail @gmail.com"  # receiver email address
    body = "Attendance file"  # email body
    filename = os.path.join("Attendance", file)  # attach the file

# mail information
    yag = yagmail.SMTP("sender mail******@gmail.com", "pasword********")

# sent the mail
    yag.send(
        to=receiver,
        subject="Attendance report is ready !",  # email subject
        contents=body,  # email body
        attachments=filename,  # file attached
    )

most_recent_file = get_most_recent_file("Attendance")
mail(most_recent_file)
