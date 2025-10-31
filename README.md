🌿 Mental Health Support Chatbot

An AI-powered mental health chatbot built using Streamlit and Ollama, designed to provide emotional support, positive affirmations, and guided meditation.
This chatbot promotes well-being by offering empathetic responses and stress-relief resources in a calm, user-friendly interface.

🧠 Features

🗣️ AI Chat Support: Have natural, supportive conversations about how you feel.

💬 Positive Affirmations: Get uplifting messages to boost your mood.

🧘 Guided Meditation: Receive short meditation scripts to help you relax.

🎨 Beautiful Background: Includes a customizable background image with modern styling.

🧾 Persistent Chat History: Keeps track of previous messages during the session.

🧩 Tech Stack

Python 3.10+

Streamlit – for UI and deployment

Ollama – for AI model interaction (uses gemma3:1b model by default)

Base64 / Pathlib – for image handling and encoding

🚀 Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/mental-health-support-chatbot.git
cd mental-health-support-chatbot

2️⃣ Install dependencies

Make sure you have Python and pip installed, then run:

pip install streamlit ollama

3️⃣ Add a background image

Place an image file named background.jpg in the same folder as mental_support.py.

4️⃣ Run the app
streamlit run mental_support.py

🧘 How It Works

Type your feelings or any question into the chatbot.

The AI (via Ollama’s gemma3:1b model) provides a supportive and empathetic reply.

Click:

💬 “Give me a Positive Affirmation” for motivation.

🧘 “Give me a Guided Meditation” for a calming experience.

💡 Customization

To change the AI model, modify this line in the code:

response = ollama.chat(model="gemma3:1b", messages=st.session_state['conversation_history'])


You can replace the background.jpg with any preferred calming image.

🧑‍💻 Author

**ASHUTOSH SHARMA**

⚠️ Disclaimer

This chatbot is not a substitute for professional mental health advice or therapy.
If you are in crisis or need immediate support, please contact a licensed mental health professional or local helpline.
