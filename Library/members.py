from flask import Flask
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Member,Book,Trasaction
from . import db
import datetime
members = Blueprint('members', __name__)


# This route is for members list. It lists all members.
@members.route('/member_list', methods=['GET', 'POST'])
def member_list( ):
    if request.method == 'POST':
        search_input = request.form.get('search_input')
        data = []
        members = Member.query.all()
        for member in members :
            if search_input.lower() in member.fullname.lower() :
                data.append(member)
        return render_template('member_list.html', data=data)

    data = Member.query.all()
    return render_template('member_list.html', data=data)

# This route will be used to add new member.
@members.route('/member_form', methods=['GET', 'POST'])
def member_form():
    if request.method == 'POST':
        fullname = request.form.get('member_fullname')
        email = request.form.get('member_email')
        phone = request.form.get('member_phone')

        if len(fullname) < 4:
            flash('Invalid Name! Name must have more than 4 characters.', category='error')
        elif ('@' not in email) and ('.com' not in email):
            flash('Invalid Email! Please Enter Valid Email.', category='error')
        
        
        else:
            new_member = Member(fullname=fullname, email=email, phone=phone)
            db.session.add(new_member)
            db.session.commit()
        return redirect(url_for('members.member_list'))
    return render_template('member_form.html')

# This route is for list of members with outstanding debts, ordered by most to least.
@members.route('/payments', methods=['GET', 'POST'])
def payments():
    if request.method == 'POST':
        search_input = request.form.get('search_input')
        data = []
        members = Member.query.all()
        for member in members :
            if search_input.lower() in member.fullname.lower() :
                data.append(member)
        return render_template('payments.html', data=data)
    data = Member.query.all()
    return render_template('payments.html',data=data)

@members.route('/confirm_payment/<int:id>', methods=['GET', 'POST'])
def confirm_payment(id):
    if request.method == "POST":
        amount = request.form.get('amount')
        member = Member.query.get(id)
        member = member.query.filter_by(id=id).first()
        pay = member.debt
        pay = pay - int(amount)
        member.query.filter_by(id=id).update(dict(debt=pay))
        db.session.commit()
        return redirect(url_for('members.payments'))
    data = Member.query.get(id)
    return render_template('confirm_payment.html', data=data)



@members.route('/confirm_delete/<int:id>', methods=['GET','POST'])
def confirm_delete(id):
    member = Member.query.get(id)
    data = member
    return render_template('confirm_delete.html', data=data)



@members.route('/delete-member/<int:id>', methods=['POST'])
def delete_member(id):
    if request.method == 'POST':
        member = Member.query.get(id)
        db.session.delete(member)
        db.session.commit()

        return redirect(url_for('members.member_list'))


@members.route('/update_member/<int:id>', methods=['GET', 'POST'])
def update_member(id):
    if request.method=='POST':
        member = Member.query.get(id)
        fullname = request.form.get('member_fullname')
        email = request.form.get('member_email')
        phone = request.form.get('member_phone')

        if len(fullname) < 4:
            flash('Invalid Name! Name must have more than 4 characters.', category='error')
        elif ('@' not in email) and ('.com' not in email):
            flash('Invalid Email! Please Enter Valid Email.', category='error')
        
        
        else:
            member.query.filter_by(id=id).update(dict(fullname=fullname))
            member.query.filter_by(id=id).update(dict(email=email))
            member.query.filter_by(id=id).update(dict(phone=phone))
            db.session.commit()
        return redirect(url_for('members.member_list'))

    member = Member.query.get(id)
    return render_template('member_update_form.html', data=member)
    
@members.route('/confirm_member/<int:member_id>/<int:book_id>', methods=['POST'])
def confirm_member(member_id, book_id):
    if request.method == 'POST':
        member = Member.query.get(member_id)
        member_state = True
        member.query.filter_by(id=member_id).update(dict(has_book=member_state))
        db.session.commit()
        book = Book.query.get(book_id)
        book_state = True
        book.query.filter_by(id=book_id).update(dict(issued=book_state))
        db.session.commit()
        member_id = member_id
        book_id = book_id
        isuued_date = datetime.datetime.now()
        returned_date = None
        new_transaction = Trasaction(book_id=book_id,member_id=member_id,isuued_date=isuued_date,returned_date=returned_date)
        db.session.add(new_transaction)
        db.session.commit()
        return redirect(url_for('books.issued_books'))