sets = set()


def create_set(equip):
    if equip.activities is not None:
        for key in dict.keys(equip.activities):
            if key != '':
                sets.add(key)


def printkey():
    for key in sets:
        print(key)
    print('nombre clé :',len(sets))