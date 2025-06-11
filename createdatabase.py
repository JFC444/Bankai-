import pyodbc
# 1. Datenbankverbindung und Tabelle erstellen
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'  # ggf. anpassen
    'DATABASE=MojoJojo;'
    'UID=sa;'
    'PWD=felijopanda.99'
)

cursor = conn.cursor()     # Skript zum erstellen einer Tabelle 
cursor.execute("""          
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Teilnehmer')
BEGIN
    CREATE TABLE Teilnehmer (
        TeilnehmerID INT IDENTITY(1,1) PRIMARY KEY,
        Vorname NVARCHAR(50),
        Nachname NVARCHAR(50),
        Geburtsdatum DATE,
        Email NVARCHAR(100)
    )
END
""")
conn.commit()
 
# 2. Einträge einfügen
daten = [
    ('Martin', 'Krieg', '1995-07-21', 'martin.krieg@example.com'),
    ('Johanna', 'Cotta', '1998-04-12', 'johanna.cotta@example.com'),
    ('Rafael', 'Neumann', '2000-01-28', 'rafael.neumann@example.com')
]
for eintrag in daten:
    cursor.execute("INSERT INTO Teilnehmer (Vorname, Nachname, Geburtsdatum, Email) VALUES (?, ?, ?, ?)", eintrag)
conn.commit()
print("✅ Datensätze eingefügt.")
 
# 3. Daten anzeigen
print("\n📄 Aktuelle Teilnehmer:")
cursor.execute("SELECT * FROM Teilnehmer")
for row in cursor.fetchall():
    print(f"{row.TeilnehmerID}: {row.Vorname} {row.Nachname}, {row.Email}")
 
# 4. Datensatz aktualisieren
cursor.execute("UPDATE Teilnehmer SET Email = ? WHERE TeilnehmerID = ?", ('martin.neu@example.com', 1))
conn.commit()
print("\n✏️ Datensatz 1 aktualisiert.")
 
# 5. Datensatz löschen
cursor.execute("DELETE FROM Teilnehmer WHERE TeilnehmerID = ?", (3,))
conn.commit()
print("\n🗑️ Datensatz 3 gelöscht.")
 
# Ergebnisse nach Änderung anzeigen
print("\n📄 Teilnehmer nach Änderungen:")
cursor.execute("SELECT * FROM Teilnehmer")
for row in cursor.fetchall():
    print(f"{row.TeilnehmerID}: {row.Vorname} {row.Nachname}, {row.Email}")
 
# Verbindung schließen
cursor.close()
conn.close()