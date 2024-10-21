from flask import Flask, render_template, request, redirect, url_for

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []

@app.route('/')
def home():
    return render_template("index.html", books = all_books)

@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        #to get data from the form
        bookTitle = request.form["title"]
        bookAuthor = request.form["author"]
        bookRating = request.form["rating"]

        #to make a dictionary for the book
        newBook = {
            "title": bookTitle,
            "author": bookAuthor,
            "rating": int(bookRating)
        }

        #to add book to the list containing all books
        all_books.append(newBook)

        #to redirect to homepage
        return redirect(url_for("home"))
    
    #to render the "add.html template when user visits the /add page
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

