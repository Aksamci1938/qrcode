import qrcode

qrcode = \
    qrcode.make(
        "https://birbuketsiir.com")

qrcode.save\
    ('bbs.png')

print\
    (' QR kodunuz oluşturulmuştur.')
    
    #qrcode libary download (pip install qrcode pillow) ty <3
