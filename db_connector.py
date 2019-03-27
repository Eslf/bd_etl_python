import cx_Oracle
from sqlalchemy import create_engine
import sqlalchemy as db

host='10.121.5.11'
port='1521'
sid='DBLAB'
user='1152123138'
password='026051996'
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

query_socios = engine.execute('SELECT * FROM SOCIOS')
query_tipos_socios = engine.execute('SELECT * FROM TIPOS_SOCIOS')


result_socios = []
result_tipos_socios = []
result_dm_socios = []

print("Create Result Tipos Socios")
for row in query_tipos_socios:
    result_tipos_socios.append(row)

print("\n Print de Resultado Tipos Socios:")
print(result_tipos_socios)

print("\nCreate Result Socios")
for row in query_socios:
    tipo = ""
    # cod_tipo = 1
    result_socios.append(row)

    for linha in result_tipos_socios:
        if (row[2] == linha[0]):
            tipo = linha[3]
        # ++cod_tipo

    result_dm_socios.append([row[0],row[4],tipo])


print("\n Print de Resultado Socios:")
print(result_socios)

print("\n----------------------")


print("\n Print de Array-Insert dm_socio:")
print(result_dm_socios)

print("\n----------------------")



for row_dm in result_dm_socios:

    engine.execute('INSERT INTO DM_SOCIO (ID_SOC,NOM_SOC,TIPO_SOCIO) VALUES (:id,:nome,:tipo)',{'id': str(row_dm[0]),'nome': str(row_dm[1]),'tipo': str(row_dm[2])})

print("inserts done")