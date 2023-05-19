from fastapi import APIRouter, HTTPException
from app.schemas.schemas import Filme
from app.db.db import collection 
'''add_filme'''


router = APIRouter()

@router.post("/filmes")
async def add_filmes(filme: Filme):
    result = await collection.insert_one(filme.dict())
    filme_id = str(result.inserted_id)
    return {"id": filme_id, **filme.dict()}


@router.get("/filmes")
async def get_filmes():
    filmes = []
    cursor = collection.find()
    async for document in cursor:
        document.pop('_id', None)
        filmes.append(Filme(**document))

    return filmes


@router.get("/filmes/{nome_filme}")
async def get_filme_by_name(nome_filme: str):
    filme = await collection.find_one({"nome":nome_filme.capitalize()})
    if filme:
        filme.pop('_id', None)
        return Filme(**filme)

    else:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    


@router.put("/filmes/{nome_filme}")
async def put_filme(nome_filme:str, filme:Filme):
    result = await collection.update_one({"nome": nome_filme.capitalize()}, {"$set": filme.dict()})
    if result.modified_count == 1:
        return {"message": f"Filme '{nome_filme}' atualizado com sucesso!"}
    else:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    

@router.delete("/filmes/{nome_filme}")
async def delete_filme(nome_filme:str):
    result = await collection.delete_one({"nome":nome_filme.capitalize()})
    if result.deleted_count == 1:
        return {"message":f"Filme {nome_filme} deletado com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Filme não encontrado")










# metodo alternativo
'''
@router.post('/filmes', response_model=Filme)
async def post_filme(filme:Filme):
    result = await add_filme(filme.dict())
    if result:
        return result
    raise HTTPException(400, "Something went wrong")
'''
