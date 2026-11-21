# Coded By can-codev
# Copyright (C) 2026 can-codev
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License v3.0
# SPDX-License-Identifier: GPL-3.0-or-later


import sys
import os
import html
import numpy as np
from PIL import Image, ImageEnhance
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFileDialog, QTextEdit, QSlider, QComboBox,
    QMessageBox, QGroupBox, QCheckBox, QFrame, QScrollArea,
    QSplitter, QSizePolicy, QColorDialog, QTabWidget, QLineEdit,
    QProgressBar
)
from PyQt5.QtCore import Qt, QPoint, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import (
    QPixmap, QFont, QFontMetrics, QPainter, QColor, QImage,
    QPalette, QTextOption
)


BRAND_NAME = "can-codev"

COLORS = {
    'background': '#080808',
    'panel': '#141414',
    'dark': '#101010',
    'darker': '#0A0A0A',
    'text': '#EAEAEA',
    'text_secondary': '#9AA0A6',
    'primary': '#00C2FF',
    'primary_dark': '#0099CC',
    'primary_light': '#62D9FF',
    'accent': '#1DB4FF',
    'border': '#2B2B2B',
    'success': '#35C759',
    'danger': '#F44336',
    'button_bg': '#00C2FF',
    'button_hover': '#1DB4FF',
    'button_pressed': '#0099CC',
}

LANGUAGES = {
    "Türkçe": "tr",
    "English": "en"
}

TRANSLATIONS = {
    "tr": {
        "app_title": "ASCII Studio Pro",
        "tab_image_ascii": "Resimden ASCII",
        "tab_stylized_text": "Stilli Metin",
        "image_preview": "Resim Önizleme",
        "no_image_selected": "Resim seçilmedi",
        "drop_hint": "Resmi buraya sürükleyip bırakabilirsiniz",
        "ascii_settings": "ASCII Ayarları",
        "ascii_width": "ASCII Genişliği",
        "character_preset": "Karakter Seti",
        "custom_characters": "Özel Karakterler (koyu > açık)",
        "color_mode": "Renk Modu",
        "black_white": "Siyah & Beyaz",
        "colored": "Renkli",
        "contrast": "Kontrast",
        "brightness": "Parlaklık",
        "gamma": "Gamma",
        "sharpness": "Keskinlik",
        "edge_strength": "Kenar Belirginliği",
        "dithering": "Dithering (Doku)",
        "dither_none": "Kapalı (Keskin)",
        "dither_ordered": "Ordered Bayer (Önerilen)",
        "dither_floyd": "Floyd-Steinberg",
        "auto_levels": "Otomatik Seviyeler (Auto-Levels)",
        "invert_brightness": "Parlaklığı Ters Çevir",
        "auto_update": "Otomatik Güncelle",
        "auto_detect_btn": "Otomatik Algıla ve Optimize Et",
        "detection_info": "Analiz",
        "transparency": "Şeffaflık",
        "transparent_area": "Şeffaf Alan",
        "keep_empty": "Boş Bırak",
        "use_dot": "Nokta Kullan",
        "blend_background": "Arka Planla Birleştir",
        "background_color": "Arka Plan Rengi",
        "choose": "Seç",
        "actions": "İşlemler",
        "copy_ascii": "ASCII Kopyala",
        "save_txt": "TXT Kaydet",
        "save_html": "HTML Kaydet",
        "save_png_preview": "PNG Önizleme Kaydet",
        "ascii_preview": "ASCII Önizleme",
        "preview_fontsize": "Önizleme Yazı Boyutu",
        "size": "Boyut",
        "mode": "Mod",
        "ready": "Hazır",
        "processing": "İşleniyor...",
        "analyzing": "Analiz ediliyor...",
        "error": "Hata",
        "load_image": "Resim Yükle",
        "select_image": "Resim Seç",
        "image_files": "Resim Dosyaları",
        "image_not_loaded": "Resim yüklenemedi",
        "image_too_large": "Görsel boyutu çok büyük, genişliği düşürün.",
        "text_input": "Metin Girişi",
        "type_text_here": "Metninizi buraya yazın...",
        "text_style": "Metin Stili",
        "style_preset": "Stil Haznesi",
        "force_uppercase": "Büyük Harfe Zorla",
        "add_space_between_letters": "Harfler Arasına Boşluk Ekle",
        "copy_text": "Metni Kopyala",
        "styled_text_preview": "Stilli Metin Önizleme",
        "example": "Örnek",
        "your_styled_text_here": "Stilli metniniz burada görünecek.",
        "copied": "Kopyalandı",
        "saved": "Kaydedildi",
        "ascii_copied": "ASCII metni panoya kopyalandı.",
        "styled_text_copied": "Stilli metin panoya kopyalandı.",
        "txt_saved": "TXT dosyası başarıyla kaydedildi.",
        "html_saved": "HTML dosyası başarıyla kaydedildi.",
        "png_saved": "PNG önizleme başarıyla kaydedildi.",
        "styled_saved": "Stilli metin başarıyla kaydedildi.",
        "save_styled_text": "Stilli Metni Kaydet",
        "language": "Dil",
        "designed_by": "Coded by",
        "save_png": "PNG Kaydet",
        "save_html_dialog": "HTML Kaydet",
        "save_txt_dialog": "TXT Kaydet",
        "style": "Stil",
        "normal": "Normal",
        "style_category": "Stil Kategorisi",
        "auto_tuned_msg": "Otomatik ayar uygulandı.",
    },
    "en": {
        "app_title": "ASCII Studio Pro",
        "tab_image_ascii": "Image to ASCII",
        "tab_stylized_text": "Stylized Text",
        "image_preview": "Image Preview",
        "no_image_selected": "No image selected",
        "drop_hint": "You can drag and drop an image here",
        "ascii_settings": "ASCII Settings",
        "ascii_width": "ASCII Width",
        "character_preset": "Character Set",
        "custom_characters": "Custom Characters (dark > light)",
        "color_mode": "Color Mode",
        "black_white": "Black & White",
        "colored": "Colored",
        "contrast": "Contrast",
        "brightness": "Brightness",
        "gamma": "Gamma",
        "sharpness": "Sharpness",
        "edge_strength": "Edge Strength",
        "dithering": "Dithering",
        "dither_none": "Off (Sharp)",
        "dither_ordered": "Ordered Bayer (Recommended)",
        "dither_floyd": "Floyd-Steinberg",
        "auto_levels": "Auto Levels",
        "invert_brightness": "Invert Brightness",
        "auto_update": "Auto Update",
        "auto_detect_btn": "Auto-Detect and Optimize",
        "detection_info": "Analysis",
        "transparency": "Transparency",
        "transparent_area": "Transparent Area",
        "keep_empty": "Keep Empty",
        "use_dot": "Use Dot",
        "blend_background": "Blend with Background",
        "background_color": "Background Color",
        "choose": "Choose",
        "actions": "Actions",
        "copy_ascii": "Copy ASCII",
        "save_txt": "Save TXT",
        "save_html": "Save HTML",
        "save_png_preview": "Save PNG Preview",
        "ascii_preview": "ASCII Preview",
        "preview_fontsize": "Preview Font Size",
        "size": "Size",
        "mode": "Mode",
        "ready": "Ready",
        "processing": "Processing...",
        "analyzing": "Analyzing...",
        "error": "Error",
        "load_image": "Load Image",
        "select_image": "Select Image",
        "image_files": "Image Files",
        "image_not_loaded": "Image could not be loaded",
        "image_too_large": "The image is too large. Reduce the ASCII width.",
        "text_input": "Text Input",
        "type_text_here": "Type your text here...",
        "text_style": "Text Style",
        "style_preset": "Style Preset",
        "force_uppercase": "Force Uppercase",
        "add_space_between_letters": "Add Space Between Letters",
        "copy_text": "Copy Text",
        "styled_text_preview": "Styled Text Preview",
        "example": "Example",
        "your_styled_text_here": "Your stylized text will appear here.",
        "copied": "Copied",
        "saved": "Saved",
        "ascii_copied": "ASCII text copied to clipboard.",
        "styled_text_copied": "Styled text copied to clipboard.",
        "txt_saved": "TXT file saved successfully.",
        "html_saved": "HTML file saved successfully.",
        "png_saved": "PNG preview saved successfully.",
        "styled_saved": "Styled text saved successfully.",
        "save_styled_text": "Save Styled Text",
        "language": "Language",
        "designed_by": "Coded by",
        "save_png": "Save PNG",
        "save_html_dialog": "Save HTML",
        "save_txt_dialog": "Save TXT",
        "style": "Style",
        "normal": "Normal",
        "style_category": "Style Category",
        "auto_tuned_msg": "Auto settings applied.",
    }
}


ASCII_PRESETS = {
    "Classic Dark": "@%#*+=-:. ",
    "Detailed": "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
    "Clean Gradient": "█▓▒░:. ",
    "Blocks": "█▉▊▋▌▍▎▏░▒▓ ",
    "Sharp": "@#S%?*+;:,. ",
    "Smooth": "¶§Ø©%#*+=-:. ",
    "Light Reverse": " .:-=+*#%@",
}


def _build_math_map(upper_start, lower_start, digit_start=None):
    m = {}
    for i in range(26):
        m[chr(ord('A') + i)] = chr(upper_start + i)
        m[chr(ord('a') + i)] = chr(lower_start + i)
    if digit_start is not None:
        for i in range(10):
            m[str(i)] = chr(digit_start + i)
    return m


def _fullwidth_map():
    m = {' ': '\u3000'}
    for o in range(0x21, 0x7F):
        m[chr(o)] = chr(o + 0xFEE0)
    return m


def _range_map(chars, start):
    return {c: chr(start + i) for i, c in enumerate(chars)}


_UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_LO = "abcdefghijklmnopqrstuvwxyz"

