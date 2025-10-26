#!/usr/bin/env python3
"""
Script de test pour vérifier que l'application Flask fonctionne correctement
avant le déploiement sur Railway.
"""

import os
import sys
import time
import requests
from threading import Thread

# Ajouter le répertoire courant au path pour importer app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_app():
    """Test l'application Flask"""
    print("🧪 Test de l'application Flask...")
    
    # Import de l'app
    try:
        from app import app
        print("✅ Import de l'app réussi")
    except Exception as e:
        print(f"❌ Erreur d'import: {e}")
        return False
    
    # Test des routes
    with app.test_client() as client:
        print("🔍 Test des routes...")
        
        # Test route principale
        response = client.get('/')
        if response.status_code == 200:
            print("✅ Route '/' fonctionne")
        else:
            print(f"❌ Route '/' échoue: {response.status_code}")
            return False
        
        # Test route avec paramètre
        response = client.get('/hello/Railway')
        if response.status_code == 200:
            print("✅ Route '/hello/<name>' fonctionne")
        else:
            print(f"❌ Route '/hello/<name>' échoue: {response.status_code}")
            return False
        
        # Test route health
        response = client.get('/health')
        if response.status_code == 200:
            print("✅ Route '/health' fonctionne")
        else:
            print(f"❌ Route '/health' échoue: {response.status_code}")
            return False
    
    print("🎉 Tous les tests passent ! L'application est prête pour Railway.")
    return True

if __name__ == "__main__":
    success = test_app()
    sys.exit(0 if success else 1)