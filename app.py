from flask import Flask, render_template, request
from snippet_finder import load_snippets, search
import os

app = Flask(__name__)

docs = load_snippets()

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    query = ""

    if request.method == "POST":
        query = request.form["query"]
        ranked = search(query, docs)

        for name, score in ranked:
            if score > 0:
                filepath = os.path.join("code_snippets", name)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                results.append({
                    "name": name,
                    "score": score,
                    "content": content
                })

    return render_template("index.html", results=results, query=query)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)