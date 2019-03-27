import cx_Oracle
from sqlalchemy import create_engine

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

result = engine.execute('SELECT * FROM ARTISTAS')

for row in result:
    print(row)