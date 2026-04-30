from flask import Flask, send_from_directory, abort, redirect
from werkzeug.middleware.proxy_fix import ProxyFix
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

PORT = int(os.environ.get("PORT", 6002))


@app.route("/")
def serve_root():
    index_path = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(index_path):
        return send_from_directory(BASE_DIR, "index.html")
    abort(404)


@app.route("/<path:path>")
def serve_file_or_page(path):
    # Nếu người dùng truy cập .html thì chuyển về URL gọn
    # Ví dụ /lumohub.html -> /lumohub
    if path.endswith(".html"):
        clean_path = path[:-5]
        if clean_path == "index":
            return redirect("/", code=301)
        return redirect(f"/{clean_path}", code=301)

    # 1. Ưu tiên trả file thật trước: css, js, ảnh, txt...
    real_file = os.path.join(BASE_DIR, path)
    if os.path.isfile(real_file):
        return send_from_directory(BASE_DIR, path)

    # 2. Nếu không phải file thật thì xem như page không có .html
    # Ví dụ /lumohub -> lumohub.html
    html_file = f"{path}.html"
    html_path = os.path.join(BASE_DIR, html_file)

    if os.path.isfile(html_path):
        return send_from_directory(BASE_DIR, html_file)

    abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)