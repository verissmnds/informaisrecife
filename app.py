import streamlit as st
import pandas as pd
import numpy as np
import re  # Add this line to import the 're' module

st.set_page_config(page_title="Análise das Mediações Informais de Recife", page_icon="📐", layout="wide")

df = pd.read_csv('Bruna.colab.csv', delimiter=";")

# Lista de temas
politica = '"João Campos"|"secretaria"|"Túlio Gadelha"|"Marília Arraes"|"João Paulo"|"Priscila Krause"|"Daniel Coelho"|"prefeito"|"prefeita"|"prefeitura"'
infraestrutura = r'\bconstrução|integral|asfalto|bueiro|esgoto|energia|perigo|limpeza|chuva|barreira|lixo\b'
seguranca = r'\bseguran[çc]a|crime|morre|agre.|pol.cia|assalto|roubo|morto|morte|matou|furto|tráfico|droga|assassinato|assassino|assassinar|assassina|assassinei?s?|assassinaram\b'
denuncias = r'moradores|moradoras|Moradores'


def remove_hashtags(message):
    return re.sub(r'#\w+', '', message)

df['Message'] = df['Message'].apply(remove_hashtags)

# Condições
condicoes = [df['Message'].str.contains(politica, na=False, case=False, regex=True),
             df['Message'].str.contains(infraestrutura, na=False, case=False, regex=True),
             df['Message'].str.contains(seguranca, na=False, case=False, regex=True),
             df['Message'].str.contains(denuncias, na=False, case=False, regex=True)]

# Escolhas
choices = ['Política', 'Infraestrutura', 'Segurança', 'Denúncias']

# Cria a variável TEMAS
df['Temas'] = np.select(condicoes, choices, default='Outros')

df2 = df[['Profile', 'Date', 'Message', 'Number of Reactions, Comments & Shares', 'Temas', 'Link']]


def main():
    st.title('Análise de Mediações Informais da cidade do Recife.')
    st.caption('Por Bruna Verissimo, graduanda em Comunicação Digital na Fundação Getúlio Vargas')

    st.header("Todas as publicações analisadas")
    st.dataframe(df)

    st.header("As 10 publicações com mais engajamento")
    st.markdown("Elas estão organizadas em ordem decrescente, da maior para a menor")
    st.dataframe(df2.sort_values(by='Number of Reactions, Comments & Shares', ascending=False).head(10))

    st.header('Infraestrutura')
    st.markdown("Aqui estão as publicações relacionadas ao tema Infraestrutura")
    st.dataframe(df2[df2['Temas'] == 'Infraestrutura'])

    st.header('Segurança')
    st.markdown("Aqui estão as publicações relacionadas ao tema Segurança")
    st.dataframe(df2[df2['Temas'] == 'Segurança'])

    st.header('Política')
    st.markdown("Aqui estão as publicações relacionadas ao tema Política")
    st.dataframe(df2[df2['Temas'] == 'Política'])

    st.header('Denúncias')
    st.markdown("Aqui estão as publicações relacionadas ao tema Denúncias")
    st.dataframe(df2[df2['Temas'] == 'Denúncias'])

    st.header('Nova 10coberta Ordinária')
    st.markdown("Aqui estão as publicações unicamente da página @novadescobertaordinaria")
    st.dataframe(df2[df2['Profile'] == 'NOVA 10COBERTA ORDINÁRIA'])


if __name__ == '__main__':
    main()
