from epltoolset import PdConnection

"<cred_set_name>": {
        "HOST": "10.121.5.11",
        "PORT": 1521,
        "SID": "DBLAB",
        "USERNAME": "1152123138",
        "PASSWORD": "026051996",
    }

# Instantiate a connection object
cn = PdConnection(cred_set="TEST_SPOT", cred_file='.connectcreds.creds')

# Check everything is in order
if cn.cred_file_exists():
    print("Specified Credential File Exists")
if cn.cred_set_exists():
    print("Specified Credential File Exists")
cn.load_cred_set()
if cn.can_connect():
    print("Tested that connection Possible")

    df = cn.sql_to_dataframe(sql="SELECT * FROM example_table_rr")
    print(df.head())