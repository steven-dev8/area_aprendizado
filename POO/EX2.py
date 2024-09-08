class Sabao:
    def __init__(self, marca, sabao):
        self.marca = marca
        self.sabao = sabao
        self.tipo_liquido = ['Roupas Delicadas','Água Fria', 'Lavagem a mão']
        self.tipo_po = ['Roupas muito suja', 'Água quente', 'Lavagem em grande quantidade']

    def exibir_info(self):
        if self.sabao in ['líquido', 'liquido']:
            print(f'O Sabão Líquido da {self.marca}: É formulado com uma mistura de água e agentes de limpeza líquidos.')
            for i in self.tipo_liquido:
                print(f' •{i}')
        elif self.sabao in ['pó', 'po']:
            print(f'Sabão em Pó da {self.marca}: Contém agentes de limpeza secos, geralmente combinados com outros ingredientes como branqueadores e agentes de amaciamento.')
            for i in self.tipo_po:
                print(f' •{i}')
        else:
            print('TIPO DE SABÃO INVALIDO!!!')

marca = input('Qual a marca do sabão? ').upper()
tipo = input('Qual o tipo do sabão? ').lower()

sabao = Sabao(marca, tipo)

sabao.exibir_info()