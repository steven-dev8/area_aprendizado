class Animal:
    def fazer_barulho(self):
        raise NotImplementedError("Subclasse deve implementar este método")

class Cachorro(Animal):
    def fazer_barulho(self):
        print("O cachorro faz: Au Au!")

class Gato(Animal):
    def fazer_barulho(self):
        print("O gato faz: Miau!")

def fazer_barulho_do_animal(animal):
    animal.fazer_barulho()

# Criando instâncias dos objetos
cachorro = Cachorro()
gato = Gato()

cachorro.fazer_barulho()
gato.fazer_barulho()
