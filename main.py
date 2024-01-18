from flask import Flask, render_template, url_for, request

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/", methods=["GET", "POST"])
def accueil():
    if request.method == "POST":
        name = request.form.get("name")
        city = request.form.get("city")
        return render_template('infos.html', name = name, city = city)
    else :
        return render_template('accueil.html', var='Laboratoire 1')


@app.errorhandler(404)
def error_page(error):
    return render_template('error404.html', error='Erreur 404, Page Non-Trouvée', img_error=url_for('static', filename='error.png')), 404


if __name__ == "__main__":
    app.run(debug=True)