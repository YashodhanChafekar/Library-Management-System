
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Book
from . import db

books = Blueprint('books', __name__)

# This route is for importing books from FRAPPE API.
@books.route('/import_books', methods=['GET','POST'])
def import_books():
    return render_template('import_books.html')

# This route is for books from DATABASE. This is also where user lands first.
@books.route('/', methods=['GET','POST'])
def book_list():
    if request.method == 'POST':
        search_input = request.form.get('search_input')
        data = []
        books = Book.query.all()
        for book in books :
            if search_input.lower() in book.name.lower() :
                data.append(book)
            elif search_input.lower() in book.author.lower() :
                data.append(book)
        return render_template('book_list.html', data=data)

        

    data = Book.query.all()
    return render_template('book_list.html', data=data)

# This route is for book form.
@books.route('/book_form', methods=['GET', 'POST'])
def book_form():
    if request.method == 'POST':
        name = request.form.get('book_name')
        isbn = request.form.get('book_isbn')
        author = request.form.get('book_author')
        publisher = request.form.get('book_publisher')

        new_book = Book(name=name, isbn=isbn, author=author, publisher=publisher)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('books.book_list'))
    return render_template('book_form.html')

@books.route('/delete-book/<int:id>', methods=['POST'])
def delete_book(id):
    if request.method == 'POST':
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()

        return redirect('/')

@books.route('/confirm_book_delete/<int:id>', methods=['GET','POST'])
def confirm_delete(id):
    book = Book.query.get(id)
    data = book
    return render_template('confirm_book_delete.html', data=data)


@books.route('/update_book/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    if request.method=='POST':
        book = Book.query.get(id)
        name = request.form.get('book_name')
        isbn = request.form.get('book_isbn')
        author = request.form.get('book_author')
        publisher = request.form.get('book_publisher')

        book.query.filter_by(id=id).update(dict(name=name))
        book.query.filter_by(id=id).update(dict(isbn=isbn))
        book.query.filter_by(id=id).update(dict(author=author))
        book.query.filter_by(id=id).update(dict(publisher=publisher))
        db.session.commit()
        return redirect('/')

    book = Book.query.get(id)
    return render_template('book_update_form.html', data=book)






# This route is for issued books.
@books.route('/issued_books', methods=['GET','POST'])
def issued_books():
    return render_template('issued_books.html')

# This route is for returned books.
@books.route('/returned_books', methods=['GET','POST'])
def returned_books():
    return render_template('returned_books.html') 