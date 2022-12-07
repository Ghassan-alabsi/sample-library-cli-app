import typer
#from typing import optional
from rich.console import Console
from rich.table import Table
from typing import Optional
from connect import connect
import psycopg2
from config import config
import datetime
from database import add, delete, signup, update, get_books, search_name, search_author,recent_added, mostread_books, most_favorite, mostread_genres, mostread_authors, markread


console = Console()
app = typer.Typer()



@app.command("start")
def start():
    typer.secho(f'''Welcome to Library CLI!\n\n
        You can execute command '--help' to see the possible commands''', fg=typer.colors.GREEN)
    connect()


@app.command("sign_up")
def sign_up(username: str):
    typer.echo(f"Nice that you are signing up!")
    signup(username)


@app.command("add_book")
def add_book():
    name= input("Name: ")
    author= input("Author: ")
    pages= input("# pages: ")
    genre= input("Genre: ")
    typer.echo(f"Book is added!")
    add(name, author,pages,genre)


@app.command("delete_book")
def delete_book():
    typer.echo(f"Book is deleted!")
    delete()


@app.command("update_book")
def update_book():
    typer.echo(f"Book is updated!")
    update() 
   
   
# Example function for tables, you can add more columns/row.

@app.command("get_book")
def get_book(name:str):
       typer.echo(f"Books are displayed!")
       books= get_books(name)
       display_table(books)

@app.command("search_by_name")
def search_by_name(name:str):
       typer.echo(f"Books are displayed!")
       books= search_name(name)
       display_table(books)
@app.command("search_by_author")
def search_by_author(author:str):
       typer.echo(f"Books are displayed!")
       books= search_author(author)
       display_table(books)

@app.command("recently_added")
def recently_added(author: Optional[str]= typer.Argument("")):
       typer.echo(f"Books are displayed!")
       books= recent_added(author)
       display_table(books)

@app.command("most_read_books")
def most_read_books(genre: Optional[str]= typer.Argument("")):
       typer.echo(f"Books are displayed!")
       books= mostread_books(genre)
       print(books)
       table = Table(show_header=True, header_style="bold blue")

       table.add_column("Book ID", style="dim", min_width=10, justify=True)
       table.add_column("Book Name", style="dim", min_width=10, justify=True)
       table.add_column("Author", style="dim", min_width=10, justify=True)
       table.add_column("Genre", style="dim", min_width=10, justify=True)
       table.add_column("Count", style="dim", min_width=10, justify=True)
       for book in books:
           table.add_row(str(book[0]), book[1], book[2], str(book[3]), str(book[4]))
       console.print(table)


@app.command("most_favorite_books")
def most_favorite_books(genre: Optional[str]= typer.Argument("")):
       typer.echo(f"Books are displayed!")
       books= most_favorite(genre)
       table = Table(show_header=True, header_style="bold blue")

       table.add_column("Book ID", style="dim", min_width=10, justify=True)
       table.add_column("Book Name", style="dim", min_width=10, justify=True)
       table.add_column("Author", style="dim", min_width=10, justify=True)
       table.add_column("Genre", style="dim", min_width=10, justify=True)
       table.add_column("Count", style="dim", min_width=10, justify=True)
       for book in books:
           table.add_row(str(book[0]), book[1], book[2], str(book[3]), str(book[4]))
       console.print(table)

@app.command("most_read_genres")
def most_read_genres():
       typer.echo(f"Books are displayed!")
       books= mostread_genres()
       table = Table(show_header=True, header_style="bold blue")

       table.add_column("Genre", style="dim", min_width=10, justify=True)
       table.add_column("Count", style="dim", min_width=10, justify=True)
       for book in books:
           table.add_row(str(book[0]), str(book[1]))
       console.print(table)

@app.command("most_read_authors")
def most_read_authors():
       typer.echo(f"Books are displayed!")
       books= mostread_authors()
       table = Table(show_header=True, header_style="bold blue")

       table.add_column("Genre", style="dim", min_width=10, justify=True)
       table.add_column("Count", style="dim", min_width=10, justify=True)
       for book in books:
           table.add_row(str(book[0]), str(book[1]))
       console.print(table)

@app.command("mark_read")
def mark_read(book_id, username):
       typer.echo(f"Books are displayed!")
       books= markread(book_id, username)
@app.command("display_table")
def display_table(books):


    table = Table(show_header=True, header_style="bold blue")

    table.add_column("Book ID", style="dim", min_width=10, justify=True)
    table.add_column("Book Name", style="dim", min_width=10, justify=True)
    table.add_column("Author", style="dim", min_width=10, justify=True)
    table.add_column("Pages", style="dim", min_width=10, justify=True)
    table.add_column("Genre", style="dim", min_width=10, justify=True)
    table.add_column("Availability", style="dim", min_width=10, justify=True)
    if bool(books) is True:
        for book in books:
            table.add_row(str(book[0]),book[1], book[2], str(book[3]), book[4], str(book[5]), book[6])
        console.print(table)
    else:
        console.print(table)

if __name__ == "__main__":
    app()
    

