from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def search_by_title(cls, query):
        if not query:
            return cls.query.all()
        return cls.query.filter(cls.title.ilike(f"%{query}%")).all()
