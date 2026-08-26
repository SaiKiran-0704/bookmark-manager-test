from flask import Flask, render_template, request, redirect
from models import db, Bookmark

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookmarks.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    search_query = request.args.get("q", "").strip()
    if search_query:
        bookmarks = Bookmark.query.filter(
            Bookmark.title.ilike(f"%{search_query}%") | Bookmark.url.ilike(f"%{search_query}%")
        ).order_by(Bookmark.created_at.desc()).all()
    else:
        bookmarks = Bookmark.query.order_by(Bookmark.created_at.desc()).all()
    return render_template("index.html", bookmarks=bookmarks, search_query=search_query)


@app.route("/add", methods=["POST"])
def add_bookmark():
    title = request.form.get("title")
    url = request.form.get("url")
    if title and url:
        db.session.add(Bookmark(title=title, url=url))
        db.session.commit()
    return redirect("/")


@app.route("/delete/<int:bookmark_id>", methods=["POST"])
def delete_bookmark(bookmark_id):
    bookmark = Bookmark.query.get(bookmark_id)
    if bookmark:
        db.session.delete(bookmark)
        db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
