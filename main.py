from flask import Flask, send_from_directory
import os

app = Flask(__name__)

PDF_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_FILENAME = "./doc.pdf"

@app.route("/download", methods=["GET"])
def download_pdf():
    try:
        return send_from_directory(PDF_DIR, PDF_FILENAME, as_attachment=True)
    except FileNotFoundError:
        return {"error": "Arquivo não encontrado."}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
