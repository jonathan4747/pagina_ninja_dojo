from dojoninja_app.config.mysqlconnection import connectToMySQL
from dojoninja_app.modelos.modelo_ninja import Ninja

class Dojo:
    
    def __init__(self,id,name,created_at,updated_at):
        self.id = id
        self.name=name
        self.created_at=created_at
        self.updated_at=updated_at
        self.ninjas= []
        
    '''def __init__(self,diccionario):
        self.id = diccionario['id']
        self.name= diccionario['name']
        self.created_at= diccionario['created_at']
        self.updated_at= diccionario['updated_at']
        self.ninjas= []'''
    
    def agregarNinjas(self,ninja):
        self.ninjas.append(ninja)
        
    @classmethod
    def agregarDojo(cls,nuevoDojo):
        query = "INSERT INTO dojos(name,created_at,updated_at) VALUES(%(name)s,NOW(),NOW());"
        resultado = connectToMySQL("ninjas_dojos").query_db(query,nuevoDojo)
        return resultado
    
    @classmethod
    def obtenerListaDojo(estorefiereaClase):
        query = "SELECT * FROM dojos;"
        resultado = connectToMySQL( "ninjas_dojos" ).query_db( query )
        print("LISTA DOJOS", resultado)
        listaDojos = []
        for dojo in resultado:
            #listaDojos.append(estorefiereaClase(dojo))
            listaDojos.append( Dojo(dojo["id"],dojo["name"],dojo["created_at"],dojo["updated_at"]) )
        return listaDojos
    
    @classmethod
    def listaNinjas(cls,dojo):
        query="SELECT* FROM dojos LEFT JOIN ninjas ON dojos.id=ninjas.dojo_id WHERE dojos.id= %(id)s;"
        resultado = connectToMySQL( "ninjas_dojos" ).query_db( query,dojo )
        print("que es",resultado)
        listadeNinjas=[]
        for Nin in resultado:
            Nin = {
                "id" : Nin["name"],
                "first_name": Nin["first_name"],
                "last_name": Nin["last_name"],
                "age":Nin["age"],
                "dojo_id":Nin["dojo_id"],
                "created_at":Nin["created_at"],
                "updated_at":Nin["updated_at"]
            }
            listadeNinjas.append(Ninja(Nin["id"], Nin["first_name"], Nin["last_name"], 
                                       Nin["age"], Nin["dojo_id"], Nin["created_at"], Nin["updated_at"]))
            print("ESTO ES NIN", listadeNinjas)  
        #listadeNinjas.append(Ninja(Nin)) 
        #listadeNinjas = Ninja.listadeNinjas(resultado)
         
        return listadeNinjas 
    
        
        
        
 
    