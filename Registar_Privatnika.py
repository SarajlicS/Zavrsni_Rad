import sqlite3
connection=sqlite3.connect("RUGIPP_REGISTRI.db")
crsr=connection.cursor()


class Registar_Privatnika:
    def __init__(self,JIB,naziv_firme,adresa_firme):
        self.JIB=JIB
        self.naziv=naziv_firme
        self.adresa=adresa_firme


    def privatnici(connection, priv):
        sql = ''' INSERT INTO Registar_Privatnika (JIB,Naziv,Adresa)
                      VALUES(?,?,?) '''
        params = (priv.JIB, priv.naziv, priv.adresa)
        crsr.execute(sql, params)
        connection.commit()

while True:
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
    rp = int(
        input('NALAZITE SE U REGISTRU PRIVATNIKA \nZa unos Privatne firme unesite 1, \nZa azuriranje podataka o Privatnoj firmi unesite 2,'
              ' \nZa brisanje Privatne firme iz Registra Privatnika unesite 3, \nZa uvid u podatke Privatnika unesite 4,'
              ' \nZa izlaz iz Registra Privatnika unesite 0, \nUNESI BROJ:'))
    if rp == 0:
        print("Registar Privatnika je zatvoren.")
        break

    elif rp == 1:
        rp1 = Registar_Privatnika(int(input("Unesi JIB privatne geodetske organizacije: ")), input("Unesi Naziv privatne geodetske organizacije: "),input("Unesi Adresu firme: "))
        Registar_Privatnika.privatnici(connection, rp1)
    elif rp == 2:
        pjib = int(input("Unesi JIB Privatne Geodetske organizacije koja se azurira:"))
        while True:
            print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
            azurp = int(input(
                "Za azuriranje Naziva privatne geodetske organizacije unesite 1, \nZa azuriranje Adrese unesite 2, \nZa azuriranje svih podataka unesite 3, "
                "\nZa prekid azuriranja unesite 0, \nUNESI BROJ:"))
            if azurp == 0:
                print("Azuriranje podataka o Privatnicima je zavrseno.")
                break
            elif azurp == 1:
                mp = pjib
                igo = input("Unesite novo Ime Geodetske organizacije:")
                crsr.execute('''UPDATE Registar_Privatnika SET Naziv = ? WHERE JIB=?''', (igo, mp))
                connection.commit()
            elif azurp == 2:
                mp = pjib
                ago = input("Unesite novu Adresu geodetske organizacije:")
                crsr.execute('''UPDATE Registar_Privatnika SET Adresa = ? WHERE JIB=?''', (ago, mp))
                connection.commit()
            elif azurp == 3:
                mp = pjib
                igo = input("Unesite novo Ime Geodetske organizacije:")
                ago = input("Unesite novu Adresu geodetske organizacije:")
                crsr.execute(
                    '''UPDATE Registar_Privatnika SET Naziv = ?, Adresa = ? WHERE JIB=?''',(igo, ago, mp))
                connection.commit()
            else:
                print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

    elif rp == 3:
        brisp = int(input("Unesi JIB geodetske organizacije koju zelite da izbrisete iz Registra Privatnika:"))
        crsr.execute('''DELETE FROM Registar_Privatnika WHERE JIB=?''', (brisp, ))
        connection.commit()

    elif rp == 4:
        crsr.execute('''SELECT * FROM Registar_Privatnika''')
        ansl = crsr.fetchall()
        for p1 in ansl:
            print(p1)
        a2=input("Za povratak u Regisar Privatnika pritisni ENTER")

    else:
        print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")