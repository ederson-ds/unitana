from flask import Flask, render_template, flash, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from forms import ContasapagarForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "sdf4fewfw3f"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://eanyxqcj:82NViBUH7ayhJrzfSNJeIPSY34O3epdm@batyr.db.elephantsql.com:5432/eanyxqcj"
db = SQLAlchemy(app)


class Contasapagar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    emissao = db.Column(db.DateTime, nullable=False)


posts = [
    {
        'author': 'Ederson Duarte',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2021'
    },
    {
        'author': 'Ederson Duarte',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2021'
    }
]


@app.route('/')
def index():
    return render_template('home.html', posts=posts)


@app.route('/contasapagar')
def contasapagar():
    contas_objetos = Contasapagar.query.all()
    return render_template('contasapagar/contasapagar.html', contas=contas_objetos)

@app.route('/contasapagar/inserir', methods=['GET', 'POST'])
def contasapagaradd():
    form = ContasapagarForm()
    if form.validate_on_submit():
        flash('Conta cadastrada com sucesso!', 'success')
    return render_template('contasapagar/contasapagaradd.html', form=form)


if __name__ == "__main__":
    app.run()
