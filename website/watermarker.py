from PIL import Image

def watermark_image(input_image_path, output_image_path, watermark_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    width, height = base_image.size
    watermark = watermark.resize((width, height))
    watermark.putalpha(128)

    watermarked_image = Image.new('RGBA', base_image.size)
    watermarked_image.paste(base_image, (0, 0))
    watermarked_image.paste(watermark, (0, 0), watermark)

    watermarked_image = watermarked_image.convert('RGB')

    watermarked_image.save(output_image_path)

