
from flask import Blueprint, render_template, request, flash, redirect, url_for
import requests
import json
from .models import Book, Member, Transaction, BookRecord
from . import db
import datetime
from datetime import date

books = Blueprint('books', __name__)

# This route is for importing books from FRAPPE API.
@books.route('/import_books', methods=['GET','POST'])
def import_books():
    if request.method == "POST":
        book_info = request.form.get('book_info')
        book_info = json.loads(book_info)
    
        for i in range(int(book_info['count'])):
            new_book = Book(name=book_info['book_title'], isbn=book_info['book_isbn'], author=book_info['book_author'], publisher=book_info['book_publisher'])
            db.session.add(new_book)
            db.session.commit()
        return {'title': book_info['book_title'], 'count': book_info['count']}
    else:
        req = requests.get("https://frappe.io/api/method/frappe-library")
        data = req.json()
        return render_template('import_books.html', data=data['message'])


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
            elif search_input.lower() in book.author.lower():
                data.append(book)
        return render_template('book_list.html', data=data)
    data = Book.query.all()
    return render_template('book_list.html',data=data)


# This route is for book form.
@books.route('/book_form', methods=['GET', 'POST'])
def book_form():
    if request.method == 'POST':
        name = request.form.get('book_name')
        isbn = request.form.get('book_isbn')
        author = request.form.get('book_author')
        publisher = request.form.get('book_publisher')
        """ pages = request.form.get('book_pages') """
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
@books.route('/issued_book/', methods=['GET','POST'])
def issued_books():
    if request.method == 'POST':
        search_input = request.form.get('search_input')
        data = []
        members =[]
        book=[]
        books = Book.query.all()
        for i in books:
            if i.issued:
                book.append(i)
        for book in book :
            if search_input.lower() in book.name.lower() :
                data.append(book)
            elif search_input.lower() in book.author.lower():
                data.append(book)
            print(data)
        for i in data:
                if i:
                    id = i.id
                    transaction = Transaction.query.filter_by(book_id=id).first()
                    member = transaction.member_id
                    m = Member.query.get(member)
                    members.append(m.fullname)
        data = (data,members)
        return render_template('issued_books.html', data=data)
    members = []
    books=[]
    book = Book.query.all()
    for i in book:
        if i.issued:
            books.append(i)
    for i in books:
        id = i.id
        transaction = Transaction.query.filter_by(book_id=id, returned_date=None).first()
        member = transaction.member_id
        m = Member.query.get(member)
        if m:
            members.append(m.fullname)
        else:
            members.append("NA")
    data = (books,members)
    return render_template('issued_books.html',data=data)

@books.route('/issue_this_book/<int:id>', methods=['GET','POST'])
def issue_this_book(id):
    book_id = id
    member = Member.query.all()
    data = (member, book_id)
    return render_template('issue_this_book.html', data=data)

    
# This route is for returned books.
@books.route('/confirm_return/<int:book_id>/', methods=['GET','POST'])
def confirm_return(book_id):
    if request.method == "POST":
        book_issue_state_flase(book_id)
        member_has_book_false(book_id)
        update_member_debt(book_id)
        return redirect(url_for('books.get_transaction'))
    
    book = Book.query.get(book_id)
    data = book
    return render_template('confirm_return.html',data=data) 


@books.route('/Transaction', methods=['GET','POST'])
def get_transaction():
    transaction = Transaction.query.all()
    data = transaction
    members=[]
    books=[]
    for j in transaction:
        book = Book.query.get(j.book_id)
        if book:
            books.append(book.name)
        else:
            books.append('NA')
    for i in transaction:
        member = Member.query.get(i.member_id)
        if member:
            members.append(member.fullname)
        else:
            members.append('NA')
    data = (data,members,books)
            
    return render_template('transaction.html', data=data) 


def book_issue_state_flase(book_id):
    book = Book.query.get(book_id)
    state = False
    book.query.filter_by(id=book_id).update(dict(issued=state))
    db.session.commit()


def member_has_book_false(book_id):
    transaction = Transaction.query.all()
    transaction = Transaction.query.filter_by(book_id=book_id, returned_date=None).first()
    member_id = transaction.member_id
    Member.query.filter_by(id=member_id).update(dict(has_book=False))
    db.session.commit()

    
def update_member_debt(book_id):
    transaction = Transaction.query.filter_by(book_id=book_id, returned_date=None).first()
    returned_date = datetime.datetime.now()
    Transaction.query.filter_by(book_id=book_id).update(dict(returned_date=returned_date))
    db.session.commit()
    member_id = transaction.member_id
    y = transaction.returned_date
    x = transaction.isuued_date
    ans = (y-x).days
    ans = int(ans)
    member = Member.query.filter_by(id=member_id).first()
    if member:
        if member.debt == 0 and member is not None:
            pay = 8 + 8*ans
        elif member.debt and member is not None:
            pay = int(member.debt) + 8 + 8*ans
        member = Member.query.get(member_id)
        member.query.filter_by(id=member_id).update(dict(debt=pay))
        db.session.commit()
        