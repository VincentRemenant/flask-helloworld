from flask import Flask

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir la route pour la page d'accueil
@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><p>Bienvenue dans votre première application Flask!</p>'

# Route supplémentaire avec un paramètre
@app.route('/hello/<name>')
def hello_name(name):
    return f'<h1>Hello, {name}!</h1><p>Ravi de vous rencontrer!</p>'

# Point d'entrée principal
if __name__ == '__main__':
    # Lancer le serveur de développement
    app.run(debug=True, host='127.0.0.1', port=5000)