STYLE_MAPS = {
    "Normal": {},
    "Bold Serif": _build_math_map(0x1D400, 0x1D41A, 0x1D7CE),
    "Italic Serif": {**_build_math_map(0x1D434, 0x1D44E), 'h': 'ℎ'},
    "Bold Script": _build_math_map(0x1D4D0, 0x1D4EA),
    "Double Struck": {
        **_build_math_map(0x1D538, 0x1D552, 0x1D7D8),
        'C': 'ℂ', 'H': 'ℍ', 'N': 'ℕ', 'P': 'ℙ',
        'Q': 'ℚ', 'R': 'ℝ', 'Z': 'ℤ'
    },
    "Sans Bold": _build_math_map(0x1D5D4, 0x1D5EE, 0x1D7EC),
    "Sans Italic": _build_math_map(0x1D608, 0x1D622),
    "Sans Bold Italic": _build_math_map(0x1D63C, 0x1D656),
    "Monospace": _build_math_map(0x1D670, 0x1D68A, 0x1D7F6),
    "Medieval": _build_math_map(0x1D56C, 0x1D586),
    "Fullwidth": _fullwidth_map(),
    "Bubble": {
        **_range_map(_LO, 0x24D0),
        **_range_map(_UP, 0x24B6)
    },
    "Parenthesized": _range_map(_LO, 0x249C),
    "Squared Letters": _range_map(_UP, 0x1F130),
    "Circled Negative": _range_map(_UP, 0x1F150),
    "Squared Negative": _range_map(_UP, 0x1F170),
    "Small Caps": {
        'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ',
        'f': 'ꜰ', 'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ',
        'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ',
        'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ',
        'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ',
        'z': 'ᴢ'
    },
    "Squared CJK": {
        'a': '卂', 'b': '乃', 'c': '匚', 'd': 'ᗪ', 'e': '乇',
        'f': '千', 'g': 'Ꮆ', 'h': '卄', 'i': '丨', 'j': 'ﾌ',
        'k': 'Ҝ', 'l': 'ㄥ', 'm': '爪', 'n': '几', 'o': 'ㄖ',
        'p': '卩', 'q': 'Ɋ', 'r': '尺', 's': '丂', 't': 'ㄒ',
        'u': 'ㄩ', 'v': 'ᐯ', 'w': '山', 'x': '乂', 'y': 'ㄚ',
        'z': '乙'
    },
    "Glitch Lite": {
        'a': 'Δ', 'b': 'ß', 'c': '₵', 'd': 'Đ', 'e': 'Ɇ',
        'f': '₣', 'g': '₲', 'h': 'Ħ', 'i': 'ł', 'j': 'J',
        'k': 'Ҝ', 'l': 'Ł', 'm': 'M', 'n': '₦', 'o': 'Ø',
        'p': '₱', 'q': 'Q', 'r': 'Ɽ', 's': '₴', 't': 'Ŧ',
        'u': 'Ʉ', 'v': 'V', 'w': '₩', 'x': 'Ӿ', 'y': '¥',
        'z': 'Ƶ'
    },
    "Greek Tech": {
        'a': 'Λ', 'b': 'ß', 'c': 'ᄃ', 'd': 'D', 'e': 'Σ',
        'f': 'F', 'g': 'G', 'h': 'Ή', 'i': 'I', 'j': 'J',
        'k': 'K', 'l': 'L', 'm': 'M', 'n': 'П', 'o': 'Ө',
        'p': 'P', 'q': 'Q', 'r': 'Я', 's': 'Ƨ', 't': 'Ƭ',
        'u': 'Ц', 'v': 'V', 'w': 'Щ', 'x': 'X', 'y': 'Y',
        'z': 'Z'
    },
    "Runic": {
        'a': 'ᚨ', 'b': 'ᛒ', 'c': 'ᚲ', 'd': 'ᛞ', 'e': 'ᛖ',
        'f': 'ᚠ', 'g': 'ᚷ', 'h': 'ᚺ', 'i': 'ᛁ', 'j': 'ᛃ',
        'k': 'ᚲ', 'l': 'ᛚ', 'm': 'ᛗ', 'n': 'ᚾ', 'o': 'ᛟ',
        'p': 'ᛈ', 'q': 'Q', 'r': 'ᚱ', 's': 'ᛊ', 't': 'ᛏ',
        'u': 'ᚢ', 'v': 'ᚡ', 'w': 'ᚹ', 'x': 'ᛪ', 'y': 'ᛦ',
        'z': 'ᛉ'
    },
    "Superscript": {
        'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ',
        'f': 'ᶠ', 'g': 'ᵍ', 'h': 'ʰ', 'i': 'ⁱ', 'j': 'ʲ',
        'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'n': 'ⁿ', 'o': 'ᵒ',
        'p': 'ᵖ', 'q': 'q', 'r': 'ʳ', 's': 'ˢ', 't': 'ᵗ',
        'u': 'ᵘ', 'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ', 'y': 'ʸ',
        'z': 'ᶻ', '0': '⁰', '1': '¹', '2': '²', '3': '³',
        '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸',
        '9': '⁹'
    },
    "Subscript": {
        'a': 'ₐ', 'e': 'ₑ', 'h': 'ₕ', 'i': 'ᵢ', 'j': 'ⱼ',
        'k': 'ₖ', 'l': 'ₗ', 'm': 'ₘ', 'n': 'ₙ', 'o': 'ₒ',
        'p': 'ₚ', 'r': 'ᵣ', 's': 'ₛ', 't': 'ₜ', 'u': 'ᵤ',
        'v': 'ᵥ', 'x': 'ₓ', '0': '₀', '1': '₁', '2': '₂',
        '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇',
        '8': '₈', '9': '₉'
    },
}

STYLE_CATEGORIES = {
    "All": None,
    "Unicode Fonts": [
        "Normal", "Small Caps", "Fullwidth", "Bold Serif",
        "Italic Serif", "Bold Script", "Double Struck", "Sans Bold",
        "Sans Italic", "Sans Bold Italic", "Monospace", "Medieval"
    ],
    "Symbols": [
        "Squared CJK", "Bubble", "Circled Negative", "Squared Letters",
        "Squared Negative", "Parenthesized", "Glitch Lite", "Greek Tech",
        "Runic"
    ],
    "Combining": [
        "Strikethrough", "Underline", "Wavy Below", "Dotted Above",
        "Double Dotted", "Crossed", "Ring Above", "Tilde Overlay",
        "Double Underline", "X Above"
    ],
    "Converters": [
        "Superscript", "Subscript", "Upside Down", "Mirror",
        "Leet Speak", "Morse Code", "Binary"
    ],
    "Decorators": [
        "Aesthetic Wide", "Sparkle", "Arrow", "Star Frame",
        "Wave Decoration", "Heart Frame", "Diamond Frame",
        "Lightning Frame", "Flower Frame", "Music Frame"
    ],
    "Frames": [
        "Box Frame", "Fancy Frame", "Double Box Frame",
        "Round Box Frame", "Shadow Box Frame"
    ],
}

COMBINING_STYLES = {
    "Strikethrough": '\u0336',
    "Underline": '\u0332',
    "Wavy Below": '\u0330',
    "Dotted Above": '\u0307',
    "Double Dotted": '\u0308',
    "Crossed": '\u0337',
    "Ring Above": '\u030A',
    "Tilde Overlay": '\u0334',
    "Double Underline": '\u0333',
    "X Above": '\u033D',
}

UPSIDE_DOWN_MAP = {
    'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ',
    'g': 'ƃ', 'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l',
    'm': 'ɯ', 'n': 'u', 'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ',
    's': 's', 't': 'ʇ', 'u': 'n', 'v': 'ʌ', 'w': 'ʍ', 'x': 'x',
    'y': 'ʎ', 'z': 'z', 'A': '∀', 'B': 'q', 'C': 'Ɔ', 'D': 'p',
    'E': 'Ǝ', 'F': 'Ⅎ', 'G': 'פ', 'H': 'H', 'I': 'I', 'J': 'ſ',
    'K': 'ʞ', 'L': '˥', 'M': 'W', 'N': 'N', 'O': 'O', 'P': 'Ԁ',
    'Q': 'Q', 'R': 'ɹ', 'S': 'S', 'T': '┴', 'U': '∩', 'V': 'Λ',
    'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z', '1': 'Ɩ', '2': 'ᄅ',
    '3': 'Ɛ', '4': 'ㄣ', '5': 'ϛ', '6': '9', '7': 'ㄥ', '8': '8',
    '9': '6', '0': '0', '.': '˙', ',': "'", "'": ',', '"': '„',
    '!': '¡', '?': '¿', '(': ')', ')': '(', '[': ']', ']': '[',
    '{': '}', '}': '{', '<': '>', '>': '<', '&': '⅋', '_': '‾'
}

MIRROR_MAP = {
    'a': 'ɒ', 'b': 'd', 'c': 'ɔ', 'd': 'b', 'e': 'ɘ', 'f': 'Ꮈ',
    'g': 'ǫ', 'h': 'ʜ', 'i': 'i', 'j': 'ꞁ', 'k': 'ʞ', 'l': 'l',
    'm': 'm', 'n': 'ᴎ', 'o': 'o', 'p': 'q', 'q': 'p', 'r': 'ɿ',
    's': 'ꙅ', 't': 'ƚ', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x',
    'y': 'ʏ', 'z': 'z', 'A': 'A', 'B': 'ᗺ', 'C': 'Ↄ', 'D': 'ᗡ',
    'E': 'Ǝ', 'F': 'ꟻ', 'G': 'Ꭾ', 'H': 'H', 'I': 'I', 'J': 'Ⴑ',
    'K': 'ꓘ', 'L': '⌐', 'M': 'M', 'N': 'ᴎ', 'O': 'O', 'P': 'ꟼ',
    'Q': 'Ọ', 'R': 'Я', 'S': 'Ꙅ', 'T': 'T', 'U': 'U', 'V': 'V',
    'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'
}

LEET_MAP = {
    'a': '4', 'b': '8', 'c': '(', 'd': '|)', 'e': '3',
    'f': '|=', 'g': '6', 'h': '#', 'i': '1', 'j': '_|',
    'k': '|<', 'l': '|_', 'm': '|\\/|', 'n': '|\\|', 'o': '0',
    'p': '|>', 'q': '9', 'r': '|2', 's': '5', 't': '7',
    'u': '|_|', 'v': '\\/', 'w': '\\/\\/', 'x': '><',
    'y': '`/', 'z': '2',
    'A': '4', 'B': '8', 'C': '(', 'D': '|)', 'E': '3',
    'F': '|=', 'G': '6', 'H': '#', 'I': '1', 'J': '_|',
    'K': '|<', 'L': '|_', 'M': '|\\/|', 'N': '|\\|', 'O': '0',
    'P': '|>', 'Q': '9', 'R': '|2', 'S': '5', 'T': '7',
    'U': '|_|', 'V': '\\/', 'W': '\\/\\/', 'X': '><',
    'Y': '`/', 'Z': '2'
}

MORSE_MAP = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}

DECORATOR_STYLES = {
    "Aesthetic Wide": "aesthetic",
    "Sparkle": ("✦ ", " ✦"),
    "Arrow": (">>  ", "  <<"),
    "Star Frame": ("*-. -* ", " *- .-*"),
    "Wave Decoration": ("~=~= ", " =~=~"),
    "Heart Frame": ("<3 ", " <3"),
    "Diamond Frame": ("<> ", " <>"),
    "Lightning Frame": ("// ", " //"),
    "Flower Frame": ("(* ", " *)"),
    "Music Frame": ("# ", " #"),
}

