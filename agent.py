import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from schemas import RelatorioPesquisa

load_dotenv()

class EstadoAgente(TypedDict):
    tema: str
    relatorio: RelatorioPesquisa | None

llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.2)
llm_estruturado = llm.with_structured_output(RelatorioPesquisa)

def gerar_relatorio_node(state: EstadoAgente):
    tema = state["tema"]
    prompt = f"Crie um relatório de pesquisa detalhado sobre o seguinte tema: {tema}."
    resultado = llm_estruturado.invoke(prompt)
    return {"relatorio": resultado}

workflow = StateGraph(EstadoAgente)
workflow.add_node("gerar_relatorio", gerar_relatorio_node)
workflow.add_edge(START, "gerar_relatorio")
workflow.add_edge("gerar_relatorio", END)

app_grafo = workflow.compile()

# ==========================================================
# 🧪 BLOCO DE TESTE 
# ==========================================================
if __name__ == "__main__":
    print("🧪 Testando o agente diretamente pelo terminal...")
    
    estado_teste = {
        "tema": "O futuro dos carros elétricos",
        "relatorio": None
    }
    
    resposta = app_grafo.invoke(estado_teste)

    print("\n--- TESTE CONCLUÍDO COM SUCESSO ---")
    relatorio = resposta["relatorio"]
    print(f"Título: {relatorio.titulo}")
    print(f"Resumo: {relatorio.resumo[:120]}...")
    print(f"Pontos-chave encontrados: {len(relatorio.pontos_chave)}")