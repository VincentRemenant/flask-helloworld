from flask import Flask
import os

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

# Route de santé pour Railway
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'message': 'Server is running'}, 200

# Point d'entrée principal pour le développement local
if __name__ == '__main__':
    # Utiliser les variables d'environnement pour Railway
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    print(f"🚀 Démarrage du serveur sur {host}:{port}")
    print(f"🐛 Mode debug: {debug}")
    
    # Lancer le serveur
    app.run(debug=debug, host=host, port=port)