FRAME_STYLES = {
    "Box Frame": {
        "tl": "┌", "tr": "┐", "bl": "└", "br": "┘", "h": "─", "v": "│"
    },
    "Fancy Frame": {
        "tl": "╔", "tr": "╗", "bl": "╚", "br": "╝", "h": "═", "v": "║"
    },
    "Double Box Frame": {
        "tl": "╔", "tr": "╗", "bl": "╚", "br": "╝", "h": "═", "v": "║"
    },
    "Round Box Frame": {
        "tl": "╭", "tr": "╮", "bl": "╰", "br": "╯", "h": "─", "v": "│"
    },
    "Shadow Box Frame": {
        "tl": "┌", "tr": "┒", "bl": "┕", "br": "┛",
        "h_top": "─", "h_bot": "━", "v_left": "│", "v_right": "┃"
    },
}


def stylize_text(text, style_name):
    if style_name in STYLE_MAPS:
        mapping = STYLE_MAPS[style_name]
        if not mapping:
            return text

        out = []
        for ch in text:
            if ch in mapping:
                out.append(mapping[ch])
            elif ch.lower() in mapping:
                out.append(mapping[ch.lower()])
            else:
                out.append(ch)
        return "".join(out)

    if style_name in COMBINING_STYLES:
        c = COMBINING_STYLES[style_name]
        return "".join(ch + c if ch.strip() else ch for ch in text)

    if style_name == "Upside Down":
        return "".join(UPSIDE_DOWN_MAP.get(ch, ch) for ch in reversed(text))

    if style_name == "Mirror":
        return "".join(MIRROR_MAP.get(ch, ch) for ch in reversed(text))

    if style_name == "Leet Speak":
        return "".join(LEET_MAP.get(ch, ch) for ch in text)

    if style_name == "Morse Code":
        parts = []
        for ch in text:
            lo = ch.lower()
            if lo in MORSE_MAP:
                parts.append(MORSE_MAP[lo])
            elif ch == ' ':
                parts.append('/')
            else:
                parts.append(ch)
        return ' '.join(parts)

    if style_name == "Binary":
        return ' '.join(format(ord(ch), '08b') for ch in text)

    if style_name in DECORATOR_STYLES:
        dec = DECORATOR_STYLES[style_name]
        if dec == "aesthetic":
            return '  '.join(text)
        if isinstance(dec, tuple):
            return f"{dec[0]}{text}{dec[1]}"

    if style_name in FRAME_STYLES:
        frame = FRAME_STYLES[style_name]
        lines = text.split('\n')
        ml = max((len(line) for line in lines), default=0)

        if style_name == "Shadow Box Frame":
            ht = frame["h_top"]
            hb = frame["h_bot"]
            vl = frame["v_left"]
            vr = frame["v_right"]

            res = [frame["tl"] + ht * (ml + 2) + frame["tr"]]
            for line in lines:
                res.append(f"{vl} {line.ljust(ml)} {vr}")
            res.append(frame["bl"] + hb * (ml + 2) + frame["br"])
            return '\n'.join(res)

        h = frame["h"]
        v = frame["v"]
        res = [frame["tl"] + h * (ml + 2) + frame["tr"]]
        for line in lines:
            res.append(f"{v} {line.ljust(ml)} {v}")
        res.append(frame["bl"] + h * (ml + 2) + frame["br"])
        return '\n'.join(res)

    return text


def get_all_style_names():
    names = list(STYLE_MAPS.keys())
    for style in (
        list(COMBINING_STYLES.keys())
        + ["Upside Down", "Mirror", "Leet Speak", "Morse Code", "Binary"]
        + list(DECORATOR_STYLES.keys())
        + list(FRAME_STYLES.keys())
    ):
        if style not in names:
            names.append(style)
    return names


def get_style_names_for_category(cat):
    if cat == "All" or cat is None:
        return get_all_style_names()
    return STYLE_CATEGORIES.get(cat, get_all_style_names())


class TranslatorMixin:
    def set_language_code(self, code):
        self.lang = code

    def trx(self, key):
        return TRANSLATIONS.get(
            getattr(self, 'lang', 'tr'),
            TRANSLATIONS["en"]
        ).get(key, key)


def show_themed_message(parent, title, text, icon=QMessageBox.Information):
    msg = QMessageBox(parent)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setIcon(icon)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setStyleSheet(
        f"QMessageBox {{ background-color: {COLORS['dark']}; }}"
        f"QMessageBox QLabel {{ color: {COLORS['text']}; min-width: 260px; font-size: 10pt; }}"
        f"QMessageBox QPushButton {{ background-color: {COLORS['button_bg']}; color: white; border: none; border-radius: 6px; padding: 8px 16px; min-width: 80px; font-weight: 600; }}"
        f"QMessageBox QPushButton:hover {{ background-color: {COLORS['button_hover']}; }}"
    )
    msg.exec_()


class ImageAnalyzer:
    @staticmethod
    def analyze(pil_rgba):
        try:
            rgb = pil_rgba.convert("RGB")
            small = rgb.resize((256, 256), Image.BILINEAR)
            arr = np.array(small).astype(np.float32)
            gray = (
                0.2126 * arr[:, :, 0]
                + 0.7152 * arr[:, :, 1]
                + 0.0722 * arr[:, :, 2]
            )

            mean = float(np.mean(gray))
            std = float(np.std(gray))
            p2, p98 = np.percentile(gray, (2, 98))
            dyn = float(p98 - p2)
            gx = np.abs(np.diff(gray, axis=1)).mean()
            gy = np.abs(np.diff(gray, axis=0)).mean()
            edge = float((gx + gy) / 2)

            rg = arr[:, :, 0] - arr[:, :, 1]
            yb = 0.5 * (arr[:, :, 0] + arr[:, :, 1]) - arr[:, :, 2]
            colorful = float(
                np.sqrt(np.std(rg) ** 2 + np.std(yb) ** 2)
            )

            alpha = (
                np.array(pil_rgba.resize((128, 128)))[:, :, 3]
                if pil_rgba.mode == "RGBA"
                else None
            )
            has_trans = bool(
                alpha is not None and np.mean(alpha < 250) > 0.02
            )

            return {
                "mean": mean,
                "std": std,
                "p2": float(p2),
                "p98": float(p98),
                "dynamic": dyn,
                "edge": edge,
                "colorful": colorful,
                "is_dark": mean < 80,
                "is_bright": mean > 175,
                "low_contrast": std < 35 or dyn < 85,
                "high_detail": edge > 11,
                "is_colorful": colorful > 28,
                "has_transparency": has_trans,
                "orig_w": pil_rgba.width,
                "orig_h": pil_rgba.height
            }
        except Exception:
            return {
                "mean": 127,
                "std": 40,
                "p2": 20,
                "p98": 230,
                "dynamic": 210,
                "edge": 10,
                "colorful": 20,
                "is_dark": False,
                "is_bright": False,
                "low_contrast": False,
                "high_detail": False,
                "is_colorful": False,
                "has_transparency": False,
                "orig_w": 800,
                "orig_h": 600
            }

    @staticmethod
    def recommend(st):
        rec = {
            "brightness": 0,
            "contrast": 10,
            "gamma": 100,
            "sharpness": 120,
            "edge": 25,
            "width": 150,
            "charset": "Detailed",
            "dither": 1,
            "autolevels": False,
            "invert": False,
            "colored": False
        }

        if st["is_dark"]:
            rec["brightness"] = 22
            rec["gamma"] = 118
            rec["contrast"] = 18
            rec["charset"] = "Classic Dark"
        elif st["is_bright"]:
            rec["brightness"] = -8
            rec["gamma"] = 92
            rec["contrast"] = 12
            rec["charset"] = "Detailed"

        if st["low_contrast"]:
            rec["contrast"] = 38
            rec["autolevels"] = True
            rec["charset"] = "Sharp"

        if st["high_detail"]:
            rec["width"] = 190
            rec["edge"] = 32
            rec["sharpness"] = 135
            rec["charset"] = "Detailed"
            rec["dither"] = 1
        else:
            rec["width"] = 130
            rec["edge"] = 18

        try:
            ar = st["orig_w"] / max(1, st["orig_h"])
            if ar > 1.8:
                rec["width"] = min(260, rec["width"] + 30)
            if ar < 0.6:
                rec["width"] = max(90, rec["width"] - 30)
        except Exception:
            pass

        if st["is_colorful"]:
            rec["colored"] = True
        if st["mean"] > 225:
            rec["invert"] = True

        rec["width"] = int(max(60, min(280, rec["width"])))
        return rec

    @staticmethod
    def describe_tr(st, rec):
        parts = []
        if st["is_dark"]:
            parts.append("koyu")
        elif st["is_bright"]:
            parts.append("aydınlık")
        else:
            parts.append("dengeli ton")

        if st["low_contrast"]:
            parts.append("düşük kontrast")
        else:
            parts.append("iyi kontrast")

        if st["high_detail"]:
            parts.append("yüksek detay")
        else:
            parts.append("yumuşak detay")

        if st["is_colorful"]:
            parts.append("renkli")
        if st["has_transparency"]:
            parts.append("şeffaflık var")

        return (
            f"{', '.join(parts)} -> {rec['charset']}, "
            f"Genişlik: {rec['width']}"
        )

    @staticmethod
    def describe_en(st, rec):
        parts = []
        if st["is_dark"]:
            parts.append("dark")
        elif st["is_bright"]:
            parts.append("bright")
        else:
            parts.append("balanced")

        parts.append(
            "low contrast" if st["low_contrast"] else "good contrast"
        )
        parts.append("detailed" if st["high_detail"] else "smooth")

        if st["is_colorful"]:
            parts.append("colorful")

        return (
            f"{', '.join(parts)} -> {rec['charset']}, "
            f"Width: {rec['width']}"
        )


BAYER_4 = (
    np.array(
        [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]],
        dtype=np.float32
    ) / 16.0 - 0.5
)


def _sobel_mag(gray):
    g = gray.astype(np.float32)
    gp = np.pad(g, 1, mode='edge')

    gx = (
        -gp[:-2, :-2] - 2 * gp[1:-1, :-2] - gp[2:, :-2]
        + gp[:-2, 2:] + 2 * gp[1:-1, 2:] + gp[2:, 2:]
    )
    gy = (
        -gp[:-2, :-2] - 2 * gp[:-2, 1:-1] - gp[:-2, 2:]
        + gp[2:, :-2] + 2 * gp[2:, 1:-1] + gp[2:, 2:]
    )

    mag = np.sqrt(gx * gx + gy * gy)
    m = mag.max()
    if m > 0:
        mag = mag / m * 255.0
    return mag


