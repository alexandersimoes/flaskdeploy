import os
from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('home.html')
 
app.wsgi_app = ProxyFix(app.wsgi_app)
app.debug = bool(os.environ.get('PRODUCTION'))
 
if __name__ == '__main__':
    app.run()
    # EHRGh7dpz9gb