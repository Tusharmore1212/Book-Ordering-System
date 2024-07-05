from django.shortcuts import render, redirect
from mybooks.models import Book,Buyerinfo
from mybooks.form import BookForm
from django.http import FileResponse,HttpResponse
from pdfdocument.document import PDFDocument
from django.views.generic import ListView

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def buybook(request,id):
    book = Book.objects.get(id=id)
    return render(request,'buy_now.html',{'book':book})

def dobuying(request,id):
    if request.method == "POST":
        name = request.POST['customerName']
        email = request.POST['customeremail']
        phone = request.POST['cphone']
        address = request.POST['cadd']
        quantity = int(request.POST['quantity'])
        print("working")
        b = Book.objects.get(pk=id)
        print(b.quantity)
        if quantity<=b.quantity:
            print("working")
            try:
                b.quantity = b.quantity-quantity
                c =Buyerinfo()
                c.cname = name
                c.cemail = email
                c.cphone = phone
                c.cadd = address
                c.quantity = quantity
                c.bname = b.name
                c.price = b.price
                total = b.price*quantity
                c.totalamout= total
                b.save()
                c.save()
                return redirect('/thanks/')
               
            except:
                error_message = f"{b.quantity} books available."
                return render(request, 'buy_now.html', {'error_message': error_message})
        else:
            error_message = f"{b.quantity} books available."
            return render(request, 'buy_now.html', {'error_message': error_message})
        
def thanks(request):
    return render(request,'thanks.html')

