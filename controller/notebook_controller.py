from controller import app, AlchemyEncoder
from flask import request, render_template, redirect, url_for
from model import db
from model.note import Note
from model.notebook import Notebook
import json

@app.route("/notebook/<notebook_id>", methods=["GET"])
def view__single_notebook(notebook_id):
    notebook = db.session.query(Note).filter(Note.notebook_id == notebook_id).first()
    notebook_title = db.session.query(Notebook).filter(Notebook.id == notebook_id).first()
    return render_template("notebook.html", title=notebook_title.title, notebook = notebook, current_notebook = notebook_title)


@app.route("/notebook", methods=["POST"])
def add_notebook():
    notebook_data = request.form
    notebook = Notebook(**notebook_data)
    db.session.add(notebook)
    db.session.commit()
    return redirect( url_for ( "get_notebooks" ) ) 