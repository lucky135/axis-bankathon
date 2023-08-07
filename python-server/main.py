from flask import Flask
from flask_restx import Api
from app.read_resume.routes import readResumeNS
from app.improve_jd.routes import improveJdNS

app=Flask(__name__)
api = Api(app)

api.add_namespace(readResumeNS)
api.add_namespace(improveJdNS)


if __name__=='__main__':
    app.run(debug=True, port=8887)