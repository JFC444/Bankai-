import pyodbc   # Skript zum Verbinden mit einer SQL Server-Datenbank und Abfragen
# 1. Verbindung zur SQL Server-Datenbank herstellen
conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=localhost;DATABASE=master;Trusted_Connection=yes;'
)
# 2. Überprüfen, ob die Datenbank "Berserk" existiert, und ggf. erstellen     
cursor = conn.cursor()
cursor.execute("SELECT * FROM sys.tables WHERE name = 'Bankai'")

cursor.execute("SELECT name FROM sys.tables")   # Abfrage aller Tabellen in der Datenbank
print("Tabellen in der Datenbank:")
for row in cursor.fetchall():
    print(" -", row.name)

cursor.execute("SELECT * FROM Berserk.dbo.Kunden")   # Abfrage der Tabelle "Kunden" in der Datenbank "Berserk"
print("\nInhalt der Tabelle 'Kunden':")
columns = [column[0] for column in cursor.description]   
rows = cursor.fetchall()
 
for row in rows:         # Ausgabe der Spaltennamen und Zeileninhalte
    print(dict(zip(columns, row)))
 
cursor.close()  # Schließen des Cursors
# 3. Verbindung schließen
conn.close()