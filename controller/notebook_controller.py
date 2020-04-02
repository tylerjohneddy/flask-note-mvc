from controller import app, AlchemyEncoder
from flask import request, render_template, redirect, url_for
from model import db
from model.note import Note
import json

@app.route("/notebook/<notebook_id>", methods=["GET"])
def view__single_notebook(notebook_id):
    notebook = db.session.query(Notebook).filter(Note.notebook_id == notebook_id).first()
    return render_template("notebook.html", title=notebook.text, notebook = notebook)