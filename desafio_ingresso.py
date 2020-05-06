import requests as rq
import json
import pandas as pd
pd.set_option("display.max_columns", 10)
url="https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=9a567130d6089d3751f304a5643eacc808572d89"

r=rq.get(url)
obj_json=json.loads(r.text)

with open("\\Users\\Alberto\\Desktop\\code_nation\\curso_python\\answer.json", 'w') as output: 
   output.write(json.dumps(obj_json))
   
dados = pd.read_json("answer.json", lines=True)   
dados.columns
n_casas=dados["numero_casas"].loc[0]
dados["cifrado"]
dados["decifrado"]

alfabeto="abcdefghijklmnopqrstuvwxyz"

alfabeto.find("b")
string_decifrada=""
for i in dados["cifrado"].loc[0]:
    if i in alfabeto:
        pos=alfabeto.find(i)-n_casas
        string_decifrada=string_decifrada+alfabeto[pos]
    else:
        string_decifrada=string_decifrada+i
string_decifrada 
dados["decifrado"]=string_decifrada


#Algoritmo Shal
import hashlib
dados["decifrado"].loc[0].encode("utf-8")
shal=hashlib.sha1(dados["decifrado"].loc[0].encode("utf-8"))
shal.hexdigest()
dados["resumo_criptografico"]=shal.hexdigest()

dados.to_dict("records")[0]
with open("\\Users\\Alberto\\Desktop\\code_nation\\curso_python\\answer.json", 'w') as output: 
   output.write(json.dumps(dados.to_dict("records")[0]))

url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=9a567130d6089d3751f304a5643eacc808572d89'
#Duas formas de fazer
files = {'answer': open('answer.json', 'rb')}
files = dict(answer = open('answer.json', 'rb'))  

r=rq.post(url=url, files=files)
r.text
r.content