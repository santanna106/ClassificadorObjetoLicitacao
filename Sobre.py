import streamlit as st 


st.title('🏢 Classificador de Objeto da Licitação ')

st.header('Descrição do Aplicativo')
st.write(
    """
        As compras, locações, prestações de serviços - incluindo os técnico-profissionais especializados,
        contratações de obras de arquitetura e engenharia; contratações de tecnologia da informação e comunicação, 
        concessões e permissão de uso de bens públicos [REF01]  
        precisam passar por procedimentos administrativos formais chamados de Licitações [REF02]. Estes procedimentos 
        devem obedecer às normas gerais da lei 14.133, de abril de 2021 observando os princípios da legalidade, da impessoalidade, da moralidade,
        da publicidade, do interesse público e da probidade administrativa.[REF03]. Desta forma,
        todo o processo que envolva contratações pelo serviço público estão sujeitos às fiscalizações da sociedade civil,
        do Tribunais de Contas e dos ministérios públicos estaduais e federais.  

    """) 

st.write(
    """
        As fiscalizações objetivam identificar irregularidades, mau uso do dinheiro público,
        além de embasar investigações de atos corruptos que podem causar grandes prejuízos sociais.
        Com o objetivo de apoiar a análise das compras e aquisições do estado da Bahia, o Ministério Público 
        estadual desenvolveu o BI Licitômetro. Esta ferramenta possibilita o desenvolvimento de várias análises sobre os 
        processos de compras firmados pelos órgãos públicos do estado da Bahia.

    """) 


st.write(
    """
        Uma das funcionalidades do Licitômetro é agrupar as licitações através da descrição dos objetos
        que motivaram a criação dos processos de compra. Essa classificação é baseada atualmente em palavras chave.
        A utilização das palavras chave como critério de classificação tem gerado incoerências na determinação das 
        classes dos objetos licitados. Pois, em muitas descrições a palavra chave está presente. Porém, o objeto licitado
        não corresponde ao que está sendo classificado pelo filtro. Diante deste problema foi avaliado a dificuldade em 
        aperfeiçoar o filtro perante o volume de licitações que necessitam ser classificadas e da flexibilidade existente
          na descrição das licitações  para realização de uma classificação mais aderente ao que foi contratado pelos órgãos 
          públicos. Essa realidade motivou o estudo para aplicar um algoritmo de classificação de 
          Machine Learning para realização das classificações dos Objetos das Licitações. 
          Pois, traria um método com mais flexibilidade para reconhecer os tipos de objetos licitados através das técnicas de 
          Processamento de Linguagem Natural.
        
    """) 




st.subheader('Equipe')

st.markdown("""
            <ul>
                <li>Gabriel Andrade de Sant'Anna</li>
                <li>Rubia Teles de Souza</li>
                <li>Ludmilla Palmeira Andrade</li>
            </ul>
""", unsafe_allow_html=True)