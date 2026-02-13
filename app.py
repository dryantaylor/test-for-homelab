from flask import Flask, render_template_string

app = Flask(__name__)

INDEX_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Index</title>
</head>
<body>
  <h1>Hello World</h1>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(INDEX_HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
