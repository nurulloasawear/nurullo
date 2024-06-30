import qrcode
from io import BytesIO
from django.core.files import File

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    buffer = BytesIO()
    img.save(buffer, 'PNG')
    buffer.seek(0)
    print("QR Code generated and buffered")
    return File(buffer, name='qr_code.png')

def get_youtube_embed_url(youtube_url):
    if "youtube.com" in youtube_url:
        video_id = youtube_url.split("v=")[-1]
        return f"https://www.youtube.com/embed/{video_id}"
    elif "youtu.be" in youtube_url:
        video_id = youtube_url.split("/")[-1]
        return f"https://www.youtube.com/embed/{video_id}"
    return youtube_url
