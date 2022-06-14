
"""----------------------------------------------LOGIKA VEZANA ZA TABLU I MOGUCE POTEZE IGRACA-------------------------------------------------"""
#⚪-COVEK
#⚫-AI

def Tabla(tabla):
    print(tabla[0] + "(00)----------------------" + tabla[1] + "(01)----------------------" + tabla[2] + "(02)");
    print("|                           |                           |");
    print("|       " + tabla[8] + "(08)--------------" + tabla[9] + "(09)--------------" + tabla[10] + "(10)     |");
    print("|       |                   |                    |      |");
    print("|       |                   |                    |      |");
    print("|       |        " + tabla[16] + "(16)-----" + tabla[17] + "(17)-----" + tabla[18] + "(18)       |      |");
    print("|       |         |                   |          |      |");
    print("|       |         |                   |          |      |");
    print(tabla[3] + "(03)---" + tabla[11] + "(11)----" + tabla[19] + "(19)               " + tabla[20] + "(20)----" +
          tabla[12] + "(12)---" + tabla[4] + "(04)");
    print("|       |         |                   |          |      |");
    print("|       |         |                   |          |      |");
    print("|       |        " + tabla[21] + "(21)-----" + tabla[22] + "(22)-----" + tabla[23] + "(23)       |      |");
    print("|       |                   |                    |      |");
    print("|       |                   |                    |      |");
    print("|       " + tabla[13] + "(13)--------------" + tabla[14] + "(14)--------------" + tabla[15] + "(15)     |");
    print("|                           |                           |");
    print("|                           |                           |");
    print(tabla[5] + "(05)----------------------" + tabla[6] + "(06)----------------------" + tabla[7] + "(07)");

def proveri_da_li_je_polje_zauzeto(tabla):
    for polje in range(len(tabla)):
        if tabla[polje]=="X":
            return True
        return False

def proveri_da_li_polje_pripada_korisniku(tabla, pozicija):
    if tabla[pozicija]=="⚪":
        return True
    return False

def pronadji_korisnikove_mice(tabla, oznaka):
    broj_formiranih_mica=0
    for figurica in mica:
        if (tabla[figurica[0]], tabla[figurica[1]], tabla[figurica[2]])==oznaka:
            broj_formiranih_mica+=1
    return broj_formiranih_mica

def potez_igraca(tabla):

    trenutna_pozicija=""
    zeljena_pozicija=""

    while trenutna_pozicija=="":
        trenutna_pozicija=input("Unesite na kojoj poziciji se nalzi figurica sa kojom zelite da odigrate potez: ")

        if trenutna_pozicija in pozicije:

            if proveri_da_li_je_figurica_blokirana(tabla, pozicije[trenutna_pozicija])==True or proveri_da_li_polje_pripada_korisniku(tabla, pozicije[trenutna_pozicija])!=True:
                trenutna_pozicija=""
                print(" Nije moguce odigrati potez sa figuricom na zeljenoj poziciji! Pokusajte ponovo sa drugim izborom :) ")

        else:
            trenutna_pozicija=""
            print("Odabrali ste nepostojece polje! Molimo Vas pokusajte ponovo!")

    while zeljena_pozicija=="":

        zeljena_pozicija=input("Unesite zeljenu poziciju na koju zelite da pozicionirate figuricu: ")

        if pozicije[zeljena_pozicija] in susedna_polja[pozicije[zeljena_pozicija]]:

            if tabla[pozicije[zeljena_pozicija]]!="X":
                zeljena_pozicija=""
                print("Ne mozete se pozicionirati na dato polje! Zeljeno polje je zauzeto!")

        else:
            zeljena_pozicija=""
            print("Odaberite jedno od susednih polja! Ne mozete se pozicionirati na odbrano polje, pokusajte ponovo!")

    tabla[pozicije[trenutna_pozicija]], tabla[pozicije[zeljena_pozicija]]="X", tabla[pozicije[trenutna_pozicija]]
    return trenutna_pozicija, zeljena_pozicija

