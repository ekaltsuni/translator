import streamlit as st
from translator import translate
from translator import format_language

st.set_page_config(
    page_title="Translation App",
    page_icon="🪄",
    menu_items={
        'About': "Created by Eleni Kaltsouni."
    }
)

st.title("Translate your text")
st.write("")

st.write("Choose your languages")
st.write("")

# lists of available languages
translate_from = ['English', 'Finnish', 'French', 'German', 'Greek', 'Italian', 'Russian', 'Spanish']
translate_to = ['English', 'Finnish', 'French', 'German', 'Greek', 'Italian', 'Russian', 'Spanish']

option_from = st.selectbox(
    'Translate from:',
    translate_from)

# condition that pairs translate to and translate from languages based on available models
if option_from == 'English':
    translate_to = ['Finnish', 'French', 'German', 'Greek', 'Italian', 'Russian', 'Spanish']
elif option_from == 'Finnish':
    translate_to = ['English', 'French', 'German', 'Greek', 'Italian', 'Russian', 'Spanish']
elif option_from == 'French':
    translate_to = ['English', 'German', 'Greek', 'Russian', 'Spanish']
elif option_from == 'German':
    translate_to = ['English', 'Finnish', 'French', 'Greek', 'Italian', 'Spanish']
elif option_from == 'Greek':
    translate_to = ['Finnish', 'French']
elif option_from == 'Italian':
    translate_to = ['English', 'French', 'German', 'Spanish']
elif option_from == 'Russian':
    translate_to = ['English', 'Finnish', 'French', 'Spanish']
elif option_from == 'Spanish':
    translate_to = ['English', 'Finnish', 'French', 'German', 'Greek', 'Italian', 'Russian']


option_to = st.selectbox(
    'to:',
    translate_to)
st.write("")

# user input text area with empty value
input_text = st.text_area("Enter your text below", value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
button = st.button('Translate')

# progress bar
if button:
    # output text generation by calling the translate method along with its parameters
    output_text = translate(input_lang=format_language(option_from), input_text=input_text,
                            output_lang=format_language(option_to))

    st.write("")

    # text area with value the translated text
    st.text_area('See your text below :point_down:', value=output_text, height=None, max_chars=None, key=None, help=None, on_change=None,
                 args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")