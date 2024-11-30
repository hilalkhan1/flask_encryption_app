from flask import Flask, render_template, request
from encryption import EncryptionAlgorithms

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        algorithm = request.form["algorithm"]
        action = request.form["action"]
        text = request.form.get("text", "")  # Default to an empty string if not provided
        shift = request.form.get("shift", "")
        key = request.form.get("key", "")

        result = ""
        try:
            if algorithm == "ROT-13":
                result = EncryptionAlgorithms.rot13_encrypt_decrypt(text)

            elif algorithm == "Caesar":
                shift = int(shift) if shift else 0
                if action == "Encrypt":
                    result = EncryptionAlgorithms.caesar_encrypt(text, shift)
                elif action == "Decrypt":
                    result = EncryptionAlgorithms.caesar_decrypt(text, shift)

            elif algorithm == "Columnar":
                if action == "Encrypt":
                    result = EncryptionAlgorithms.columnar_encrypt(text, key)
                elif action == "Decrypt":
                    result = EncryptionAlgorithms.columnar_decrypt(text, key)

        except Exception as e:
            result = f"Error: {str(e)}"

        return render_template("index.html", result=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)