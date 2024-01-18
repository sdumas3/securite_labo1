from flask import Flask, render_template, url_for, request  # importation des librairies

app = Flask(__name__, template_folder='templates', static_folder='static')  # définition variable app


# J'ai mis mes .html en deux fichiers pour le get et le post puisque rien n'était spécifié pour cela
@app.route("/", methods=["GET", "POST"])  # route de la commande get et post
def accueil():
    if request.method == "POST":  # définition de la condition if si c'est un post
        name = request.form.get("name")  # on va chercher le nom inscrit dans le formulaire
        city = request.form.get("city")  # on va chercher la ville dans incrite le formulaire
        return render_template('infos.html', name=name, city=city)  # on load la page infos.html qui comprend les infos entrées dans le formulaire
    else:  # définition de la condition si ce n'est pas un post
        return render_template('accueil.html', var='Laboratoire 1')  # on load la page accueil.html qui consiste en la page d'accueil


@app.errorhandler(404)  # route si un erreur 404 est soulevée
def error_page(error):
    return render_template('error404.html', error='Erreur 404, Page Non-Trouvée'), 404  # on load la page error.html qui est la page d'erreur


if __name__ == "__main__":
    app.run(debug=True)
