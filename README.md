# Messenger AI Agent with Python 🤖💬

This project is a **Facebook Messenger chatbot** powered by **Google Gemini AI** and built with **Python + Flask**. It automatically responds to user messages in a **friendly, human-like tone** on behalf of your organization.

---

## ✨ Features

- Facebook Messenger integration (via Graph API)
- AI-powered replies using **Gemini 1.5 Flash**
- Separate **system prompt** + **user prompt**
- Responds in **English** or **Bengali** depending on input
- Tokens and keys managed via `config.json` (no hardcoding)
- Easy to deploy locally or on a server

---

## 📂 Project Structure

```
Messenger-Ai-Agent-with-Python/
│── main.py           # Flask app with webhook + AI reply logic
│── config.json       # Store API keys & tokens here
│── requirements.txt  # Python dependencies
│── README.md         # Project documentation
```

---

## ⚙️ Requirements

- Python 3.10+ (works with 3.13 as tested)
- Facebook Page + App (for Messenger API)
- Gemini API key

---

## 📥 Installation

1. **Clone the repo**
    ```bash
    git clone https://github.com/sharifulislam141/Messenger-Ai-Agent-with-Python.git
    cd Messenger-Ai-Agent-with-Python
    ```

2. **Create a virtual environment (recommended)**
    ```bash
    python -m venv venv
    # Mac/Linux
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configuration**
    Create a `config.json` file in the root folder:
    ```json
    {
      "VERIFY_TOKEN": "your_webhook_verify_token",
      "PAGE_ACCESS_TOKEN": "your_facebook_page_access_token",
      "GEMINI_API_KEY": "your_gemini_api_key"
    }
    ```
    - `VERIFY_TOKEN`: Any string you choose (must match in Facebook app settings)
    - `PAGE_ACCESS_TOKEN`: Found in your Facebook Developer App → Messenger → Settings
    - `GEMINI_API_KEY`: Get one from Google AI Studio

---

## 🚀 Run the Bot

Start the Flask server:
```bash
python main.py
```
You should see:
```
 * Running on http://127.0.0.1:5000
```

Expose your local server to the internet using ngrok:
```bash
ngrok http 5000
```
Copy the generated `https://xxxxx.ngrok.io` URL and set it as your Webhook URL in Facebook Developer settings.

---

## 🧪 Test the Bot

Send a message to your Facebook Page.

The bot will:
- Receive the message
- Generate a reply using Gemini AI
- Send the response back via Messenger

---

## 🛠️ Customization

- Modify the system prompt in `main.py` inside `generate_reply()` to change personality/tone.
- You can extend to support:
    - Image/file replies
    - Logging chat history
    - Quick replies / buttons

---

## 📜 License

MIT License © 2025 Shariful Islam

---

## 🙌 Acknowledgements

- Flask
- Requests
- Google Generative AI
- Facebook Graph API