def proveri_da_li_je_figurica_blokirana(tabla, pozicija_igraca):
    for polje in susedna_polja[pozicija_igraca]:
        if tabla[polje]!="X":
            return True
        return False

def proveri_da_li_je_formacija_od_dve(tabla, oznaka):

    for figurica in mica:
        formacija=0
        if (tabla[figurica[0]]==oznaka and tabla[figurica[1]]==oznaka and tabla[figurica[2]]=="X") or (tabla[figurica[0]]=="X" and tabla[figurica[1]]==oznaka and tabla[figurica[2]]==oznaka) or (tabla[figurica[0]]==oznaka and tabla[figurica[1]]=="X" and tabla[figurica[2]]==oznaka):
            formacija+=1
    return formacija

def proveri_da_li_je_igrac_skroz_blokiran(tabla, pozicija_igraca):
    for pozicija in range(len(tabla)):
        if tabla[pozicija]==pozicija_igraca:
            if proveri_da_li_je_figurica_blokirana(tabla, pozicija):
                return True
        return False

def prebroj_figurice_na_tabli(tabla, oznaka_figurice):
    suma=0
    for igrac in tabla:
        if igrac==oznaka_figurice:
            suma+=1
        return suma

def pronadji_pobednika(tabla):

    if prebroj_figurice_na_tabli(tabla, "⚪") < 3 or proveri_da_li_je_igrac_skroz_blokiran(tabla, "⚪"):
        print("Cestitamo! Odneli ste pobedu :)")
        exit()
    else:
        print("Nazalost, izgubili ste... Vise srece drugi put :(")

def postavi_igraca_na_tablu(tabla):
    pozicija_igraca=""
    while pozicija_igraca=="":
        pozicija_igraca=input("Molimo Vas unesite poziciju na koju zelite da postavite Vasu figuricu: ")
        if pozicija_igraca in susedna_polja:
            if tabla[pozicija_igraca]=="X":
                tabla[pozicija_igraca]=="⚪"
            else:
                pozicija_igraca=""
                print("Na polje koje ste odabrali nije moguce postaviti figuricu! Molimo Vas odaberite drugu poziciju :)")
        else:
            print("Uneli ste nepostojece polje! Molimo Vas unesite tacan naziv zeljene pozicije!")
    return pozicija_igraca

#NE ZABORAVI, DA PROVERIS NAKNADNO!!!!!!!!
def proveri_da_li_je_igrac_formirao_micu(tabla, pozicija, oznaka):
    print()
    
def proveri_da_li_sve_figurice_igraca_formiraju_micu(tabla, pozicija_figurice):
    for pozicija in range(len(tabla)):
        if pozicija==tabla[pozicija_figurice]:
            if proveri_da_li_je_igrac_formirao_micu(tabla, pozicija, pozicija_figurice):
                return True
        return False

#DOVRSI USLOV!!!!!
def proveri_da_li_je_moguce_ukloniti_protivnicku_figuricu(tabla, pozicija1, pozicija2):
    print()

def mica_u_L(tabla, figurica):
    suma=0
    for pozicija in range(len(tabla)):
        if tabla[pozicija]==figurica and tabla[mica_horizontalno[pozicija][0]]==figurica and tabla[mica_uspravno[pozicija][0]]==figurica and tabla[mica_uspravno[pozicija][1]]==figurica and tabla[mica_horizontalno[pozicija][1]]==figurica:
            suma+=1
    return suma

def mica_u_malo_L(tabla):
    for pozicija in range(len(tabla)):
        malo_l = tabla[pozicija] + tabla[mica_uspravno[pozicija][0]] + tabla[mica_uspravno[pozicija][1]] + tabla[mica_horizontalno[pozicija][0]] + tabla[mica_horizontalno[pozicija][1]]
        return malo_l

def pojedi_protivnicku_figuricu(tabla):

    pozicija_sa_koje_se_uklanja_figurica=""

    while pozicija_sa_koje_se_uklanja_figurica=="":

        pozicija_sa_koje_se_uklanja_figurica=input("Unesite poziciju sa koje se uklanja protivnicka figurica:")

        if proveri_da_li_je_moguce_ukloniti_protivnicku_figuricu(tabla,pozicije[pozicija_sa_koje_se_uklanja_figurica], "⚫" ):
            tabla[pozicije[pozicija_sa_koje_se_uklanja_figurica]]="X"
        else:
            pozicija_sa_koje_se_uklanja_figurica=""
            print("Ne mozete ukloniti figuricu sa zeljene pozicije! Molimo Vas odaberite neku drugu poziciju :) ")

"""------------------------------------------------------------------ HEURISTIKE -----------------------------------------------------------------"""

"""https://kartikkukreja.wordpress.com/2014/03/17/heuristicevaluation-function-for-nine-mens-morris/"""
"""FAZA 1 = 18 * (1) + 26 * (2) + 1 * (3) + 9 * (4) + 10 * (5) + 7 * (6)"""
"""FAZA 2 = 14 * (1) + 43 * (2) + 10 * (3) + 11 * (4) + 8 * (7) + 1086 * (8)"""
"""povratne vrednosti u zavisnosti od ishoda- 1-igrac pobedjuje , -1-ai vodi , 0-nereseno """
"""(1)-vraca odredjenu vrednost u zavisnosti o toga koji je korisnik formirao micu poslednjim potezom
   (2)- vraca odredjenu vrednost u zavisnosti od broja formiranih mica igraca-interesuje nas broj koji se dobija kao razlika broja ai i igracevih formiranih mica
   (3)-vraca broj blokiranih figurica (figurica ukljestena izmedju protivnickih)-interesuje nas broj koji se dobija dobijen kao razlika ai-jevih i nasih
   (4)- broj koji se dobija kao razlika izmedju nasih f. i  f. kompjutera
   (5)- razlika izmedju nasih f. i f. kompjutera koje se nalaze u uzastopnoj formaciji od dve
   (6)- razlika izmedju nasih f. i f. kompjutera koji se nalaze u formaciji od 3(dodamo jos jednu na bilo koju stranu i dobijamo formiranu micu)
   (7)-razlika izmedju nasih i protivnikovih "spojenih" mica(mica, gde je jedna zajednicka "L")
   (8)- pobednik-ako imamo manje od 3 ili smo blokirani- gubimo -1, pobeda 1, nereseno 0
   """

def heuristika_za_fazu_1(tabla, node):
    heuristika_faza1=0
    heuristika_faza1+=18*heuristika1(node)
    heuristika_faza1+=26*heuristika2(tabla)
    heuristika_faza1+=heuristika3(tabla)
    heuristika_faza1+=9*heuristika4(tabla)
    heuristika_faza1+=10*heuristika5(tabla)
    heuristika_faza1+=7*heuristika6(tabla)
    return heuristika_faza1

def heuristika_za_fazu2(tabla, node):
    heuristika_faza2=0
    heuristika_faza2+=14*heuristika1(node)
    heuristika_faza2+=43*heuristika2(tabla)
    heuristika_faza2+=10*heuristika3(tabla)
    heuristika_faza2+=11*heuristika4(tabla)
    heuristika_faza2+=8*heuristika7(tabla)
    heuristika_faza2+=1086*heuristika8(tabla)
    return heuristika_faza2

def heuristika_za_fazu3(tabla, node):
    heuristika_faza3=0
    heuristika_faza3+=16*heuristika1(node)
    heuristika_faza3+=10*heuristika5(tabla)
    heuristika_faza3+=heuristika6(tabla)
    heuristika_faza3+=1190*heuristika8(tabla)
    return heuristika_faza3


def heuristika1(node):
    print("")

def heuristika4(tabla):
    return prebroj_figurice_na_tabli(tabla,"⚪")-prebroj_figurice_na_tabli(tabla,"⚫")

def heuristika8(tabla):
    if prebroj_figurice_na_tabli(tabla,"⚫" )<3 and proveri_da_li_je_igrac_skroz_blokiran(tabla, "⚫")==True:
        return 1
    if prebroj_figurice_na_tabli(tabla,"⚪")<3 and proveri_da_li_je_igrac_skroz_blokiran(tabla, "⚪")==True:
        return -1
    return 0

