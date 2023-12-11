# Verificação para a pergunta 1
# A base da a mesma informação de várias maneiras. Aqui generalizamos essas informações em uma só chave específica.
def verifica(inf):
    motivo = inf
    if 'PERECIMENTO' in inf or 'PERECIMENT' in inf or 'PERECIMEN' in inf:
        motivo = 'PERECIMENTO'
    elif 'EXPORTACAO' in inf or 'EXPORTADA' in inf or 'EXP' in inf or 'EXPORT' in inf:
        motivo = 'EXPORTAÇÃO'
    elif 'ACIDENTE' in inf or 'ACIDENTADA' in inf:
        motivo = 'ACIDENTE'
    elif 'MUD.DE MARCAS' in inf or 'MUDANCA' in inf or 'MUD.MARCAS' in inf or 'MUD.MARCA' in inf or 'MUD.DE MARCA' in inf:
        motivo = 'MUDANÇA DE MARCA'
    elif 'ASSUMIU' in inf:
        motivo = 'ASSUMIDO EM OUTRO ESTADO'
    elif 'DEVOLUCAO' in inf or 'DEVOLVIDA' in inf:
        motivo = 'DEVOLUÇÃO'
    elif 'PEDIDO' in inf or 'PEDIMENTO' in inf or 'SOLICITACAO' in inf:
        motivo = 'PEDIDO DO PROPRIETÁRIO'
    return motivo


# Elimina os motivos da questão 1 com 15 ou menos casos.
def elimina(dado):
    dic = dado
    eliminados = []
    for key, value in dic.items():
        f'{key}{value}'
        if value <= 15:
            eliminados.append(key)
    for x in range(len(eliminados)):
        dic.pop(eliminados[x])
    return dic


# Ordena o dicionário em ordem alfabética para as chaves str e do menor para o maior para as chaves int.
def org(dados):
    result = {}
    for key in sorted(dados.keys()):
        result[key] = dados[key]
    return result


# Organização de estados que não existem mais na questão 3.
def org_UF(uf):
    UF_nova = uf
    if 'GB' in UF_nova:
        UF_nova = 'RJ'
    return UF_nova


# Transforma o dicionário em duas listas correspondentes aos valores de x e y para a criação do gráfico de barras com eixo x/y independente.
def transformar(dicionario):
    x = []
    y = []
    dic = dicionario
    for key, value in dic.items():
        f'{key}{value}'
        x.append(key)
        y.append(value)
    xy = [x, y]
    return xy
