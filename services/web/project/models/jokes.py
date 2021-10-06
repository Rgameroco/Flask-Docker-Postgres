from sqlalchemy.sql.functions import func
from flask_sqlalchemy import SQLAlchemy
from flask import (
    Flask
)
from sqlalchemy import Column, Integer, DateTime,Boolean,String
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class Jokes(db.Model):
    __tablename__ = "jokes"
    
    id = Column(Integer, primary_key=True)
    active = Column(Boolean(), default=True, nullable=False)
    joke = Column(String(256), nullable=False)
    createAt = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, email):
        self.email = email
    
    def save(self):
        db.session.add(self)
        return db.session.commit()
    
    def delete(self):
            db.session.delete(self)
            return db.session.commit()

        
