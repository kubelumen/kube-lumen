from flask import Flask, jsonify

app = Flask(name)

@app.route("/health")
def health():
return jsonify({
"project": "KubeLumen",
"status": "skeleton-ready"
})

if name == "main":
app.run(host="0.0.0.0", port=5000)
