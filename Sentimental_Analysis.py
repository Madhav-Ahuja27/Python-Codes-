from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
import numpy as np

# docs = ['the',
#  'and',
#  'you',
#  'for',
#  'have',
#  'that',
#  "i'm",
#  'just',
#  'but',
#  'with',
#  'was',
#  'not',
#  'this',
#  'get',
#  'good',
#  'like',
#  'are',
#  'all',
#  'out',
#  'your']
# sentiments = {
#     'the': 'Neutral',
#     'and': 'Neutral',
#     'you': 'Neutral',
#     'for': 'Neutral',
#     'have': 'Neutral',
#     'that': 'Neutral',
#     "i'm": 'Neutral',
#     'just': 'Neutral',
#     'but': 'Neutral',
#     'with': 'Neutral',
#     'was': 'Neutral',
#     'not': 'Negative',
#     'this': 'Neutral',
#     'get': 'Neutral',
#     'good': 'Positive',
#     'like': 'Positive',
#     'are': 'Neutral',
#     'all': 'Neutral',
#     'out': 'Neutral',
#     'your': 'Neutral'
# }


docs = ['the', 'and', 'you', 'for', 'have', 'that', "i'm", 'just', 'but', 'with', 'was', 'not', 'this', 'get', 'good', 'like', 'are', 'all', 'out', 'your']

additional_words = ['excellent', 'amazing', 'awesome', 'hate', 'dislike', 'awful', 'horrible', 'love', 'fantastic']
additional_sentiments = ['Positive', 'Positive', 'Positive', 'Negative', 'Negative', 'Negative', 'Negative', 'Positive', 'Positive']

all_words = docs + additional_words

all_sentiments = {
    'the': 'Neutral',
    'and': 'Neutral',
    'you': 'Neutral',
    'for': 'Neutral',
    'have': 'Neutral',
    'that': 'Neutral',
    "i'm": 'Neutral',
    'just': 'Neutral',
    'but': 'Neutral',
    'with': 'Neutral',
    'was': 'Neutral',
    'not': 'Negative',
    'this': 'Neutral',
    'get': 'Neutral',
    'good': 'Positive',
    'like': 'Positive',
    'are': 'Neutral',
    'all': 'Neutral',
    'out': 'Neutral',
    'your': 'Neutral',
    'excellent': 'Positive',
    'amazing': 'Positive',
    'awesome': 'Positive',
    'hate': 'Negative',
    'dislike': 'Negative',
    'awful': 'Negative',
    'horrible': 'Negative',
    'love': 'Positive',
    'fantastic': 'Positive'
}


all_labels = np.array([2 if all_sentiments[word] == 'Positive' else 0 if all_sentiments[word] == 'Negative' else 1 for word in all_words])



# labels = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1])
# labels = np.array([1 if sentiments[word] == 'Positive' else 0 if sentiments[word] == 'Negative' else 2 for word in docs])

tokenizer = Tokenizer()
tokenizer.fit_on_texts(docs)
sequences = tokenizer.texts_to_sequences(docs)
sequences = pad_sequences(sequences, padding='post')

model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=100, input_length=sequences.shape[1]))
model.add(Bidirectional(LSTM(64, return_sequences=True)))
model.add(Bidirectional(LSTM(32)))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))


model.add(Dense(3, activation='softmax'))

model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(sequences, all_labels, epochs=10, batch_size=32, validation_split=0.2)

print("Chatbot: Hi there! I'm a sentiment analysis chatbot.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    user_seq = tokenizer.texts_to_sequences([user_input])
    user_seq = pad_sequences(user_seq, padding='post', maxlen=sequences.shape[1])

    prediction = model.predict(user_seq)
    sentiment = np.argmax(prediction)

    sentiment_labels = {0: 'Negative', 1: 'Neutral' , 2: 'Positive'}

    print(f"Chatbot: You seem {sentiment_labels[sentiment]}")
