import streamlit as st
import pandas as pd
from app import df_reviews
from app import df_books
import plotly.express as px
import openpyxl

df_mapeado = pd.read_excel("datasets/df_reviews_mapeado.xlsx")

books_names = df_books["book title"].unique() # Achando nomes unicos
book_name = st.sidebar.selectbox("Escolha um livro", books_names) # Colocando os nomes únicos na slide bar

# Fazendo o filtro no dataframe em função do nome do livro
chosed_book = df_books[df_books["book title"] == book_name] 
reviews_book = df_mapeado[df_mapeado["book title"] == book_name] #

# Do livro selecionado, queremos que apareça o nome, o preço, o gênero, a nota e o ano
book_title = chosed_book["book title"].iloc[0]
book_author = chosed_book["author"].iloc[0]
book_genre = chosed_book["genre"].iloc[0]
book_price = chosed_book["book price"].iloc[0]
book_rating = chosed_book["rating"].iloc[0]
book_year = chosed_book["year of publication"].iloc[0]

# Imprimindo no streamlit
st.title(book_title)
st.write(f"**Autor:** {book_author}")
st.write(f"**Gênero:** {book_genre}")
st.write(f"**Preço:** ${book_price:.2f}")
st.write(f"**Avaliação:** {book_rating}/5")
st.write(f"**Ano de Publicação:** {book_year}")

# Contar a frequência de cada sentimento
contagem_sentimentos = reviews_book['sentimento'].value_counts().reset_index()
contagem_sentimentos.columns = ['sentimento', 'sentimento_numerico']

# Criar o gráfico de barras
fig3 = px.bar(contagem_sentimentos,
             x='sentimento',
             y='sentimento_numerico',
             text='sentimento_numerico',
             labels={'sentimento': 'Sentimento', 'sentimento_numerico': 'Quantidade'},
             title='Distribuição dos Sentimentos das Reviews')

st.plotly_chart(fig3)

st.divider() # Colocar um divisor na tela
for _, line in reviews_book.iterrows():
  st.write(f"**Usuário:** {line['reviewer']}")
  st.write(f"**Título:** {line['review title']}")
  st.write(f"**Sentimento presente na avaliação:** {line['sentimento']}")
  st.write(f"**Descrição:** {line['review description']}")
  st.write(f"**Data:** {line['date']}")
  st.write("---")

