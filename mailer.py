from email.message import EmailMessage

from aiosmtplib import SMTP


class Mailer:

    def __init__(self, email: str, app_password: str):
    
        self.sender_email = email
    
        self.auth_key = app_password

        self.smtp_host = "smtp.gmail.com"
    
        self.smtp_port = 587

        self.smtp: SMTP | None = None

    async def connect(self):
    
        self.smtp = SMTP(
    
            hostname=self.smtp_host,
    
            port=self.smtp_port,
    
            start_tls=True,
    
        )
    
        await self.smtp.connect()
    
        await self.smtp.login(self.sender_email, self.auth_key)

    async def send(self, target_email: str, subject: str, body: str):
    
        if not self.smtp:
    
            raise RuntimeError("SMTP not connected")

        message = EmailMessage()
    
        message["From"] = self.sender_email
    
        message["To"] = target_email
    
        message["Subject"] = subject
    
        message.set_content(body)

        await self.smtp.send_message(message)

        print(
    
            f"✅ Email sent from {self.sender_email} to {target_email}"
        )

    async def close(self):
    
        if self.smtp:
    
            await self.smtp.quit()
