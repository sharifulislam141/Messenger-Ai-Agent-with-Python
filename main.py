from flask import Flask, request
import requests
import google.generativeai as genai
import config

app = Flask(__name__)

VERIFY_TOKEN = config.VERIFY_TOKEN
PAGE_ACCESS_TOKEN = config.PAGE_ACCESS_TOKEN
# --- Gemini Setup ---
genai.configure(api_key=config.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_reply(user_message: str):
    system_prompt = """
You are a friendly, intelligent Facebook Messenger chatbot replying on behalf of Dark Hunter 141 a cyber security team.
Guidelines:
- Be short and conversational, natural tone.
- Reply in Bengali if the user types in Bengali, otherwise reply in English.
- Use emojis occasionally.
- If confused, politely ask for clarification.
- Never mention that you are an AI or chatbot.
- If user greets, greet warmly.
"""

    combined_prompt = f"{system_prompt}\n\nUser: {user_message}\nBot:"
    response = model.generate_content(combined_prompt)

    return response.text.strip() if response and response.text else "Sorry, I couldn’t generate a reply 😅"



# def generate_reply(user_message: str):
#     # System instructions (like in your n8n AI Agent)
#     system_prompt = """
# You are a friendly, intelligent Facebook Messenger chatbot replying on behalf of Dark Hunter 141 a cyber security team.
# Guidelines:
# - Be short and conversational, natural tone.
# - Reply in Bengali if the user types in Bengali, otherwise reply in English.
# - Use emojis occasionally.
# - If confused, politely ask for clarification.
# - Never mention that you are an AI or chatbot.
# - If user greets, greet warmly.
# """

#     response = model.generate_content([
#         {"role": "system", "parts": [system_prompt]},
#         {"role": "user", "parts": [user_message]}
#     ])

#     return response.text.strip() if response and response.text else "Sorry, I couldn’t generate a reply 😅"




@app.route("/")
def home():
    return "Hello, World!"



@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Facebook verification
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Invalid verification token"

    elif request.method == "POST":
        data = request.json
        print(data)

        for entry in data.get("entry", []):
            for messaging_event in entry.get("messaging", []):
                if "message" in messaging_event:
                    sender_id = messaging_event["sender"]["id"]
                    user_message = messaging_event["message"].get("text")

                    if user_message:
                        # --- AI Reply ---
                        # prompt = f"User message: {user_message}\nReply in a natural, short, friendly tone."
                        # response = model.generate_content(prompt)
                        # reply = response.text.strip()
                        print("User message:", user_message)
                        reply = generate_reply(user_message)
                        print(reply)


                        send_message(sender_id, reply)

        return "OK", 200


def send_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v17.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "messaging_type": "RESPONSE",
        "message": {"text": message_text},
    }
    requests.post(url, json=payload)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
