from flask import Blueprint, request

from http_status_codes import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from database import Person, db


persons = Blueprint('persons', __name__, url_prefix='/api/v1/')


@persons.get('/persons')
def get_persons():
    response = Person.query.all()
    persons_list = [item.to_dict() for item in response]
    return {'persons': persons_list}, HTTP_200_OK


@persons.post('/persons')
def add_person():
    response = request.get_json()

    neccesary_fields = ['firstname', 'lastname', 'email']
    for field in neccesary_fields:
        if field not in response.keys():
            return {'error': '404', 'message': f'{field} is a neccesary field'}, HTTP_400_BAD_REQUEST

    if Person.query.filter_by(email=response.get('email')).first():
        return {'error': '400', 'message': 'email is already taken'}, HTTP_400_BAD_REQUEST

    person = Person(
        firstname=response.get('firstname'),
        lastname=response.get('lastname'),
        email=response.get('email'),
        age=response.get('age'),
        bio=response.get('bio')
    )

    db.session.add(person)
    db.session.commit()
    return person.to_dict(), HTTP_201_CREATED


@persons.get('/persons/<int:id>')
def get_person(id):
    result = Person.query.filter_by(id=id).first()
    if not result:
        return {'code': '404', 'message': 'Person not found'}, HTTP_404_NOT_FOUND
    return result.to_dict(), HTTP_200_OK


@persons.put('/persons/<int:id>')
def update_person(id):
    response = request.get_json()

    neccesary_fields = ['firstname', 'lastname', 'email']
    for field in neccesary_fields:
        if field not in response.keys():
            return {'error': '404', 'message': f'{field} is a neccesary field'}, HTTP_400_BAD_REQUEST

    person = Person.query.filter_by(id=id).first()

    if not person:
        return {'code': '404', 'message': 'Person not found'}, HTTP_404_NOT_FOUND

    for field in response:
        setattr(person, field, response[field])
    db.session.commit()
    return person.to_dict(), HTTP_200_OK


@persons.delete('/persons/<int:id>')
def delete_person(id):
    person = Person.query.filter_by(id=id).first()
    if not person:
        return {'code': '404', 'message': 'Person not found'}, HTTP_404_NOT_FOUND
    db.session.delete(person)
    db.session.commit()
    return {}, HTTP_204_NO_CONTENT
