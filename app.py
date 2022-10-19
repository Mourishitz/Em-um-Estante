from flask import Flask, render_template, request, redirect, session, flash


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
app.secret_key = 'secret'


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


@app.route('/authenticate', methods=['POST',])
def authenticate():
    if 'alohomora' == request.form['password']:
        session['current_user'] = request.form['username']
        flash(f'{session["current_user"]} logado com sucesso!')
        return redirect('/')
    else:
        flash('Não encontramos o seu usuário')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['current_user'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')


app.run(debug=True)
