import sqlite3
connection=sqlite3.connect("RUGIPP_REGISTRI.db")
crsr=connection.cursor()


class Registar_Geodeta:
    def __init__(self,JMBG,ime,prezime,strucna_sprema,broj_strucnog,red_licence):
        self.JMBG=JMBG
        self.ime=ime
        self.prezime=prezime
        self.sprema=strucna_sprema
        self.strucni=broj_strucnog
        self.licenca=red_licence

    def geodete(connection,geo):
        sql=''' INSERT INTO Registar_Geodeta (JMBG,Ime,Prezime,Strucna_sprema,Broj_Uvjerenja_Strucni,Red_Licence)
                      VALUES(?,?,?,?,?,?) '''
        params = (geo.JMBG, geo.ime, geo.prezime, geo.sprema, geo.strucni, geo.licenca)
        crsr.execute(sql, params)
        connection.commit()


while True:
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
    rg = int(input('NALAZITE SE U REGISTRU GEODETA \nZa unos Geodete unesite 1, \nZa azuriranje podataka Geodete unesite 2,'
                   ' \nZa brisanje Geodete iz registra unesite 3, \nZa uvid u podatke Geodeta unesite 4,'
                   ' \nZa izlaz iz Registra Geodeta unesite 0, \nUNESI BROJ:'))
    if rg == 0:
        print("Registar Geodeta je zatvoren.")
        break

    elif rg == 1:
        rg1 = Registar_Geodeta(int(input("Unesi JMBG: ")), input("Unesi Ime: "), input("Unesi Prezime: "),
                                      input('Unesi visinu strucne spreme: '),
                                      input("Unesi broj uvjerenja strucnog ispita: "),
                                      int(input("Unesi red licence (1 ili 2): ")))
        Registar_Geodeta.geodete(connection, rg1)

    elif rg == 2:
        maticni = int(input("Unesi JMBG Geodete koji se azurira:"))
        while True:
            print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
            azur= int(input("Za azuriranje Imena unesite 1, \nZa azuriranje Prezimena unesite 2, \nZa azuriranje Strucne spreme unesite 3,"
                            " \nZa azuriranje Broja Uvjerenja strucog ispita unesite 4, \nZa azuriranje Reda licence unesite 5,"
                            " \nZa azuriranje svih podataka unesite 6, \nZa prekid azuriranja unesite 0, \nUNESI BROJ:"))
            if azur == 0:
                print("Azuriranje Geodete je zavrseno.")
                break
            elif azur == 1:
                m = maticni
                i=input("Unesite novo Ime Geodete:")
                crsr.execute('''UPDATE Registar_Geodeta SET Ime = ? WHERE JMBG=?''',(i,m))
                connection.commit()
            elif azur == 2:
                m = maticni
                p=input("Unesite novo Prezime Geodete:")
                crsr.execute('''UPDATE Registar_Geodeta SET Prezime = ? WHERE JMBG=?''',(p,m))
                connection.commit()
            elif azur == 3:
                m = maticni
                vss=input("Unesite novu Visinu strucne spreme:")
                crsr.execute('''UPDATE Registar_Geodeta SET Strucna_sprema = ? WHERE JMBG=?''',(vss,m))
                connection.commit()
            elif azur == 4:
                m = maticni
                bus=input("Unesite novi Broj Uvjerenja strucnog ispita:")
                crsr.execute('''UPDATE Registar_Geodeta SET Broj_Uvjerenja_Strucni = ? WHERE JMBG=?''',(bus,m))
                connection.commit()
            elif azur == 5:
                m = maticni
                rl=input("Unesite novi Red Licence:")
                crsr.execute('''UPDATE Registar_Geodeta SET Red_Licence = ? WHERE JMBG=?''',(rl,m))
                connection.commit()
            elif azur == 6:
                m = maticni
                i = input("Unesite novo Ime Geodete:")
                p = input("Unesite novo Prezime Geodete:")
                vss = input("Unesite novu Visinu strucne spreme:")
                bus = input("Unesite novi Broj Uvjerenja strucnog ispita:")
                rl=input("Unesite novi Red Licence:")
                crsr.execute('''UPDATE Registar_Geodeta SET Ime = ?, Prezime = ?, Strucna_sprema = ?, Broj_Uvjerenja_Strucni = ?, Red_Licence = ? WHERE JMBG=?''',(i,p,vss,bus,rl,m))
                connection.commit()
            else:
                print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

    elif rg == 3:
        bris = int(input("Unesi JMBG Geodete kog zelite da izbrisete iz Registra Geodeta:"))
        crsr.execute('''DELETE FROM Registar_Geodeta WHERE JMBG=?''', (bris, ))
        connection.commit()

    elif rg == 4:
        crsr.execute('''SELECT * FROM Registar_Geodeta''')
        ans = crsr.fetchall()
        for i in ans:
            print(i)
        a=input("Za povratak u Regisar Geodeta pritisni ENTER")


    else:
        print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")
