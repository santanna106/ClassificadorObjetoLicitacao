import streamlit as st 
import pandas as pd
import numpy as np
from transformers import pipeline

def load_model():
    return pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")
st.header('Classificação de Assessoria Jurídica')

classifier = load_model()

st.divider()
# Entrada do usuário para o texto
input_text = st.text_area("Entre com o texto que deseja classificar", "")
# Definição do tópico
topic_description ="serviços de assessoramento jurídico e serviços advocatícios e consultoria juridica"
#topic_description = "serviços de assessoramento jurídico, serviços advocatícios, consultoria jurídica e despesas com contratação de serviços advocatícios e de assessoramento jurídico"

if st.button("Classifica"):
    if input_text:
        # Classificação
        result = classifier(input_text, [topic_description], hypothesis_template="Este texto é sobre {}.")
        score = result['scores'][0]

        if score > 0.80:
            resultado = "É assessoria Jurídica"
        else:
            resultado = "Não é Assessoria Jurídica"
        st.write(resultado)
        #st.write("Resultado")
    else:
        st.write("Please enter text to classify.")