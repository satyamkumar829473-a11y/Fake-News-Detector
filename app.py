from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Load dataset
data = pd.read_csv("news.csv")

X = data["text"]
y = data["label"]

vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vector, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    news = request.form['news']

    news_vector = vectorizer.transform([news])

    prediction = model.predict(news_vector)[0]
    probabilities = model.predict_proba(news_vector)[0]
    confidence = max(probabilities) * 100

    if confidence < 60:
         return render_template('index.html',prediction="No news available" ,confidence=round(confidence,2))

    return render_template(
        'index.html',
        prediction=prediction,
        confidence=round(confidence, 2)
    )

if __name__ == '__main__':
    app.run(debug=True)