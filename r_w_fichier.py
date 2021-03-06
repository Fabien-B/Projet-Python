import xlrd
import equipement
import re


def import_file(filename, equipmentList):
    """
    Lit le fichier .xls et extrait les informations dans une liste
    :param filename: Le nom du fichier
    :param equipmentList: La liste des equipements
    :return:
    """
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_index(0)
    for i in range(1, sh.nrows):
        equipmentList.append(equipement.Equipment())
        fill_equipment(sh, i, equipmentList[-1])


def fill_equipment(sh, nEq, eq_current):
    """
    Interprète chaque colonne de la ligne pour
    remplir les attributs de l'équipement
    :param sh: Le fichier
    :param nEq: La ligne considérée
    :param eq_current: l'équipement correspondant à
    la ligne considérée
    :return:
    """
    eq_current.quartier = set_from_file_quartier(sh.cell_value(nEq, 0))
    eq_current.name = sh.cell_value(nEq, 1)
    eq_current.adresse = sh.cell_value(nEq, 2)
    eq_current.type = set_from_file_type(sh.cell_value(nEq, 3))
    eq_current.activities = set_from_file_activities(sh.cell_value(nEq, 4))
    eq_current.revetement = set_from_file_revetement(sh.cell_value(nEq, 5))
    eq_current.size = set_from_file_size(sh.cell_value(nEq, 6))
    eq_current.eclairage = set_from_file_eclairage(sh.cell_value(nEq, 7))
    eq_current.arrosage = set_from_file_arrosage(sh.cell_value(nEq, 8))
    eq_current.vestiaire = set_from_file_vestiaire(sh.cell_value(nEq, 9))
    eq_current.sanitaires = set_from_file_sanitaires(sh.cell_value(nEq, 10))
    eq_current.douches = set_from_file_douches(sh.cell_value(nEq, 11))
    eq_current.capaMax = set_from_file_capaMax(sh.cell_value(nEq, 12))
    eq_current.tribunes = set_from_file_tribunes(sh.cell_value(nEq, 13))
    eq_current.clubHouse = set_from_file_clubHouse(sh.cell_value(nEq, 14))
    eq_current.categorie = set_from_file_categorie(sh.cell_value(nEq, 15))
    eq_current.date = set_from_file_date(sh.cell_value(nEq, 16))
    eq_current.accesHand = set_from_file_accesHand(sh.cell_value(nEq, 17))
    eq_current.toilettesHand = set_from_file_toilettesHand(sh.cell_value(nEq, 18))


def set_from_file_quartier(content):
    """
    Extrait le quartier de l'équipement
    :param content:
    :return:
    """
    content = str(content)
    return content.replace(',', '.')


def set_from_file_activities(content):
    """
    Extrait les activités de l'équipement
    :param content:
    :return:
    """
    if content != '':
        dictionnaire = {}
        last = None
        liste = content.replace('/', ',').replace(' et ', ' + ').replace('-', ' ').replace('  ', ' ').replace('0m', '0 m').split(',')
        for equip in liste:
            equip = equip.split('+')
            if len(equip) == 1:
                equip = equip[0].replace(')', '').split('(')
                equip[0] = equip[0].strip(' )(').lower().capitalize()
                if len(equip) == 1 or not equip[1].isnumeric():
                    dictionnaire[equip[0].strip(' )(')] = 1
                else:
                    dictionnaire[equip[0].strip(' )(')] = int(equip[1])
            else:
                for (i, temp) in enumerate(equip):
                    num = re.sub(r'\D', "", temp)
                    if num:
                        if i < 1:
                            temp = temp.strip(' )(').replace(')', '').split('(')
                            temp[0] = temp[0].strip(' )(').lower().capitalize()
                            if len(temp) == 1 or not temp[1].isnumeric():
                                dictionnaire[temp[0].strip(' )(')] = 1
                            else:
                                dictionnaire[temp[0].strip(' )(')] = int(temp[1])
                            last = temp[0]
                        else:
                            temp = temp.strip(' )(').replace(')', '').split('(')
                            temp[0] = temp[0].strip(' )(').lower().capitalize()
                            num1 = re.sub(r'\D', "", last)
                            num2 = re.sub(r'\D', "", temp[0])
                            last = last.replace(str(num1), str(num2))
                            if len(temp) == 1 or not temp[1].isnumeric():
                                dictionnaire[last.strip(' )(')] = 1
                            else:
                                dictionnaire[last.strip(' )(')] = int(temp[1])
                    else:
                        temp = temp.strip(' )(').replace(')', '').split('(')
                        temp[0] = temp[0].strip(' )(').lower().capitalize()
                        if len(temp) == 1 or not temp[1].isnumeric():
                            dictionnaire[temp[0].strip(' )(')] = 1
                        else:
                            dictionnaire[temp[0].strip(' )(')] = int(temp[1])
        return dictionnaire
    else:
        return {'Non renseigné': 1}


def set_from_file_type(content):
    """
    Extrait le type de l'équipement
    :param content:
    :return:
    """
    return content.capitalize()