class AsciiEngine:
    @staticmethod
    def convert(
        image_path, width, chars, is_colored, contrast, brightness,
        gamma_val, sharpness_val, invert, edge_strength, auto_levels,
        dither_mode, alpha_mode_idx, bg_rgb
    ):
        try:
            orig = Image.open(image_path).convert("RGBA")

            if contrast != 0:
                orig = ImageEnhance.Contrast(orig).enhance(
                    1.0 + contrast / 100.0
                )

            if brightness != 0:
                orig = ImageEnhance.Brightness(orig).enhance(
                    1.0 + brightness / 100.0
                )

            if sharpness_val != 100:
                orig = ImageEnhance.Sharpness(orig).enhance(
                    max(0.0, sharpness_val / 100.0)
                )

            if gamma_val != 100:
                g = max(0.2, min(3.0, gamma_val / 100.0))
                inv = 1.0 / g
                lut = [
                    int(max(0, min(255, round(
                        255 * ((i / 255) ** inv)
                    ))))
                    for i in range(256)
                ] * 4

                if len(lut) < 1024:
                    lut = (lut * 4)[:1024]

                try:
                    orig = orig.point(lut)
                except Exception:
                    pass

            aspect = orig.height / max(1, orig.width)
            height = max(1, int(width * aspect * 0.52))

            if width * height > 90000:
                scale = (90000 / (width * height)) ** 0.5
                width = max(40, int(width * scale))
                height = max(20, int(height * scale))

            small = orig.resize((width, height), Image.LANCZOS)
            data = np.array(small).astype(np.float32)
            rgb = data[:, :, :3]
            alpha = data[:, :, 3] / 255.0

            if alpha_mode_idx == 2:
                bg = np.zeros_like(rgb)
                bg[:, :, 0] = bg_rgb[0]
                bg[:, :, 1] = bg_rgb[1]
                bg[:, :, 2] = bg_rgb[2]
                rgb = (
                    rgb * alpha[:, :, None]
                    + bg * (1.0 - alpha[:, :, None])
                )

            rgb_u = np.clip(rgb, 0, 255).astype(np.uint8)
            gray = (
                0.2126 * rgb[:, :, 0]
                + 0.7152 * rgb[:, :, 1]
                + 0.0722 * rgb[:, :, 2]
            )

            if auto_levels:
                lo, hi = np.percentile(gray, (2, 98))
                if hi - lo > 8:
                    gray = np.clip(
                        (gray - lo) / (hi - lo) * 255,
                        0,
                        255
                    )

            if edge_strength > 0:
                mag = _sobel_mag(gray)
                k = (edge_strength / 100.0) * 0.55
                gray = np.clip(gray - mag * k, 0, 255)

            if invert:
                gray = 255 - gray

            n = len(chars)
            if n < 2:
                chars = "@%#*+=-:. "
                n = len(chars)

            ch_arr = np.array(list(chars))

            if dither_mode == 1:
                bh, bw = BAYER_4.shape
                tiled = np.tile(
                    BAYER_4,
                    (height // bh + 1, width // bw + 1)
                )[:height, :width]
                spread = (255.0 / max(1, n - 1)) * 0.85
                gray_j = np.clip(gray + tiled * spread, 0, 255)
                idx = np.clip(
                    (gray_j / 255.0 * (n - 1)).astype(int),
                    0,
                    n - 1
                )

            elif dither_mode == 2:
                buf = gray.copy().astype(np.float32)
                idx = np.zeros((height, width), dtype=int)

                for y in range(height):
                    for x in range(width):
                        old = buf[y, x]
                        ni = int(round(old / 255.0 * (n - 1)))
                        ni = max(0, min(n - 1, ni))
                        idx[y, x] = ni
                        newv = ni / (n - 1) * 255.0
                        err = old - newv

                        if x + 1 < width:
                            buf[y, x + 1] += err * 7 / 16

                        if y + 1 < height:
                            if x > 0:
                                buf[y + 1, x - 1] += err * 3 / 16
                            buf[y + 1, x] += err * 5 / 16
                            if x + 1 < width:
                                buf[y + 1, x + 1] += err * 1 / 16

            else:
                idx = np.clip(
                    (gray / 255.0 * (n - 1)).astype(int),
                    0,
                    n - 1
                )

            char_grid = ch_arr[idx]
            mask_trans = alpha <= 0.04

            if np.any(mask_trans):
                if alpha_mode_idx == 0:
                    char_grid[mask_trans] = ' '
                elif alpha_mode_idx == 1:
                    char_grid[mask_trans] = '.'

            lines_plain = ["".join(row.tolist()) for row in char_grid]
            plain = "\n".join(lines_plain)

            if is_colored:
                html_lines = []

                for y in range(height):
                    parts = []
                    for x in range(width):
                        ch = char_grid[y, x]

                        if mask_trans[y, x] and alpha_mode_idx != 2:
                            if ch == ' ':
                                parts.append(' ')
                                continue
                            parts.append(
                                '<span style="color:rgb(150,150,150)">'
                                f'{html.escape(ch)}</span>'
                            )
                            continue

                        r, g, b = rgb_u[y, x]
                        parts.append(
                            f'<span style="color:rgb({int(r)},{int(g)},{int(b)})">'
                            f'{html.escape(ch)}</span>'
                        )

                    html_lines.append("".join(parts))

                body = "\n".join(html_lines)

                html_text = (
                    f"<html><body style='background:{COLORS['darker']};'>"
                    f"<pre style='font-family:Consolas,Courier New,monospace;"
                    f"line-height:1.0;margin:0;'>"
                    f"{body}</pre></body></html>"
                )
            else:
                html_text = (
                    f"<html><body style='background:{COLORS['darker']};"
                    f"color:{COLORS['text']};'>"
                    f"<pre style='font-family:Consolas,Courier New,monospace;"
                    f"line-height:1.0;margin:0;'>"
                    f"{html.escape(plain)}</pre></body></html>"
                )

            return {
                "success": True,
                "plain": plain,
                "html": html_text,
                "width": width,
                "height": height,
                "is_html": is_colored,
                "colors": rgb_u if is_colored else None
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "plain": "",
                "html": "",
                "width": 0,
                "height": 0,
                "is_html": False,
                "colors": None
            }


class AsciiWorker(QThread):
    finished = pyqtSignal(dict)

    def __init__(self, params):
        super().__init__()
        self.params = params

    def run(self):
        res = AsciiEngine.convert(**self.params)
        self.finished.emit(res)


class CustomTitleBar(QWidget, TranslatorMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.set_language_code("tr")
        self.setFixedHeight(38)
        self.dragging = False
        self.drag_position = QPoint()

        self.setStyleSheet(
            f"background:qlineargradient(x1:0,y1:0,x2:1,y2:0,"
            f"stop:0 {COLORS['accent']},stop:1 #0A2540);"
            f"border-top-left-radius:12px;border-top-right-radius:12px;"
        )

        lay = QHBoxLayout(self)
        lay.setContentsMargins(14, 0, 8, 0)
        lay.setSpacing(8)

        self.dot = QLabel("●")
        self.dot.setStyleSheet(
            f"color:{COLORS['primary']};font-size:13px;background:transparent;"
        )
        lay.addWidget(self.dot)

        self.title_label = QLabel("")
        self.title_label.setStyleSheet(
            "color:white;font-weight:700;font-size:12px;background:transparent;"
        )
        lay.addWidget(self.title_label)
        lay.addStretch()

        self.minimize_btn = self.create_button("")
        self.minimize_btn.clicked.connect(self.parent.showMinimized)

        self.maximize_btn = self.create_button("")
        self.maximize_btn.clicked.connect(self.toggle_maximize)

        self.close_btn = self.create_button("", close=True)
        self.close_btn.clicked.connect(self.parent.close)

        lay.addWidget(self.minimize_btn)
        lay.addWidget(self.maximize_btn)
        lay.addWidget(self.close_btn)

        self.retranslate_ui()

    def create_button(self, text, close=False):
        button = QPushButton(text)
        button.setFixedSize(34, 26)

        if close:
            button.setStyleSheet(
                "QPushButton{background:rgba(255,255,255,0.12);color:white;"
                "border:none;border-radius:6px;font-weight:700;}"
                "QPushButton:hover{background:#F44336;}"
                "QPushButton:pressed{background:#A40E26;}"
            )
        else:
            button.setStyleSheet(
                "QPushButton{background:rgba(255,255,255,0.12);color:white;"
                "border:none;border-radius:6px;font-weight:700;}"
                "QPushButton:hover{background:rgba(255,255,255,0.22);}"
                "QPushButton:pressed{background:rgba(255,255,255,0.30);}"
            )
        return button

    def retranslate_ui(self):
        self.title_label.setText(
            f"{self.trx('app_title')}  ·  {BRAND_NAME}"
        )

    def toggle_maximize(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = (
                e.globalPos() - self.parent.frameGeometry().topLeft()
            )
            e.accept()

    def mouseMoveEvent(self, e):
        if (
            self.dragging
            and e.buttons() == Qt.LeftButton
            and not self.parent.isMaximized()
        ):
            self.parent.move(e.globalPos() - self.drag_position)
            e.accept()

    def mouseReleaseEvent(self, e):
        self.dragging = False
        e.accept()

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.toggle_maximize()


class FooterSignature(QLabel, TranslatorMixin):
    def __init__(self):
        super().__init__()
        self.set_language_code("tr")
        self.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.setStyleSheet(
            f"color:{COLORS['text_secondary']};font-size:11px;"
            f"font-weight:600;padding:4px 6px;background:transparent;"
        )
        self.retranslate_ui()

    def retranslate_ui(self):
        self.setText(f"{self.trx('designed_by')} {BRAND_NAME}")


class LabeledSlider(QWidget, TranslatorMixin):
    def __init__(self, title_key, minimum, maximum, value, suffix=""):
        super().__init__()
        self.set_language_code("tr")
        self.title_key = title_key
        self.suffix = suffix

        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(4)

        self.title = QLabel("")
        self.title.setStyleSheet(
            f"color:{COLORS['text_secondary']};font-size:10px;"
            f"background:transparent;"
        )
        lay.addWidget(self.title)

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(6)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(minimum, maximum)
        self.slider.setValue(value)

        self.value_label = QLabel(str(value) + suffix)
        self.value_label.setFixedWidth(52)
        self.value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.value_label.setStyleSheet(
            f"color:{COLORS['primary']};font-weight:700;font-size:10px;"
            f"background:{COLORS['darker']};border:1px solid {COLORS['border']};"
            f"border-radius:4px;padding:2px 4px;"
        )

        self.slider.valueChanged.connect(
            lambda v: self.value_label.setText(str(v) + self.suffix)
        )

        row.addWidget(self.slider)
        row.addWidget(self.value_label)
        lay.addLayout(row)

        self.retranslate_ui()

    def retranslate_ui(self):
        self.title.setText(self.trx(self.title_key))

    def setValue(self, value):
        self.slider.setValue(value)

    def value(self):
        return self.slider.value()


class ImageAsciiPage(QWidget, TranslatorMixin):
    def __init__(self):
        super().__init__()
        self.set_language_code("tr")
        self.image_path = None
        self.ascii_plain = ""
        self.ascii_html = ""
        self.current_is_html = False
        self.last_colors = None
        self.bg_color = QColor("#07090D")
        self._worker = None
        self.setAcceptDrops(True)

        self.update_timer = QTimer(self)
        self.update_timer.setSingleShot(True)
        self.update_timer.timeout.connect(self.update_ascii)

        self.init_ui()

    def init_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(0, 0, 0, 0)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setHandleWidth(8)

        self.build_left_panel()
        self.build_right_panel()

        self.splitter.addWidget(self.left_panel)
        self.splitter.addWidget(self.right_panel)
        self.splitter.setSizes([400, 760])
        self.splitter.setStretchFactor(0, 0)
        self.splitter.setStretchFactor(1, 1)

        main.addWidget(self.splitter)
        self.retranslate_ui()

    def build_left_panel(self):
        self.left_panel = QWidget()
        self.left_panel.setObjectName("leftPanel")
        self.left_panel.setMinimumWidth(365)
        self.left_panel.setMaximumWidth(520)

        outer = QVBoxLayout(self.left_panel)
        outer.setContentsMargins(0, 0, 0, 0)

        scroll = QScrollArea()
        scroll.setObjectName("controlScroll")
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)

        self.left_content = QWidget()
        self.left_content.setObjectName("leftContent")

        L = QVBoxLayout(self.left_content)
        L.setContentsMargins(12, 12, 12, 12)
        L.setSpacing(12)

        lang_group = QGroupBox()
        lh = QHBoxLayout(lang_group)
        lh.setContentsMargins(12, 10, 12, 10)

        self.language_label = QLabel()
        self.language_combo = QComboBox()
        self.language_combo.setMinimumWidth(110)

        self.language_combo.addItems(list(LANGUAGES.keys()))
        self.language_combo.setCurrentText("Türkçe")

        lh.addWidget(self.language_label)
        lh.addStretch()
        lh.addWidget(self.language_combo)
        L.addWidget(lang_group)

        self.select_image_btn = QPushButton()
        self.select_image_btn.setObjectName("primaryButton")
        self.select_image_btn.setMinimumHeight(42)
        self.select_image_btn.clicked.connect(self.select_image)
        L.addWidget(self.select_image_btn)

        self.auto_btn = QPushButton()
        self.auto_btn.setObjectName("autoButton")
        self.auto_btn.setMinimumHeight(38)
        self.auto_btn.clicked.connect(self.auto_detect_and_apply)
        L.addWidget(self.auto_btn)

        self.detect_label = QLabel("")
        self.detect_label.setWordWrap(True)
        self.detect_label.setStyleSheet(
            f"color:{COLORS['primary_light']};background:{COLORS['darker']};"
            f"border:1px solid {COLORS['border']};border-radius:6px;"
            f"padding:7px 9px;font-size:10px;"
        )
        L.addWidget(self.detect_label)

        self.preview_group = QGroupBox()
        pv = QVBoxLayout(self.preview_group)

        self.original_image_label = QLabel()
        self.original_image_label.setObjectName("previewLabel")
        self.original_image_label.setAlignment(Qt.AlignCenter)
        self.original_image_label.setMinimumHeight(200)
        self.original_image_label.setMaximumHeight(280)
        self.original_image_label.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        pv.addWidget(self.original_image_label)
        L.addWidget(self.preview_group)

        self.settings_group = QGroupBox()
        S = QVBoxLayout(self.settings_group)
        S.setSpacing(10)

        self.width_control = LabeledSlider(
            "ascii_width", 40, 280, 150
        )
        self.width_control.slider.valueChanged.connect(self.schedule_update)
        S.addWidget(self.width_control)

        self.character_preset_label = QLabel()
        self.char_combo = QComboBox()
        self.char_combo.addItems(list(ASCII_PRESETS.keys()))
        self.char_combo.setCurrentText("Detailed")
        self.char_combo.currentIndexChanged.connect(self.on_charset_changed)
        S.addWidget(self.character_preset_label)
        S.addWidget(self.char_combo)

        self.custom_characters_label = QLabel()
        self.custom_chars = QTextEdit()
        self.custom_chars.setFixedHeight(62)
        self.custom_chars.setPlainText(ASCII_PRESETS["Detailed"])
        self.custom_chars.textChanged.connect(self.schedule_update)
        S.addWidget(self.custom_characters_label)
        S.addWidget(self.custom_chars)

        mr = QHBoxLayout()
        self.color_mode_label = QLabel()
        self.color_combo = QComboBox()
        self.color_combo.currentIndexChanged.connect(self.schedule_update)
        mr.addWidget(self.color_mode_label)
        mr.addStretch()
        mr.addWidget(self.color_combo)
        S.addLayout(mr)

        dr = QHBoxLayout()
        self.dither_label = QLabel()
        self.dither_combo = QComboBox()
        self.dither_combo.currentIndexChanged.connect(self.schedule_update)
        dr.addWidget(self.dither_label)
        dr.addStretch()
        dr.addWidget(self.dither_combo)
        S.addLayout(dr)

        self.contrast_control = LabeledSlider(
            "contrast", -100, 100, 10
        )
        self.contrast_control.slider.valueChanged.connect(self.schedule_update)
        S.addWidget(self.contrast_control)

        self.brightness_control = LabeledSlider(
            "brightness", -100, 100, 0
        )
        self.brightness_control.slider.valueChanged.connect(self.schedule_update)
        S.addWidget(self.brightness_control)

        self.gamma_control = LabeledSlider(
            "gamma", 40, 220, 100
        )
        self.gamma_control.slider.valueChanged.connect(self.schedule_update)
        S.addWidget(self.gamma_control)

        self.sharpness_control = LabeledSlider(
            "sharpness", 0, 300, 120
        )
        self.sharpness_control.slider.valueChanged.connect(self.schedule_update)
        S.addWidget(self.sharpness_control)

        self.edge_control = LabeledSlider(
            "edge_strength", 0, 100, 25
        )
        self.edge_control.slider.valueChanged.connect(self.schedule_update)
        S.addWidget(self.edge_control)

        self.autolevels_check = QCheckBox()
        self.autolevels_check.stateChanged.connect(self.schedule_update)
        S.addWidget(self.autolevels_check)

        self.invert_check = QCheckBox()
        self.invert_check.stateChanged.connect(self.schedule_update)
        S.addWidget(self.invert_check)

        self.auto_update_check = QCheckBox()
        self.auto_update_check.setChecked(True)
        S.addWidget(self.auto_update_check)

        self.transparency_group = QGroupBox()
        TL = QVBoxLayout(self.transparency_group)

        ar = QHBoxLayout()
        self.transparent_area_label = QLabel()
        self.alpha_combo = QComboBox()
        self.alpha_combo.currentIndexChanged.connect(self.schedule_update)
        ar.addWidget(self.transparent_area_label)
        ar.addStretch()
        ar.addWidget(self.alpha_combo)
        TL.addLayout(ar)

        br = QHBoxLayout()
        self.background_color_label = QLabel()
        self.bg_color_btn = QPushButton()
        self.bg_color_btn.setObjectName("secondaryButton")
        self.bg_color_btn.clicked.connect(self.choose_bg_color)
        br.addWidget(self.background_color_label)
        br.addStretch()
        br.addWidget(self.bg_color_btn)
        TL.addLayout(br)

        S.addWidget(self.transparency_group)
        L.addWidget(self.settings_group)

        self.actions_group = QGroupBox()
        A = QVBoxLayout(self.actions_group)
        A.setSpacing(8)

        self.copy_btn = QPushButton()
        self.copy_btn.setObjectName("secondaryButton")
        self.copy_btn.clicked.connect(self.copy_ascii)
        self.copy_btn.setEnabled(False)
        A.addWidget(self.copy_btn)

        self.save_txt_btn = QPushButton()
        self.save_txt_btn.setObjectName("secondaryButton")
        self.save_txt_btn.clicked.connect(self.save_ascii_txt)
        self.save_txt_btn.setEnabled(False)
        A.addWidget(self.save_txt_btn)

        self.save_html_btn = QPushButton()
        self.save_html_btn.setObjectName("secondaryButton")
        self.save_html_btn.clicked.connect(self.save_ascii_html)
        self.save_html_btn.setEnabled(False)
        A.addWidget(self.save_html_btn)

        self.save_png_btn = QPushButton()
        self.save_png_btn.setObjectName("secondaryButton")
        self.save_png_btn.clicked.connect(self.save_preview_as_image)
        self.save_png_btn.setEnabled(False)
        A.addWidget(self.save_png_btn)

        L.addWidget(self.actions_group)
        L.addStretch()

        scroll.setWidget(self.left_content)
        outer.addWidget(scroll)

    def build_right_panel(self):
        self.right_panel = QWidget()
        self.right_panel.setObjectName("rightPanel")
        self.right_panel.setMinimumWidth(500)

        R = QVBoxLayout(self.right_panel)
        R.setContentsMargins(12, 12, 12, 12)
        R.setSpacing(10)

        top = QHBoxLayout()
        self.preview_title = QLabel()
        self.preview_title.setStyleSheet(
            f"color:{COLORS['primary']};font-size:13px;"
            f"font-weight:800;background:transparent;"
        )

        self.size_info = QLabel()
        self.size_info.setStyleSheet(
            f"color:{COLORS['text_secondary']};font-size:10px;"
            f"background:transparent;"
        )

        top.addWidget(self.preview_title)
        top.addStretch()
        top.addWidget(self.size_info)
        R.addLayout(top)

        self.progress = QProgressBar()
        self.progress.setRange(0, 0)
        self.progress.setFixedHeight(4)
        self.progress.setTextVisible(False)
        self.progress.setVisible(False)
        R.addWidget(self.progress)

        self.ascii_preview = QTextEdit()
        self.ascii_preview.setObjectName("asciiPreview")
        self.ascii_preview.setReadOnly(True)
        self.ascii_preview.setWordWrapMode(QTextOption.NoWrap)
        self.ascii_preview.setFont(QFont("Consolas", 9))
        self.ascii_preview.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        R.addWidget(self.ascii_preview)

        fr = QHBoxLayout()
        self.fontsize_label = QLabel()
        self.font_slider = QSlider(Qt.Horizontal)
        self.font_slider.setRange(6, 18)
        self.font_slider.setValue(9)
        self.font_slider.setMaximumWidth(220)
        self.font_slider.valueChanged.connect(
            lambda v: self.ascii_preview.setFont(QFont("Consolas", v))
        )
        fr.addWidget(self.fontsize_label)
        fr.addWidget(self.font_slider)
        fr.addStretch()
        R.addLayout(fr)

        bot = QHBoxLayout()
        self.status_label = QLabel()
        self.status_label.setStyleSheet(
            f"color:{COLORS['text_secondary']};font-size:10px;"
            f"background:transparent;"
        )
        bot.addWidget(self.status_label)
        bot.addStretch()

        self.signature = FooterSignature()
        bot.addWidget(self.signature)
        R.addLayout(bot)

    def retranslate_ui(self):
        self.language_label.setText(self.trx("language"))
        self.select_image_btn.setText(self.trx("load_image"))
        self.auto_btn.setText(self.trx("auto_detect_btn"))

        if not self.detect_label.text():
            self.detect_label.setText(
                f"{self.trx('detection_info')}: -"
            )

        self.preview_group.setTitle(self.trx("image_preview"))

        if not self.image_path:
            self.original_image_label.setText(
                f"{self.trx('no_image_selected')}\n{self.trx('drop_hint')}"
            )

        self.settings_group.setTitle(self.trx("ascii_settings"))
        self.character_preset_label.setText(
            self.trx("character_preset")
        )
        self.custom_characters_label.setText(
            self.trx("custom_characters")
        )
        self.color_mode_label.setText(self.trx("color_mode"))

        ci = self.color_combo.currentIndex()
        self.color_combo.blockSignals(True)
        self.color_combo.clear()
        self.color_combo.addItems([
            self.trx("black_white"),
            self.trx("colored")
        ])
        self.color_combo.setCurrentIndex(max(0, ci))
        self.color_combo.blockSignals(False)

        self.dither_label.setText(self.trx("dithering"))

        di = self.dither_combo.currentIndex()
        self.dither_combo.blockSignals(True)
        self.dither_combo.clear()
        self.dither_combo.addItems([
            self.trx("dither_none"),
            self.trx("dither_ordered"),
            self.trx("dither_floyd")
        ])
        self.dither_combo.setCurrentIndex(1 if di < 0 else di)
        self.dither_combo.blockSignals(False)

        self.autolevels_check.setText(self.trx("auto_levels"))
        self.invert_check.setText(self.trx("invert_brightness"))
        self.auto_update_check.setText(self.trx("auto_update"))

        self.transparency_group.setTitle(self.trx("transparency"))
        self.transparent_area_label.setText(self.trx("transparent_area"))

        ai = self.alpha_combo.currentIndex()
        self.alpha_combo.blockSignals(True)
        self.alpha_combo.clear()
        self.alpha_combo.addItems([
            self.trx("keep_empty"),
            self.trx("use_dot"),
            self.trx("blend_background")
        ])
        self.alpha_combo.setCurrentIndex(max(0, ai))
        self.alpha_combo.blockSignals(False)

        self.background_color_label.setText(
            self.trx("background_color")
        )
        self.bg_color_btn.setText(self.trx("choose"))

        self.actions_group.setTitle(self.trx("actions"))
        self.copy_btn.setText(self.trx("copy_ascii"))
        self.save_txt_btn.setText(self.trx("save_txt"))
        self.save_html_btn.setText(self.trx("save_html"))
        self.save_png_btn.setText(self.trx("save_png_preview"))

        self.preview_title.setText(self.trx("ascii_preview"))
        self.fontsize_label.setText(self.trx("preview_fontsize"))

        if (
            self.size_info.text() == ""
            or "Boyut" in self.size_info.text()
            or "Size" in self.size_info.text()
        ):
            self.size_info.setText(f"{self.trx('size')}: -")

        if (
            self.status_label.text() in ("Hazır", "Ready", "")
            or not self.image_path
        ):
            self.status_label.setText(self.trx("ready"))

        controls = [
            self.width_control,
            self.contrast_control,
            self.brightness_control,
            self.gamma_control,
            self.sharpness_control,
            self.edge_control
        ]
        for widget in controls:
            widget.set_language_code(self.lang)
            widget.retranslate_ui()

        self.signature.set_language_code(self.lang)
        self.signature.retranslate_ui()

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            path = url.toLocalFile()
            if path.lower().endswith(
                ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')
            ):
                self.load_path(path)
                break

    def choose_bg_color(self):
        color = QColorDialog.getColor(
            self.bg_color,
            self,
            self.trx("choose")
        )
        if color.isValid():
            self.bg_color = color
            self.schedule_update()

    def on_charset_changed(self):
        name = self.char_combo.currentText()
        if name in ASCII_PRESETS:
            self.custom_chars.blockSignals(True)
            self.custom_chars.setPlainText(ASCII_PRESETS[name])
            self.custom_chars.blockSignals(False)
            self.schedule_update()

    def schedule_update(self):
        if self.auto_update_check.isChecked():
            self.update_timer.start(200)

    def get_chars(self):
        chars = self.custom_chars.toPlainText().replace("\n", "")
        chars = "".join(dict.fromkeys(chars))
        if len(chars) < 2:
            chars = "@%#*+=-:. "
        return chars

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            self.trx("select_image"),
            "",
            f"{self.trx('image_files')} "
            "(*.png *.jpg *.jpeg *.bmp *.gif *.webp)"
        )
        if file_path:
            self.load_path(file_path)

    def load_path(self, file_path):
        self.image_path = file_path
        self.status_label.setText(os.path.basename(file_path))
        self.update_preview_image()
        self.update_ascii()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.update_preview_image()

    def update_preview_image(self):
        if not self.image_path:
            return

        pixmap = QPixmap(self.image_path)
        if pixmap.isNull():
            self.original_image_label.setText(
                self.trx("image_not_loaded")
            )
            self.original_image_label.setPixmap(QPixmap())
            return

        scaled = pixmap.scaled(
            self.original_image_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.original_image_label.setPixmap(scaled)

    def auto_detect_and_apply(self):
        if not self.image_path:
            return

        self.status_label.setText(self.trx("analyzing"))
        QApplication.processEvents()

        try:
            pil = Image.open(self.image_path).convert("RGBA")
            stats = ImageAnalyzer.analyze(pil)
            rec = ImageAnalyzer.recommend(stats)

            controls = [
                (self.brightness_control, "brightness"),
                (self.contrast_control, "contrast"),
                (self.gamma_control, "gamma"),
                (self.sharpness_control, "sharpness"),
                (self.edge_control, "edge"),
                (self.width_control, "width")
            ]

            for control, key in controls:
                control.blockSignals(True)
                control.setValue(rec[key])
                control.blockSignals(False)
                control.value_label.setText(str(rec[key]))

            self.autolevels_check.blockSignals(True)
            self.autolevels_check.setChecked(rec["autolevels"])
            self.autolevels_check.blockSignals(False)

            self.invert_check.blockSignals(True)
            self.invert_check.setChecked(rec["invert"])
            self.invert_check.blockSignals(False)

            if rec["charset"] in ASCII_PRESETS:
                self.char_combo.blockSignals(True)
                self.char_combo.setCurrentText(rec["charset"])
                self.char_combo.blockSignals(False)

                self.custom_chars.blockSignals(True)
                self.custom_chars.setPlainText(
                    ASCII_PRESETS[rec["charset"]]
                )
                self.custom_chars.blockSignals(False)

            self.dither_combo.blockSignals(True)
            self.dither_combo.setCurrentIndex(rec["dither"])
            self.dither_combo.blockSignals(False)

            self.color_combo.blockSignals(True)
            self.color_combo.setCurrentIndex(
                1 if rec["colored"] else 0
            )
            self.color_combo.blockSignals(False)

            if self.lang == "tr":
                desc = ImageAnalyzer.describe_tr(stats, rec)
            else:
                desc = ImageAnalyzer.describe_en(stats, rec)

            self.detect_label.setText(
                f"{self.trx('detection_info')}: {desc}"
            )
            self.status_label.setText(self.trx("auto_tuned_msg"))
            self.update_ascii()

        except Exception as e:
            show_themed_message(
                self,
                self.trx("error"),
                str(e),
                QMessageBox.Critical
            )

    def collect_params(self):
        return dict(
            image_path=self.image_path,
            width=self.width_control.value(),
            chars=self.get_chars(),
            is_colored=(self.color_combo.currentIndex() == 1),
            contrast=self.contrast_control.value(),
            brightness=self.brightness_control.value(),
            gamma_val=self.gamma_control.value(),
            sharpness_val=self.sharpness_control.value(),
            invert=self.invert_check.isChecked(),
            edge_strength=self.edge_control.value(),
            auto_levels=self.autolevels_check.isChecked(),
            dither_mode=self.dither_combo.currentIndex(),
            alpha_mode_idx=self.alpha_combo.currentIndex(),
            bg_rgb=(
                self.bg_color.red(),
                self.bg_color.green(),
                self.bg_color.blue()
            )
        )

    def update_ascii(self):
        if not self.image_path:
            return

        if self._worker and self._worker.isRunning():
            try:
                self._worker.terminate()
                self._worker.wait(300)
            except Exception:
                pass

        self.status_label.setText(self.trx("processing"))
        self.progress.setVisible(True)

        self._worker = AsciiWorker(self.collect_params())
        self._worker.finished.connect(self._on_done)
        self._worker.start()

    def _on_done(self, res):
        self.progress.setVisible(False)

        if not res.get("success"):
            self.ascii_preview.setPlainText(
                f"{self.trx('error')}: {res.get('error')}"
            )
            self.status_label.setText(self.trx("error"))
            self.size_info.setText(f"{self.trx('size')}: -")

            for button in [
                self.copy_btn,
                self.save_txt_btn,
                self.save_html_btn,
                self.save_png_btn
            ]:
                button.setEnabled(False)
            return

        self.ascii_plain = res["plain"]
        self.ascii_html = res["html"]
        self.current_is_html = res["is_html"]
        self.last_colors = res["colors"]

        if self.current_is_html:
            self.ascii_preview.setHtml(self.ascii_html)
        else:
            self.ascii_preview.setPlainText(self.ascii_plain)

        mode = self.color_combo.currentText()
        self.size_info.setText(
            f"{self.trx('size')}: {res['width']} x {res['height']} "
            f"| {self.trx('mode')}: {mode}"
        )
        self.status_label.setText(self.trx("ready"))

        for button in [
            self.copy_btn,
            self.save_txt_btn,
            self.save_html_btn,
            self.save_png_btn
        ]:
            button.setEnabled(True)

    def copy_ascii(self):
        if not self.ascii_plain:
            return

        QApplication.clipboard().setText(self.ascii_plain)
        show_themed_message(
            self,
            self.trx("copied"),
            self.trx("ascii_copied")
        )

    def save_ascii_txt(self):
        if not self.ascii_plain:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            self.trx("save_txt_dialog"),
            "ascii_art.txt",
            "Text Files (*.txt)"
        )
        if not file_path:
            return

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.ascii_plain)

            show_themed_message(
                self,
                self.trx("saved"),
                self.trx("txt_saved")
            )
        except Exception as e:
            show_themed_message(
                self,
                self.trx("error"),
                str(e),
                QMessageBox.Critical
            )

    def save_ascii_html(self):
        if not self.ascii_html:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            self.trx("save_html_dialog"),
            "ascii_art.html",
            "HTML Files (*.html)"
        )
        if not file_path:
            return

        try:
            content = self.ascii_html

            if not self.current_is_html:
                content = (
                    "<!DOCTYPE html><html><head>"
                    "<meta charset='utf-8'><title>ASCII Art</title>"
                    "</head>"
                    f"<body style='background:{COLORS['darker']};"
                    f"color:{COLORS['text']};display:flex;"
                    f"justify-content:center;padding:20px;'>"
                    "<pre style='font-family:Consolas,Courier New,monospace;"
                    "line-height:1.0;margin:0;font-size:9px;'>"
                    f"{html.escape(self.ascii_plain)}"
                    "</pre></body></html>"
                )

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

            show_themed_message(
                self,
                self.trx("saved"),
                self.trx("html_saved")
            )
        except Exception as e:
            show_themed_message(
                self,
                self.trx("error"),
                str(e),
                QMessageBox.Critical
            )

    def save_preview_as_image(self):
        if not self.ascii_plain:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            self.trx("save_png"),
            "ascii_preview.png",
            "PNG Files (*.png)"
        )
        if not file_path:
            return

        try:
            font = QFont("Consolas", 10)
            font.setStyleHint(QFont.Monospace)
            metrics = QFontMetrics(font)

            cw = metrics.horizontalAdvance('M')
            chh = metrics.height()
            lines = self.ascii_plain.split('\n')
            h = len(lines)
            w = max((len(line) for line in lines), default=1)
            iw = w * cw + 20
            ih = h * chh + 20

            if iw > 5000 or ih > 5000:
                show_themed_message(
                    self,
                    self.trx("error"),
                    self.trx("image_too_large"),
                    QMessageBox.Warning
                )
                return

            img = QImage(iw, ih, QImage.Format_RGB32)
            img.fill(QColor(COLORS['darker']))

            painter = QPainter(img)
            painter.setFont(font)

            if self.current_is_html and self.last_colors is not None:
                cols = self.last_colors

                for y, line in enumerate(lines):
                    for x, char in enumerate(line):
                        if y < cols.shape[0] and x < cols.shape[1]:
                            r, g, b = cols[y, x]
                            painter.setPen(
                                QColor(int(r), int(g), int(b))
                            )
                        else:
                            painter.setPen(QColor(COLORS['text']))

                        painter.drawText(
                            10 + x * cw,
                            10 + (y + 1) * chh - metrics.descent(),
                            char
                        )
            else:
                painter.setPen(QColor(COLORS['text']))
                for y, line in enumerate(lines):
                    painter.drawText(
                        10,
                        10 + (y + 1) * chh - metrics.descent(),
                        line
                    )

            painter.end()
            img.save(file_path, "PNG")

            show_themed_message(
                self,
                self.trx("saved"),
                self.trx("png_saved")
            )
        except Exception as e:
            show_themed_message(
                self,
                self.trx("error"),
                str(e),
                QMessageBox.Critical
            )


