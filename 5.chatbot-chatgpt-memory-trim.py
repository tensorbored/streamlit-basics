######################## Build a ChatGPT-like app #######################
# with self created list memory function: remembering upto last 4 messages and 1 system message

# from openai import OpenAI
from groq import Groq
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
client = Groq(api_key= os.getenv("GROQ_API_KEY"))

# Set a default model
if "groqai_model" not in st.session_state:
    st.session_state["groqai_model"] = "llama3-8b-8192"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    #sens user's message to the LLM and get a response
    messages=[
    {"role": "system", "content": "You are a helpful assistant"},
    *st.session_state.messages
    ]

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        assitant_response = client.chat.completions.create(
            model=st.session_state["groqai_model"],
            messages=messages
        )
        response=(assitant_response.choices[0].message.content)
        st.markdown(response)
        # response = st.write_stream(stream)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Keep last 4 messages only
    if len(st.session_state.messages)>4:
        st.session_state.messages=st.session_state.messages[-4:]

    with st.expander("Show Messages"):
        st.write(st.session_state.messages)
    print(st.session_state.messages)