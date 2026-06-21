#!/usr/bin/env python3
"""Generate a QR code PNG from a URL.

Usage:  python make_qr.py https://yourname.github.io/contact/
Output: qr.png  (high error-correction, good for printing on a poster/slide)
"""
import sys
import qrcode
from qrcode.constants import ERROR_CORRECT_H

url = sys.argv[1] if len(sys.argv) > 1 else "https://yourname.github.io"

qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=16, border=3)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="#15191e", back_color="white")
img.save("qr.png")
print(f"Wrote qr.png  ->  {url}")
