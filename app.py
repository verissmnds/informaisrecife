import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Análise das Mídias Informais de Recife", page_icon="📐", layout="wide")

df = pd.read_csv('Bruna.colab.csv', delimiter = ";")
display(df)
