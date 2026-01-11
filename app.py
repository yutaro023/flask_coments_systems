import flask
from db import db

app = flask.Flask(__name__)

app.secret_key = "Chave_super_secreta"

@app.route('/index.html')
def index_redirect():
    return flask.redirect(flask.url_for('home'))

@app.route("/", methods=["GET", "POST"])
def home():
    name = flask.request.form.get("name_user")
    e_mail = flask.request.form.get("e_mail")
    password = flask.request.form.get("key_word")
    date = flask.request.form.get("birth_date")
    if(name and e_mail and password and date):
        result = db.sign_up(name, e_mail, password, date)
        if(result == 'email_existe'):
            return flask.render_template("index.html", error=result)
        return flask.redirect(flask.url_for("menssages"))
    return flask.render_template("index.html")

@app.route("/menssages", methods=["GET", "POST"])
def menssages(): 
    if flask.request.method == "POST":
        comentario = flask.request.form.get("comentario")
        if comentario:
            db.insert_coment(comentario)
        return flask.redirect(flask.url_for("menssages"))
    comentarios = db.get_comment()
    return flask.render_template("menssages.html", comentarios=comentarios)

@app.route("/login", methods=["GET", "POST"])
def login():
    value = False
    if(flask.request.method == "POST"):
        e_mail = flask.request.form.get("e_mail")
        password = flask.request.form.get("key_word")
        isExistCredentials = db.credentials_is_existy(e_mail, password)
        if(isExistCredentials == True):
            return flask.redirect(flask.url_for("menssages"))
        else:
            value = True
    return flask.render_template("login.html", error=value)
if __name__ == "__main__":
    app.run(debug=True, port=5000)