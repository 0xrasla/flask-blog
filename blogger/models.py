from blogger import db


class Blog(db.Document):
    title = db.StringField()
    content = db.StringField()
    author = db.StringField()

    def to_json(self):
        return {"title": self.title, "author": self.author, "content": self.content}
