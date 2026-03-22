from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "logs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    
    if request.method == "POST":
        file = request.files["logfile"]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        error = warning = info = 0

        with open(filepath, "r") as f:
            for line in f:
                if "ERROR" in line:
                    error += 1
                elif "WARNING" in line:
                    warning += 1
                elif "INFO" in line:
                    info += 1

        result = {
            "ERROR": error,
            "WARNING": warning,
            "INFO": info
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
