from scipy.optimize import linprog

# Funcao para calcular o valor economico mensal de uma area marinha
def calcular_valor_area_marinha(tamanho_m2, valor_pesca_anual, valor_turismo_anual, valor_recursos_naturais):
    tamanho_ha = tamanho_m2 / 10000  # Convertendo metros quadrados para hectares
    valor_total = (valor_pesca_anual + valor_turismo_anual + (valor_recursos_naturais * 2))
    valor_anual = (valor_total / tamanho_ha) * 1000
    valor_final = valor_anual / 12
    return valor_final

# Funcao para otimizar a alocacao de recursos com programacao linear
def otimizar_alocacao_recursos():

    # Como linprog faz minimizacao, usamos os coeficientes negativos para maximizar
    c = [-1, -1.5, -2]

    # Coeficientes das desigualdades
    A = [
        [1, 0, 0],  # Restringe x1 <= 40 (pesca)
        [0, 1, 0],  # Restringe x2 <= 25 (turismo)
        [0, 0, -1], # Restringe x3 >= 15 (conservação) -> -x3 <= -15
        [1, 1, 1],  # Restringe x1 + x2 + x3 <= 100 (total de recursos)
        [-1, 0, 0], # Restringe x1 >= 10 (pesca) -> -x1 <= -10
        [0, -1, 0]  # Restringe x2 >= 5 (turismo) -> -x2 <= -5
    ]

    # Lado direito das desigualdades (valores das restricoes)
    b = [40, 25, -15, 100, -10, -5]

    # As variaveis nao podem ser negativas
    x_bounds = (0, None)
    bounds = [x_bounds, x_bounds, x_bounds]

    # Realizando a otimizacao
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return res

#funcao para imprimir mensagem com os dados das funcoes
def print_resultados(res, tamanho, valor_pescaria, valor_turismo, valor_meio_ambiente):
    # Caso a otimizacao tenha sucesso
    if res.success:
        # Calcula o valor da area utilizando dados ficticios
        valor_area = calcular_valor_area_marinha(tamanho, valor_pescaria, valor_turismo, valor_meio_ambiente)
        print(f"\nValor econômico mensal estimado da área marinha: ${valor_area:.2f}")

        # proporcao recomendada seguindo calculo linear do livro "Marine Conservation: Science, Policy, and Management"
        print(f'Solução otimizada encontrada')
        print(f'Pesca (x1): {res.x[0]:.2f} unidades alocadas para área')  
        print(f'Turismo (x2): {res.x[1]:.2f} unidades alocadas para área')  
        print(f'Conservação (x3): {res.x[2]:.2f} unidades alocadas para área')  

        # Valor monetário total da função objetivo maximizada
        valor_otimizacao = -res.fun
        print(f'Valor da otimização objetiva por mês em dólares: ${valor_otimizacao:.2f}')

        # Valor mensal total destinado à gestão da área marinha e seus recursos
        valor_mensal_total = valor_otimizacao + valor_area
        print(f'Valor mensal total destinado à gestão da área marinha e seus recursos: ${valor_mensal_total:.2f}')
        
    else:
        # Se não foi encontrada uma solução viável
        print('Nenhuma solução viável foi encontrada.')

# Dados ficticios para area
tamanho = 1000000  # 1000000 m^2 
valor_pescaria = 500000  # $500000
valor_turismo = 200000  # $200000
valor_meio_ambiente = 100000  # $1000000

# Executa todas as funcoes
otimizacao = otimizar_alocacao_recursos()
print_resultados(otimizacao, tamanho, valor_pescaria, valor_turismo, valor_meio_ambiente)
