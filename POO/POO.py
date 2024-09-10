class Block():  # Esta é a definição da classe Block
    def __init__(self):  # Construtor da classe que inicializa os atributos
        self.block = False  # O atributo 'self.block' é inicializado com o valor booleano False
    
    # Métodos que definem as funcionalidades do objeto Block
    def liberar(self):
        self.block = True  # Define o atributo 'block' como True

    def bloquear(self):
        self.block = False  # Define o atributo 'block' como False
    
    def status(self):
        # Retorna uma string indicando se o bloco está liberado ou bloqueado
        return 'Bloco liberado' if self.block else 'Bloco bloqueado'
    
bloco = Block()  # Cria uma instância da classe Block, chamada 'bloco'

# Agora, 'bloco' é um objeto da classe Block e possui os métodos definidos na classe
bloco.liberar()  # Usa o método 'liberar' para definir o bloco como liberado (block = True)
bloco.bloquear()  # Usa o método 'bloquear' para definir o bloco como bloqueado (block = False)
print(bloco.status())  # Imprime o status atual do bloco, baseado no valor do atributo 'block'