def set_from_file_revetement(content):
    """
    Extrait le revetement de l'équipement
    :param content:
    :return:
    """
    contentList = content.split()
    revetList = []
    for revet in contentList:
        revetList.append(revet.strip(','))
    if revetList == []:
        revetList = ['Non renseigné']
    return revetList


def set_from_file_size(content):
    """
    Extrait la taille de l'équipement
    :param content:
    :return:
    """
    terrainList = content.replace('et', '+').split('+')
    terrainSizes = []
    for terrain in terrainList:
        terrain = terrain.replace('*', 'x')
        terrain = terrain.replace('X', 'x')
        sizeStr = terrain.split('x')
        size = []
        for axis in sizeStr:
            longAxe = axis.strip('m ?')
            if longAxe != '':
                longAxe = longAxe.replace(',', '.')
                try:
                    longAxe = float(longAxe)
                except ValueError:
                    print(longAxe)
                size.append(longAxe)
        terrainSizes.append(tuple(size))
    return terrainSizes


def set_from_file_eclairage(content):
    """
    Détermine si l'équipement comporte un éclairage
    :param content:
    :return:
    """
    if content.lower().__contains__("oui"):
        return 1
    if content.lower().__contains__("non"):
        return 0
    else:
        return 999


def set_from_file_arrosage(content):
    """
    Détermine si l'équipement comporte un arrosage
    :param content:
    :return:
    """
    if content.lower().__contains__("oui"):
        return 1
    if content.lower().__contains__("non"):
        return 0
    else:
        return 999


def set_from_file_vestiaire(content):
    """
    Extrait le nombre de vestiaire de l'équipement
    :param content:
    :return:
    """
    nbJA = str(content).split('(')
    nbVestiaires = []
    for chaine in nbJA:
        chaine = chaine.strip(' )+')
        chaine = chaine.split('+')
        nbVest = 0
        for nb in chaine:
            if nb != '':
                nbVest += int(float(nb))
        nbVestiaires.append(nbVest)
    if len(nbVestiaires) == 1:
        nbVestiaires.append(0)
    nbVestiaires = tuple(nbVestiaires)
    return nbVestiaires


def set_from_file_sanitaires(content):
    """
    Determine si l'équipement est muni de sanitaires
    :param content:
    :return:
    """
    content = str(content).lower()
    if content == '':
        return 0
    if content.__contains__('oui'):
        return 1
    else:
        return int(float(content))


def set_from_file_douches(content):
    """
    Extrait le nombre de douches collectives ou
    individuelles de l'équipement
    :param content:
    :return:
    """
    content = content.replace('/', ',')
    content = content.split(',')
    nb = [None, None]
    for indCo in content:
        if indCo.__contains__('ind'):
            indCo = ''.join(filter(lambda x: x.isdigit(), str(indCo)))
            if indCo.isdigit():
                nb[0] = int(indCo)
            else:
                nb[0] = 1
        if indCo.__contains__('col'):
            indCo = ''.join(filter(lambda x: x.isdigit(), str(indCo)))
            if indCo.isdigit():
                nb[1] = int(indCo)
            else:
                nb[0] = 1
        if indCo.__contains__('oui'):
            nb[1] = 1     #s'il n'est pas précisé si elles sont collectives ou individuelles, on choisit collectives
    return nb


def set_from_file_capaMax(content):
    """
    Extrait la capacité max de l'équipement
    :param content:
    :return:
    """
    digits = ''.join(filter(lambda x: x.isdigit(), str(content)))
    if digits == '':
        return 0
    else:
        return int(digits)


def set_from_file_tribunes(content):
    """
    Extrait le nombre de place dans les tribunes
    de l'équipement
    :param content:
    :return:
    """
    digits = ''.join(filter(lambda x: x.isdigit(), str(content)))
    if digits == '':
        return 0
    else:
        return int(digits)


def set_from_file_clubHouse(content):
    """
    Determine si l'équipement est affecté d'un club House
    :param content:
    :return:
    """
    if str(content).lower().__contains__('oui'):
        return 1
    elif str(content).lower().__contains__('non'):
        return 0
    else:
        return 999


def set_from_file_categorie(content):
    """
    Extrait la catégorie de l'équipement
    :param content:
    :return:
    """
    if content == '':
        return 0
    else:
        return str(content)


def set_from_file_date(content):
    """
    Extrait la date de construction de l'équipement
    :param content:
    :return:
    """
    if content == '' or content == '?':
        return 0
    else:
        return int(content)


def set_from_file_accesHand(content):
    """
    Determine si l'équipement est muni d'un accès Handicapé
    :param content:
    :return:
    """
    if content == 'O' or content == '1':
        return 1
    elif content == 'N' or content == '0':
        return 0
    else:
        return 999


def set_from_file_toilettesHand(content):
    """
    Determine si l'équipement est affublé de toilettes Handicapé
    :param content:
    :return:
    """
    if content == 'O' or content == '1':
        return 1
    elif content == 'N' or content == '0':
        return 0
    else:
        return 999