class StylizedTextPage(QWidget, TranslatorMixin):
    def __init__(self):
        super().__init__()
        self.set_language_code("tr")
        self.current_output = ""
        self.init_ui()

    def init_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setHandleWidth(8)

        self.build_left_panel()
        self.build_right_panel()

        self.splitter.addWidget(self.left_panel)
        self.splitter.addWidget(self.right_panel)
        self.splitter.setSizes([400, 760])
        self.splitter.setStretchFactor(0, 0)
        self.splitter.setStretchFactor(1, 1)

        root.addWidget(self.splitter)

        self.retranslate_ui()
        self.generate_text()

    def build_left_panel(self):
        self.left_panel = QWidget()
        self.left_panel.setObjectName("leftPanel")
        self.left_panel.setMinimumWidth(365)
        self.left_panel.setMaximumWidth(520)

        outer = QVBoxLayout(self.left_panel)
        outer.setContentsMargins(0, 0, 0, 0)

        scroll = QScrollArea()
        scroll.setObjectName("controlScroll")
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)

        self.left_content = QWidget()
        self.left_content.setObjectName("leftContent")

        L = QVBoxLayout(self.left_content)
        L.setContentsMargins(12, 12, 12, 12)
        L.setSpacing(12)

        self.input_group = QGroupBox()
        il = QVBoxLayout(self.input_group)

        self.text_input = QLineEdit()
        il.addWidget(self.text_input)
        L.addWidget(self.input_group)

        self.style_group = QGroupBox()
        sl = QVBoxLayout(self.style_group)

        self.category_label = QLabel()
        self.category_combo = QComboBox()
        self.style_preset_label = QLabel()
        self.style_combo = QComboBox()

        self.style_preview_label = QLabel()
        self.style_preview_label.setWordWrap(True)
        self.style_preview_label.setStyleSheet(
            f"color:{COLORS['primary_light']};background:{COLORS['darker']};"
            f"border:1px solid {COLORS['border']};border-radius:6px;"
            f"padding:9px;font-size:13px;min-height:22px;"
        )

        self.uppercase_check = QCheckBox()
        self.spaced_check = QCheckBox()

        sl.addWidget(self.category_label)
        sl.addWidget(self.category_combo)
        sl.addWidget(self.style_preset_label)
        sl.addWidget(self.style_combo)
        sl.addWidget(self.style_preview_label)
        sl.addWidget(self.uppercase_check)
        sl.addWidget(self.spaced_check)
        L.addWidget(self.style_group)

        self.actions_group = QGroupBox()
        al = QVBoxLayout(self.actions_group)

        self.copy_btn = QPushButton()
        self.copy_btn.setObjectName("secondaryButton")
        self.copy_btn.clicked.connect(self.copy_text)
        al.addWidget(self.copy_btn)

        self.save_btn = QPushButton()
        self.save_btn.setObjectName("secondaryButton")
        self.save_btn.clicked.connect(self.save_text)
        al.addWidget(self.save_btn)

        L.addWidget(self.actions_group)
        L.addStretch()

        scroll.setWidget(self.left_content)
        outer.addWidget(scroll)

        self.category_combo.addItems(list(STYLE_CATEGORIES.keys()))
        self.populate_style_combo("All")
        self.category_combo.currentIndexChanged.connect(
            self.on_category_changed
        )
        self.style_combo.currentIndexChanged.connect(self.on_style_changed)
        self.text_input.textChanged.connect(self.generate_text)
        self.uppercase_check.stateChanged.connect(self.generate_text)
        self.spaced_check.stateChanged.connect(self.generate_text)

    def build_right_panel(self):
        self.right_panel = QWidget()
        self.right_panel.setObjectName("rightPanel")
        self.right_panel.setMinimumWidth(500)

        R = QVBoxLayout(self.right_panel)
        R.setContentsMargins(12, 12, 12, 12)
        R.setSpacing(10)

        top = QHBoxLayout()

        self.title = QLabel()
        self.title.setStyleSheet(
            f"color:{COLORS['primary']};font-size:13px;"
            f"font-weight:800;background:transparent;"
        )

        self.preview_info = QLabel()
        self.preview_info.setStyleSheet(
            f"color:{COLORS['text_secondary']};font-size:10px;"
            f"background:transparent;"
        )

        top.addWidget(self.title)
        top.addStretch()
        top.addWidget(self.preview_info)
        R.addLayout(top)

        self.output_preview = QTextEdit()
        self.output_preview.setObjectName("asciiPreview")
        self.output_preview.setReadOnly(True)
        self.output_preview.setFont(QFont("Consolas", 14))
        self.output_preview.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        R.addWidget(self.output_preview)

        self.example_group = QGroupBox()
        sl2 = QVBoxLayout(self.example_group)

        self.sample_scroll = QScrollArea()
        self.sample_scroll.setWidgetResizable(True)
        self.sample_scroll.setFixedHeight(210)
        self.sample_scroll.setFrameShape(QFrame.NoFrame)

        self.sample_content = QWidget()
        v = QVBoxLayout(self.sample_content)
        v.setSpacing(2)

        self.sample_label = QLabel()
        self.sample_label.setWordWrap(True)
        self.sample_label.setStyleSheet(
            f"color:{COLORS['text_secondary']};background:transparent;"
            f"font-size:11px;padding:4px;"
        )
        self.sample_label.setTextInteractionFlags(
            Qt.TextSelectableByMouse
        )

        v.addWidget(self.sample_label)
        self.sample_scroll.setWidget(self.sample_content)
        sl2.addWidget(self.sample_scroll)
        R.addWidget(self.example_group)

        bot = QHBoxLayout()
        bot.addStretch()

        self.signature = FooterSignature()
        bot.addWidget(self.signature)
        R.addLayout(bot)

    def populate_style_combo(self, cat):
        if not hasattr(self, 'style_combo'):
            return

        self.style_combo.blockSignals(True)
        self.style_combo.clear()
        self.style_combo.addItems(get_style_names_for_category(cat))
        self.style_combo.blockSignals(False)

    def on_category_changed(self):
        self.populate_style_combo(self.category_combo.currentText())
        self.update_style_preview()
        self.generate_text()

    def on_style_changed(self):
        self.update_style_preview()
        self.generate_text()

    def update_style_preview(self):
        if not hasattr(self, 'style_combo'):
            return

        name = self.style_combo.currentText()
        if not name:
            self.style_preview_label.setText("")
            return

        try:
            styled = stylize_text("Hello World", name)
        except Exception:
            styled = "Hello World"

        if len(styled) > 200:
            styled = styled[:200] + "..."

        self.style_preview_label.setText(f"> {styled}")

    def update_examples(self):
        word = self.text_input.text().strip() or "Hello"
        if len(word) > 12:
            word = word[:12]

        names = get_style_names_for_category(
            self.category_combo.currentText()
        )[:20]

        lines = []
        for name in names:
            try:
                styled = stylize_text(word, name)
                if len(styled) > 100:
                    styled = styled[:100] + "…"
                lines.append(f"  {name}:  {styled}")
            except Exception:
                lines.append(f"  {name}:  {word}")

        self.sample_label.setText("\n".join(lines))

    def retranslate_ui(self):
        self.input_group.setTitle(self.trx("text_input"))
        self.text_input.setPlaceholderText(
            self.trx("type_text_here")
        )

        self.style_group.setTitle(self.trx("text_style"))
        self.category_label.setText(self.trx("style_category"))
        self.style_preset_label.setText(self.trx("style_preset"))
        self.uppercase_check.setText(self.trx("force_uppercase"))
        self.spaced_check.setText(
            self.trx("add_space_between_letters")
        )

        self.actions_group.setTitle(self.trx("actions"))
        self.copy_btn.setText(self.trx("copy_text"))
        self.save_btn.setText(self.trx("save_txt"))

        self.title.setText(self.trx("styled_text_preview"))
        self.preview_info.setText(self.trx("ready"))
        self.example_group.setTitle(self.trx("example"))

        self.signature.set_language_code(self.lang)
        self.signature.retranslate_ui()

        self.update_style_preview()
        self.generate_text()

    def generate_text(self):
        if not hasattr(self, 'style_combo'):
            return

        text = self.text_input.text()
        name = self.style_combo.currentText()

        if not name:
            self.output_preview.setPlainText(
                self.trx("your_styled_text_here")
            )
            return

        if self.uppercase_check.isChecked():
            text = text.upper()

        result = stylize_text(text, name)

        if (
            self.spaced_check.isChecked()
            and name not in FRAME_STYLES
            and '\n' not in result
        ):
            result = " ".join(list(result))

        self.current_output = result
        self.output_preview.setPlainText(
            result if result else self.trx("your_styled_text_here")
        )
        self.preview_info.setText(f"{self.trx('style')}: {name}")
        self.update_examples()

    def copy_text(self):
        if not self.current_output:
            return

        QApplication.clipboard().setText(self.current_output)
        show_themed_message(
            self,
            self.trx("copied"),
            self.trx("styled_text_copied")
        )

    def save_text(self):
        if not self.current_output:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            self.trx("save_styled_text"),
            "styled_text.txt",
            "Text Files (*.txt)"
        )
        if not file_path:
            return

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.current_output)

            show_themed_message(
                self,
                self.trx("saved"),
                self.trx("styled_saved")
            )
        except Exception as e:
            show_themed_message(
                self,
                self.trx("error"),
                str(e),
                QMessageBox.Critical
            )


