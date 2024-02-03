import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Configurer les paires de questions et réponses pour l'IA
pairs = [
    ["Bonjour", ["Bonjour! Je suis Alice, votre assistante. Comment puis-je vous aider aujourd'hui?"]],
    ["Comment ça va?", ["Je suis une IA, donc je n'ai pas d'émotions, mais merci de demander! Comment puis-je vous assister?"]],
    ["Quel est ton nom?", ["Je m'appelle Alice, votre assistante virtuelle."]],
    ["Que peux-tu faire?", ["Je suis ici pour engager une conversation avec vous. Posez-moi des questions ou partagez simplement vos pensées!"]],
    ["Peux-tu me donner des informations sur Python?", ["Bien sûr! Python est un langage de programmation interprété, polyvalent et convivial. Comment puis-je vous aider davantage?"]],
    ["Au revoir", ["Au revoir! N'hésitez pas à revenir si vous avez d'autres questions."]],
    ["(.*)", ["Je suis désolée, je ne suis qu'une simple assistante de conversation et je ne peux pas effectuer d'actions spécifiques. Comment puis-je vous aider à discuter?"]]
]

# Créer l'objet Chat
alice_chatbot = Chat(pairs, reflections)

# Fonction pour obtenir la réponse de l'IA
def obtenir_reponse():
    user_input = user_input_text.get("1.0", "end-1c")
    response = alice_chatbot.respond(user_input)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "Vous: " + user_input + "\n")
    chat_history.insert(tk.END, "Alice: " + response + "\n\n")
    chat_history.config(state=tk.DISABLED)
    user_input_text.delete("1.0", tk.END)

# Interface graphique avec Tkinter
root = tk.Tk()
root.title("Assistant Virtuel - Alice")

# Zone de texte pour l'entrée utilisateur
user_input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
user_input_text.pack(pady=10)

# Bouton pour envoyer la question de l'utilisateur
send_button = tk.Button(root, text="Envoyer", command=obtenir_reponse)
send_button.pack()

# Zone de texte pour afficher la conversation
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
chat_history.pack(pady=10)
chat_history.config(state=tk.DISABLED)

# Lancer l'interface graphique
root.mainloop()
