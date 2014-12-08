import xlrd
import equipement

def import_file(filename,equipmentList):
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_index(0)
    for i in range(1,sh.nrows):
        equipmentList.append(equipement.Equipment())
        fill_equipment(sh,i,equipmentList[-1])

def fill_equipment(sh,nEq,eq_current):
    eq_current.quartier=set_from_file_quartier(sh.cell_value(nEq,0))
    eq_current.name=sh.cell_value(nEq,1)
    eq_current.adresse=sh.cell_value(nEq,2)
    eq_current.type=set_from_file_type(sh.cell_value(nEq,3))
    eq_current.activities=set_from_file_activities(sh.cell_value(nEq,4))
    eq_current.revetement=set_from_file_revetement(sh.cell_value(nEq,5))
    eq_current.size=set_from_file_size(sh.cell_value(nEq,6))
    eq_current.eclairage=set_from_file_eclairage(sh.cell_value(nEq,7))
    eq_current.arrosage=set_from_file_arrosage(sh.cell_value(nEq,8))
    eq_current.vestiaire=set_from_file_vestiaire(sh.cell_value(nEq,9))
    eq_current.sanitaires=set_from_file_sanitaires(sh.cell_value(nEq,10))
    eq_current.douches=set_from_file_douches(sh.cell_value(nEq,11))
    eq_current.capaMax=set_from_file_capaMax(sh.cell_value(nEq,12))
    eq_current.tribunes=set_from_file_tribunes(sh.cell_value(nEq,13))
    eq_current.clubHouse=set_from_file_clubHouse(sh.cell_value(nEq,14))
    eq_current.categorie=set_from_file_categorie(sh.cell_value(nEq,15))
    eq_current.date=set_from_file_date(sh.cell_value(nEq,16))
    eq_current.accesHand=set_from_file_accesHand(sh.cell_value(nEq,17))
    eq_current.toilettesHand=set_from_file_toilettesHand(sh.cell_value(nEq,18))


def set_from_file_quartier(content):
    content = str(content)
    return content.replace(',', '.')









def set_from_file_type(content):            #TODO: écrire toutes les fonctions d'importation
    print(content)







def set_from_file_activities(content):
    print(content)







def set_from_file_revetement(content):
    print(content)







def set_from_file_size(content):
    print(content)







def set_from_file_eclairage(content):
    print(content)







def set_from_file_arrosage(content):
    print(content)







def set_from_file_vestiaire(content):
    print(content)







def set_from_file_sanitaires(content):
    print(content)







def set_from_file_douches(content):
    print(content)







def set_from_file_capaMax(content):
    print(content)







def set_from_file_tribunes(content):
    print(content)







def set_from_file_clubHouse(content):
    print(content)







def set_from_file_categorie(content):
    print(content)







def set_from_file_date(content):
    print(content)







def set_from_file_accesHand(content):
    print(content)







def set_from_file_toilettesHand(content):
    print(content)
