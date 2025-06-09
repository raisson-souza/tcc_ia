from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def download_file(file_name):
    try:
        return send_from_directory(BASE_PATH, f"./files/{ file_name }", as_attachment=True)
    except FileNotFoundError:
        return {"error": "Arquivo não encontrado."}, 404

@app.route("/download/freud", methods=["GET"])
def download_freud():
    return download_file("freud.pdf")

@app.route("/download/change", methods=["GET"])
def download_change():
    return download_file("change.pdf")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
