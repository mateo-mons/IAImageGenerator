import streamlit as st
import os
import openai
#from dotenv import load_dotenv

#load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")

st.title("Generador de imagenes con DALL-E")

with st.form("images_form"):
    text = st.text_input("Prompt")
    num_images = st.number_input("Numero de imagenes a generar", min_value=1, max_value=10, value=1)
    image_size = st.selectbox("Tamaño de la imagen", ["256x256", "512x512", "1024x1024"], index=0)
    submit_button = st.form_sumbit_button(label="Generar imágenes")

if submit_button:
    st.write("Generando imagenes...")
    response = openai.Image.create(
        prompt = text,
        n = num_images,
        size = image_size
    )
    
    for i in range(num_images):
        url = response.data[i].url
        st.image(url, caption=f'Imagen {i+1}', use_column_width=True)

