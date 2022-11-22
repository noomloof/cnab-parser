def transaction_type_finder(x):
    match x:
        case "1":
            return {
                'type': 'Entrada',
                'description': 'Débito'
            }
        case "2":
            return {
                'type': 'Saida',
                'description': 'Boleto'
            }
        case "3":
            return {
                'type': 'Saida',
                'description': 'Financiamento'
            }
        case "4":
            return {
                'type': 'Entrada',
                'description': 'Crédito'
            }
        case "5":
            return {
                'type': 'Entrada',
                'description': 'Recebimento empréstimo'
            }
        case "6":
            return {
                'type': 'Entrada',
                'description': 'Vendas'
            }
        case "7":
            return {
                'type': 'Entrada',
                'description': 'Recebimento ted'
            }
        case "8":
            return {
                'type': 'Entrada',
                'description': 'Recebimento doc'
            }
        case "9":
            return {
                'type': 'Saida',
                'description': 'Aluguel'
            }
