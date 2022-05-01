'''This is Language Translator App'''
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

try:
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    def englishToFrench(englishtext):
        '''Take English as a string and convert it to French'''
        if englishtext == '':
            frenchtext=''
        else:
            translation = language_translator.translate(
                text=englishtext,
                model_id='en-fr').get_result()
            frenchtext=translation['translations'][0]['translation']
        return frenchtext
    def frenchToEnglish(frenchtext):
        '''Take French as a string and convert it to Enghish'''
        if frenchtext == '':
            englishtext=''
        else:
            translation = language_translator.translate(
                text=frenchtext,
                model_id='fr-en').get_result()
            englishtext=translation['translations'][0]['translation']
        return englishtext
except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)
