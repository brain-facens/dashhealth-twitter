# 
# __Análise de Tweets Sobre "Sáude" de Sorocaba__

## __Descrição Técnica__
Projeto no qual o objetivo é analisar o conteúdo de tweets sobre saúde na região de Sorocaba e apresentar visualmente em um dashboard os resultados encontrados.[em Python3.8](#)

## __Teoria__

### **Python 3 e suas bibliotecas**
[Python 3](https://docs.python.org/3/tutorial/index.html) é uma linguagem de programação, e utiliza identações para diferenciar seu contexto de execução. Neste projeto, ela foi utilizada para obter os dados da API do Twitter e gerar um Dashboard com os resultados obtidos. Neste projeto foram utilizados algumas bibliotecas do Python3: [Dash](https://plotly.com/dash/),[pyngrok](https://pypi.org/project/pyngrok/) e [wordcloud](https://amueller.github.io/word_cloud/). As bibliotecas de mais importancia e seu motivo para serem utilizadas serão explicados mais a frente no passo a passo. 

## __Guia de Instalação__
Instale o requirements.txt:

```
pip install -r requirements.txt
```

## __Guia de Implementação__
Primeiramente, o usuário deve criar uma conta n
## __Fotos__
![WhatsApp Image 2021-12-07 at 15 26 16](https://user-images.githubusercontent.com/87439511/145266062-35e08866-8b88-418a-9f88-7d3008a9e9ca.jpeg)
![grafico de dispersao](https://user-images.githubusercontent.com/87439511/145267200-919db758-b1ee-4f90-bb6f-0bec283a3678.jpeg)

![nuvem de palavra](https://user-images.githubusercontent.com/87439511/145267280-29c1f88f-6588-47c8-8987-fa711f94ed5f.jpeg)

![analise semanal](https://user-images.githubusercontent.com/87439511/145267331-2953bf0c-67b4-484f-a7a4-ba37507162e7.jpeg)

Para realizar a Captura dos Tweets utiliza-se o script api_twitter.py
Depois de gerados os arquivos do api_twitter.py, utilize o script api_dashboard.py para gerar o dashboard.
Os arquivos devem ser gerados semanalmente.
