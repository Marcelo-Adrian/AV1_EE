# Avaliação 1 - Economia de Energia

Este projeto aborda a análise de um sistema energético de referência (RES) para avaliar cenários de consumo de energia e impactos de eletrificação no transporte. Ele projeta o consumo energético de 2023 a 2030, considerando dois cenários principais:

- **Cenário Business as Usual (BaU):** Projeção do consumo com base no crescimento médio dos anos anteriores.
- **Cenário de Eletrificação do Transporte:** Impactos da introdução de veículos elétricos no consumo de energia elétrica.

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
   - Gráficos de evolução do consumo de energia e emissões.

## Como executar:

- **Passo 1:** Clone o repositório.
   ```bash
   git clone https://github.com/Marcelo-Adrian/AV1_EE.git
   ```
- **Passo 2:** Inicie o ambiente virtual e ative-o.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

- **Passo 3:** Baixe os requerimentos.
   ```bash
   pip install matplotlib
   ```
- **Passo 4:** Selecione qual cenário executar.
   Caso deseje executar o cenário Business as Usual (BaU):
   ```bash
   python3 business.py
   ```
   Caso deseje executar o cenário de eletrificação:
   ```bash
   python3 eletric.py
   ```
- **Passo 5:** Desative o ambiente virtual.
   Caso deseje executar o cenário de eletrificação:
   ```bash
   deactivate
   ```

