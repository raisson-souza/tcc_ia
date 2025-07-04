from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def download_file(file_name):
    try:
        return send_from_directory(BASE_PATH, f"./files/{ file_name }", as_attachment=True)
    except FileNotFoundError:
        return {"error": "Arquivo não encontrado."}, 404

# A INTERPRETAÇÃO DOS SONHOS
@app.route("/download/sonhos", methods=["GET"])
def download_freud():
    return download_file("freud.pdf")

# PSICANÁLISE
@app.route("/download/psicanalise", methods=["GET"])
def download_psicanalise():
    return download_file("psicanalise.pdf")

# ONTOPSICOLOGIA
@app.route("/download/ontopsicologia", methods=["GET"])
def download_ontopsicologia():
    return download_file("ontopsicologia.pdf")

# MISTA
@app.route("/download/mista", methods=["GET"])
def download_mista():
    return download_file("mista.pdf")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
