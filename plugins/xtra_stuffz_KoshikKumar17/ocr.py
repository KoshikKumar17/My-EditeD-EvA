# (c) Koshik Kumar (@KoshikKumar17)

import os
import io
from PIL import Image
import pytesseract # pip install pytesseract (requirements.txt)
from pyrogram import Client as Koshik
from pyrogram import filters

 def start_ocr(input_file):
    text = ""
    if input_file.file_size < 10 * 1024 * 1024:  # Check if file size is less than 10MB
        if input_file.mime_type.startswith('image'):
            with io.BytesIO() as ocr:
                input_file.download(ocr)
                ocr.seek(0)
                image = Image.open(ocr)
                text = pytesseract.image_to_string(image)
            # Delete the downloaded image
            os.remove(ocr)
    return text

# Command handler
@Koshik.on_message(filters.command(["ocr"]))
def ocr_command(bot, message):
    z = messages.reply_text("__Checking...⚡__", quote=True)
    if message.reply_to_message and message.reply_to_message.photo:
        z.edit_text("**Fetching... OCR**", quote=True)
        replied_photo = message.reply_to_message.photo[-1]  # Get the highest resolution photo
        text = start_ocr(replied_photo)
        z.delete()
        if text:
            message.reply_text(text, quote=True)
        else:
            message.reply_text("**Failed to perform OCR on the provided image.**", quote=True)
    else:
        z.edit_text("**Please reply to any image**", quote=True)
