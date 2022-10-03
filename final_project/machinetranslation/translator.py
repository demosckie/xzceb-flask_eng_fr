"""translator"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv



load_dotenv()



apikey = os.environ['apikey']

url = os.environ['url']

authenticator = IAMAuthenticator('u5EooYiJ85xIe3xc85B91GEulyziV_vSFBzPdSUlHlCc')

language_translator = LanguageTranslatorV3(

    version='2018-05-01',

    authenticator=authenticator

)

language_translator.set_service_url('url')



translation = language_translator.translate(

    text='Hello, how are you?',

    model_id='en-fr').get_result()

print(json.dumps(translation, indent=2, ensure_ascii=False))



def englishtofrench(english_text):

    """English to French Translation"""

    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()

    return french_text.get("translations")[0].get("translate")



def frenchtoenglish(french_text):

    """French to English Translation"""

    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()

    return english_text.get("translations")[0].get("translate")
