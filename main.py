from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
def accueil():
    return render_template('accueil.html', var='Laboratoire 1')


@app.errorhandler(404)
def error_page(error):
    return render_template('error404.html', error='Erreur 404, Page Non-Trouvée', img_error=url_for('static', filename='error.png')), 404


if __name__ == "__main__":
    app.run(debug=True)