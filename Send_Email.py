import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER_EMAIL = "EMAIL_ADD"
SENDER_PASSWORD = "PASSWORD_ADD"
RECIPIENTS = [
   "EMAILS"

]

def send_resume_email():
    for recipient in RECIPIENTS:
        msg = MIMEMultipart("alternative")
        msg["From"] = "Change this"
        msg["To"] = recipient
        msg["Subject"] = "Application for Software Engineer Position"

        # Your exact plain message
        plain = """
Hi Team,
I’m a Software Engineer with 2 years of experience at  ----.

I’m reaching out regarding potential Software Engineering roles.

Open to: PAN India (in-office) or Remote.

My resume: --

LinkedIn Profile: --

Looking forward to hearing from you.

Thank you,
--
"""

        # Optional HTML formatting to make links clickable and clean
        html = """
<html>
  <body>
    <p>Hi Team,<br>
    I’m a <strong>Software Engineer</strong> with nearly 2.5 years of experience at <strong>--</strong> - a unicorn fintech startup.</p>

    <p>I’m reaching out regarding potential Software Engineering roles.</p>

    <p><strong>Open to:</strong> PAN India(in-office) or Remote.</p>

    <p><strong>My resume:</strong> add here</p>

    <p><strong>LinkedIn Profile:</strong> add here </p>

    <p><strong>Looking forward to hearing from you.</strong></p>

    <p>Thank you,<br>
    --</p>
  </body>
</html>
"""

        msg.attach(MIMEText(plain, "plain"))
        msg.attach(MIMEText(html, "html"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient, msg.as_string())
            server.quit()
            print(f"✅ Sent to {recipient}")
        except Exception as e:
            print(f"❌ Failed for {recipient}: {e}")

send_resume_email()
