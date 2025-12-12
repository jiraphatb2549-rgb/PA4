import streamlit as st
import pandas as pd
import google.generativeai as genai

st.title('Translate Thai to Russian')

st.sidebar.header('Thai to Russian (Google Gemini API)')
api_key = st.sidebar.text_input('Enter your Gemini API Key:', type='password')

if api_key:
    genai.configure(api_key=api_key)

thai_text = st.text_area('Enter Thai text to translate to Russian:', height=200)

if "russian_translation" not in st.session_state:
    st.session_state.russian_translation = None

if "example_usage" not in st.session_state:
    st.session_state.example_usage = None


# --- TRANSLATE ---
if st.button('Translate'):
    if api_key and thai_text:
        try:
            model = genai.GenerativeModel("models/gemini-2.5-flash")   
            prompt = f"Translate this Thai text into Russian:\n\n{thai_text}"
            response = model.generate_content(prompt)
            st.session_state.russian_translation = response.text.strip()

            st.subheader('Russian Translation')
            st.write(st.session_state.russian_translation)

        except Exception as e:
            st.error(f"Translation Error: {e}")
    else:
        st.error("Please provide both API key and Thai text.")


# --- EXAMPLE USAGE ---
if st.button('Show Example Usage'):
    if api_key and st.session_state.russian_translation:
        try:
            model = genai.GenerativeModel("models/gemini-2.5-flash")   
            prompt = (
                f"Provide an example sentence using this Russian text:\n\n"
                f"{st.session_state.russian_translation}"
            )
            response = model.generate_content(prompt)
            st.session_state.example_usage = response.text.strip()

            st.subheader("Example Usage in Russian")
            st.write(st.session_state.example_usage)

            df = pd.DataFrame({
                "Thai Text": [thai_text],
                "Russian Translation": [st.session_state.russian_translation],
                "Example Usage": [st.session_state.example_usage]
            })
            st.table(df)

        except Exception as e:
            st.error(f"Example Usage Error: {e}")
    else:
        st.error("Please translate first.")









