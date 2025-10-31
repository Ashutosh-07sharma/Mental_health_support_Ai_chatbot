import streamlit as st
import ollama
import base64
from pathlib import Path

# Page configuration
st.set_page_config(page_title="Mental Health Chatbot")

# Function to convert image to base64
def get_base64(background_path):
    p = Path(background_path)
    if not p.exists():
        raise FileNotFoundError(f"Background file not found: {p.resolve()}")
    with p.open('rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load background image (make sure 'background.jpg' is in the same folder)
bin_str = get_base64('background.jpg')

# ✅ CSS styling for background
background_style = f"""
<style>
  /* Set full-page background */
  .stApp {{
    background-image: url("data:image/jpg;base64,{bin_str}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
  }}

  /* Optional translucent effect for main content */
  .stApp > .main {{
    background-color: rgba(255, 255, 255, 0.85);
    padding: 1.5rem;
    border-radius: 12px;
  }}

  /* Optional: transparent sidebar if present */
  .stSidebar {{
    background: rgba(255, 255, 255, 0.6) !important;
  }}

  /* Make titles and text more readable on bright backgrounds */
  h1, h2, h3, h4, h5, h6, p, label {{
    color: #1a1a1a;
  }}
</style>
"""

st.markdown(background_style, unsafe_allow_html=True)

# Initialize session history
st.session_state.setdefault('conversation_history', [])

# Chatbot response function
def generate_response(user_input):
    st.session_state['conversation_history'].append({"role": "user", "content": user_input})
    response = ollama.chat(model="gemma3:1b", messages=st.session_state['conversation_history'])
    ai_response = response['message']['content']
    st.session_state['conversation_history'].append({"role": "assistant", "content": ai_response})
    return ai_response

# Affirmation generator
def generate_affirmation():
    prompt = "Provide a positive affirmation to encourage someone who is feeling stressed or overwhelmed."
    response = ollama.chat(model="gemma3:1b", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Meditation guide generator
def generate_meditation_guide():
    prompt = "Provide a 5-minute guided meditation to help someone relax and reduce stress."
    response = ollama.chat(model="gemma3:1b", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Title
st.markdown(
    """
    <style>
        h1 {
            color: #003366 !important;   /* Dark blue color */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌿 Mental Health Support Agent")

# Display conversation
for msg in st.session_state['conversation_history']:
    role = "You" if msg['role'] == "user" else "AI"
    st.markdown(f"**{role}:** {msg['content']}")

# Input area
user_message = st.text_input("How can I help you today?")

# Generate response
if user_message:
    with st.spinner("Thinking..."):
        ai_response = generate_response(user_message)
        st.markdown(f"**AI:** {ai_response}")

# Buttons for affirmations and meditation
col1, col2 = st.columns(2)

with col1:
    if st.button("💬 Give me a Positive Affirmation"):
        affirmation = generate_affirmation()
        st.markdown(f"**Affirmation:** {affirmation}")

with col2:
    if st.button("🧘 Give me a Guided Meditation"):
        meditation_guide = generate_meditation_guide()
        st.markdown(f"**Guided Meditation:** {meditation_guide}")
