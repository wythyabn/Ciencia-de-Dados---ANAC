# Discentes: < Equipe 2 >
# Francisco Israel Bezerra da Silva
# Victor Gabriel Alves da Costa
# Wythynny Ayane Batista Nogueira

# AVISO: Ao executar o código, para visualizar o próximo gráfico basta fechar o plotado no momento.
import json
import matplotlib.pyplot as plt
import funcoes

with open('dados_aeronaves.json', 'r', encoding='UTF-8-sig') as arq:
    base = json.load(arq)


# 1 - Indique os principais motivos de cancelamento de matrícula de aeronaves?
def perg1(dados):
    result = {}

    for linha in dados:
        motivo = linha['DSMOTIVOCANC']
        if motivo:
            mot = funcoes.verifica(motivo)
            if mot in result:
                result[mot] += 1
            else:
                result[mot] = 1
        else:
            motivo = 'MATRICULA NÃO CANCELADA'
            if motivo in result:
                result[motivo] += 1
            else:
                result[motivo] = 1
    result = funcoes.elimina(result)
    return result


# 2 - Quantas aeronaves foram registradas em cada ano no período de 2010 a 2020?
def perg2(dados):
    result = {}

    for linha in dados:
        ano = linha['DT_MATRICULA']
        if ano != '':
            ano = int(ano[:4])
            if 2010 <= ano <= 2020:
                if ano in result:
                    result[ano] += 1
                else:
                    result[ano] = 1
    ordem = funcoes.org(result)
    return ordem


# 3 - Quais os estados do Brasil que residem a maior quantidade de operadores de aeronave?
def perg3(dados):
    result = {}

    for linha in dados:
        uf = linha['UFOPERADOR']
        if uf:
            UF = funcoes.org_UF(uf)
            if UF in result:
                result[UF] += 1
            else:
                result[UF] = 1
    result_F = funcoes.org(result)
    return result_F


# 4 - Qual a quantidade de registros de aeronaves privadas, em que os proprietários vivem em São Paulo e no Rio de Janeiro
# no período de 2010 – 2022?
def perg4(dado):
    result_SP = {}
    result_RJ = {}

    for linha in dado:
        UF_prop = linha['SGUF']
        categ = linha['CDCATEGORIA']
        ano = linha['DT_MATRICULA']
        if categ and UF_prop:
            if categ != ' ' and ano != '':
                ano = int(ano[:4])
                if 'PRI' in categ and 2010 <= ano <= 2022:
                    if UF_prop == 'SP':
                        if ano in result_SP:
                            result_SP[ano] += 1
                        else:
                            result_SP[ano] = 1
                    elif UF_prop == 'RJ':
                        if ano in result_RJ:
                            result_RJ[ano] += 1
                        else:
                            result_RJ[ano] = 1
    result_SP = funcoes.org(result_SP)
    result_RJ = funcoes.org(result_RJ)
    result_F = [result_SP, result_RJ]
    return result_F


# 5 - Quais fabricantes possuem a maior quantidade de aeronaves fabricadas e registradas com categoria: transporte de passageiros?
def perg5(dados):
    result = {}

    for linha in dados:
        fabricante = linha['NMFABRICANTE']
        categ = linha['CDCATEGORIA']
        if fabricante:
            if categ and categ == 'TPR':
                if fabricante in result:
                    result[fabricante] += 1
                else:
                    result[fabricante] = 1
    result = funcoes.org(result)
    return result


# Gráfico da pergunta 1 <Pizza básico>
resultado = perg1(base)
labels = resultado.keys()
sizes = resultado.values()

plt.pie(sizes, labels=labels)
plt.legend(title='QUANT. CASOS', labels=sizes, loc='upper right', bbox_to_anchor=(1.1, 1))
plt.title('GRÁFICO PERGUNTA 1', fontsize=18)
plt.show()


# Gráfico da pergunta 2 <Linha>
resultado2 = perg2(base)
x = resultado2.keys()
y = resultado2.values()
posicao_x = list(range(len(x)))

plt.plot(y, linewidth=3.0, c='r', marker='o')
plt.xticks(posicao_x, x)
plt.title('GRÁFICO PERGUNTA 2', fontsize=18)
plt.xlabel('ANOS', fontsize=13)
plt.ylabel('QUANT. DE REGISTROS', fontsize=13)
plt.show()


# Gráfico da questão 3 <Barras>
resultado3 = perg3(base)
xy = funcoes.transformar(resultado3)
x = xy[0]
y = xy[1]

for i in range(len(resultado3)):
    plt.text(x[i], y[i], y[i], ha='center', va='bottom')
plt.bar(x, y, width=0.8)
plt.title('GRÁFICO PERGUNTA 3', fontsize=18)
plt.ylabel('QUANT. OPERADORES RESIDENTES', fontsize=13)
plt.xlabel('ESTADOS BRASILEIROS (UF)', fontsize=13)
plt.show()


# Gráfico da pergunta 4 <linha>
resultado4 = perg4(base)

dado_SP = resultado4[0]
x1 = dado_SP.keys()
y1 = dado_SP.values()
posicao_x1 = list(range(len(x1)))

dado_RJ = resultado4[1]
y2 = dado_RJ.values()

plt.plot(y1, linewidth=3.0, c='r', marker='o', label='SP')
plt.plot(y2, linewidth=3.0, c='b', marker='o', label='RJ')
plt.xticks(posicao_x1, x1)
plt.title('GRÁFICO PERGUNTA 4', fontsize=18)
plt.xlabel('ANOS', fontsize=13)
plt.ylabel('QUANT. REGIS. AERONAVES PRIVADAS', fontsize=13)
plt.legend(fontsize=18)
plt.show()


# Gráfico da pergunta 5 <barras>
resultado5 = perg5(base)
xy = funcoes.transformar(resultado5)
cord_x = xy[0]
cord_y = xy[1]

for c in range(len(resultado5)):
    plt.text(cord_y[c], cord_x[c], cord_y[c], ha='left', va='center')
plt.title('GRÁFICO PERGUNTA 5', fontsize=18)
plt.yticks(fontsize=7.7, rotation=38)
plt.ylabel('FABRICANTES', fontsize=13)
plt.xlabel('QUANT. AERONAVE DE TRANSPORTE DE PASSAGEIROS REGISTRADA', fontsize=13)
plt.barh(cord_x, cord_y)
plt.show()
