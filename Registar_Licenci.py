import sqlite3
connection=sqlite3.connect("RUGIPP_REGISTRI.db")
crsr=connection.cursor()


class Registar_Licenci:
    def __init__(self,JMBG,broj_licence,ime,prezime,godina_licence,red_licence):
        self.JMBG=JMBG
        self.broj=broj_licence
        self.ime=ime
        self.prezime=prezime
        self.godina_licence=godina_licence
        self.licenca=red_licence


    def licence(connection, lic):
        sql = ''' INSERT INTO Registar_Licenci (JMBG,BROJ_Licence,Ime,Prezime,Godina_Licence,Red_Licence)
                      VALUES(?,?,?,?,?,?) '''
        params = (lic.JMBG, lic.broj, lic.ime, lic.prezime, lic.godina_licence, lic.licenca)
        crsr.execute(sql, params)
        connection.commit()

while True:
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
    rl = int(
        input('NALAZITE SE U REGISTRU LICENCI \nZa unos nove Licence unesite 1, \nZa azuriranje podataka o Licenci unesite 2,'
              ' \nZa brisanje Licence iz registra unesite 3, \nZa uvid u podatke Licenci unesite 4,'
              ' \nZa izlaz iz Registra Licenci unesite 0, \nUNESI BROJ:'))
    if rl == 0:
        print("Registar Licenci je zatvoren.")
        break

    elif rl == 1:
        rl1 = Registar_Licenci(int(input("Unesi JMBG: ")), input("Unesi Broj Licence: "),input("Unesi Ime nosioca licence: "), input("Unesi Prezime nosioca licence: "), int(input("Unesi godinu izdavanja licence: ")), int(input("Unesi red licence (1 ili 2): ")) )
        Registar_Licenci.licence(connection, rl1)

    elif rl == 2:
        matl = int(input("Unesi JMBG Geodete cija se Licenca azurira:"))
        while True:
            print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
            azurl= int(input("Za azuriranje Broja Licence unesite 1, \nZa azuriranje Imena nosica licence unesite 2, \nZa azuriranje Prezimena nosioca licence unesite 3, "
                             "\nZa azuriranje Godine izdavanja Licence unesite 4,\nZa azuriranje Reda Licence unesite 5,"
                            " \nZa azuriranje svih podataka unesite 6, \nZa prekid azuriranja unesite 0, \nUNESI BROJ:"))
            if azurl == 0:
                print("Azuriranje Licenci je zavrseno.")
                break
            elif azurl == 1:
                ml = matl
                bl=input("Unesite novi Broj Licence:")
                crsr.execute('''UPDATE Registar_Licenci SET BROJ_Licence = ? WHERE JMBG=?''',(bl,ml))
                connection.commit()
            elif azurl == 2:
                ml = matl
                inl=input("Unesite novo Ime nosioca Licence:")
                crsr.execute('''UPDATE Registar_Licenci SET Ime = ? WHERE JMBG=?''',(inl,ml))
                connection.commit()
            elif azurl == 3:
                ml = matl
                pn=input("Unesite novo Prezime nosioca Licence:")
                crsr.execute('''UPDATE Registar_Licenci SET Prezime = ? WHERE JMBG=?''',(pn,ml))
                connection.commit()
            elif azurl == 4:
                ml = matl
                gil=input("Unesite novu godinu izdavanja Licence:")
                crsr.execute('''UPDATE Registar_Licenci SET Godina_Licence = ? WHERE JMBG=?''',(gil,ml))
                connection.commit()
            elif azurl == 5:
                ml = matl
                rll=input("Unesite novi Red Licence:")
                crsr.execute('''UPDATE Registar_Licenci SET Red_Licence = ? WHERE JMBG=?''',(rll,ml))
                connection.commit()
            elif azurl == 6:
                ml = matl
                bl = input("Unesite novi Broj Licence:")
                inl=input("Unesite novo Ime nosioca Licence:")
                pn=input("Unesite novo Prezime nosioca Licence:")
                gil=input("Unesite novu godinu izdavanja Licence:")
                rll=input("Unesite novi Red Licence:")
                crsr.execute('''UPDATE Registar_Licenci SET BROJ_Licence = ?, Ime = ?, Prezime = ?, Godina_Licence = ?, Red_Licence = ? WHERE JMBG=?''',(bl,inl,pn,gil,rll,ml))
                connection.commit()
            else:
                print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

    elif rl == 3:
        brisl = int(input("Unesi JMBG nosica licence ciju licencu zelite da izbrisete iz Registra Licenci:"))
        crsr.execute('''DELETE FROM Registar_Licenci WHERE JMBG=?''', (brisl, ))
        connection.commit()

    elif rl == 4:
        crsr.execute('''SELECT * FROM Registar_Licenci''')
        ansl = crsr.fetchall()
        for l1 in ansl:
            print(l1)
        a1=input("Za povratak u Regisar Licenci pritisni ENTER")

    else:
        print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

