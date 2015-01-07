sets = set()
allEquipSet = set()


def create_set(equiplist):
    for equip in equiplist:
        if equip.activities is not None:
            for key in dict.keys(equip.activities):
                if key != '':
                    sets.add(key)


def equip_set(equiplist):
    for equip in equiplist:
        allEquipSet.add(equip)
    print(allEquipSet)


def filtrer_set_par_acti(actiName):
    tempSet = set()
    for equip in allEquipSet:
        if actiName in equip.activities:
            tempSet.add(equip)
    return tempSet


def printkey():
    for key in sets:
        print(key)
    print('nombre clé :', len(sets))