class MainWindow(QMainWindow, TranslatorMixin):
    def __init__(self):
        super().__init__()
        self.set_language_code("tr")
        self.setWindowTitle(f"{BRAND_NAME} ASCII Studio")
        self.setGeometry(100, 80, 1240, 800)
        self.setMinimumSize(1000, 700)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.init_ui()
        self.apply_styles()
        self.set_dark_palette()

        self.image_ascii_page.language_combo.currentTextChanged.connect(
            self.on_language_changed
        )

        self.retranslate_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        ml = QVBoxLayout(self.central_widget)
        ml.setContentsMargins(0, 0, 0, 0)
        ml.setSpacing(0)

        self.title_bar = CustomTitleBar(self)
        ml.addWidget(self.title_bar)

        self.content_widget = QWidget()
        self.content_widget.setObjectName("contentWidget")

        cl = QVBoxLayout(self.content_widget)
        cl.setContentsMargins(10, 10, 10, 10)

        self.tabs = QTabWidget()
        self.tabs.setObjectName("mainTabs")

        self.image_ascii_page = ImageAsciiPage()
        self.stylized_text_page = StylizedTextPage()

        self.tabs.addTab(self.image_ascii_page, "")
        self.tabs.addTab(self.stylized_text_page, "")

        cl.addWidget(self.tabs)
        ml.addWidget(self.content_widget)

    def on_language_changed(self, name):
        code = LANGUAGES.get(name)
        if code:
            self.set_language_everywhere(code)

    def set_language_everywhere(self, code):
        self.lang = code

        self.title_bar.set_language_code(code)
        self.title_bar.retranslate_ui()

        self.image_ascii_page.set_language_code(code)
        self.image_ascii_page.retranslate_ui()

        self.stylized_text_page.set_language_code(code)
        self.stylized_text_page.retranslate_ui()

        selected_name = next(
            (name for name, language_code in LANGUAGES.items()
             if language_code == code),
            "Türkçe"
        )

        if (
            self.image_ascii_page.language_combo.currentText()
            != selected_name
        ):
            self.image_ascii_page.language_combo.blockSignals(True)
            self.image_ascii_page.language_combo.setCurrentText(
                selected_name
            )
            self.image_ascii_page.language_combo.blockSignals(False)

        self.retranslate_ui()

    def retranslate_ui(self):
        self.setWindowTitle(
            f"{BRAND_NAME} {self.trx('app_title')}"
        )
        self.tabs.setTabText(0, self.trx("tab_image_ascii"))
        self.tabs.setTabText(1, self.trx("tab_stylized_text"))

    def apply_styles(self):
        self.setStyleSheet(
            f"QMainWindow {{ background: transparent; color: {COLORS['text']}; font-family: 'Segoe UI'; font-size: 9pt; }}"
            f"#contentWidget {{ background-color: {COLORS['background']}; border-bottom-left-radius: 12px; border-bottom-right-radius: 12px; }}"
            f"#leftPanel, #rightPanel, #leftContent {{ background-color: {COLORS['panel']}; border-radius: 10px; }}"
            f"QScrollArea, #controlScroll {{ background-color: {COLORS['panel']}; border: none; }}"
            f"QScrollArea > QWidget > QWidget {{ background-color: {COLORS['panel']}; }}"
            f"QTabWidget::pane {{ border: 1px solid {COLORS['border']}; background: {COLORS['background']}; border-radius: 10px; top: -1px; }}"
            f"QTabBar::tab {{ background: {COLORS['dark']}; color: {COLORS['text_secondary']}; border: 1px solid {COLORS['border']}; padding: 12px 24px; margin-right: 6px; border-top-left-radius: 8px; border-top-right-radius: 8px; font-weight: 600; font-size: 9pt; min-width: 130px; }}"
            f"QTabBar::tab:selected {{ background: {COLORS['panel']}; color: {COLORS['primary']}; border-bottom: 1px solid {COLORS['panel']}; }}"
            f"QTabBar::tab:hover {{ background: {COLORS['panel']}; color: {COLORS['primary_light']}; }}"
            f"QSplitter::handle {{ background-color: {COLORS['border']}; margin: 4px 0; border-radius: 3px; }}"
            f"QSplitter::handle:hover {{ background-color: {COLORS['primary_dark']}; }}"
            f"QGroupBox {{ border: 1px solid {COLORS['border']}; border-radius: 10px; margin-top: 12px; padding-top: 14px; font-weight: 700; font-size: 9pt; background-color: {COLORS['dark']}; color: {COLORS['text']}; }}"
            f"QGroupBox::title {{ subcontrol-origin: margin; left: 10px; padding: 0 8px; color: {COLORS['primary']}; background-color: {COLORS['dark']}; }}"
            f"QLabel {{ color: {COLORS['text']}; background: transparent; }}"
            f"#previewLabel {{ border: 2px dashed {COLORS['border']}; border-radius: 10px; background-color: {COLORS['darker']}; color: {COLORS['text_secondary']}; font-size: 11px; padding: 8px; }}"
            f"#asciiPreview {{ background-color: {COLORS['darker']}; color: {COLORS['text']}; border: 1px solid {COLORS['border']}; border-radius: 10px; font-family: 'Consolas', 'Courier New', monospace; padding: 8px; line-height: 1.0; }}"
            f"QTextEdit, QComboBox, QLineEdit {{ background-color: {COLORS['darker']}; color: {COLORS['text']}; border: 1px solid {COLORS['border']}; border-radius: 7px; padding: 7px; selection-background-color: {COLORS['primary']}; }}"
            f"QTextEdit:focus, QComboBox:focus, QLineEdit:focus {{ border: 1px solid {COLORS['primary']}; }}"
            f"QComboBox QAbstractItemView {{ background-color: {COLORS['darker']}; color: {COLORS['text']}; border: 1px solid {COLORS['border']}; selection-background-color: {COLORS['primary']}; selection-color: black; }}"
            f"QCheckBox {{ color: {COLORS['text']}; spacing: 8px; background: transparent; }}"
            f"QCheckBox::indicator {{ width: 16px; height: 16px; border: 1px solid {COLORS['border']}; border-radius: 4px; background: {COLORS['darker']}; }}"
            f"QCheckBox::indicator:checked {{ background-color: {COLORS['primary']}; border: 1px solid {COLORS['primary']}; }}"
            f"QSlider::groove:horizontal {{ border: none; height: 5px; background: {COLORS['border']}; border-radius: 2px; }}"
            f"QSlider::handle:horizontal {{ background: {COLORS['primary']}; width: 15px; height: 15px; margin: -5px 0; border-radius: 7px; border: none; }}"
            f"QSlider::handle:horizontal:hover {{ background: {COLORS['primary_light']}; }}"
            f"QSlider::sub-page:horizontal {{ background: {COLORS['primary']}; border-radius: 2px; }}"
            f"QPushButton {{ border-radius: 8px; padding: 9px 12px; font-weight: 700; border: 1px solid {COLORS['border']}; }}"
            f"QPushButton#primaryButton {{ background-color: {COLORS['button_bg']}; color: white; border: none; }}"
            f"QPushButton#primaryButton:hover {{ background-color: {COLORS['button_hover']}; }}"
            f"QPushButton#primaryButton:pressed {{ background-color: {COLORS['button_pressed']}; }}"
            f"QPushButton#autoButton {{ background-color: #0E3A5D; color: {COLORS['primary_light']}; border: 1px solid {COLORS['primary_dark']}; }}"
            f"QPushButton#autoButton:hover {{ background-color: #134A75; border-color: {COLORS['primary']}; color: white; }}"
            f"QPushButton#secondaryButton {{ background-color: {COLORS['dark']}; color: {COLORS['text']}; border: 1px solid {COLORS['border']}; }}"
            f"QPushButton#secondaryButton:hover {{ background-color: {COLORS['panel']}; border-color: {COLORS['primary']}; color: {COLORS['primary_light']}; }}"
            f"QPushButton#secondaryButton:pressed {{ background-color: {COLORS['primary_dark']}; color: white; }}"
            f"QPushButton:disabled {{ background-color: {COLORS['darker']}; color: {COLORS['text_secondary']}; border-color: {COLORS['border']}; }}"
            f"QProgressBar {{ background: {COLORS['darker']}; border: none; border-radius: 2px; }}"
            f"QProgressBar::chunk {{ background: {COLORS['primary']}; border-radius: 2px; }}"
            f"QScrollBar:vertical {{ background: {COLORS['darker']}; width: 10px; border-radius: 5px; margin: 2px; }}"
            f"QScrollBar::handle:vertical {{ background: {COLORS['border']}; border-radius: 5px; min-height: 24px; }}"
            f"QScrollBar::handle:vertical:hover {{ background: {COLORS['primary_dark']}; }}"
            f"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0px; }}"
            f"QScrollBar:horizontal {{ background: {COLORS['darker']}; height: 10px; border-radius: 5px; margin: 2px; }}"
            f"QScrollBar::handle:horizontal {{ background: {COLORS['border']}; border-radius: 5px; min-width: 24px; }}"
            f"QScrollBar::handle:horizontal:hover {{ background: {COLORS['primary_dark']}; }}"
            f"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0px; }}"
        )

    def set_dark_palette(self):
        pal = self.palette()
        pal.setColor(QPalette.Window, QColor(COLORS['background']))
        pal.setColor(QPalette.WindowText, QColor(COLORS['text']))
        pal.setColor(QPalette.Base, QColor(COLORS['dark']))
        pal.setColor(QPalette.AlternateBase, QColor(COLORS['darker']))
        pal.setColor(QPalette.Text, QColor(COLORS['text']))
        pal.setColor(QPalette.Button, QColor(COLORS['dark']))
        pal.setColor(QPalette.ButtonText, QColor(COLORS['text']))
        pal.setColor(QPalette.Highlight, QColor(COLORS['primary']))
        pal.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(pal)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(COLORS['background']))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 12, 12)


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setFont(QFont("Segoe UI", 9))

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
