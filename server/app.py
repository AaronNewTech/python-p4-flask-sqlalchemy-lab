from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)

# Configuration for the database URI and to disable modification tracking
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Flask-Migrate extension to handle database migrations
migrate = Migrate(app, db)

# Initialize the Flask-SQLAlchemy extension with the Flask app
db.init_app(app)

@app.route('/')
def home():
    # Simple home page route
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    # Query the Animal with the specified ID from the database
    animal = Animal.query.filter(Animal.id == id).first()
    
    if animal:
        # Prepare the response body with Animal information
        response_body = f'''
            <ul>ID: {animal.id}</ul>
            <ul>Name: {animal.name}</ul>
            <ul>Species: {animal.species}</ul>
            <ul>Zookeeper: {animal.zookeeper.name}</ul>
            <ul>Enclosure: {animal.enclosure.environment}</ul>
        '''
    
    else:
        response_body = '<h1>404 animal not found</h1>'
    response = make_response(response_body)
    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    # Query the Zookeeper with the specified ID from the database
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    
    if zookeeper:
        # Prepare the response body with Zookeeper information and their animals
        response_body = f'''
            <ul>ID: {zookeeper.id}</ul>
            <ul>Name: {zookeeper.name}</ul>
            <ul>Birthday: {zookeeper.birthday}</ul>
        '''
        for animal in zookeeper.animals:
            response_body += f'<ul>Animal: {animal.name}</ul>'
        
        response_body += '</ul></ul>'
    else:
        response_body = '<h1>404 zookeeper not found</h1>'
    
    response = make_response(response_body)
    return response

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    # Query the Enclosure with the specified ID from the database
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    
    if enclosure:
        # Prepare the response body with Enclosure information and the animals in it
        response_body = f'''
            <ul>ID: {enclosure.id}</ul>
            <ul>Environment: {enclosure.environment}</ul>
            <ul>Open to Visitors: {enclosure.open_to_visitors}</ul>
        '''
        for animal in enclosure.animals:
            response_body += f'<ul>Animal: {animal.name}</ul>'
        
        response_body += '</ul></ul>'
    else:
        response_body = '<h1>404 enclosure not found</h1>'
    
    response = make_response(response_body)
    return response

if __name__ == '__main__':
    # Run the Flask app on port 5555 in debug mode
    app.run(port=5555, debug=True)
