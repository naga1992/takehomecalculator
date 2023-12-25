import streamlit as st
import google.generativeai as genai
import os,io
from pathlib import Path
import PIL.Image as Image


st.title("Take home calculator")
st.markdown('''
Steps to use the app
            
1. Obtain your Gemini Pro key from [Google's Maker Suite](https://makersuite.google.com/app/apikey).
2. Here is a [step by step guide on how to get your gemini pro api key](https://scribehow.com/shared/Guide_How_to_Create_an_API_Key_in_Google_Makersuite__wOUuE2IFSjG5CFxWGEyU7A)
3. Upload the image containing the salary breakup
            ''')
api_key = st.sidebar.text_input(
    label="add your gemini pro key",
    help="get your key here https://makersuite.google.com/app/apikey"
)
uploaded_file = st.sidebar.file_uploader("upload a image of your salary breakup")

if api_key and (uploaded_file is not None) and st.sidebar.button("Submit"):

   
    
    bytes_data = uploaded_file.getvalue()
    image = Image.open(io.BytesIO(bytes_data))
    genai.configure(api_key=api_key)

    # Set up the model
    generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    # Validate that an image is present
   
    image_parts = [
    {
        "mime_type": "image/jpeg",
        "data": bytes_data
    },
    ]

    prompt_parts = [
    "You are a expert CA ,who is well versed in Indian tax laws , \
    Show me the tax calulation for the below salary breakup \
    Dont make up caluclations, if you are unable to caluate return unable to calculate tax based on the given image \
    Add a discalimer at the end to contact a real financial adiviser for more detailed and accurate calucations",
    
    image_parts[0],
    ]

    response = model.generate_content(prompt_parts)
    st.write(response.text)

