#from fileinput import filename
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
from URL_to_QR import generate_QR
 
app = Flask(__name__)
     
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['post'])    
def my_form_post():
    url = request.form["message"]
    QR = generate_QR(url)
    QR.save('static/uploads/output.png')
    return redirect(url_for("static",filename = 'uploads/output.png'),code= 301)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True)

