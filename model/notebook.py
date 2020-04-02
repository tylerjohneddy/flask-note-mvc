from model import db


class Notebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    notes = db.relationship("Note", cascade="all,delete", back_populates="notebook")