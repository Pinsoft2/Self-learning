from flask import Flask, render_template
import pandas as pd

app = Flask("Day28 Dictionary")

@app.route("/")
def home():
    return render_template("home.html")

df = pd.read_csv("venv/dictionary.csv")
@app.route("/api/v1/<word>")
def translate(word):
    definition = df.loc[df["word"]==word]["definition"].squeeze().replace("\n","")
    return {"word": word,
            "definition": definition}

if __name__ == "__main__":
    app.run(debug=True)