import streamlit as st
from openai_chat import OpenAIChat

chatbot = OpenAIChat()

# Set page title and favicon
st.set_page_config(page_title="Chat UI", page_icon="💬", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f9f9f9;
        }
        .chat-container {
            max-width: 700px;
            margin: 0 auto;
        }
        .chat-message {
            padding: 10px;
            margin: 5px 0;
            border-radius: 8px;
            max-width: 75%;
        }
        .user-message {
            background-color: #0078FF;
            color: white;
            align-self: flex-end;
            margin-left: auto;
        }
        .bot-message {
            background-color: #E9E9EB;
            color: black;
            align-self: flex-start;
            margin-right: auto;
        }
        .message-container {
            display: flex;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("🤖 Parthi bot ")
st.sidebar.write("Configure chatbot options here.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
st.write("<div class='chat-container'>", unsafe_allow_html=True)
for message in st.session_state.messages:
    role_class = "user-message" if message["role"] == "user" else "bot-message"
    st.markdown(
        f"<div class='message-container'><div class='chat-message {role_class}'>{message['content']}</div></div>",
        unsafe_allow_html=True
    )
st.write("</div>", unsafe_allow_html=True)

# Multi-line input box
# user_input = st.text_area("Type your message...", key="user_input", placeholder="Ask me anything...", height=100)

prompt = st.chat_input("Say something")
        

@st.dialog("Finding Response..")
def dialog():
    with st.spinner("Wait for it...", show_time=True):
            # bot_response = chatbot.get_response(prompt)
        
            st.session_state.messages.append({"role": "bot", "content": "bot_response"})

            # Clear input after sending
            st.rerun()


if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    dialog()

# # Handle user input when "Send" button is clicked
# if st.button("Send"):
#     if user_input.strip():  # Avoid empty messages
#         # Store user message
#         st.session_state.messages.append({"role": "user", "content": user_input})

#         # Dummy chatbot response (Replace this with OpenAI API integration)
#         # bot_response = "I'm ChatGPT, how can I assist you today?"
#         dialog()