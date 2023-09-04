import xmltodict
import os
import pandas as pd

def pegar_infos(nome_arquivo, valores):
    #print(f'pegar arquivo {nome_arquivo}')
    with open(f'nfs/{nome_arquivo}',"rb") as arquivo_xml: #o "r" significa que é formato leitura
        dic_arquivo = xmltodict.parse(arquivo_xml)
       # print(json.dumps(dic_arquivo, indent=4)) #facilita e melhora o formato de leitura com indentação
        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo["NFe"]['infNFe']
        else:
            infos_nf = dic_arquivo["nfeProc"]["NFe"]['infNFe']
        numero_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf['emit']['xNome']
        cnpj_empresa = infos_nf['emit']['CNPJ']
        nome_cliente = infos_nf['dest']['xNome']
        endereco = infos_nf['dest']['enderDest']
        if "vol" in infos_nf['transp']:
            peso_bruto = infos_nf['transp']['vol']['pesoB']
        else:
            peso_bruto = 'Peso nao informado'
        valores.append([numero_nota, empresa_emissora, cnpj_empresa, nome_cliente, endereco, peso_bruto])

lista_arquivos = os.listdir("nfs")

colunas = ["numero_nota", "empresa_emissora", "cnpj_empresa", "nome_cliente", "endereco", "peso_bruto"]
valores = []

for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)
    
tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel("Conversor_de_notas.xlsx", index=False) #index=false pq o indice normalmente aparece como uma coluna de indice por padrao no python
