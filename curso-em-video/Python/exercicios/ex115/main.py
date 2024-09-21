import cadastro

while True:
    init = cadastro.menu()
    
    if init == 1:
        cadastro.view()
    elif init == 2:
        cadastro.cadastrar()
    else:
        break
    