from flask import Flask, send_from_directory, abort
from werkzeug.middleware.proxy_fix import ProxyFix
import os

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
PORT = int(os.environ.get('PORT', 6002))

@app.route('/<path:page>')
def serve_page(page):
    if page.endswith('.html'):
        return '', 301

    html_file = f'{page}.html'
    if os.path.exists(html_file):
        return send_from_directory('.', html_file)
    
    if page == '' or page == '/':
        if os.path.exists('index.html'):
            return send_from_directory('.', 'index.html')
    
    abort(404)

@app.route('/')
def serve_root():
    if os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
