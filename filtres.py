
class Filtre():
    def __init__(self):
        self.activitiesSet = set()
        self.allEquipSet = set()

    def create_set(self, equiplist):
        for equip in equiplist:
            if equip.activities is not None:
                for key in dict.keys(equip.activities):
                    if key != '':
                        self.activitiesSet.add(key)

    def equip_set(self,equiplist):
        for equip in equiplist:
            self.allEquipSet.add(equip)


    def filtrer_set_par_acti(self,actiName):
        tempSet = set()
        for equip in self.allEquipSet:
            if actiName in equip.activities:
                tempSet.add(equip)
        return tempSet


    def printkey(self):
        for key in self.activitiesSet:
            print(key)
        print('nombre clé :', len(self.activitiesSet))
