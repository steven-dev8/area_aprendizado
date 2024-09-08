class Animal():
    def fazer_som(self):
        raise NotImplementedError('Subclasse')
    
class Gato(Animal):
    def fazer_som(self):
        print('O gato faz miau')

class Cachorro(Animal):
    def fazer_som(self):
        print('O cachorro faz au au')

def som_animal(animal):
    animal.fazer_som()

cachorro = Cachorro()
gatinho = Gato()

som_animal(cachorro)
som_animal(gatinho)