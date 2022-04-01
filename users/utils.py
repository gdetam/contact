import os
import secrets
import smtplib
from email.mime.text import MIMEText

from PIL import Image

from contact_app.settings import MEDIA_ROOT

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


def add_watermark(avatar):
    image = Image.open(avatar)
    watermark = Image.open(MEDIA_ROOT + '/watermark.png')
    image.paste(watermark, (5, 10))
    random_hex = secrets.token_hex(8)
    _, file_extension = os.path.splitext(avatar.name)
    new_filename = f'photos/{random_hex}{file_extension}'
    image.save(MEDIA_ROOT + '/' + new_filename)
    return new_filename


def send_message(user, user_like):
    msg = MIMEText(
        f'Вы понравились {user.first_name}!'
        f' Почта участника: {user_like.email}')
    msg['Subject'] = 'Вы понравились!'
    msg['From'] = os.environ.get('EMAIL_HOST_USER')
    msg['To'] = user.email
    server = smtplib.SMTP(os.environ.get('EMAIL_HOST'))
    server.starttls()
    server.login(msg['From'], os.environ.get('EMAIL_HOST_PASSWORD'))
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()
