import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide") # para as coisas ficarem na largura toda

st.title("Análise de informações de livros")
st.header("Entendendo melhor os livros da Amazon!")

df_reviews = pd.read_csv(r"C:\Users\adrianab\Projetos\Analise_dados\datasets\customer reviews.csv")
df_books = pd.read_csv(r"C:\Users\adrianab\Projetos\Analise_dados\datasets\Top-100 Trending Books.csv")

#colocar o mesmo nome de coluna com nome do livro nas duas tabelas
df_reviews.rename(columns={'book name': 'book title'}, inplace=True) #agora nas duas tabelas usaremos book title

#st.write(df_books) #imprimir na tela do streamlit a tabela com os preços

price_max = df_books["book price"].max() # selecionando o preço máximo
price_min = df_books["book price"].min() # selecionando o preço máximo

price_slider = st.slider( #esse é o preço selecionado no slider do streamlit
"Selecione o preço desejado", # Texto exibido acima do slider
min_value=int(price_min), #preço mínimo
max_value=int(price_max), #preço máximo
value=int(price_max) # Valor inicial
)

df_filtro_slider = df_books[df_books["book price"] <= price_slider] #o preço selecionado no slider vai filtrar o dataframe
st.write(df_filtro_slider) #mostrar o dataframe filtrado

fig1 = px.bar(df_filtro_slider['year of publication'].value_counts())
fig2 = px.histogram(df_filtro_slider, x='rating')

#st.plotly_chart(fig1) #se usar essa opção o gráfico fica na largura toda da pagina
#st.plotly_chart(fig2)

col1, col2 = st.columns(2) #essa opção divide em colunas
col1.plotly_chart(fig1, key="fig1_col1") #coloca cada figura em uma coluna
col2.plotly_chart(fig2, key="fig2_col2")