# L!BRARY
This is Library Management Project.
This Project was a great help for building my skills around web development. 
In every single step I went through this project I got to learn something new.
---
___
This project uses flask with SQLAlchemy for backend and Bootstrap for styling.
For making this project work. You have to follow to simple steps.

```
pip install flask

pip install sqlalchemy
```
The Library Management System can be used only by Librarian. This system allows:
* CRUD Operations on Books and members.
* Book has status flags as _issued_ or _not issued_.
* Members has status _Book Assigned_ and _Book Not Assigned_.
* Member cannot have outstanding debt of more than INR 500.
* System Records Trasactions with _issued date_ and _Returned Date_ with _book id_ and _member id_ involved.
* There is payments page as well which is simple page without any online integration.
* Librarian Can Import books from Api in page import_books.html.
___
Landing Page of application is Book List Page.

Book
![BookListPage](https://user-images.githubusercontent.com/108964197/180740596-c75575f0-b231-4ad4-8f9e-de98d06de949.png)

___
When clicked on Add New Book below form will be shown.
Add New Book
![Add New Book Form](https://user-images.githubusercontent.com/108964197/180740667-6fb6c421-272c-4641-a3e1-c7f873387a25.png)

___
After Clicking on issue this book user will visit below page.
Member Confirmation
![Member Confirmation Page](https://user-images.githubusercontent.com/108964197/180740853-c88d86a8-3b2c-48be-8952-a424d4105196.png)
___
Issued Books
![Issued books](https://user-images.githubusercontent.com/108964197/180740935-83b1c9d5-1b12-4b1f-9f7e-37f8091184a7.png)
___
After Clicking on Return This book user will visit below page.
Book Return Confirmation
![Book Return Confirmation](https://user-images.githubusercontent.com/108964197/180741011-b15dab9f-6cb3-497c-8f04-40881a3054a0.png)
___
On returning Trasactions page will be updated.
Trasaction page already has transaction when it was issued. On returning the book this trasaction will update returned date from none to present value.
![TransactionsPage](https://user-images.githubusercontent.com/108964197/180741092-92dda015-033d-49e1-aedf-43e67ca7956e.png)
___
Members Page
![Memberspage](https://user-images.githubusercontent.com/108964197/180741136-6e8fc51e-c477-4aca-8673-0010df26c3da.png)

___
Add New Member
![Add New Member](https://user-images.githubusercontent.com/108964197/180741195-da0d2fca-2d82-47f6-be89-1ed006b4349a.png)

___
Payment Page
Only members having debt will be shown here.
![Payment Page](https://user-images.githubusercontent.com/108964197/180741259-4f2d531c-a967-4c91-be69-63c3aa62347e.png)
___
Pay Page
![Payform](https://user-images.githubusercontent.com/108964197/180741759-8a43cec7-a8ed-4522-b293-f1d0c957d603.png)

___
Import Book Page
This page import books into system with API use.
![Screenshot 2022-07-25 145049](https://user-images.githubusercontent.com/108964197/180743086-9c65a85d-79fc-493a-b270-1fc19fc40333.png)

___

Member are charged on Per day basis. There is no Membership fee.
Member Can have on one book at a time.
For Each day member has a book he will be charged on per day INR 8 basis.
And He will charge on return. Member cannot have debt of more than INR 500 if he wants a book.




