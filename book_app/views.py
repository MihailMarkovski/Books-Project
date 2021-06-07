from django.shortcuts import render, redirect

# Create your views here.
from book_app.forms import BookForm
from book_app.models import Book


def index(request):

    context = {
        'books': Book.objects.all(),
    }

    return render(request, 'book/index.html', context)


def create(request):
    if request.method == 'GET':
        context = {
            'form': BookForm,

        }
        return render(request, 'book/create.html', context)

    else:
        form = BookForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('books index')

    context = {
        'form': form
    }
    return render(request, 'book/index.html', context)


def edit(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'GET':
        form = BookForm(instance=book)
        context = {
            'form': form
        }


        return render(request, 'book/edit.html', context)

    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()

        return redirect('books index')
