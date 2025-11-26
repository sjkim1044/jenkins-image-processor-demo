from PIL import Image

def convert_to_gray(input_path: str, output_path: str) -> str:
    img = Image.open(input_path).convert("L")
    img.save(output_path)
    return output_path
