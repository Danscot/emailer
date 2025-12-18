import asyncio

from mailer import Mailer

async def main():

    email = input('Enter the sender email : ')

    auth = input("Enter your account auth key : ")

    mailer = Mailer(

        email=email,

        app_password=auth
    )

    await mailer.connect()

    target_email = input("Enter the target email : ")

    subject = input("Enter the email's subject : ")

    body = input("Enter the email's body : ")

    await mailer.send(

        target_email=target_email,

        subject=subject,

        body=body
    )

    await mailer.close()

asyncio.run(main())
