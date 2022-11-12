import qrcode

def generate_QR(user_url):
    qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=1
    )
    data = user_url # put your text or Link here
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')
    qr_img.save('qr-img/output.png')
    return qr_img
    
