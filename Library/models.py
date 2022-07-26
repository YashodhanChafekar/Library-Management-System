
from . import db
from sqlalchemy.sql import func

class Trasaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'),
        nullable=False)
    book = db.relationship('Book')  
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'),
        nullable=False)
    member = db.relationship('Member')
    returned = db.Column(db.Boolean, default=False )
    returned_date = db.Column(db.DateTime(timezone=True))
    isuued_date = db.Column(db.DateTime(timezone=True), default=func.now())



class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    isbn = db.Column(db.String(20))
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
    issued = db.Column(db.Boolean, default=False )
    

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(13))
    debt = db.Column(db.Integer)
    has_book = db.Column(db.Boolean, default=False )
    #isuued_date = db.Column(db.DateTime(timezone=True), default=func.now())

class BookRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100))
    book_isbn = db.Column(db.String(100))
    count = db.Column(db.Integer)
