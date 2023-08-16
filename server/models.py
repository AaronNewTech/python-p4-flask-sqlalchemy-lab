from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Zookeeper(db.Model):
    # creates table for zookeeper
    __tablename__ = 'zookeepers'
    
    # creates columns in zookeeper table for id, name and birthday
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)
    
    # creates a relationship between two models and connects them to each other. 
    # syntax plural child variable = db.relationship('child Class', backreference='parent table name')
    animals = db.relationship('Animal', backref='zookeeper')
    

class Enclosure(db.Model):
    # creates table for enclosure
    __tablename__ = 'enclosures'

    # creates columns in enclosure table for id, environment, and open for visitors
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)
    
    # creates a relationship between two models and connects them to each other. 
    # syntax plural child variable = db.relationship('child Class', backreference='parent table name')
    animals = db.relationship('Animal', backref='enclosure')


class Animal(db.Model):
    # creates table for animal
    __tablename__ = 'animals'

    # creates columns for animal table for id, name and species
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    # creates a foreign key to connect to zookeeper database that goes in the animal database
    # this is a child of the Zookeeper class
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    
    # creates a foreign key to connect to enclosure database that goes in the animal database
    # this is a child of the Enclosure class
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))
    

