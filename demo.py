from flask import Flask
from resume_quality_prediction.logger.log import logging
from resume_quality_prediction.exception import CustomException
import os, sys

app= Flask(__name__)

@app.route('/', methods= ["GET", "POST"])
def index():
    try:
        raise Exception ("We are raising our custom exception")
    except Exception as e:
        resume= CustomException(e, sys)
        logging.info(resume.error_message)
        logging.info("We are testing our log file")
        return "hello world"
    

if __name__=="__main__":
    app.run(debug= True)