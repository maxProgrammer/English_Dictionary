# importar mysql connector module
import mysql.connector

# cria e seta objeto de conexão
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

# criar cursor para executar operações sql
cursor = con.cursor()

word = input("Enter a word: ")

# executar query
query = cursor.execute("select * from Dictionary where Expression = '%s' " % word)

# realizar leitura da query
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])

else:
    print("No word found!")