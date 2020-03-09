from db import db
class LibraryModel(db.Model):
    __tablename__ = 'library'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    available = db.Column(db.String(10))


    def __init__(self, name, available):
        self.name = name
        self.available = available


    def json(self):
        return {'name':self.name, 'available':self.available}

    @classmethod
    def find_by_name(cls, name):
        return LibraryModel.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=? Limit=1

    def save_to_db(self):
        db.session.add(self)  # SQLAlchemy
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
