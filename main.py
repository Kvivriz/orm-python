from mysql.connector import (connection)
from mysql.connector import errorcode
import os
from load_dotenv import load_dotenv
load_dotenv()
SENHA=os.getcwd('SENHA_SQL')

bd_conexao = connection.MySQLConnection(
    host='localhost',
    user='root',
    password=SENHA,
    database='bd_python'
)