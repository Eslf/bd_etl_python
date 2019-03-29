import cx_Oracle
from sqlalchemy import create_engine
import sqlalchemy as db

host='localhost'
port='1521'
sid='orclcdb'
user='locadora'
password='oracle'
sid = cx_Oracle.makedsn(host, port, sid=sid)

cstr = 'oracle://{user}:{password}@{sid}'.format(
    user=user,
    password=password,
    sid=sid
)

engine =  create_engine(
    cstr,
    convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=True
)

dw_host='localhost'
dw_port='1521'
dw_sid='orclcdb'
dw_user='dw_locadora'
dw_password='oracle'
dw_sid = cx_Oracle.makedsn(dw_host, dw_port, sid=dw_sid)

dw_cstr = 'oracle://{user}:{password}@{sid}'.format(
    user=dw_user,
    password=dw_password,
    sid=dw_sid
)

dw_engine =  create_engine(
    dw_cstr,
    convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=True
)

# ------------------ INICIO SECAO DE TABELAS SOCIOS ------------------

# query_socios = engine.execute('SELECT * FROM SOCIOS')
# query_tipos_socios = engine.execute('SELECT * FROM TIPOS_SOCIOS')
#
#
# result_socios = []
# result_tipos_socios = []
# result_dm_socios = []
#
# print("Create Result Tipos Socios")
# for row in query_tipos_socios:
#     result_tipos_socios.append(row)
#
# print("\n Print de Resultado Tipos Socios:")
# print(result_tipos_socios)
#
# print("\nCreate Result Socios")
# for row in query_socios:
#     tipo = ""
#     # cod_tipo = 1
#     result_socios.append(row)
#
#     for linha in result_tipos_socios:
#         if (row[2] == linha[0]):
#             tipo = linha[3]
#         # ++cod_tipo
#
#     result_dm_socios.append([row[0],row[4],tipo])
#
#
# print("\n Print de Resultado Socios:")
# print(result_socios)
#
# print("\n----------------------")
#
#
# print("\n Print de Array-Insert dm_socio:")
# print(result_dm_socios)
#
# print("\n----------------------")
#
#
#
# for row_dm in result_dm_socios:
#
#     dw_engine.execute('INSERT INTO DM_SOCIO (ID_SOC,NOM_SOC,TIPO_SOCIO) VALUES (:id,:nome,:tipo)',{'id': str(row_dm[0]),'nome': str(row_dm[1]),'tipo': str(row_dm[2])})
#
# print("inserts done")

# ------------------ FIM SECAO DE TABELAS SOCIOS ------------------



# ------------------ INICIO SECAO DE TABELAS ARTISTAS ------------------

# query_artistas = engine.execute('SELECT * FROM ARTISTAS')
#
# print("Print Artistas")
#
# result_artistas = []
#
# for row in query_artistas:
#     result_artistas.append(row)
#
#
# print(result_artistas)
#
# result_dw_artistas = []
#
# for linha in result_artistas:
#
#     # tipo = ""
#     # nac_bras = ""
#     #
#     # if linha[1] == "B":
#     #     tipo = "Banda"
#     # elif linha[1] == "D":
#     #     tipo = "Dupla"
#     # elif linha[1] == "I":
#     #     tipo = "Artista Individual"
#     #
#     # if linha[2] == "V":
#     #     nac_bras = "Artista Nacional"
#     # else:
#     #     nac_bras = "Artista Internacional"
#
#     result_dw_artistas.append([linha[0],linha[1],linha[2],linha[6]])
#
# print("\n------ Print DW Artistas -------")
#
# print(result_dw_artistas)
#
# for row_dw in result_dw_artistas:
#     dw_engine.execute('INSERT INTO DM_ARTISTA (ID_ART,TPO_ART, NAC_BRAS, NOM_ART) VALUES (:id, :tipo, :nac_bras, :nome)',
#                       {'id': str(row_dw[0]), 'tipo': str(row_dw[1]), 'nac_bras': str(row_dw[2]), 'nome': str(row_dw[3])})
#
# print("inserts done")


# ------------------ FIM SECAO DE TABELAS ARTISTAS ------------------



# ------------------ INICIO SECAO DE TABELAS GRAVADORAS ------------------

# query_gravadoras = engine.execute('SELECT * FROM GRAVADORAS')
#
# print("Print Artistas")
#
# result_gravadoras = []
#
# for row in query_gravadoras:
#     result_gravadoras.append(row)
#
#
# print(result_gravadoras)
#
# result_dw_gravadoras = []
#
# for linha in result_gravadoras:
#
#     result_dw_gravadoras.append([linha[0],linha[1],linha[2],linha[3]])
#
# print("\n------ Print DW Gravadoras -------")
#
# print(result_dw_gravadoras)
# #
# for row_dw in result_dw_gravadoras:
#     dw_engine.execute('INSERT INTO DM_GRAVADORA (ID_GRAV,UF_GRAV, NAC_BRAS, NOM_GRAV) VALUES (:id, :uf, :nac_bras, :nome)',
#                       {'id': str(row_dw[0]), 'uf': str(row_dw[1]), 'nac_bras': str(row_dw[2]), 'nome': str(row_dw[3])})
#
# print("inserts done")


# ------------------ FIM SECAO DE TABELAS GRAVADORAS ------------------


# ------------------ INICIO SECAO DE TABELAS TITULOS ------------------

query_titulos = engine.execute('SELECT * FROM TITULOS')

print("Print Titulos")

result_titulos = []

for row in query_titulos:
    result_titulos.append(row)


print(result_titulos)

result_dw_titulos = []

for linha in result_titulos:

    result_dw_titulos.append([linha[0],linha[1],linha[2],linha[7]])

print("\n------ Print DW Gravadoras -------")

print(result_dw_titulos)
#
# for row_dw in result_dw_titulos:
#     dw_engine.execute('INSERT INTO DM_TITULO (ID_GRAV,UF_GRAV, NAC_BRAS, NOM_GRAV) VALUES (:id, :uf, :nac_bras, :nome)',
#                       {'id': str(row_dw[0]), 'uf': str(row_dw[1]), 'nac_bras': str(row_dw[2]), 'nome': str(row_dw[3])})
# print("inserts done")
#


# ------------------ FIM SECAO DE TABELAS TITULOS ------------------