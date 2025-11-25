from PIL import Image
import sys

def convert_to_gray(input_file, output_file):
    img = Image.open(input_file).convert("L")
    img.save(output_file)
    print("이미지 변환 완료:", output_file)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_to_gray(input_file, output_file)
