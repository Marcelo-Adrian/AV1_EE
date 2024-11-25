import matplotlib.pyplot as plt

def calcular_demanda_atual():
    # Dados de consumo de energia para transporte (em TEP) de 2020 a 2022
    transporte_pessoas = [47102, 49264, 50403]  # Energia usada para transporte de pessoas
    transporte_carga = [47924, 51539, 53091]  # Energia usada para transporte de carga
    anos = 3
    inicio_ano = 2020
    
    # Energia total do setor de transporte (pessoas + carga)
    energia_total_transporte = [
        transporte_pessoas[i] + transporte_carga[i] 
        for i in range(anos)
    ]

    # Exibição da energia total para transporte para cada ano
    print("Energia total de transporte (em TEP) para cada ano:")
    for i in range(anos):
        print(f"{inicio_ano + i}: {energia_total_transporte[i]:.3f} TEP")
    
    # Retorna os anos e os valores calculados
    anos_lista = [inicio_ano + i for i in range(anos)]
    return anos_lista, energia_total_transporte


def projetar_demanda_com_veiculos_eletricos(energia_total_transporte, p, q):
    # Estimativa de crescimento médio da demanda de energia
    crescimento_2021 = (energia_total_transporte[1] - energia_total_transporte[0]) / energia_total_transporte[0]
    crescimento_2022 = (energia_total_transporte[2] - energia_total_transporte[1]) / energia_total_transporte[1]
    crescimento_medio = (crescimento_2021 + crescimento_2022) / 2

    # Projeção de demanda de energia para os próximos anos
    energia_atual = energia_total_transporte[2]
    anos_projecao = [2023]  # Inicia projeção a partir de 2023
    energia_projetada = [energia_atual * (1 + crescimento_medio)]  # Valor de 2023
    energia_total_com_eletricos = [energia_projetada[0] * (1 + (p + q) / 100)]  # Projeção de 2023 com eletrificação

    print("\nProjeção de consumo de energia com eletrificação:")
    print(f"2023 (sem eletrificação): {energia_projetada[0]:.3f} TEP")
    print(f"2023 (com eletrificação): {energia_total_com_eletricos[0]:.3f} TEP")
    
    # Projeções para os anos seguintes
    for ano in range(2024, 2031):
        energia_atual = energia_projetada[-1] * (1 + crescimento_medio)
        energia_projetada.append(energia_atual)
        
        # Calculando o impacto da eletrificação para cada ano
        energia_eletrica_pessoas = energia_projetada[-1] * p / 100
        energia_eletrica_carga = energia_projetada[-1] * q / 100
        energia_total_com_eletricos.append(energia_projetada[-1] + energia_eletrica_pessoas + energia_eletrica_carga)
        
        anos_projecao.append(ano)
        print(f"{ano} (sem eletrificação): {energia_projetada[-1]:.3f} TEP")
        print(f"{ano} (com eletrificação): {energia_total_com_eletricos[-1]:.3f} TEP")
    
    # Retorna os anos projetados e os valores projetados
    return anos_projecao, energia_projetada, energia_total_com_eletricos


def plotar_graficos(anos, energia_total_transporte, anos_projecao, energia_projetada, energia_total_com_eletricos):
    # Gráfico de energia total de transporte e projeções
    plt.figure(figsize=(10, 6))

    # Dados históricos
    plt.plot(anos, energia_total_transporte, marker='o', label="Energia Total de Transporte (Histórico)", color="blue")

    # Conexão entre 2022 e 2023 (pontilhada)
    plt.plot([anos[-1], anos_projecao[0]], [energia_total_transporte[-1], energia_projetada[0]], 
             linestyle="--", color="orange")

    # Projeções futuras
    plt.plot(anos_projecao, energia_projetada, marker='o', linestyle="--", label="Projeção de Energia sem Eletrificação", color="orange")
    plt.plot(anos_projecao, energia_total_com_eletricos, marker='o', linestyle="--", label="Projeção de Energia com Eletrificação", color="green")

    # Configurações do gráfico
    plt.title("Impacto da Eletrificação do Transporte no Consumo de Energia Total (em TEP)", fontsize=14)
    plt.xlabel("Ano", fontsize=12)
    plt.ylabel("Energia (TEP)", fontsize=12)
    plt.xticks(range(2020, 2031))
    plt.legend(fontsize=10)
    plt.grid(alpha=0.5)
    plt.tight_layout()

    # Exibe o gráfico
    plt.show()


def main():
    # Calcula a energia total para transporte
    anos, energia_total_transporte = calcular_demanda_atual()

    # Parâmetros p (percentual de eletrificação para pessoas) e q (percentual para carga)
    p = 30 
    q = 20

    # Projeta a demanda com eletrificação
    anos_projecao, energia_projetada, energia_total_com_eletricos = projetar_demanda_com_veiculos_eletricos(
        energia_total_transporte, p, q
    )

    # Plota os gráficos
    plotar_graficos(anos, energia_total_transporte, anos_projecao, energia_projetada, energia_total_com_eletricos)


if __name__ == "__main__":
    main()
