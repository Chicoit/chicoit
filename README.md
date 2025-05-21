# Chatbot FLE Marketing

Un chatbot simple pour la formation FLE (Français Langue Étrangère) spécialisé dans le domaine du marketing et du e-commerce.

## Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers

2. Créez un environnement virtuel (recommandé) :
```bash
python -m venv venv
```

3. Activez l'environnement virtuel :
- Windows :
```bash
venv\Scripts\activate
```
- Linux/Mac :
```bash
source venv/bin/activate
```

4. Installez les dépendances :
```bash
pip install -r requirements.txt
```

5. Téléchargez le modèle de langue français pour spaCy :
```bash
python -m spacy download fr_core_news_sm
```

## Utilisation

1. Lancez le chatbot :
```bash
python chatbot_fle.py
```

2. Interagissez avec le chatbot en tapant vos questions ou réponses
3. Tapez 'quit' pour quitter

## Fonctionnalités

- Réponses aux questions sur le marketing digital
- Informations sur le e-commerce
- Gestion des conflits clients
- Vocabulaire professionnel du marketing
- Support en français

## Personnalisation

Vous pouvez personnaliser les réponses du chatbot en modifiant la liste `marketing_data` dans le fichier `chatbot_fle.py`. 