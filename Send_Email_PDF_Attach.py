import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

SENDER_EMAIL = "EMAIL here"
SENDER_PASSWORD = "password here"
RECIPIENTS = [

]

RESUME_PATH = "path here"  # 📝 Replace with full path if needed

def send_resume_email():
    for recipient in RECIPIENTS:
        msg = MIMEMultipart("mixed")  # Changed to mixed for attachments
        msg["From"] = "email here"
        msg["To"] = recipient
        msg["Subject"] = "Application for Software Engineer Position"

        # Email body
        plain = """
Hi Team,
I’m a Software Engineer with nearly 2.5 years of experience at --.

I’m reaching out regarding potential Software Engineering roles.

Open to: PAN India (in-office) or Remote.

My resume is attached with this email.

LinkedIn Profile: --

Looking forward to hearing from you.

Thank you,
--
"""

        html = """
<html>
  <body>
    <p>Hi Team,<br>
    I’m a <strong>Software Engineer</strong> with nearly 2.5 years of experience at

    <p>I’m reaching out regarding potential Software Engineering roles.</p>

    <p><strong>Open to:</strong> PAN India(in-office) or Remote.</p>

    <p><strong>LinkedIn Profile:</strong> </p>

    <p>I’ve attached my resume for your reference.</p>

    <p><strong>Looking forward to hearing from you.</strong></p>

    <p>Thank you,<br>
    --</p>
  </body>
</html>
"""

        # Attach plain and HTML versions
        # msg.attach(MIMEText(plain, "plain"))
        msg.attach(MIMEText(html, "html"))

        # Attach the PDF
        try:
            with open(RESUME_PATH, "rb") as f:
                part = MIMEApplication(f.read(), _subtype="pdf")
                part.add_header('Content-Disposition', 'attachment', filename="SHALAKA RESUME.pdf")
                msg.attach(part)
        except Exception as e:
            print(f"⚠️ Couldn't attach resume: {e}")
            continue

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
