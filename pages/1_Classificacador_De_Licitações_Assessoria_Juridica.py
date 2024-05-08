import streamlit as st
from pathlib import Path
from joblib import load


path_model = Path(__file__).parent.parent / "ml/classificador_assessoria.joblib"
path_tfidf = Path(__file__).parent.parent / "ml/vetorizador.joblib"

st.title('Executar Modelo')

with open (path_model,"rb") as arquivo:
    modelo = load(arquivo)

with open (path_tfidf,"rb") as arquivo:
    vetorizar = load(arquivo)


      
objeto_licitacao = st.text_area("Objeto da Licitação", value="", label_visibility="visible")


if st.button("Classificar Licitação", key="clear", type="primary"):
  txt = objeto_licitacao.lower()
  vetorizar = load(path_tfidf)
  texto_vetorizado = vetorizar.transform([txt])
  modelo =load(path_model)
  # Suponha que `dados_teste` sejam seus dados de teste
  resultado = modelo.predict(texto_vetorizado)
  classificacao = ""
  cor=""
  if resultado == 1:
     classificacao = "Assessoria Jurídica"
     cor = "#33ff33"
  else:
     classificacao = "Não é Assessoria Jurídica"
     cor = "#ff0000"

  st.write("")
  st.markdown(f'<p style="background-color:{cor};font-size:24px;border-radius:2%;">{classificacao}</p>', unsafe_allow_html=True)
  objeto_licitacao=""
      