from pydantic import BaseModel, Field

class RelatorioPesquisa(BaseModel):
    titulo: str = Field(description="Título claro e chamativo para o relatório")
    resumo: str = Field(description="Resumo detalhado do tema abordado")
    pontos_chave: list[str] = Field(description="Lista com 3 a 5 pontos mais importantes")
    conclusao: str = Field(
        default="Conclusão elaborada com base na análise geral do tema.", 
        description="Conclusão objetiva sobre o assunto"
    )