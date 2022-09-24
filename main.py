from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    responce = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    responce.raise_for_status()
    blog_data = responce.json()
    return render_template("index.html", data=blog_data)

@app.route('/post/<blog_id>')
def blog(blog_id):
    responce = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    responce.raise_for_status()
    blog_data = responce.json()
    return render_template("post.html", data=blog_data, blog_id=int(blog_id))

if __name__ == "__main__":
    app.run(debug=True)
