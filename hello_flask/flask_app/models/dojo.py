from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
        
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        result = connectToMySQL('dojo_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in result:
            dojos.append(dojo)
        return dojos
            
    @classmethod
    def dojo_save(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, Now(), Now());'
        print(query)
        result = connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)
        return result
    
    @classmethod
    def dojo_with_ninjas(cls, data):
        query = """
        SELECT * FROM dojos 
        LEFT JOIN ninjas on dojos.id = ninjas.dojo_id 
        WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        print(dojo)
        for row in results:
            students = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(students))
        return dojo