
### Overview:
This repository contains a simple Streamlit application that utilizes Google's Generative AI to generate content based on a user-provided image. Specifically, the application takes an image as input and generates a text response related to tax calculations based on the visual content. 


### Try it out in Streamlit 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://takehomecalculator-mm9y9i6q8n7ed8s4plhrzd.streamlit.app/)

### Prerequisites:
1. Python 3.x
2. Streamlit
3. Google Generative AI package (`google.generativeai`)
4. PIL (Pillow) library for image processing

### Setup:
1. **Installation**:
   - Install the necessary Python packages using pip:
     ```
      pip install -r requirements.txt
     ```
   
2. **API Key**:
   - Obtain your Gemini Pro key from [Google's Maker Suite](https://makersuite.google.com/app/apikey).
   - Here is a [step by step guide on how to get your gemini pro api key](https://scribehow.com/shared/Guide_How_to_Create_an_API_Key_in_Google_Makersuite__wOUuE2IFSjG5CFxWGEyU7A)
   - Input this key into the application via the Streamlit sidebar when prompted.

### Usage:
1. **Running the Application**:
   - Navigate to the directory containing the code.
   - Run the Streamlit application using the following command:
     ```
     streamlit run takehomecalc.py
     ```
   
2. **Input Requirements**:
   - Upload an image file using the file uploader in the Streamlit sidebar.
   - Provide your Gemini Pro key in the specified text input field.
   - Click the "Submit" button to initiate the content generation process.

3. **Output**:
   - Upon successful execution, the application will display the generated text content related to tax calculations based on the uploaded image.

