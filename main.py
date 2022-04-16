#execute "pip install sqlalchemy" antes do primeiro uso

from tokenize import Number
from sqlalchemy import BigInteger
from inter_soc_amb.find_intersections import Api_functions
# # 1278194
# # 846730
# print('Digite o identificador da apolice a ser verificada: ')
# id_proposta = int(input())
# find_inter_soc = Api_functions(id_proposta)
# find_inter_soc._find_intersections()

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    id_proposta: int


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/findInter/")
async def find_intersection(item: Item):
    item_dict = item.dict()
    if item.id_proposta:
        api_func = Api_functions(item.id_proposta)
        answer = api_func._find_intersections()
        
    return answer