from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')  #@app.route() ile sayfamızı oluşturduk.
def Index():
    return render_template("index.html", email="")

@app.route('/about')
def About():
    return render_template("about.html")

@app.route('/accessories')
def Accessories():
    return render_template("accessories.html")

@app.route('/apparel')
def Apparel():
    return render_template("apparel.html")

@app.route('/beauty_care')
def BeautyCare():
    return render_template("beauty_care.html")

@app.route('/blog')
def Blog():
    return render_template("blog.html")

@app.route('/jewelry')
def Jewelry():
    return render_template("jewelry.html")

@app.route('/new_arrival')
def NewArrival():
    return render_template("new_arrival.html")

@app.route('/news')
def News():
    return render_template("news.html")

@app.route('/shoes')
def Shoes():
    return render_template("shoes.html")

@app.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':     # Sunucuya kullanıcının verilerini göndermek için 'POST' istek yöntemini kullandık.
        if request.form:

            email = request.form['email']
            password = request.form['password']
            if email == 'nidademir13042015@gmail.com' and password == 'admin':
                return render_template("index.html", email="Nida")
            else:
                return render_template("login.html", message="Email yada parola yanlış")
    else:
        return render_template("login.html")

@app.route('/signup')
def Signup():
    return render_template("login.html")



