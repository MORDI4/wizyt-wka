from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template("index.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        message = request.form.get('message')
        print(message)
        return render_template("contact.html")
    