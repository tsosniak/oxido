import requests
from bs4 import BeautifulSoup
import openai
import logging
from dotenv import load_dotenv
import os

URL = 'https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt'

PROMPT = """I am a developer. Based on TEXT variable, return me a HTML code that follows the below instructions: 1. 
Use only html tags that correspond to the content in TEXT variable: avoid tags like 'doctype', 'html',  'head', 
'body' etc., but you can use tags like 'h1', 'p' and other that make HTML code beautiful. 2. Think of the places 
where you can insert several graphics. Mark them using the <img> tag with the src="image_placeholder.jpg" attribute. 
Add an alt attribute to each image with the exact prompt that can be used to generate the graphic. Place captions 
under graphics using the appropriate HTML tag. 3. Don't add any CSS or Javascript code! 4. Don't give me any 
explanation or programming code! I need just mentioned HTML file as response! 5. Remove ```html and ``` from your 
response!. My TEXT variable is: [PLACEHOLDER] """

load_dotenv()

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')

openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    logging.error('The OPENAI_API_KEY environment variable is not set.')
    exit()


def fetch_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(separator='\n')
        return text
    except requests.exceptions.RequestException as e:
        logging.error(f"RequestException: Unable to fetch the webpage: {e}")
        return None


def send_prompt_to_openai(prompt_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_text}
            ],
            # max_tokens=300,
            temperature=0.3
        )
        generated_text = response.choices[0].message['content'].strip()
        return generated_text
    except openai.error.OpenAIError as e:
        logging.error(f"OpenAIError: Error in sending prompt to OpenAI: {e}")
        return None


def save_response_as_html(generated_text, filename='artykul.html'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("<body>\n")
            file.write(f"{generated_text}\n")
            file.write("</body>\n")
        logging.info(f"Response saved as {filename}")
    except IOError as e:
        logging.error(f"IOError: Error in saving response as HTML: {e}")


if __name__ == "__main__":
    original_text = fetch_text_from_url(URL)
    if original_text:
        PROMPT = PROMPT.replace('[PLACEHOLDER]', original_text)
        openai_response = send_prompt_to_openai(PROMPT)
        if openai_response:
            save_response_as_html(openai_response)
        else:
            logging.error("No response received from OpenAI.")
    else:
        logging.error("No text fetched from the URL.")
