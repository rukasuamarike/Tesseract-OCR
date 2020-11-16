import sys

try:
    from PIL import Image, ImageDraw
except ImportError:
    import Image, ImageDraw, ImageShow
    from PIL.Image.ImageShow import show, MacViewer
import pytesseract
from pytesseract import Output


def ocr_core(filename, lang=None):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename), lang=lang)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

def ocr_box(filename,lang=None):
    print(ocr_core(filename))
    boxes = pytesseract.image_to_boxes(Image.open(filename), lang=lang)
    with Image.open(filename) as img:
        draw = ImageDraw.Draw(img)
        for b in boxes.splitlines():
            b = b.split(' ')
            draw.rectangle([int(b[1]), int(b[2]), int(b[3]), int(b[4])], outline=(255, 0, 0))

        img.show()
    return img

def ocr_box2(filename,lang=None):
    print(ocr_core(filename))
    img = Image.open(filename)
    d = pytesseract.image_to_data(img, output_type=Output.DICT, lang=lang)

    with Image.open(filename) as img:
        draw = ImageDraw.Draw(img)
        n_boxes = len(d['text'])
        for i in range(n_boxes):
            if int(d['conf'][i]) > 60:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                draw.rectangle([x, y, x + w, y + h], outline=(255,0,0))
        img.show()

    return img

