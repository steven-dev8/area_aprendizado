from datetime import datetime

def voto(year):
    IDADE = datetime.now().year - year

    if IDADE >= 18 and IDADE <= 70:
        return print(f'Com {IDADE}: VOTO OBRIGATÓRIO')
    elif IDADE > 70 or IDADE >= 16:
        return print(f'Com {IDADE}: VOTO OPCIONAL')
    else:
        return print(f'Com {IDADE}: VOTO NEGADO')

print('-=' * 15)
voto(int(input('Em que ano você nasceu? ')))