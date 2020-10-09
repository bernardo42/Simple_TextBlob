from textblob import TextBlob
import nltk
from newspaper import Article

# Get the article
url = 'https://everythingcomputerscience.com/'
article = Article(url)

# Do some NLP
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

# Get the summary article
text = article.summary

# Create a textblob object
obj = TextBlob(text)
# This return a value between -1 and 1
sentiment = obj.sentiment.polarity
print(sentiment)

if sentiment == 0:
    print("The text is neutral")
elif sentiment > 0:
    print("The text is positive")
else:
    print("The text is negative")
    
# Try in other text
text2 = 'I am lazy'

obj2 = TextBlob(text2)

sentiment2 = obj2.sentiment.polarity
print(sentiment2)

if sentiment2 == 0:
    print("The text is neutral")
elif sentiment2 > 0:
    print("The text is positive")
else:
    print("The text is negative")
    

text3 = 'I am Smart'

obj3 = TextBlob(text3)

sentiment3 = obj3.sentiment.polarity
print(sentiment3)

if sentiment3 == 0:
    print("The text is neutral")
elif sentiment3 > 0:
    print("The text is positive")
else:
    print("The text is negative")