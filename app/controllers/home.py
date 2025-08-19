from app import app, db
from flask import Flask, render_template, redirect
from sqlalchemy.exc import IntegrityError

@app.route("/")
def home():
    return render_template('index.html')