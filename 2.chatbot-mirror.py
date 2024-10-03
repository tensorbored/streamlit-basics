####################### Build a bot that mirrors your input #######################
import streamlit as st
# st.write("Streamlit version", st.__version__)


st.title("Echo Bot")
print("st.session_state1: ",st.session_state)

# st.markdown(
#     """
# <style>
#     .st-emotion-cache-4oy321 {
#         flex-direction: row-reverse;
#         text-align: right;
#     }
# </style>
# """,
#     unsafe_allow_html=True,
# )

# https://discuss.streamlit.io/t/how-to-right-justify-st-chat-message/46794/4
st.markdown(
    """
<style>
    .st-emotion-cache-janbn0 {
        flex-direction: row-reverse;
        text-align: right;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown (prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})