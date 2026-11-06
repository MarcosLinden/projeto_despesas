despesas = []

def cadastrar_despesas(descricao, valor, categoria):
        despesa = {"descrição": descricao, "valor": valor, "categoria:": categoria}
        for item in despesas:
            if descricao.lower() == item['descrição'].lower():
                return False

        despesas.append(despesa)
        return True

dentista = cadastrar_despesas('Aparelho ortodontico', 125, 'Cuidado pessoal')
curso  = cadastrar_despesas('Curso técnico', 161, 'Estudo')
moto = cadastrar_despesas('Moto',641,'Manutenção')




def listar_despesas():
    if not despesas:
        print('Lista de despesas vazia')

    else:
        for despesa in despesas:
            print(despesa)

listar_despesas()

def calcular_despesas():
    total = 0
    for despesa in despesas:
        total += despesa['valor']

    return f'Valor total em despesas: R${total}'

print(calcular_despesas())