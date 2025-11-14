import requests
import os
import time

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

API_KEY = "AIzaSyCIF-rc3wBEGShF1mQZ15UDcIy-CSCLMRA" 
MODEL = "gemini-2.0-flash"
HISTORY_FILE = "chat_history.txt"

conversation_history = []

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def afficher_ascii():
    art = f"""
{RED}┏┓┏┓┏┓────┏┓───────────────── 
┃┃┃┃┃┃────┃┃───────────────── -----
┃┃┃┃┃┃┏━━┓┃┃─┏━━┓┏━━┓┏┓┏┓┏━━┓ ___
┃┗┛┗┛┃┃┃━┫┃┃─┃┏━┛┃┏┓┃┃┗┛┃┃┃━┫ ___
┗┓┏┓┏┛┃┃━┫┃┗┓┃┗━┓┃┗┛┃┃┃┃┃┃┃━┫ ___
─┗┛┗┛─┗━━┛┗━┛┗━━┛┗━━┛┗┻┻┛┗━━┛____
-------─┏┓───── 
-------┏┛┗┓──── 
-------┗┓┏┛┏━━┓ 
-------─┃┃─┃┏┓┃ 
-------─┃┗┓┃┗┛┃ 
-------─┗━┛┗━━┛ 
─┏┓───────────────────┏┓───────┏┓─___ 
─┗┛───────────────────┃┃──────┏┛┗┓___ 
─┏┓┏━━┓┏━━┓┏━━┓┏━━┓───┃┗━┓┏━━┓┗┓┏┛___ 
─┃┃┃┏┓┃┃━━┫┃┏┓┃┃┏┓┃───┃┏┓┃┃┏┓┃─┃┃─___ 
┏┛┃┃┗┛┃┣━━┃┃┗┛┃┃┏┓┃───┃┗┛┃┃┗┛┃─┃┗┓___ 
┗━┛┗━━┛┗━━┛┗━━┛┗┛┗┛───┗━━┛┗━━┛─┗━┛___{RESET}
"""
    print(art)

def sauvegarder_historique(pseudo, msg, bot_msg):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{pseudo}: {msg}\nBot: {bot_msg}\n\n")

def envoyer_message(message):
    conversation_history.append({"text": message})

    full_conversation = "\n".join([m["text"] for m in conversation_history])

    url = f"https://generativelanguage.googleapis.com/v1/models/{MODEL}:generateContent?key={API_KEY}"
    data = {"contents": [{"parts": [{"text": full_conversation}]}]}

    response = requests.post(url, json=data)

    if response.status_code != 200:
        print(RED + "Erreur API :" + RESET, response.text)
        return None

    res_json = response.json()
    bot_response = res_json["candidates"][0]["content"]["parts"][0]["text"]

    conversation_history.append({"text": bot_response})

    return bot_response

def menu():
    print(CYAN + "\n=== MENU PRINCIPAL ===" + RESET)
    print(GREEN + "1 - Continuer le chat" + RESET)
    print(YELLOW + "2 - Quitter" + RESET)
    print(BLUE + "3 - Contacter" + RESET)
    choix = input(CYAN + "Sélectionne une option : " + RESET)
    return choix

def chat_loop(pseudo):
    print(GREEN + f"\n --> Conversation commencée, {pseudo} ! \n --> Tape 'menu' pour revenir au menu \n" + RESET)
    while True:
        msg = input(GREEN + f"{pseudo} : " + RESET)
        if msg.lower() == "quit":
            print(RED + "Chat terminé." + RESET)
            break
        if msg.lower() == "menu":
            break

        print(YELLOW + "--> Bot est en train de répondre....." + RESET)
        time.sleep(0.5)
        rep = envoyer_message(msg)
        if rep:
            print(BLUE + "Bot : " + RESET + rep)
            print("\a") 
            sauvegarder_historique(pseudo, msg, rep)

clear_screen()
afficher_ascii()
pseudo = input(GREEN + "--> Entrez votre pseudo : " + RESET)

while True:
    choix = menu()
    if choix == "1":
        chat_loop(pseudo)
    elif choix == "2":
        print(RED + "\n --> Merci d'avoir utilisé le chat. Au revoir !" + RESET)
        break
    elif choix == "3":
        print(CYAN + "\nContact email : " + RESET + "josoanantenaina4@gmail.com")
    else:
        print(RED + "Option invalide. Réessaie." + RESET)
