#!/usr/bin/env python
# coding: utf-8

# ## Complete Text Processing

# In[11]:


get_ipython().system('pip install pandas')


# In[48]:


import pandas as pd
import numpy as np
import spacy 


# In[49]:


from spacy.lang.en.stop_words import STOP_WORDS as stopwords


# In[14]:


df=pd.read_csv('Twitter_Data.csv',encoding='utf-8',header=None)


# In[15]:


df


# In[16]:


df[1].value_counts()


# In[17]:


df.columns={"chat","sentiment"}


# In[18]:


df


# In[19]:


df['sentiment'].value_counts()


# In[20]:


df['word_counts']=df['chat'].apply(lambda x:len(str(x).split()))


# In[21]:


df


# In[22]:


df['word_counts'].max()


# In[23]:


df['word_counts'].min()


# In[24]:


df[df['word_counts']==5]


# In[25]:


def char_counts(x):
    s=x.split()
    x=''.join(s)
    return  len(x)


# In[26]:


char_counts('uday')


# In[231]:


df['char_counts']=df['sentiment'].apply(lambda x:char_counts(str(x)))


# In[232]:


df


# In[233]:


df['char_counts'].max()


# In[234]:


df['Average_word']=df['char_counts']/df['word_counts']


# In[235]:


df


# In[237]:


df['sentiment'] = df['sentiment'].astype(str)


# In[238]:


df['stop_words_lenth']=df['chat'].apply(lambda x:len([t for t in x if t in stopwords]))


# In[239]:


df


# In[240]:


df['numeric_count']=df['sentiment'].apply(lambda x:( len([t for t in x if t.isdigit()])))


# In[241]:


df


# In[244]:


df['Upper_case_count']=df['sentiment'].apply(lambda x:len([t for t in x.split() if t.isupper()]))


# In[245]:


df.head()


# In[246]:


contractions={
    "ain't": "am not",
  "aren't": "are not",
  "can't": "cannot",
  "can't've": "cannot have",
  "'cause": "because",
  "could've": "could have",
  "couldn't": "could not",
  "couldn't've": "could not have",
  "didn't": "did not",
  "doesn't": "does not",
  "don't": "do not",
  "hadn't": "had not",
  "hadn't've": "had not have",
  "hasn't": "has not",
  "haven't": "have not",
  "he'd": "he would",
  "he'd've": "he would have",
  "he'll": "he will",
  "he'll've": "he will have",
  "he's": "he is",
  "how'd": "how did",
  "how'd'y": "how do you",
  "how'll": "how will",
  "how's": "how is",
  "I'd": "I would",
  "I'd've": "I would have",
  "I'll": "I will",
  "I'll've": "I will have",
  "I'm": "I am",
  "I've": "I have",
  "isn't": "is not",
  "it'd": "it had",
  "it'd've": "it would have",
  "it'll": "it will",
  "it'll've": "it will have",
  "it's": "it is",
  "let's": "let us",
  "ma'am": "madam",
  "mayn't": "may not",
  "might've": "might have",
  "mightn't": "might not",
  "mightn't've": "might not have",
  "must've": "must have",
  "mustn't": "must not",
  "mustn't've": "must not have",
  "needn't": "need not",
  "needn't've": "need not have",
  "o'clock": "of the clock",
  "oughtn't": "ought not",
  "oughtn't've": "ought not have",
  "shan't": "shall not",
  "sha'n't": "shall not",
  "shan't've": "shall not have",
  "she'd": "she would",
  "she'd've": "she would have",
  "she'll": "she will",
  "she'll've": "she will have",
  "she's": "she is",
  "should've": "should have",
  "shouldn't": "should not",
  "shouldn't've": "should not have",
  "so've": "so have",
  "so's": "so is",
  "that'd": "that would",
  "that'd've": "that would have",
  "that's": "that is",
  "there'd": "there had",
  "there'd've": "there would have",
  "there's": "there is",
  "they'd": "they would",
  "they'd've": "they would have",
  "they'll": "they will",
  "they'll've": "they will have",
  "they're": "they are",
  "they've": "they have",
  "to've": "to have",
  "wasn't": "was not",
  "we'd": "we had",
  "we'd've": "we would have",
  "we'll": "we will",
  "we'll've": "we will have",
  "we're": "we are",
  "we've": "we have",
  "weren't": "were not",
  "what'll": "what will",
  "what'll've": "what will have",
  "what're": "what are",
  "what's": "what is",
  "what've": "what have",
  "when's": "when is",
  "when've": "when have",
  "where'd": "where did",
  "where's": "where is",
  "where've": "where have",
  "who'll": "who will",
  "who'll've": "who will have",
  "who's": "who is",
  "who've": "who have",
  "why's": "why is",
  "why've": "why have",
  "will've": "will have",
  "won't": "will not",
  "won't've": "will not have",
  "would've": "would have",
  "wouldn't": "would not",
  "wouldn't've": "would not have",
  "y'all": "you all",
  "y'alls": "you alls",
  "y'all'd": "you all would",
  "y'all'd've": "you all would have",
  "y'all're": "you all are",
  "y'all've": "you all have",
  "you'd": "you had",
  "you'd've": "you would have",
  "you'll": "you you will",
  "you'll've": "you you will have",
  "you're": "you are",
  "you've": "you have",
    "i'll":"i will"
}


