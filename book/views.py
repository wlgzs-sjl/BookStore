import pymysql
from django.shortcuts import render, redirect


# Create your views here.
# 书本信息列表处理函数
def index(request):
    conn = pymysql.connect(host="localhost", user="root", passwd="sjl13121", db="BookStore", charset='utf8')
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT id,book_name,book_author,book_type,book_price,book_press FROM book_books")
        books = cursor.fetchall()
    return render(request, 'books/index.html', {'books': books})

# 书本信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'books/add.html')
    else:
        book_name = request.POST.get('book_name', '')
        book_author = request.POST.get('book_author', '')
        book_type = request.POST.get('book_type', '')
        book_price = request.POST.get('book_price', '')
        book_press = request.POST.get('book_press', '')
        conn = pymysql.connect(host="localhost", user="root", passwd="sjl13121", db="BookStore", charset='utf8')
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO book_books (book_name,book_author,book_type,book_price,book_press) "
                           "values (%s,%s,%s,%s,%s)", [book_name, book_author, book_type, book_price, book_press])
            conn.commit()
        return redirect('../')

# 书本信息搜索处理函数
def select(request):
    if request.method == 'GET':
        return render(request, 'books/select.html')
    else:
        book_name = request.POST.get('book_name', '')
        conn = pymysql.connect(host="localhost", user="root", passwd="sjl13121", db="BookStore", charset='utf8')
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,book_name,book_author,book_type,book_price,book_press FROM book_books where book_name =%s",[book_name])
            books = cursor.fetchall()
        return render(request, 'books/list.html', {'books': books})

# 书本信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = pymysql.connect(host="localhost", user="root", passwd="sjl13121", db="BookStore", charset='utf8')
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,book_name,book_author,book_type,book_price,book_press FROM book_books where id =%s", [id])
            book = cursor.fetchone()
        return render(request, 'books/edit.html', {'book': book})
    else:
        id = request.POST.get("id")
        book_name = request.POST.get('book_name', '')
        book_author = request.POST.get('book_author', '')
        book_type = request.POST.get('book_type', '')
        book_price = request.POST.get('book_price', '')
        book_press = request.POST.get('book_press', '')
        conn = pymysql.connect(host="localhost", user="root", passwd="sjl13121", db="BookStore", charset='utf8')
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE book_books set book_name=%s,book_author=%s,book_type=%s,book_price=%s,book_press=%s where id =%s",
                           [book_name, book_author, book_type, book_price, book_press, id])
            conn.commit()
        return redirect('../')

# 书本信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = pymysql.connect(host="localhost", user="root", passwd="sjl13121", db="BookStore", charset='utf8')
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM book_books WHERE id =%s", [id])
        conn.commit()
    return  redirect('../')
