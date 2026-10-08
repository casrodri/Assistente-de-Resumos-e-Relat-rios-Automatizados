import streamlit as st
from agent import app_grafo

st.set_page_config(
    page_title="Relatório de Pesquisa com IA", 
    page_icon="🤖", 
    layout="centered"
)

st.title("🤖 Gerador de Relatórios com IA")
st.markdown("---")

tema_input = st.text_input("Tema da pesquisa:", "O impacto da Inteligência Artificial na educação")

if st.button("Gerar Relatório", type="primary"):
    if not tema_input.strip():
        st.warning("Digite um tema válido.")
    else:
        with st.spinner("Gerando relatório..."):
            estado_inicial = {"tema": tema_input, "relatorio": None}
            
            # Executa o grafo
            resposta_final = app_grafo.invoke(estado_inicial)
            relatorio = resposta_final["relatorio"]
            
            if relatorio:
                st.success("Relatório gerado.")
                st.markdown("---")
                
                # Título Principal
                st.markdown(f"## {relatorio.titulo}")
                st.markdown("---")
                
                # Seções limpas e diretas
                st.subheader("1. Resumo")
                st.write(relatorio.resumo)
                
                st.subheader("2. Pontos-Chave")
                for i, ponto in enumerate(relatorio.pontos_chave, 1):
                    st.markdown(f"**2.{i}.** {ponto}")
                
                st.subheader("3. Conclusão")
                st.write(relatorio.conclusao)
                
                st.markdown("---")
                st.caption("Stack: LangGraph | Pydantic | Groq | Streamlit")