# In[247]:


contractions


# In[248]:


text2="i didn't shouldn't i'll won't"


# In[249]:


def cont_to_exp(text2):
    for key in contractions:
        value=contractions[key]
        text2=text2.replace(key,value)
    return text2
    
    


# In[250]:


cont_to_exp(text2)


# In[252]:


get_ipython().run_cell_magic('timeit', '', "df['chat']=df['sentiment'].apply(lambda x:cont_to_exp(x))\n")


# In[253]:


df


# In[254]:


df.tail()


# In[255]:


df[df['sentiment'].str.contains('a')]


# In[256]:


import re


# In[257]:


x='@udaykiran12345 #####fhvdnjfnvdfv .....'


# In[258]:


re.sub(r'[^\w ]+',"",x)


# In[ ]:





# In[51]:


x="UDay     is   kiran"


# In[52]:


' '.join(x.split())


# In[261]:


df['sentiment'].apply(lambda x:''.join(x.split()))


# In[262]:


df


# In[57]:


columns=0


# In[61]:


from bs4 import BeautifulSoup


# In[ ]:


x='<html>UDay kiran</html>'


# In[66]:


BeautifulSoup(x,'lxml').get_text() 


# In[67]:


' '.join(x.split())


# ## Removing Accented Chars

# In[68]:


x='Accented Chars'


# In[70]:


import unicodedata


# In[72]:


def remove_accented_chars(x):
    x=unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode('utf-8','ignore')
    return x


# In[73]:


remove_accented_chars(x)


# In[74]:


import spacy


# In[75]:


nlp=spacy.load('en_core_web_sm')


# In[81]:


doc=nlp("hello ia am uday is there anyhting u want to know")


# In[114]:


for token in doc:
    
    print(token.text,token.lemma_,token.dep_,token.pos_,token.tag_)


# In[146]:


x="to this is the is the onlw way to "


# In[263]:


text=''.join(df['sentiment'])


# In[264]:


len(text)


# In[265]:


text=text.split()


# In[266]:


text=(df['sentiment'])


# In[267]:


frq_comm=pd.Series(text).value_counts()


# In[268]:


f20=frq_comm


# In[269]:


f20[5:20:1]


# In[270]:


df['sentiment']=df['sentiment'].astype(str)

df['stop_words_lenth']=df['sentiment'].apply(lambda x:len([t for t in x if t in stopwords]))


# In[272]:


df


# In[273]:


df['stop_words_lenth']


# In[1]:


get_ipython().system('pip install wordcloud')


# In[19]:


from wordcloud import WordCloud


# In[20]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


text='INDIA is my country i am ready to die'*300


# In[22]:


len(text)


# In[23]:


wc=WordCloud(width=800,height=800).generate(text)
plt.imshow(wc)
plt.axis('off')
plt.show()


# In[16]:


get_ipython().system('pip install -U textblob')


# In[24]:


get_ipython().system('python -m textblob.download_corpora')


# In[125]:


get_ipython().system('pip install textblob langdetect')

from textblob import TextBlob


# In[126]:


x='i was plyings in gardan'


# In[127]:


x=TextBlob(x).correct()


# In[128]:


x


# ## Tokenization Using Textblob

# In[129]:


Text='thanks for watching the video '


# In[130]:


TextBlob(Text).words


# In[131]:


nlp=spacy.load('en_core_web_sm')
doc=nlp(Text)
for token in doc:
    print(token)


# In[132]:


x='the prime minister of india is  Narendra Modi .he is in power for almost 10 yeras'


# In[133]:


doc=nlp(x)


# In[134]:


for noun in doc.noun_chunks:
    print(noun)


# In[135]:


TextBlob(x).words


# In[140]:


TextBlob(x).detect_language()


# In[137]:


tb.


# In[138]:


tb.translate(to='fr')


# In[141]:


from textblob import TextBlob

text = "Your text here"
blob = TextBlob(text)

try:
    language = blob.detect_language()
    print(language)
except AttributeError:
    print("TextBlob object does not have attribute 'detect_language'.")


# In[148]:


get_ipython().system('pip install --upgrade textblob')


# In[152]:


TextBlob(x)


# In[157]:


from langdetect import detect


# In[155]:


lang=detect(x)


# In[156]:


lang


# In[158]:


get_ipython().system('pip install translation')


# In[165]:


get_ipython().system('pip install textblob googletrans==4.0.0-rc1')


# In[166]:


from textblob import TextBlob

text = "Hello, how are you?"
blob = TextBlob(text)

# Detect the language of the text
detected_language = blob.detect_language()
print(f"Detected language: {detected_language}")

# Translate the text to another language (e.g., Spanish)
translated_blob = blob.translate(to='es')
print(f"Translated text: {translated_blob}")


# In[168]:


get_ipython().system('pip install translate')


# In[169]:


from translate import Translator


# In[193]:


lang=Translator(to_lang='tam')


# In[194]:


langu=lang.translate(x)



# In[195]:


langu


# In[196]:


from textblob.sentiments import NaiveBayesAnalyzer


# In[200]:


x="i am happy to kill u "


# In[201]:


tb=TextBlob(x,analyzer=NaiveBayesAnalyzer())


# In[202]:


tb.sentiment


# In[ ]:




