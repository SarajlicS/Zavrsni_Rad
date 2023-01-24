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
    rgs=int(input('RUGIPP REGISTRI \nZa pristup u Registar Geodeta unesite 1, \nZa pristup u Registar Licenci unesite 2, \nZa pristup u Registar Privatnika unesite 3, \nZa pristup u Registar Instrumenata unesite 4,\nZa izlaz iz programa unesite 0, \nUNESI BROJ:'))
    if rgs==0:
        print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
        print("Program RUGIPP Registri je zatvoren")
        break
    elif rgs==1:
        while True:
            print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
            rg = int(input(
                'NALAZITE SE U REGISTRU GEODETA \nZa unos Geodete unesite 1, \nZa azuriranje podataka Geodete unesite 2,'
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
                    azur = int(input(
                        "Za azuriranje Imena unesite 1, \nZa azuriranje Prezimena unesite 2, \nZa azuriranje Strucne spreme unesite 3,"
                        " \nZa azuriranje Broja Uvjerenja strucog ispita unesite 4, \nZa azuriranje Reda licence unesite 5,"
                        " \nZa azuriranje svih podataka unesite 6, \nZa prekid azuriranja unesite 0, \nUNESI BROJ:"))
                    if azur == 0:
                        print("Azuriranje Geodete je zavrseno.")
                        break
                    elif azur == 1:
                        m = maticni
                        i = input("Unesite novo Ime Geodete:")
                        crsr.execute('''UPDATE Registar_Geodeta SET Ime = ? WHERE JMBG=?''', (i, m))
                        connection.commit()
                    elif azur == 2:
                        m = maticni
                        p = input("Unesite novo Prezime Geodete:")
                        crsr.execute('''UPDATE Registar_Geodeta SET Prezime = ? WHERE JMBG=?''', (p, m))
                        connection.commit()
                    elif azur == 3:
                        m = maticni
                        vss = input("Unesite novu Visinu strucne spreme:")
                        crsr.execute('''UPDATE Registar_Geodeta SET Strucna_sprema = ? WHERE JMBG=?''', (vss, m))
                        connection.commit()
                    elif azur == 4:
                        m = maticni
                        bus = input("Unesite novi Broj Uvjerenja strucnog ispita:")
                        crsr.execute('''UPDATE Registar_Geodeta SET Broj_Uvjerenja_Strucni = ? WHERE JMBG=?''',
                                     (bus, m))
                        connection.commit()
                    elif azur == 5:
                        m = maticni
                        rl = input("Unesite novi Red Licence:")
                        crsr.execute('''UPDATE Registar_Geodeta SET Red_Licence = ? WHERE JMBG=?''', (rl, m))
                        connection.commit()
                    elif azur == 6:
                        m = maticni
                        i = input("Unesite novo Ime Geodete:")
                        p = input("Unesite novo Prezime Geodete:")
                        vss = input("Unesite novu Visinu strucne spreme:")
                        bus = input("Unesite novi Broj Uvjerenja strucnog ispita:")
                        rl = input("Unesite novi Red Licence:")
                        crsr.execute(
                            '''UPDATE Registar_Geodeta SET Ime = ?, Prezime = ?, Strucna_sprema = ?, Broj_Uvjerenja_Strucni = ?, Red_Licence = ? WHERE JMBG=?''',
                            (i, p, vss, bus, rl, m))
                        connection.commit()
                    else:
                        print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

            elif rg == 3:
                bris = int(input("Unesi JMBG Geodete kog zelite da izbrisete iz Registra Geodeta:"))
                crsr.execute('''DELETE FROM Registar_Geodeta WHERE JMBG=?''', (bris,))
                connection.commit()

            elif rg == 4:
                crsr.execute('''SELECT * FROM Registar_Geodeta''')
                ans = crsr.fetchall()
                for i in ans:
                    print(i)
                a = input("Za povratak u Regisar Geodeta pritisni ENTER")


            else:
                print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")
    elif rgs==2:
        while True:
            print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
            rl = int(
                input(
                    'NALAZITE SE U REGISTRU LICENCI \nZa unos nove Licence unesite 1, \nZa azuriranje podataka o Licenci unesite 2,'
                    ' \nZa brisanje Licence iz registra unesite 3, \nZa uvid u podatke Licenci unesite 4,'
                    ' \nZa izlaz iz Registra Licenci unesite 0, \nUNESI BROJ:'))
            if rl == 0:
                print("Registar Licenci je zatvoren.")
                break

            elif rl == 1:
                rl1 = Registar_Licenci(int(input("Unesi JMBG: ")), input("Unesi Broj Licence: "),
                                       input("Unesi Ime nosioca licence: "), input("Unesi Prezime nosioca licence: "),
                                       int(input("Unesi godinu izdavanja licence: ")),
                                       int(input("Unesi red licence (1 ili 2): ")))
                Registar_Licenci.licence(connection, rl1)

            elif rl == 2:
                matl = int(input("Unesi JMBG Geodete cija se Licenca azurira:"))
                while True:
                    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
                    azurl = int(input(
                        "Za azuriranje Broja Licence unesite 1, \nZa azuriranje Imena nosica licence unesite 2, \nZa azuriranje Prezimena nosioca licence unesite 3, "
                        "\nZa azuriranje Godine izdavanja Licence unesite 4,\nZa azuriranje Reda Licence unesite 5,"
                        " \nZa azuriranje svih podataka unesite 6, \nZa prekid azuriranja unesite 0, \nUNESI BROJ:"))
                    if azurl == 0:
                        print("Azuriranje Licenci je zavrseno.")
                        break
                    elif azurl == 1:
                        ml = matl
                        bl = input("Unesite novi Broj Licence:")
                        crsr.execute('''UPDATE Registar_Licenci SET BROJ_Licence = ? WHERE JMBG=?''', (bl, ml))
                        connection.commit()
                    elif azurl == 2:
                        ml = matl
                        inl = input("Unesite novo Ime nosioca Licence:")
                        crsr.execute('''UPDATE Registar_Licenci SET Ime = ? WHERE JMBG=?''', (inl, ml))
                        connection.commit()
                    elif azurl == 3:
                        ml = matl
                        pn = input("Unesite novo Prezime nosioca Licence:")
                        crsr.execute('''UPDATE Registar_Licenci SET Prezime = ? WHERE JMBG=?''', (pn, ml))
                        connection.commit()
                    elif azurl == 4:
                        ml = matl
                        gil = input("Unesite novu godinu izdavanja Licence:")
                        crsr.execute('''UPDATE Registar_Licenci SET Godina_Licence = ? WHERE JMBG=?''', (gil, ml))
                        connection.commit()
                    elif azurl == 5:
                        ml = matl
                        rll = input("Unesite novi Red Licence:")
                        crsr.execute('''UPDATE Registar_Licenci SET Red_Licence = ? WHERE JMBG=?''', (rll, ml))
                        connection.commit()
                    elif azurl == 6:
                        ml = matl
                        bl = input("Unesite novi Broj Licence:")
                        inl = input("Unesite novo Ime nosioca Licence:")
                        pn = input("Unesite novo Prezime nosioca Licence:")
                        gil = input("Unesite novu godinu izdavanja Licence:")
                        rll = input("Unesite novi Red Licence:")
                        crsr.execute(
                            '''UPDATE Registar_Licenci SET BROJ_Licence = ?, Ime = ?, Prezime = ?, Godina_Licence = ?, Red_Licence = ? WHERE JMBG=?''',
                            (bl, inl, pn, gil, rll, ml))
                        connection.commit()
                    else:
                        print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

            elif rl == 3:
                brisl = int(input("Unesi JMBG nosica licence ciju licencu zelite da izbrisete iz Registra Licenci:"))
                crsr.execute('''DELETE FROM Registar_Licenci WHERE JMBG=?''', (brisl,))
                connection.commit()

            elif rl == 4:
                crsr.execute('''SELECT * FROM Registar_Licenci''')
                ansl = crsr.fetchall()
                for l1 in ansl:
                    print(l1)
                a1 = input("Za povratak u Regisar Licenci pritisni ENTER")

            else:
                print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

    elif rgs==3:
        while True:
            print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
            rp = int(
                input(
                    'NALAZITE SE U REGISTRU PRIVATNIKA \nZa unos Privatne firme unesite 1, \nZa azuriranje podataka o Privatnoj firmi unesite 2,'
                    ' \nZa brisanje Privatne firme iz Registra Privatnika unesite 3, \nZa uvid u podatke Privatnika unesite 4,'
                    ' \nZa izlaz iz Registra Privatnika unesite 0, \nUNESI BROJ:'))
            if rp == 0:
                print("Registar Privatnika je zatvoren.")
                break

            elif rp == 1:
                rp1 = Registar_Privatnika(int(input("Unesi JIB privatne geodetske organizacije: ")),
                                          input("Unesi Naziv privatne geodetske organizacije: "),
                                          input("Unesi Adresu firme: "))
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
                            '''UPDATE Registar_Privatnika SET Naziv = ?, Adresa = ? WHERE JIB=?''', (igo, ago, mp))
                        connection.commit()
                    else:
                        print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

            elif rp == 3:
                brisp = int(input("Unesi JIB geodetske organizacije koju zelite da izbrisete iz Registra Privatnika:"))
                crsr.execute('''DELETE FROM Registar_Privatnika WHERE JIB=?''', (brisp,))
                connection.commit()

            elif rp == 4:
                crsr.execute('''SELECT * FROM Registar_Privatnika''')
                ansl = crsr.fetchall()
                for p1 in ansl:
                    print(p1)
                a2 = input("Za povratak u Regisar Privatnika pritisni ENTER")

            else:
                print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

    elif rgs==4:
        while True:
            print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
            ri = int(input(
                'NALAZITE SE U REGISTRU INSTRUMENATA \nZa unos novog Instrumenta unesite 1, \nZa azuriranje podataka o Instrumentu unesite 2,'
                ' \nZa brisanje Instrumenta iz Registra Instrumenata unesite 3, \nZa uvid u podatke Instrumenata unesite 4,'
                ' \nZa izlaz iz Registra Instrumenata unesite 0, \nUNESI BROJ:'))
            if ri == 0:
                print("Registar Instrumenata je zatvoren.")
                break

            elif ri == 1:
                ri1 = Registar_Instrumenata(input("Unesi Serijski broj instrumenta: "),
                                            input("Unesi Vrstu instrumenta (GPS,TS,NIV): "),
                                            input("Unesi Naziv instrumenta: "),
                                            input("Unesi do kada je Instrument etaloniran (dan.mjesec.godina):"))
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
                        crsr.execute('''UPDATE Registar_Instrumenata SET Etaloniran_Do = ? WHERE Serijski_Broj=?''',
                                     (ed, bi))
                        connection.commit()
                    elif azuri == 2:
                        bi = sbi
                        vi = input("Unesite izmijenjenu Vrstu instrumenta (GPS,TS,NIV):")
                        ni = input("Unesite novi naziv Instrumenta:")
                        ed = input("Unesite novi datum do kada je Instrument etaloniran (dan.mjesec.godina):")
                        crsr.execute(
                            '''UPDATE Registar_Instrumenata SET Vrsta_Instrumenta = ?, Naziv_Instrumenta = ?, Etaloniran_Do = ? WHERE Serijski_Broj=?''',
                            (vi, ni, ed, bi))
                        connection.commit()
                    else:
                        print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

            elif ri == 3:
                brisi = int(input("Unesi Serijski Broj Instrumenta koju zelite da izbrisete iz Registra Instrumenata:"))
                crsr.execute('''DELETE FROM Registar_Instrumenata WHERE Serijski_Broj=?''', (brisi,))
                connection.commit()

            elif ri == 4:
                crsr.execute('''SELECT * FROM Registar_Instrumenata''')
                ansl = crsr.fetchall()
                for i1 in ansl:
                    print(i1)
                a3 = input("Za povratak u Regisar Instrumenata pritisni ENTER")

            else:
                print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")

    else:
        print("Niste unjeli dobar broj, unesite ispravan broj iz liste.")
