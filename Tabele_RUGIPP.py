import sqlite3
connection=sqlite3.connect("RUGIPP_REGISTRI.db")
crsr=connection.cursor()

sql_command="""CREATE TABLE IF NOT EXISTS Registar_Geodeta (
JMBG INTEGER PRIMARY KEY,
Ime VARCHAR,
Prezime VARCHAR,
Strucna_sprema VARCHAR,
Broj_Uvjerenja_Strucni VARCHAR,
Red_Licence VARCHAR(1));"""
crsr.execute(sql_command)
connection.commit()

sql_command="""CREATE TABLE IF NOT EXISTS Registar_Licenci (
JMBG INTEGER (13) PRIMARY KEY,
BROJ_Licence VARCHAR,
Ime VARCHAR,
Prezime VARCHAR,
Godina_Licence INTEGER,
Red_Licence INTEGER);"""
crsr.execute(sql_command)
connection.commit()

sql_command="""CREATE TABLE IF NOT EXISTS Registar_Privatnika (
JIB INTEGER PRIMARY KEY,
Naziv VARCHAR,
Adresa VARCHAR);"""
crsr.execute(sql_command)
connection.commit()

sql_command="""CREATE TABLE IF NOT EXISTS Registar_Instrumenata (
Serijski_Broj VARCHAR PRIMARY KEY,
Vrsta_Instrumenta VARCHAR,
Naziv_Instrumenta VARCHAR,
Etaloniran_Do VARCHAR);"""
crsr.execute(sql_command)
connection.commit()