import pandas as pd
from pysentimiento import create_analyzer
import plotly.express as px

df_reviews = pd.read_csv(r"C:\Users\adrianab\Projetos\Analise_dados\datasets\customer reviews.csv")
df_books = pd.read_csv(r"C:\Users\adrianab\Projetos\Analise_dados\datasets\Top-100 Trending Books.csv")

analyzer = create_analyzer(task="sentiment", lang="en")

sentimentos = []
probabilidades = []

for index, line in df_reviews.iterrows():
  resposta = analyzer.predict(line["review description"])
  sentimento = resposta.output
  sentimentos.append(sentimento)
  probabilidade = resposta.probas[sentimento]
  probabilidades.append(probabilidade)
  
df_reviews['sentimento'] = sentimentos  
df_reviews['probabilidade'] = probabilidades

mapeamento = {'POS': 1, 'NEU': 0, 'NEG': -1}
df_reviews['sentimento_numerico'] = df_reviews['sentimento'].map(mapeamento)

df_reviews.to_excel('df_reviews_mapeado.xlsx', index=False)