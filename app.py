import os
import uuid
from flask import Flask, request, send_file, render_template_string
from process import convert_to_gray

app = Flask(__name__)

UPLOAD_DIR = "/tmp/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

PAGE_HTML = """
<!doctype html>
<title>Image Processor Demo</title>
<h1>이미지 업로드해서 흑백으로 변환</h1>
<form method="post" enctype="multipart/form-data">
  <input type="file" name="image" accept="image/*">
  <input type="submit" value="업로드 & 변환">
</form>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image")
        if not file:
            return "이미지 파일이 필요합니다.", 400

        # 입력 이미지 저장
        input_filename = f"{uuid.uuid4()}_{file.filename}"
        input_path = os.path.join(UPLOAD_DIR, input_filename)
        file.save(input_path)

        # 출력 이미지 경로
        output_filename = f"{uuid.uuid4()}_gray.png"
        output_path = os.path.join(UPLOAD_DIR, output_filename)

        # 변환
        convert_to_gray(input_path, output_path)

        return send_file(output_path, mimetype="image/png")

    return render_template_string(PAGE_HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
