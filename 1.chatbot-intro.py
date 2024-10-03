# https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps

####################### st.chat_message example #######################

import streamlit as st
import numpy as np

# method 1
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

with st.chat_message("assistant"):
    st.write("Hello human")
    # message.bar_chart(np.random.randn(30, 3))

# method 2
message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))