def heuristika3(tabla):
    broj_blokiranih_figurica_korisnika=0
    broj_blokiranih_figurica_kompjutera=0

    for pozicija in range(len(tabla)):

        if tabla[pozicija]=="⚪":
            if proveri_da_li_je_figurica_blokirana(tabla, "⚪"):
                broj_blokiranih_figurica_korisnika+=1

        if tabla[pozicija]=="⚫":
            if proveri_da_li_je_figurica_blokirana(tabla, "⚫"):
                broj_blokiranih_figurica_kompjutera+=1

    return broj_blokiranih_figurica_kompjutera-broj_blokiranih_figurica_korisnika
        
def heuristika2(tabla):
    ai_broj_mica=pronadji_korisnikove_mice(tabla, "⚫")
    korisnikove_mice=pronadji_korisnikove_mice(tabla, "⚪")
    return korisnikove_mice-ai_broj_mica 

def heuristika5(tabla):
    broj_korisnikovih_formacija_od_dve=proveri_da_li_je_formacija_od_dve(tabla,"⚪" )
    broj_ai_formacija_od_dve=proveri_da_li_je_formacija_od_dve(tabla,"⚫" ) 
    return broj_korisnikovih_formacija_od_dve-broj_ai_formacija_od_dve
        
def heuristika6(tabla):
    ai_malo_l=0
    korisnik_malo_l=0
    stanje=mica_u_malo_L(tabla)
    if stanje=="X⚫⚫⚫X" or stanje=="⚫X⚫X⚫" or stanje=="" or stanje=="⚫X⚫⚫X" or stanje=="X⚫⚫X⚫":
        ai_malo_l+=1
    if stanje=="X⚪⚪⚪X" or stanje=="⚪X⚪X⚪" or stanje=="" or stanje=="⚪X⚪⚪X" or stanje=="X⚪⚪X⚪":
        korisnik_malo_l+=1
    return korisnik_malo_l-ai_malo_l

def heuristika7(tabla):
    broj_ai_mica_u_L=mica_u_L(tabla, "⚫")
    broj_korisnikovih_mica_L=mica_u_L(tabla, "⚪")
    return broj_ai_mica_u_L-broj_korisnikovih_mica_L

def pokreni_mice(tabla):
    print("Odaberite ko je prvi na potezu: ")
    print("1. Kompjuter")
    print("2. Igrac")
    unos=eval(input("----> ").strip("/n"))
    while (unos<1 or unos>2):
        print("Odaberite jednu od ponudjenih opcija!!!")
        unos=eval(input("----> "))
    Tabla(tabla)
    tabla=list(prva_faza(tabla, unos))
    druga_faza(tabla, unos)

""""------------------------------------------------------------- PRVA FAZA ------------------------------------------------------------------------"""
def prva_faza(figurice, unos):
    print("")

