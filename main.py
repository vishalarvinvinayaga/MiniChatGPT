import streamlit as st 
from streamlit_chat import message
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

def init():
    load_dotenv()
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") ==" ":
        print("OPENAI_API_KEY not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(
        page_title = "Your own GPT",
        page_icon = "🤖"
    )


def clear_text():
    st.session_state.user_input = ""


def main():
    init()

    chat = ChatOpenAI(temperature = 0)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant")
        ]

    st.header("your own chatgpt")

    with st.sidebar:
        user_input = st.text_input(label="your message",key="user_input")

        if user_input:
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Thinking...."):
                response = chat(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))


    
    mess = st.session_state.messages
    for i, msg in enumerate(mess[1:]):
        if i%2 == 0:
            message(msg.content, is_user=True, key=str(i)+"_user")
        else:
            message(msg.content, is_user=False, key=str(i)+"_ai")



if __name__ == "__main__":
    main()