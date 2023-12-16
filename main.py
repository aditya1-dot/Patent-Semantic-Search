import streamlit as st
from utils import semantics,load_model
import random
import time
# from utils import model_bot, model_loader
# st.sidebar.title("Welcome !")
# st.sidebar.write("Effortlessly navigate the patent landscape with Team 1NeuRon's expert guidance, simplifying your journey through the complex world of patents.")
# st.sidebar.info("Powered by : 1NeuRon ")

# # Main chat interface
# st.title("Discovering Patents Effortlessly")
# st.write("Feel free to inquire about patents, and let the AI effortlessly guide you to the precise information you seek.")

# User input
# user_input = st.text_input("What is your question about patents?", "")
# load_model()
# if st.button("Send"):
    
#     if user_input:
#         # Here you'd normally call a function that processes the question and fetches the answer
#         # For example, using a predefined pipeline:
#         # response = nlp_model(question=user_input, context="The context text for the model")
#         # answer = response["answer"]
        
#         # title,abstract=semantics(user_input)
#         title,abstract=semantics(user_input)
#         # answer = "This is where the answer from the chatbot would appear."  # Placeholder
        
#         for Title,Abstract in zip(title,abstract):
#                 st.markdown(f"**Title:** ***{Title}***")
#                 st.markdown(f'**Abstract:** {Abstract}')
#                 st.markdown("----")
#         # else:
#         #     st.warning("Query not in the knowledge of Model.")


def main():
    st.sidebar.title("Welcome !")
    st.sidebar.write("Effortlessly navigate the patent landscape with Team 1NeuRon's expert guidance, simplifying your journey through the complex world of patents.")
    st.sidebar.info("Powered by : 1NeuRon ")

    # Main chat interface
    st.title("Discovering Patents Effortlessly")
    st.write("Feel free to inquire about patents, and let the AI effortlessly guide you to the precise information you seek.")

    # st.title("GlitchFix Chat bot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if u_prompt := st.chat_input("Ask your question about Pantents."):
        

        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(u_prompt)
            load_model()
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": u_prompt})

        # system_prompt = "you are a personalised career guidance to students, you will chat with students regarding their academic performance and their future career aspects. Answer queries related to this field only and deny any other questions."
        # input_prompt = system_prompt + "\n" + str(u_prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Generate response using the combined prompt
            assistant_response = semantics(query=u_prompt)

            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response:
                full_response += chunk + ""
                time.sleep(0.00025)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "")

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()


# Footer
st.sidebar.markdown("---")
