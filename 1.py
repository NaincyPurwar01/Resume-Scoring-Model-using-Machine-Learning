import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
print(stopwords.words('english'))
print(len(stopwords.words('english')))