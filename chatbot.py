import streamlit as st
import random

# Define possible bot responses
responses = [
    "Hello! How can I help you today?",
    "Hi there! What can I do for you?",
    "Hey! How can I assist you?",
    "Hi! What's up?"
]

def get_bot_response(user_input):
    return random.choice(responses)

# Streamlit interface
def main():
    st.title("Simple Chatbot with Streamlit")

    # Text input for user
    user_input = st.text_input("Enter your message here:")

    if st.button("Send"):
        if user_input:
            bot_response = get_bot_response(user_input)
            st.text_area("Bot's reply:", bot_response)
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
