from flask import Flask
from resume_quality_prediction.logger.log import logging

app= Flask(__name__)

@app.route('/', methods= ["GET", "POST"])
def index():
    logging.info("We are creating our log file")
    return "Hello World!"

if __name__=="__main__":
    app.run(debug= True)