from dojoninja_app.config.mysqlconnection import connectToMySQL

class Ninja:
    
    def __init__(self, id,first_name,last_name,age,dojo_id,created_at,updated_at):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.dojo_id=dojo_id
        self.created_at=created_at
        self.updated_at=updated_at
    
        
    '''def __init__(self, dictionary):
        self.id=dictionary['id']
        self.first_name=dictionary['first_name']
        self.last_name=dictionary['last_name']
        self.age = dictionary['age']
        self.dojo_id=dictionary['dojo_id'] 
        self.created_at=dictionary['created_at']
        self.updated_at=dictionary['updated_at']'''
        
    @classmethod
    def agregaNinja(cls,nuevoNinja):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id,created_at,updated_at) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s,NOW(),NOW());"
        print("este es el query",query)
        resultado = connectToMySQL("ninjas_dojos").query_db(query,nuevoNinja)
        return resultado
    
    @classmethod
    def listadeNinjas(cls, listaDicts):
        listaNinjas = []
        for ninjas in listaDicts:
            listaNinjas.append(cls(ninjas))
        return listaNinjas

    