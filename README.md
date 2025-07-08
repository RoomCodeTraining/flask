# Flask Hello World

Un projet Flask simple qui affiche "Hello World".

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
```

2. Activer l'environnement virtuel :
```bash
# Sur macOS/Linux :
source venv/bin/activate

# Sur Windows :
venv\Scripts\activate
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Exécution

Lancer l'application :
```bash
python app.py
```

L'application sera accessible à l'adresse : http://localhost:8080

## Routes disponibles

- `/` - Affiche "Hello, World!"
- `/hello/<name>` - Affiche "Hello, <name>!" (ex: http://localhost:8080/hello/Alice)

## Arrêt

Pour arrêter l'application, appuyez sur `Ctrl+C` dans le terminal.