"""------------------------------------------------------------- DRUGA FAZA ----------------------------------------------------------------------------"""
if __name__=="__main__":

    def uputstva():
        print()
        print("""Igra Nine Mens Morris (koja se naziva i Merels ili Mill) igra se na tabli koja se sastoji od tri koncentrična polja povezana linijama od sredine svake unutrašnje strane kvadrata do sredine odgovarajuće spoljne strane kvadrata. Komadi se igraju na uglovima i na tačkama gde se linije seku tako da ima 24 poena za igru. Uz tablu treba da bude 9 crnih i 9 belih komada obično u obliku okruglih tezgi.

        ---------------------------------------------------------------- Priprema i cilj -----------------------------------------------------------------------


        Osnovni cilj Nine Mens Morrisa je da napravi „mlinove“ – vertikalne ili horizontalne linije od tri u nizu. Svaki put kada se ovo postigne, protivnička figura se uklanja, a opšti cilj je da se smanji broj protivničkih figura na manje od tri ili da se protivnik onemogući da igra. Za početak je tabla prazna.


        ------------------------------------------------------------------Osnovna pravila------------------------------------------------------------------------

        Igrač baca novčić da odluči ko će igrati belo – beli se prvi pomera i kao rezultat ima malu prednost. Igra se odvija u dve faze. Za početak, igrači se smenjuju da igraju komad svoje boje na bilo kojoj nezauzetoj tački dok se ne odigra svih osamnaest komada. Nakon toga, igra se nastavlja naizmenično, ali svaki potez se sastoji od igrača koji pomera jednu figuru duž linije do susedne tačke.

        Tokom obe ove faze, kad god igrač postigne mlin, taj igrač odmah uklanja sa table jedan komad koji pripada protivniku koji nije deo mlina. Ako sve protivničke figure formiraju mlinove onda se pravi izuzetak i igraču je dozvoljeno da ukloni bilo koju figuru. Tek nakon formiranja mlina, figura je zarobljena, ali igrač često razbije mlin tako što će pomeriti komad iz njega, a zatim, u sledećem okretu, ponovo odigrati figuru, formirajući tako novu mlin i hvatajući drugi komad.

        Uhvaćene figure se nikada ne vraćaju na tablu i ostaju zarobljene do kraja igre. Igra je gotova kada igrač izgubi tako što je smanjen na dve figure ili ne može da se kreće.""")
        print()
        Meni_igre()

    def Meni_igre():
        print("---------------------------------------------------- Dobrodosli u igricu 'Nine Men's Morris' -----------------------------------------------------------------------")
        print("")
        print("1. Uputstva za igru")
        print("2. Pokreni igricu")
        print("")
        izbor=input(">>>>")
        print("")
        print("====================================================================================================================================================================")
        if izbor=="1":
            uputstva()
        if izbor=="2":
            pokreni_mice(tabla)
        else:
            print("Odaberite jednu od ponudjenih opcija!")
            Meni_igre()
            

    susedna_polja=[[1, 9], [0, 2, 4], [1, 14], [4, 10], [1, 3, 5, 7], [4, 13], [11, 7], [4, 6, 8], [7, 12],
                     [0, 21, 10], [3, 9, 11, 18], [6, 10, 15], [8, 13, 17],
                     [5, 12, 20, 14], [2, 13, 23], [11, 16], [15, 17, 19], [12, 16], [10, 19], [16, 18, 22, 20],
                     [13, 19], [9, 22], [21, 19, 23], [22, 14]]

    mica=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20], [21, 22, 23],
             [0, 9, 21], [3, 10, 18], [6, 11, 15], [1, 4, 7], [16, 19, 22],
             [8, 12, 17], [5, 13, 20], [2, 14, 23]]

    validacija_polja = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "l1",
            "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]

    tabla = ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X",
            "X", "X", "X"]

    pozicije = {"00": 0, "01": 1, "02": 2, "03": 3, "04": 4, "05": 5, "06": 6, "07": 7, "08": 8, "09": 9,
                "10": 10, "11": 11,
                "12": 12, "13": 13, "14": 14, "15": 15, "16": 16, "17": 17, "18": 18, "19": 19, "20": 20,
                "21": 21, "22": 22, "23": 23}

    """-------------------------------------POTREBNO NAM JE ZBOG HEURISTIKE-L FORMACIJA VI I VII STAVKA------------------------------------------"""

    mica_uspravno = [[9, 21], [4, 7], [14, 23], [10, 18], [1, 7], [13, 20], [11, 15], [1, 4], [12, 17], [0, 21], [3, 18],
                    [6, 15], [8, 17], [5, 20], [2, 23], [6, 11],
                    [19, 22], [8, 12], [3, 10], [16, 22], [5, 13], [0, 9], [16, 19], [2, 14]]
    mica_horizontalno= [[1, 2], [0, 2], [0, 1], [4, 5], [3, 5], [3, 4], [7, 8], [6, 8], [6, 7], [10, 11], [9, 11],
                      [9, 10], [13, 14], [12, 14], [12, 13], [16, 17], [15, 17],
                      [15, 16], [19, 20], [18, 20], [18, 19], [22, 23], [21, 23], [21, 22]]
    Meni_igre()

