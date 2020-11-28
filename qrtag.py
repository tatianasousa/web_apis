import requets

url = 'https://qrtag.net/api/qr(_transparent)(100).png'
img = '<img src="https://qrtag.net/api/qr.png" alt="qrtag">'

response = requets.post(url, img)