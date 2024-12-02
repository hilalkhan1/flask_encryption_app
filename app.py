from flask import Flask, render_template, request
from encryption import EncryptionAlgorithms

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    text = ""
    shift = ""
    key = ""
    action = "Encrypt"  # Default action

    if request.method == "POST":
        algorithm = request.form["algorithm"]
        action = request.form["action"]
        text = request.form.get("text", "")
        shift = request.form.get("shift", "")
        key = request.form.get("key", "")

        try:
            if algorithm == "ROT-13":
                result = EncryptionAlgorithms.rot13(text)

            elif algorithm == "Caesar":
                shift = int(shift) if shift else 0
                if action == "Encrypt":
                    result = EncryptionAlgorithms.caesar_encrypt(text, shift)
                else:
                    result = EncryptionAlgorithms.caesar_decrypt(text, shift)

            elif algorithm == "Columnar":
                if action == "Encrypt":
                    result = EncryptionAlgorithms.columnar_encrypt(text, key)
                else:
                    result = EncryptionAlgorithms.columnar_decrypt(text, key)

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template(
        "index.html",
        result=result,
        text=text,
        shift=shift,
        key=key,
        action=action
    )

if __name__ == "__main__":
    app.run(debug=True)
