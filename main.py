from flask import Flask, request 
from flask_cors import CORS  # Import CORS
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("BazaDanych.csv", sep=";")

features = ["jezyk interpretowany", "aplikacje www", "UI", "latwy poczatek", "popularny jezyk", "przetwarzanie danych", "akademicko", "zarzadzanie systemem", "dedykowanie srodowiska", "lubisz Oracle", "aplikacje na telefon", "tylko dla IOS", "google bardziej niż microsoft", "desktop", "UI", "czy gry", "duże produkcje", "zależy ci na wydajnosci", "na mikrokontrolery", "nowe technologie"]
X = df[features]
y = df['wynik']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

app = Flask(__name__) 
CORS(app)  # Włącz CORS dla wszystkich endpointów

@app.route('/lang', methods=['GET', 'POST']) 
def helloworld(): 
    if request.method == 'GET': 
        return dtree.predict([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]).tolist()
    if request.method == 'POST': 
        # Wczytanie danych z requestu i konwersja na listę
        data = request.get_json()  # Pobierz dane JSON
        return dtree.predict([data]).tolist()

if __name__ == '__main__': 
    app.run(debug=True) 
