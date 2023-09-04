import xmltodict
import os
import json

def pegar_info(nome_arquivo):
    print(f'pegar arquivo {nome_arquivo}')
    with open(f'nfs/{nome_arquivo}',"rb") as arquivo_xml: #o "r" significa que é formato leitura
        dic_arquivo = xmltodict.parse(arquivo_xml)
       # print(json.dumps(dic_arquivo, indent=4)) #facilita e melhora o formato de leitura com indentação
        try: #vai verificar se consegue pegar todas as informações
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
            print(numero_nota, empresa_emissora, cnpj_empresa, nome_cliente, endereco, peso_bruto, sep="\n")
        except Exception as e: #caso nao consiga ele encontrar todas as informações ele vai mostrar o erro e os dados da nota
            print(e)
            print(json.dumps(dic_arquivo, indent=4)) #facilita e melhora o formato de leitura com indentação



lista_arquivos = os.listdir("nfs")

for arquivo in lista_arquivos:
    pegar_info(arquivo)
    #break