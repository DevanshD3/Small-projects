
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\Dell\Downloads\sentiment-analysis-284609-a234a6af795c.json"



def language_analysis(text):
    client = language.LanguageServiceClient()
    # The text to analyze
    
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    ent_analysis = client.analyze_entities(document=document,encoding_type='UTF32')
    dir(ent_analysis)
    entities = ent_analysis.entities


    return sentiment, entities


text = 'Python is a great language i use everyday for my daily work and i make machine learning models and neural networks'

sentiment, entities = language_analysis(text)
print('Text: {}'.format(text))
# print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
for e in entities:
    print(e.name,  e.metadata, e.salience)


# document = language.types.Document(
# ...     content='Michelangelo Caravaggio, Italian painter, is '
# ...             'known for "The Calling of Saint Matthew".',
# ...     type=language.enums.Document.Type.PLAIN_TEXT,
# ... )
# >>> response = client.analyze_entities(
# ...     document=document,
# ...     encoding_type='UTF32',
# ... )
# >>> for entity in response.entities:
# ...     print('=' * 20)
# ...     print('         name: {0}'.format(entity.name))
# ...     print('         type: {0}'.format(entity.type)