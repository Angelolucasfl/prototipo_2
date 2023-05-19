from pydantic import BaseModel
from typing import Optional

class Filme(BaseModel):
    nome: str
    nota: float
    ano: Optional[int] = None
    sinopse: Optional[str] = None
    genero:  Optional[str] = None

    def capitalize_nome(self):
        self.nome = self.nome.capitalize()

    def __init__(self, nome:str, nota:float, ano:int, sinopse:str, genero:str):
        super().__init__(nome=nome, nota=nota, ano=ano, sinopse=sinopse, genero=genero)
        self.capitalize_nome()
