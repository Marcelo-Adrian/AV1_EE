# Simulação de Consumo de Energia e Emissões de CO2

Este projeto aborda a análise de um sistema energético de referência (RES) para avaliar cenários de consumo de energia e impactos de eletrificação no transporte. Ele projeta o consumo energético de 2023 a 2030, considerando dois cenários principais:

- **Cenário Business as Usual (BaU):** Projeção do consumo com base no crescimento médio dos anos anteriores.
- **Cenário de Eletrificação do Transporte:** Impactos da introdução de veículos elétricos no consumo de energia elétrica e emissões de CO2.

## Estrutura do Projeto

1. **Entradas:**

   - Dados do Balanço Energético Nacional (BEN) de 2020, 2021 e 2022.
   - Consumo de energia para transporte rodoviário de pessoas (gasolina e álcool) e carga (diesel e biodiesel).
   - Demanda de eletricidade por fonte em TEP.

2. **Cenários Simulados:**

   - **BaU:** Crescimento médio anual dos anos passados.
   - **Eletrificação:** Introdução de veículos elétricos, considerando parcelas `p%` para transporte de pessoas e `q%` para transporte de carga.

3. **Resultados Gerados:**
   - Projeções de consumo de energia por setor.
   - Impactos no custo dos combustíveis e emissões de CO2.
   - Gráficos de evolução do consumo de energia e emissões.

## Tecnologias Utilizadas

- **Linguagem de Programação:** Python
- **Visualização de Dados:** Matplotlib
- **Cálculos e Projeções:** Baseados em equações do sistema energético de referência.
