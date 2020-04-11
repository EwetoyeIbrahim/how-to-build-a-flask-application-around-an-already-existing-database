from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# --------- Configurations ------------
class Config:
    
    # Change to your Database_URI, here we are using sqlite database
    # Note that postgres URI looks like 'postgresql://UserName:password@host:port/DatabaseName'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///equimolar.db' # database
    DEBUG = True
    

def create_app():
    # Simple Application Factory
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.Model.metadata.reflect(db.engine)
    return app

app = create_app()

# -------- Models of interest ----------
class Article(db.Model):
    '''
    What is really neede is just the table name
    In this case, I will be looking at the articles table'''
    __table__ = db.Model.metadata.tables['articles']
    def __repr__(self):
        return '<Article {}>'.format(self.id)

# -------- Endpoints -------------------
@app.route('/')
def index():
    all_articles = Article.query.order_by(Article.last_mod_date.desc())
    return render_template('articles_table.html', articles=all_articles)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
