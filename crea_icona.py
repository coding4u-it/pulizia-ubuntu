#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera le icone dell'applicazione in varie dimensioni.
Richiede: python3-pil  (sudo apt install python3-pil)
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys


def crea_icona(percorso, size=256):
    """Genera un'icona con cerchio verde + scopa stilizzata."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # --- Cerchio di sfondo con gradiente semplice ---
    margine = max(2, size // 20)
    # Ombra esterna
    draw.ellipse(
        [margine + 2, margine + 2, size - margine + 2, size - margine + 2],
        fill=(0, 0, 0, 60)
    )
    # Cerchio principale (verde)
    draw.ellipse(
        [margine, margine, size - margine, size - margine],
        fill=(39, 174, 96, 255),
        outline=(255, 255, 255, 255),
        width=max(2, size // 48)
    )
    # Highlight in alto (effetto lucido)
    highlight = [
        margine + size // 8,
        margine + size // 12,
        size - margine - size // 8,
        margine + size // 4,
    ]
    draw.ellipse(highlight, fill=(255, 255, 255, 45))

    # --- Prova prima con emoji font (Noto Color Emoji) ---
    emoji = "🧹"
    disegnato = False
    for fp in [
        "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf",
        "/usr/share/fonts/truetype/noto/NotoEmoji-Regular.ttf",
    ]:
        if os.path.exists(fp):
            try:
                # Noto Color Emoji richiede dimensioni multiple di 64
                font_size = 109 if size >= 128 else 64
                font = ImageFont.truetype(fp, font_size)
                bbox = draw.textbbox((0, 0), emoji, font=font, embedded_color=True)
                w = bbox[2] - bbox[0]
                h = bbox[3] - bbox[1]
                x = (size - w) // 2 - bbox[0]
                y = (size - h) // 2 - bbox[1] + size // 30
                draw.text((x, y), emoji, font=font, embedded_color=True)
                disegnato = True
                break
            except Exception:
                continue

    # --- Fallback: disegna scopa stilizzata a mano ---
    if not disegnato:
        cx = size // 2
        # Manico
        draw.line(
            [(cx, int(size * 0.28)), (cx, int(size * 0.58))],
            fill=(255, 255, 255, 255),
            width=max(3, size // 24)
        )
        # Nodo
        draw.ellipse(
            [cx - size // 16, int(size * 0.54),
             cx + size // 16, int(size * 0.62)],
            fill=(241, 196, 15, 255)
        )
        # Setole (ventaglio)
        for i in range(-3, 4):
            x_end = cx + i * size // 11
            draw.line(
                [(cx, int(size * 0.62)), (x_end, int(size * 0.82))],
                fill=(255, 255, 255, 255),
                width=max(2, size // 40)
            )
        # Base setole
        draw.line(
            [(cx - size // 8, int(size * 0.82)),
             (cx + size // 8, int(size * 0.82))],
            fill=(255, 255, 255, 255),
            width=max(2, size // 40)
        )

    img.save(percorso, "PNG")
    print(f"  ✅ {percorso} ({size}×{size})")


if __name__ == "__main__":
    cartella = os.path.dirname(os.path.abspath(__file__))
    print("Generazione icone...")
    for dim in [16, 32, 48, 64, 128, 256]:
        crea_icona(os.path.join(cartella, f"icona_{dim}.png"), dim)
    # Icona principale
    crea_icona(os.path.join(cartella, "icona.png"), 256)
    print("Fatto!")
