# Hello


flask_first.py
```
from flask import Flask
from utils import farm

app = Flask(__name__)


@app.route('/')
def index():
    return f'<h1>{farm}</h1>'


app.run(debug=True, port=5003)
```

utils.py
```
def farm():
    wr = open("requirements.txt")
    file = [i for i in wr]
    st = '<br>'.join(file)
    return st
```
