######################## Build a ChatGPT-like app #######################

# from openai import OpenAI
from groq import Groq
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
client = Groq(
    api_key= os.getenv("GROQ_API_KEY"),
)

# Set a default model
if "groqai_model" not in st.session_state:
    # st.session_state["groqai_model"] = "gpt-3.5-turbo"
    st.session_state["groqai_model"] = "llama3-8b-8192"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# print(st.session_state.messages)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# https://discuss.streamlit.io/t/groq-x-st-write-stream-space-chat/66404
def parse_groq_stream(stream):
    for chunk in stream:
        if chunk.choices:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["groqai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        # response=(stream.choices[0].message.content)
        # st.markdown(response)
        # response = st.write_stream(stream)
        response = st.write_stream(parse_groq_stream(stream))
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # with st.expander("Show Messages"):
    #     st.write(st.session_state.messages)
    print(st.session_state.messages)