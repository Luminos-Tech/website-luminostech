from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)
PORT = 6002

@app.route('/<path:page>')
def serve_page(page):
    # Remove .html if present and redirect
    if page.endswith('.html'):
        return '', 301

    # Try to serve .html file
    html_file = f'{page}.html'
    if os.path.exists(html_file):
        return send_from_directory('.', html_file)
    
    # Try index.html for root paths
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
