# Application Flask - Hello World

Une application Flask très simple qui affiche "Hello World".

## Installation

1. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Lancez l'application :
```bash
python app.py
```

2. Ouvrez votre navigateur et allez à :
   - `http://127.0.0.1:5000/` pour voir le message "Hello World"
   - `http://127.0.0.1:5000/hello/votrenom` pour un message personnalisé

## Déploiement sur Railway

### ⚠️ Corrections pour l'erreur 502 Bad Gateway

Si vous obtenez une erreur 502, c'est généralement dû à :
1. **Mauvaise configuration du port** : Railway injecte une variable `PORT`
2. **Serveur qui n'écoute pas sur `0.0.0.0`** : Doit écouter sur toutes les interfaces
3. **Gunicorn mal configuré** : Le Procfile doit être correct

### ✅ Configuration corrigée

- **app.py** : Utilise `0.0.0.0` et la variable `PORT` de Railway
- **Procfile** : `web: gunicorn --bind 0.0.0.0:$PORT app:app`
- **Route /health** : Pour vérifier que l'app répond
- **runtime.txt** : Force Python 3.11 compatible

### Méthode 1 : Depuis GitHub (Recommandée)

1. **Poussez votre code sur GitHub** :
```bash
git add .
git commit -m "Corriger configuration pour Railway - Fix 502 error"
git push origin main
```

2. **Connectez-vous à Railway** :
   - Allez sur [railway.app](https://railway.app)
   - Connectez-vous avec votre compte GitHub
   - Cliquez sur "New Project"
   - Sélectionnez "Deploy from GitHub repo"
   - Choisissez votre repository `flask-helloworld`

3. **Railway se chargera automatiquement** :
   - De détecter qu'il s'agit d'une app Python
   - D'installer les dépendances depuis `requirements.txt`
   - De lancer l'app avec le `Procfile`
   - De vous donner une URL publique

### Méthode 2 : Depuis Railway CLI

1. **Installez Railway CLI** :
```bash
npm install -g @railway/cli
```

2. **Connectez-vous et déployez** :
```bash
railway login
railway init
railway up
```

### Variables d'environnement (optionnelles)

Sur Railway, vous pouvez définir :
- `FLASK_DEBUG=false` (pour la production)
- `PORT` (géré automatiquement par Railway)
- `HOST` (géré automatiquement par Railway)

## Structure

- `app.py` : Application Flask principale
- `requirements.txt` : Dépendances Python (Flask + Gunicorn)
- `Procfile` : Instructions de démarrage pour Railway
- `railway.json` : Configuration Railway (optionnel)
- `README.md` : Ce fichier

### Développement local
L'application fonctionne en mode debug sur le port 5000.

### Production (Railway)
L'application utilise Gunicorn comme serveur WSGI et s'adapte automatiquement au port fourni par Railway.