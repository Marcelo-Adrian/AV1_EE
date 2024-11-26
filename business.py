import matplotlib.pyplot as plt

def calcular_energia_total():
    # Dados de consumo de energia (em TEP)
    gasolina = [20166, 22137, 24227]
    alcool = [15346, 14848, 15165]
    diesel = [42950, 46300, 48188]
    biodiesel = [4974, 5239, 4903]
    eletricidade = [47102, 49264, 50403]
    anos = 3
    inicio_ano = 2020

    # Cálculo da energia total por ano
    energia_total = [
        gasolina[i] + alcool[i] + diesel[i] + biodiesel[i] + eletricidade[i]
        for i in range(anos)
    ]

    # Exibição da energia total para cada ano
    print("Energia total (em TEP) para cada ano:")
    for i in range(anos):
        print(f"{inicio_ano + i}: {energia_total[i]:.3f} TEP")
    
    # Retorna os anos e os valores calculados
    anos_lista = [inicio_ano + i for i in range(anos)]
    return anos_lista, energia_total


def projetar_consumo(energia_total):
    # Dados para projeção
    crescimento_2021 = (energia_total[1] - energia_total[0]) / energia_total[0]
    crescimento_2022 = (energia_total[2] - energia_total[1]) / energia_total[1]
    crescimento_medio = (crescimento_2021 + crescimento_2022) / 2

    # Projeção de consumo de energia para os anos futuros (incluindo 2023)
    energia_atual = energia_total[2]
    anos_projecao = [2023]  # Inicia projeção a partir de 2023
    energia_projetada = [energia_atual * (1 + crescimento_medio)]  # Valor de 2023

    print("\nProjeção de consumo de energia (em TEP):")
    print(f"2023: {energia_projetada[0]:.3f} TEP")
    for ano in range(2024, 2031):
        energia_atual = energia_projetada[-1] * (1 + crescimento_medio)
        anos_projecao.append(ano)
        energia_projetada.append(energia_atual)
        print(f"{ano}: {energia_atual:.3f} TEP")
    
    # Retorna os anos projetados e os valores projetados
    return anos_projecao, energia_projetada


def plotar_graficos(anos, energia_total, anos_projecao, energia_projetada):
    # Gráfico de energia total e projeções
    plt.figure(figsize=(10, 6))

    # Dados históricos
    plt.plot(anos, energia_total, marker='o', label="Energia Total (Histórico)", color="blue")

    # Conexão entre 2022 e 2023 (pontilhada)
    plt.plot([anos[-1], anos_projecao[0]], [energia_total[-1], energia_projetada[0]], 
             linestyle="--", color="orange")

    # Projeções futuras
    plt.plot(anos_projecao, energia_projetada, marker='o', linestyle="--", label="Projeção de Energia", color="orange")

    # Configurações do gráfico
    plt.title("Consumo de Energia Total e Projeções (em TEP)", fontsize=14)
    plt.xlabel("Ano", fontsize=12)
    plt.ylabel("Energia (TEP)", fontsize=12)
    plt.xticks(range(2020, 2031))
    plt.legend(fontsize=10)
    plt.grid(alpha=0.5)
    plt.tight_layout()

    # Exibe o gráfico
    plt.show()


def main():
    # Calcula a energia total
    anos, energia_total = calcular_energia_total()

    # Projeta o consumo de energia (inclui 2023)
    anos_projecao, energia_projetada = projetar_consumo(energia_total)

    # Plota os gráficos
    plotar_graficos(anos, energia_total, anos_projecao, energia_projetada)


if __name__ == "__main__":
    main()