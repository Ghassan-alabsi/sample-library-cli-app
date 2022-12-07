import typer
from rich.console import Console
from rich.table import Table
from typing import Optional
from connect import connect
import psycopg2
from config import config
import datetime

console = Console()
app = typer.Typer()



def signup(username: str):    
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f"INSERT INTO  public.user (user_name) VALUES ('{username}')"
    cur.execute(sql)
    conn.commit()



def add(name, author,pages,genre):
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    time = str(datetime.datetime.now())
    sql = f"""INSERT INTO  public.book (book_name, author_name, pages, genre, availability, book_date_added) 
            VALUES ('{name}', '{author}', {pages}, '{genre}', True,'{time}')"""
    cur.execute(sql)
    conn.commit()


def delete():
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" DELETE FROM public.book where book_id = 3"""
    cur.execute(sql)
    conn.commit()


def update():
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" UPDATE book SET genre = 'Advanture'
                WHERE book_id = 1
         """
    cur.execute(sql)
    conn.commit()


def get_books(name: str):
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" SELECT * FROM public.book where book_name = '{name}'
         """
    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books

def search_name(name: str):
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" SELECT * FROM public.book where book_name = '{name}'
         """
    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books
def search_author(author: str):
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" SELECT * FROM public.book where author_name = '{author}'
         """
    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books

def recent_added(author):
    list=[]
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" SELECT author_name FROM public.book 
                 """
    cur.execute(sql)
    authors = cur.fetchall()
    r= len((authors))
    for i in range(r):
         list.append(authors[i][0])


    if bool(author) is True:
        if author in list:
            conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
            cur = conn.cursor()
            sql = f""" SELECT * FROM public.book where author_name = '{author}'order by book_date_added desc limit 5
                 """
            cur.execute(sql)
            books = cur.fetchall()
            conn.commit()
            return books
        else:
            print("author does not exist!")


    elif bool(author) is False:
        conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
        cur = conn.cursor()
        sql = f""" SELECT * FROM public.book order by book_date_added desc limit 5
                     """
        cur.execute(sql)
        books = cur.fetchall()
        conn.commit()
        return books

def mostread_books(genre):
    list=[]
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" SELECT genre FROM public.book 
                 """
    cur.execute(sql)
    genres = cur.fetchall()
    r= len((genres))
    for i in range(r):
         list.append(genres[i][0])


    if bool(genre) is True:
        if genre in list:
            conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
            cur = conn.cursor()
            sql = f"""select b.book_id, b.book_name, b.author_name,b.genre, c.count
from public.book as b
join (SELECT book_id, count(mark_read) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id 
where genre = '{genre}' order by c.count desc limit 10
                 """
            cur.execute(sql)
            books = cur.fetchall()
            conn.commit()
            return books
        else:
            print("genre does not exist!")


    elif bool(genre) is False:
        conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
        cur = conn.cursor()
        sql = f""" select b.book_id, b.book_name, b.author_name,b.genre, c.count
from public.book as b
join (SELECT book_id, count(mark_read) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id 
order by c.count desc limit 10
                     """
        cur.execute(sql)
        books = cur.fetchall()
        conn.commit()
        return books

def most_favorite(genre):
    list=[]
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" SELECT genre FROM public.book 
                 """
    cur.execute(sql)
    genres = cur.fetchall()
    r= len((genres))
    for i in range(r):
         list.append(genres[i][0])


    if bool(genre) is True:
        if genre in list:
            conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
            cur = conn.cursor()
            sql = f"""select b.book_id, b.book_name, b.author_name,b.genre, c.count
from public.book as b
join (SELECT book_id, count(fav_book) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id 
where genre = '{genre}' order by c.count desc limit 10
                 """
            cur.execute(sql)
            books = cur.fetchall()
            conn.commit()
            return books
        else:
            print("genre does not exist!")


    elif bool(genre) is False:
        conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
        cur = conn.cursor()
        sql = f""" select b.book_id, b.book_name, b.author_name,b.genre, c.count
from public.book as b
join (SELECT book_id, count(fav_book) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id 
order by c.count desc limit 10
                     """
        cur.execute(sql)
        books = cur.fetchall()
        conn.commit()
        return books

def mostread_genres():

    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f"""select b.genre, sum(c.count)
from public.book as b
join (SELECT book_id, count(mark_read) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id
GROUP BY genre order by sum desc limit 5
                 """
    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books
def mostread_authors():

    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f"""select b.author_name, sum(c.count)
from public.book as b
join (SELECT book_id, count(mark_read) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id
GROUP BY author_name order by sum desc limit 5
                 """
    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books

def mark_read(book_id,username):
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f"INSERT INTO  public.command (mark_read) VALUES ('True') where "
    cur.execute(sql)
    conn.commit()







  
    
