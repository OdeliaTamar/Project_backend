import openai

from flask import Flask
import flask.cli

app = Flask(__name__)
openai.api_key = 'your_openai_api_key'
