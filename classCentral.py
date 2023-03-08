import requests
from bs4 import BeautifulSoup
from googletrans import Translator

#url = "https://www.classcentral.com/"
url = "https://www.classcentral.com/university/harvard"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# Extract the text content of the webpage using Beautiful Soup
text_content = soup.get_text()

# Use Google Translate API to translate the text content from English to Hindi
translator = Translator(service_urls=['translate.google.com'])
translated_text = translator.translate(text_content, src='en', dest='hi').text

# Print the translated content
print(translated_text)

