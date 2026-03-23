# Análise de Acidentes de Trânsito com Random Forest

## Descrição do Projeto

Este repositório apresenta a aplicação do modelo Random Forest para análise de dados de acidentes de trânsito registrados pela Polícia Rodoviária Federal (PRF) no estado da Paraíba. O estudo foi desenvolvido com o objetivo de explorar padrões nos dados, identificar relações entre variáveis e realizar a classificação da gravidade dos acidentes a partir das características observadas.

A implementação completa da análise está disponível no notebook:
👉 **https://github.com/Fabiano01EST/generalized-linear-models/blob/main/random_forest.ipynb**

---

## Base de Dados

Os dados utilizados correspondem a registros de acidentes de trânsito ocorridos no estado da Paraíba, contendo informações sobre características dos envolvidos, condições do acidente e variáveis associadas à severidade.

O conjunto de dados reúne variáveis como sexo, tipo de envolvido, condição meteorológica, fase do dia, uso do solo e tipo de pista, permitindo analisar fatores associados à classificação dos acidentes em três categorias: **Com Vítimas Fatais**, **Com Vítimas Feridas** e **Sem Vítimas**.

---

## Estrutura da Análise

A análise foi conduzida de forma sequencial, contemplando as seguintes etapas:

### 1. Preparação dos Dados

Inicialmente, foi realizada a organização da base, incluindo:

- Tratamento de valores ausentes;
- Ajuste de tipos das variáveis;
- Codificação de variáveis categóricas;
- Divisão em conjuntos de treino (75%) e teste (25%) com estratificação pela variável resposta.

### 2. Análise Exploratória

Na etapa exploratória, foram utilizadas medidas descritivas e visualizações gráficas com o objetivo de compreender o comportamento das variáveis e a distribuição das classes.

Essa etapa permitiu identificar o desbalanceamento entre as categorias da variável resposta, com predominância da classe Com Vítimas Feridas, contribuindo para uma melhor compreensão do problema de classificação.

### 3. Modelagem

A modelagem foi realizada utilizando o algoritmo Random Forest, composto por 300 árvores de decisão com profundidade máxima de 8 níveis. O modelo foi ajustado com balanceamento de classes via `class_weight="balanced"`, de forma a lidar com o desequilíbrio observado entre as categorias.

O ajuste foi conduzido buscando representar adequadamente a relação entre as características observadas e a probabilidade de ocorrência das classes da variável resposta.

### 4. Avaliação

Após o ajuste do modelo, foram analisados:

- A matriz de confusão;
- Métricas de desempenho, como acurácia e AUC-ROC;
- As curvas ROC pelo método One-vs-Rest para cada classe;
- A importância das variáveis pela diminuição média da impureza de Gini.

Essa etapa permitiu avaliar a capacidade preditiva do modelo e verificar a consistência das classificações realizadas.

---

## Organização do Repositório

- `random_forest_acidentes.py`: contém toda a implementação da análise, incluindo preparação dos dados, modelagem e avaliação dos resultados.

---

## Considerações

Este projeto possui caráter aplicado, com foco na utilização de métodos de aprendizado de máquina para análise de dados reais. A abordagem adotada permite identificar fatores associados à gravidade dos acidentes de trânsito e fornece uma base estruturada para aplicações futuras em problemas de classificação multiclasse.

---

**Autor:** Fabiano F. Santos
