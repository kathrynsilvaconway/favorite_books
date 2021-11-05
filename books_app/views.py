from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt

def index(request):
    context = {
        'users': User.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'index.html', context)

def process_reg(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        this_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash)
        request.session['first_name'] = this_user.first_name
        request.session['id'] = this_user.id
        return redirect('/books')

def process_login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        one_user = User.objects.filter(email = request.POST['email'])
        request.session['id'] = one_user[0].id
        request.session['first_name'] = one_user[0].first_name
        return redirect('/books')
    return redirect('/')

def render_home(request):
    user_id=request.session['id']
    context = {
        'user': User.objects.get(id=user_id),
        'books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def upload_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')         
    else:
        this_book = Book.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc'],
            uploaded_by = User.objects.get(id=request.session['id']),
        )
        user = User.objects.get(id=request.session['id'])
        user.books_liked.add(this_book)
        request.session['book_id'] = this_book.id
        return redirect('/books')
def display_book(request, this_book_id):
    context = {
        'book': Book.objects.get(id=this_book_id),
        'user': User.objects.get(id=request.session['id'])
    }

    return render(request, 'display_book.html', context)

def log_out(request):
    request.session.flush()
    return redirect('/')

def delete_book(request, this_book_id):
    book = Book.objects.get(id=this_book_id)
    book.delete()
    return redirect('/books')

def update_book(request, this_book_id):
    errors = Book.objects.update_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')         
    else:
        book = Book.objects.get(id=this_book_id)
        book.desc = request.POST['desc']
        book.save()
        return redirect(f'/display_book/{this_book_id}')

def add_to_likes(request, this_book_id):

    context = {
        'book': Book.objects.get(id=this_book_id),
        'user': User.objects.get(id=request.session['id'])
    }

    user = User.objects.get(id=request.session['id'])
    book = Book.objects.get(id=this_book_id)
    user.books_liked.add(book)
    
    return render(request, 'display_book.html', context)

def remove_like(request, this_book_id):
    context = {
        'book': Book.objects.get(id=this_book_id),
        'user': User.objects.get(id=request.session['id'])
    }

    user = User.objects.get(id=request.session['id'])
    book = Book.objects.get(id=this_book_id)
    user.books_liked.remove(book)
    
    return render(request, 'display_book.html', context)

def user_favorites(request, this_user_id):
    context = {
        'user': User.objects.get(id=this_user_id),
        'books': Book.objects.all()
    }
    return render(request, 'user_favorites.html', context)



# Create your views here.
