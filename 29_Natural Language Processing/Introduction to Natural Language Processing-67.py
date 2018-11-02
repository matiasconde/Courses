## 2. Overview of the Data ##

import pandas as pd
submissions = pd.read_csv("sel_hn_stories.csv")
submissions.columns = ["submission_time", "upvotes", "url", "headline"]
submissions = submissions.dropna()

print(submissions["headline"].head())


## 3. Tokenizing the Headlines ##

tokenized_headlines = []

for item in submissions["headline"]:
    tokens_row = item.split()
    tokenized_headlines.append(tokens_row)
    
    

## 4. Preprocessing Tokens to Increase Accuracy ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []

for sentence in tokenized_headlines: 
    clean_sentence = []
    for token in sentence: 
        lower_token = token.lower()
        for item in punctuation: 
            if item in lower_token:
                lower_token = lower_token.replace(item,"")
        clean_sentence.append(lower_token)
    clean_tokenized.append(clean_sentence)

## 5. Assembling a Matrix of Unique Words ##

import numpy as np
import pandas as pd
unique_tokens = []
single_tokens = []

count_words = {}

for sentence in clean_tokenized: 
    for word in sentence: 
        if word not in count_words:
            count_words[word] = 1
        else: count_words[word] += 1

for k,v in count_words.items():
    if v==1: single_tokens.append(k)

for sentence in clean_tokenized: 
    for word in sentence: 
        if word not in unique_tokens and word not in single_tokens:
            unique_tokens.append(word)
        
counts = pd.DataFrame(0,index=np.arange(len(clean_tokenized)),columns = unique_tokens)
           
            

## 6. Counting Token Occurrences ##

# We've already loaded in clean_tokenized and counts

for i,sentence in enumerate(clean_tokenized):
    for word in sentence:
        if word in counts.columns:
             counts.loc[i,word] += 1
        

## 7. Removing Columns to Increase Accuracy ##

# We've already loaded in clean_tokenized and 

word_counts = counts.sum(axis=0)

filter_words = (5<=word_counts)&(word_counts<=100)

counts = counts.loc[:,filter_words]

## 8. Splitting the Data Into Train and Test Sets ##

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(counts, submissions["upvotes"], test_size=0.2, random_state=1)

## 9. Making Predictions With fit() ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()

clf.fit(X_train,y_train)

predictions = clf.predict(X_test)

## 10. Calculating Prediction Error ##

print(predictions)
  
squares = [(predictions[i] - v)**2 for i,v in enumerate(y_test)]
    
mse = sum(squares) / len(y_test)