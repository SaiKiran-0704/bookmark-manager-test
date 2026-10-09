from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import or_

db = SQLAlchemy()


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def search_by_query(cls, query):
        if not query:
            return cls.query_all()
        search_filter = f"%{query}%"
        return cls.query.filter(
            or_(
                cls.title.ilike(search_filter),
                cls.url.ilike(search_filter)
            )
        ).all()

    @classmethod
    def query_all(cls):
        return cls.query.all()
