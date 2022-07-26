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


## Landing Page of application is List of Books in database.
![BookListPage](https://user-images.githubusercontent.com/108964197/181048121-6b7cc45e-d49d-404f-a9a1-589faffb2af9.png)
___
## When clicked on Add New Book below form will be shown.
## Add New Book
![Add New Book Form](https://user-images.githubusercontent.com/108964197/181046192-440a22c4-cb92-4b5b-a04d-fcecd42c5f7d.png)
___
## Update Book
![Update Book](https://user-images.githubusercontent.com/108964197/181046269-a50ad1a0-ed19-4e14-8f52-da385f92d45b.png)

___
## Confirm Book Delete
![Confirm Delete Book](https://user-images.githubusercontent.com/108964197/181047196-89e97c74-4ca5-474c-95e1-16b6c46fa69c.png)


___
## After Clicking on issue this book user will visit below page.
## Member Confirmation
![Member Confirmation Page](https://user-images.githubusercontent.com/108964197/181046363-2750ae33-ba07-42b1-8a6d-fb6a683cf80e.png)

___
## Issued Books will be shown on this Page.
![Issued books](https://user-images.githubusercontent.com/108964197/181046465-c9e20b47-f5d3-45c0-afee-3b9a2894f755.png)
___
## After Clicking on Return This book user will visit below page. Book Return Confirmation
![Confirm Return](https://user-images.githubusercontent.com/108964197/181046590-17f00f1a-075d-4add-b873-2ccccf24c5ad.png)

___
## On returning book Trasactions page will be updated.
## Trasaction page already has transaction when it was issued. On returning the book this trasaction will update returned date from none to present value.
![Transactions](https://user-images.githubusercontent.com/108964197/181046690-b5e692e6-5d4b-4d83-8823-5a377dc6575a.png)


___
## Members Page is used for managing Members.
![Memberspage](https://user-images.githubusercontent.com/108964197/181046810-868318df-5721-494a-8818-8f4f654ece06.png)


___
## Add New Member
![Add New Member](https://user-images.githubusercontent.com/108964197/180741195-da0d2fca-2d82-47f6-be89-1ed006b4349a.png)

___
## Update Member
![Update Member](https://user-images.githubusercontent.com/108964197/181046948-337cf243-ad99-4377-8610-3c4ff1671770.png)
___
## Member Delete Confimation
![Confirm Delete Member](https://user-images.githubusercontent.com/108964197/181047061-eb00fa5e-032a-477f-a15a-fbfb861daa0c.png)


___
## Payment Page
Only members having debt will be shown here.
![Payments ](https://user-images.githubusercontent.com/108964197/181047359-9cbc074b-b043-4314-b3a4-531ba0f350f9.png)
___
## Pay Page
![Pay Now](https://user-images.githubusercontent.com/108964197/181047430-644b8565-308f-48a7-941d-587fa71a4251.png)
___
## Import Book Page
## This page import books into system with API use.
![Import Book Page](https://user-images.githubusercontent.com/108964197/181047759-cafced00-5100-4f51-8c0a-27fba59e3824.png)
___

Member are charged on Per day basis. There is no Membership fee.
Member Can have on one book at a time.
For Each day member has a book he will be charged on per day INR 8 basis.
And He will charge on return. Member cannot have debt of more than INR 500 if he wants a book.




