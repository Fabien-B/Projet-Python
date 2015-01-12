
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


    def filtrer_set_par_acti(self,actiNames,accesHand = False):
        tempSet = set()
        for equip in self.allEquipSet:
            ActiEquipSet = set(equip.activities.keys())
            ActiRequestSet = set(actiNames)
            if ActiRequestSet & ActiEquipSet != set():
                tempSet.add(equip)
        if accesHand:
            print('Acces Hand')
            return self.filtrer_acces_hand(tempSet)
        return tempSet

    def filtrer_acces_hand(self,equipSet,state = True):     #state = True <=> renvoie les eqs AVEC acces hand, state = False <=> renvoie ceux SANS acces hand
        tempSet = set()
        for equip in equipSet:
            if state:
                if equip.accesHand:
                    tempSet.add(equip)
            else:
                if not equip.accesHand:
                    tempSet.add(equip)
        return tempSet


    def printkey(self):
        for key in self.activitiesSet:
            print(key)
        print('nombre clé :', len(self.activitiesSet))
