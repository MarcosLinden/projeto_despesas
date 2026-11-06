despesas = []

def cadastrar_despesas(descricao, valor, categoria):
        despesa = {"descrição": descricao, "valor": valor, "categoria:": categoria}
        for item in despesas:
            if descricao.lower() == item['descrição'].lower():
                return False

        despesas.append(despesa)
        return True

mercado = cadastrar_despesas('Mercado', 500, 'Alimento')
mercado1 = cadastrar_despesas('Mercado', 500, 'Alimento')

print(mercado)


def listar_despesas():
    if not despesas:
        print('Lista de despesas vazia')

    else:
        for despesa in despesas:
            print(despesa)

listar_despesas()