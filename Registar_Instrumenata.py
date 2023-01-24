import sqlite3
connection=sqlite3.connect("RUGIPP_REGISTRI.db")
crsr=connection.cursor()


class Registar_Instrumenata:
    def __init__(self,serijski_broj,vrsta_instrumenta,naziv_instrumenta, etaloniran_do):
        self.broj=serijski_broj
        self.vrsta=vrsta_instrumenta
        self.naziv=naziv_instrumenta
        self.etalon=etaloniran_do


    def instrumenti(connection, inst):
        sql = ''' INSERT INTO Registar_Instrumenata (Serijski_Broj,Vrsta_Instrumenta,Naziv_Instrumenta,Etaloniran_Do)
                      VALUES(?,?,?,?) '''
        params = (inst.broj, inst.vrsta, inst.naziv, inst.etalon)
        crsr.execute(sql, params)
        connection.commit()

while True:
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
    ri = int(input('NALAZITE SE U REGISTRU INSTRUMENATA \nZa unos novog Instrumenta unesite 1, \nZa azuriranje podataka o Instrumentu unesite 2,'
              ' \nZa brisanje Instrumenta iz Registra Instrumenata unesite 3, \nZa uvid u podatke Instrumenata unesite 4,'
              ' \nZa izlaz iz Registra Instrumenata unesite 0, \nUNESI BROJ:'))
    if ri == 0:
        print("Registar Instrumenata je zatvoren.")
        break

    elif ri == 1:
        ri1 = Registar_Instrumenata(input("Unesi Serijski broj instrumenta: "), input("Unesi Vrstu instrumenta (GPS,TS,NIV): "),
                                    input("Unesi Naziv instrumenta: "), input("Unesi do kada je Instrument etaloniran (dan.mjesec.godina):"))
        Registar_Instrumenata.instrumenti(connection, ri1)
    elif ri == 2:
        sbi = input("Unesi Seriski broj instrumenta koji se azurira:")
        while True:
            print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
            azuri = int(input(
                "Za azuriranje vremena do kada je etaloniran instrument unesite 1, \nZa azuriranje svih podataka unesite 2, "
                "\nZa prekid azuriranja unesite 0, \nUNESI BROJ:"))
            if azuri == 0:
                print("Azuriranje podataka o Instrumentima je zavrseno.")
                break
            elif azuri == 1:
                bi = sbi
                ed = input("Unesite novi datum do kada je Instrument etaloniran (dan.mjesec.godina):")
                crsr.execute('''UPDATE Registar_Instrumenata SET Etaloniran_Do = ? WHERE Serijski_Broj=?''', (ed, bi))
                connection.commit()
            elif azuri == 2:
                bi = sbi
                vi = input("Unesite izmijenjenu Vrstu instrumenta (GPS,TS,NIV):")
                ni = input("Unesite novi naziv Instrumenta:")
                ed = input("Unesite novi datum do kada je Instrument etaloniran (dan.mjesec.godina):")
                crsr.execute(
                    '''UPDATE Registar_Instrumenata SET Vrsta_Instrumenta = ?, Naziv_Instrumenta = ?, Etaloniran_Do = ? WHERE Serijski_Broj=?''',(vi, ni, ed, bi))
                connection.commit()
            else:
                print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

    elif ri == 3:
        brisi = int(input("Unesi Serijski Broj Instrumenta koju zelite da izbrisete iz Registra Instrumenata:"))
        crsr.execute('''DELETE FROM Registar_Instrumenata WHERE Serijski_Broj=?''', (brisi, ))
        connection.commit()

    elif ri == 4:
        crsr.execute('''SELECT * FROM Registar_Instrumenata''')
        ansl = crsr.fetchall()
        for i1 in ansl:
            print(i1)
        a3=input("Za povratak u Regisar Instrumenata pritisni ENTER")

    else:
        print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")