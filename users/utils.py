import os
import secrets

from PIL import Image

from contact_app.settings import MEDIA_ROOT


def add_watermark(avatar):
    image = Image.open(avatar)
    watermark = Image.open(MEDIA_ROOT + '/watermark.png')
    image.paste(watermark, (5, 10))
    random_hex = secrets.token_hex(8)
    _, file_extension = os.path.splitext(avatar.name)
    new_filename = f'photos/{random_hex}{file_extension}'
    image.save(MEDIA_ROOT + '/' + new_filename)
    return new_filename
