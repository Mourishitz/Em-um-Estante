from flask import Flask, render_template, request, redirect


class Book:
    def __init__(self, name, category, author):
        self.name = name
        self.category = category
        self.author = author


bk1 = Book('Clean Code', 'Programacao', 'Robert Cecil')
bk2 = Book('Arte da Guerra', 'Estrategia', 'Sun Tzu')
bk3 = Book('Diario de Anne Frank', 'Biografia', 'Anne Frank')
book_list = [bk1, bk2, bk3]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('list.html', title='Livros', books=book_list)


@app.route('/new')
def new():
    return render_template('new.html', title='Novo Livro')


@app.route('/create', methods=['POST', ])
def create():
    name = request.form['name']
    category = request.form['category']
    author = request.form['author']
    book = Book(name, category, author)
    book_list.append(book)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticate', methods=['POST',])
def autenticate():
    if 'alohomora' == request.form['password']:
        return redirect('/')
    else:
        return redirect('/login')

app.run(debug=True)
