"""홈 화면 아이콘 만들기: 남색 바탕에 🏯 (192, 512, 마스크용 512)  →  python make_icons.py"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = r'C:\Windows\Fonts\seguiemj.ttf'
BG = (31, 63, 110, 255)   # 쪽빛 남색 #1f3f6e


def make(size, name, scale):
    img = Image.new('RGBA', (size, size), BG)
    # 이모지 글꼴은 109px 근처에서 가장 잘 그려지므로 크게 그린 뒤 줄임
    em = Image.new('RGBA', (160, 160), (0, 0, 0, 0))
    ImageDraw.Draw(em).text((80, 80), '🏯', font=ImageFont.truetype(FONT, 109), embedded_color=True, anchor='mm')
    em = em.crop(em.getbbox())
    target = int(size * scale)
    w, h = em.size
    r = target / max(w, h)
    em = em.resize((max(1, int(w * r)), max(1, int(h * r))), Image.LANCZOS)
    # 흰 원 위에 올려 잘 보이게
    d = ImageDraw.Draw(img)
    c = int(size * scale * 0.68)
    d.ellipse((size / 2 - c, size / 2 - c, size / 2 + c, size / 2 + c), fill=(255, 255, 255, 255))
    img.alpha_composite(em, ((size - em.size[0]) // 2, (size - em.size[1]) // 2))
    img.save(os.path.join(HERE, name))


make(192, 'icon-192.png', 0.56)
make(512, 'icon-512.png', 0.56)
make(512, 'icon-maskable.png', 0.44)   # 안드로이드가 둥글게 잘라도 남는 크기
print('ok')
