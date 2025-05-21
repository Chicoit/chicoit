import random
from flask import Flask, render_template, request, jsonify
import os


class MarketingChatBot:
    def __init__(self):
        # Mots-clés marketing principaux
        self.marketing_keywords = {
            "seo": [
                "Le SEO est crucial pour votre visibilité en ligne. Nous proposons des stratégies d'optimisation adaptées à votre secteur.",
                "Notre approche SEO combine recherche de mots-clés, optimisation technique et création de contenu de qualité."
            ],
            "social_media": [
                "La gestion de vos réseaux sociaux est essentielle. Nous créons une stratégie adaptée à votre audience.",
                "Nous optimisons votre présence sur les réseaux sociaux pour maximiser votre engagement."
            ],
            "content": [
                "Le content marketing est la clé pour établir votre autorité. Nous créons du contenu pertinent et engageant.",
                "Notre stratégie de contenu vise à informer, éduquer et convertir votre audience."
            ],
            "email": [
                "L'email marketing reste un canal efficace. Nous concevons des campagnes personnalisées.",
                "Nos stratégies d'email marketing visent à maintenir l'engagement de vos clients."
            ],
            "analytics": [
                "L'analyse de données est cruciale. Nous vous aidons à comprendre vos performances.",
                "Nos rapports d'analyse vous donnent des insights actionnables."
            ]
        }

        # Scénarios de conflits
        self.conflict_scenarios = {
            "client_insatisfait": [
                "Je comprends votre frustration. Voici notre procédure : 1) Analyse de la situation 2) Solution immédiate 3) Suivi personnalisé",
                "Nous prenons votre feedback très au sérieux. Notre équipe va examiner votre cas en priorité."
            ],
            "retard_livraison": [
                "Nous nous excusons pour ce délai. Nous mettons tout en œuvre pour accélérer le processus.",
                "Votre satisfaction est notre priorité. Nous vous tiendrons informé de l'avancement."
            ],
            "probleme_technique": [
                "Notre équipe technique est mobilisée pour résoudre ce problème rapidement.",
                "Nous avons identifié la source du problème et travaillons sur une solution."
            ],
            "erreur_facturation": [
                "Nous allons corriger cette erreur de facturation immédiatement.",
                "Votre remboursement sera effectué dans les plus brefs délais."
            ],
            "communication": [
                "Nous améliorons nos canaux de communication pour être plus réactifs.",
                "Nous mettons en place un système de suivi plus efficace."
            ]
        }

        # Réponses typiques
        self.default_responses = [
            "Je peux vous aider avec le SEO, les réseaux sociaux, le content marketing, l'email marketing ou l'analyse de données. Que souhaitez-vous savoir?",
            "Pour mieux vous aider, pourriez-vous préciser votre besoin?",
            "Je suis spécialisé en marketing digital. Sur quel aspect souhaitez-vous des informations?"
        ]

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Vérifier les mots-clés marketing
        for key in self.marketing_keywords:
            if key in user_input:
                return random.choice(self.marketing_keywords[key])

        # Vérifier les scénarios de conflits
        for key in self.conflict_scenarios:
            if key in user_input:
                return random.choice(self.conflict_scenarios[key])

        return random.choice(self.default_responses)


# Configuration Flask
app = Flask(__name__)
chatbot = MarketingChatBot()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = chatbot.get_response(user_message)
    return jsonify({'response': response})


if __name__ == "__main__":
    # Créer le dossier templates s'il n'existe pas
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # Créer le fichier index.html
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write('''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assistant Marketing FLE</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .chat-container {
            max-width: 800px;
            margin: 2rem auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            padding: 2rem;
        }
        .chat-header {
            text-align: center;
            margin-bottom: 2rem;
            color: #2c3e50;
        }
        .chat-messages {
            height: 400px;
            overflow-y: auto;
            padding: 1rem;
            border: 1px solid #dee2e6;
            border-radius: 10px;
            margin-bottom: 1rem;
        }
        .message {
            margin-bottom: 1rem;
            padding: 0.8rem;
            border-radius: 10px;
            max-width: 80%;
        }
        .user-message {
            background-color: #007bff;
            color: white;
            margin-left: auto;
        }
        .bot-message {
            background-color: #e9ecef;
            color: #2c3e50;
        }
        .input-group {
            margin-top: 1rem;
        }
        .btn-send {
            background-color: #007bff;
            color: white;
            border: none;
        }
        .btn-send:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="chat-container">
            <div class="chat-header">
                <h1>Assistant Marketing FLE</h1>
                <p class="text-muted">Votre expert en marketing digital</p>
            </div>
            <div class="chat-messages" id="chat-messages">
                <div class="message bot-message">
                    Bonjour! Je suis votre assistant marketing. Comment puis-je vous aider aujourd'hui?
                </div>
            </div>
            <div class="input-group">
                <input type="text" id="user-input" class="form-control" placeholder="Tapez votre message...">
                <button class="btn btn-send" onclick="sendMessage()">Envoyer</button>
            </div>
        </div>
    </div>

    <script>
        function addMessage(message, isUser) {
            const chatMessages = document.getElementById('chat-messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
            messageDiv.textContent = message;
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        function sendMessage() {
            const input = document.getElementById('user-input');
            const message = input.value.trim();

            if (message) {
                addMessage(message, true);
                input.value = '';

                fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({message: message})
                })
                .then(response => response.json())
                .then(data => {
                    addMessage(data.response, false);
                });
            }
        }

        // Permettre l'envoi avec la touche Entrée
        document.getElementById('user-input').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    </script>
</body>
</html>
        ''')

    # Lancer l'application Flask
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 