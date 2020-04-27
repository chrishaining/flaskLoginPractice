from project import app

from flask import render_template, redirect, request


@app.route('/')
def index():
    return("Hello world")
