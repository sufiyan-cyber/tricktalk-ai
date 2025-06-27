# tricktalk-ai
# 🎭 Social Engineering Chatbot

An AI-powered chatbot that simulates how scammers use social engineering tactics to trick users.  
It’s designed to showcase the power (and danger) of conversational AI when misused.

---

 🔍 What It Does

This chatbot:
- Mimics a scammer's behaviour using social engineering
- Asks probing questions to extract personal information
- Maintains session memory to continue conversations naturally
- Responds in a human-like tone using a large language model

⚠️ Disclaimer: This is a simulated project for learning and awareness only.  
It does not promote or encourage unethical use of AI in any form.

---

## 🛠️ Tech Stack

- Streamlit — UI and app logic
- OpenRouter API — Model access via `mistralai/mistral-7b-instruct:free`
- Python — Backend logic
- dotenv — For managing API keys securely
- Hugging Face Spaces — Deployment

---

## 🚀 How to Run Locally

1. Clone the repo:

git clone https://github.com/yourusername/social-engineering-chatbot.git
cd social-engineering-chatbot

2. Install dependencies:

pip install -r requirements.txt
Create a .env file in the root directory:

OPENAI_API_KEY=your_openrouter_api_key

3.Run the app:


streamlit run app.py
🌐 Try it Online
You can try the chatbot live on Hugging Face:
👉 https://huggingface.co/spaces/Sufiyan799/cyberproject

📂 Project Structure


├── app.py              # Main Streamlit app
├── .env                # Your private API key (not committed)
├── requirements.txt    # Python dependencies
├── README.md           # Project overview

🙋‍♂️ Why I Built This
This project was created to:

Understand prompt engineering and session flow in chatbots

Explore the darker side of conversational AI

Spark discussions on AI ethics and responsible usage

📬 Feedback
Tried it? Thoughts?
Feel free to open an issue or connect with me on Linkedin https://www.linkedin.com/in/sufiyan-khan-s-056j6a3a60238/

🛡️ Disclaimer
This project is strictly for educational purposes.
It does not store or process any real data, and should not be used for actual phishing or malicious purposes.
