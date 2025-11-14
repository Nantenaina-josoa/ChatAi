import google.generativeai as genai

# Ta FAUSSE clé API
API_KEY = "AIzaSyCIF-rc3wBEGShF1mQZ15UDcIy-CSCLMRA"

# 1) Configuration
genai.configure(api_key=API_KEY)

# 2) Choix du modèle
model = genai.GenerativeModel("gemini-1.5-flash")

print("=== Mini Chat Gemini (clé factice) ===")
print("Tape 'quit' pour sortir.\n")

while True:
    user_input = input("Toi : ")

    if user_input.lower() == "quit":
        print("Chat terminé.")
        break

    try:
        response = model.generate_content(user_input)
        print("Bot :", response.text)
    except Exception as e:
        print("Erreur API :", e)
        print("Normal : la clé API est fausse !")
