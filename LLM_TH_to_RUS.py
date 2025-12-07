import streamlit as st
st.title('Translate Thai to Russian')
st.sidebar.header('Thai to Russain')
#make a sidebar for input API key of openai, using google gemini api
st.sidebar.subheader('OpenAI API Key')
api_key = st.sidebar.text_input('Enter your OpenAI API Key:', type='password')

#make a Thai text input box in the main page, middle of the page, with a button to translate.
#using google gemini api to translate the text
#use available engine from openai
thai_text = st.text_area('Enter Thai text to translate to Russian:', height=200)
if st.button('Translate'):
    if api_key and thai_text:
        import openai
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Translate the following Thai text to Russian:\n\n{thai_text}"}],
            max_tokens=1000,
            temperature=0.5,
        )
        russian_translation = response.choices[0].message.content.strip()
        st.subheader('Russian Translation')
        st.write(russian_translation)
#display the translated text in the main page
    else:
        st.error('Please enter both your OpenAI API Key and the Thai text to translate.')
#make a table that use text from user, first column is Thai text, second column is Russian translation and the third column is example usage of the translated text in Russian.
if st.button('Show Example Usage'):
    if api_key and thai_text:
        import openai
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Provide an example usage of the following Russian translation:\n\n{russian_translation}"}],
            max_tokens=1000,
            temperature=0.5,
        )
        example_usage = response.choices[0].message.content.strip()
        st.subheader('Example Usage in Russian')
        st.write(example_usage)
        st.subheader('Translation Table')
        import pandas as pd
        data = {
            'Thai Text': [thai_text],
            'Russian Translation': [russian_translation],
            'Example Usage in Russian': [example_usage]
        }
        df = pd.DataFrame(data)
        st.table(df)







