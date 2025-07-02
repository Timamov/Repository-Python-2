import base64

import pyotp
import qrcode
import io
secret = 'udfhtrgt5mogt5ig'

totp = pyotp.TOTP(secret)
otp = totp.now()
print(otp)

uri = totp.provisioning_uri(name='user@example.com', issuer_name='MyApp', image='https://cdn.hexnode.com/blogs/wp-content/uploads/2023/03/15084406/App-management-101-Cover-Image.png')
print(uri)

qr = qrcode.make(uri)
qr.show()
file = qr.save('hh.png')
buffer = io.BytesIO()
qr.save(buffer, format='PNG')
base64_qr = base64.b64encode(buffer.getvalue()).decode()
print(base64_qr)
print(f'data:image/png;base64{base64_qr}')