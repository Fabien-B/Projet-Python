from PyQt4 import QtGui

class Filtre():
    def __init__(self):
        self.activitiesSet = set()
        self.quartierSet = set()
        self.allEquipSet = set()
        self.revetementSet = set()
        self.toilettesHandSet = set()
        self.arrosageSet = set()
        self.eclairageSet = set()

    def create_set(self, equiplist):
        for equip in equiplist:
            if equip.activities is not None:
                for key in equip.activities:
                    if key != '':
                        self.activitiesSet.add(key)
                self.quartierSet.add(equip.quartier)
                for item in equip.revetement:
                    self.revetementSet.add(item)
                self.toilettesHandSet.add(equip.toilettesHand)
                self.arrosageSet.add(equip.arrosage)
                self.eclairageSet.add(equip.eclairage)

    def equip_set(self,equiplist):
        for equip in equiplist:
            self.allEquipSet.add(equip)


    def filtrer_set_par_acti(self,param,paramNames,accesHand = False):
        tempSet = set()
        for equip in self.allEquipSet:
            paramSet = set()
            if param == 'activities':
                paramSet = set(equip.__dict__[param])
            elif param == 'revetement':
                paramSet = set(equip.__dict__[param])
            else:
                paramSet = set([equip.__dict__[param]])
            ActiRequestSet = set(paramNames)
            if ActiRequestSet & paramSet != set():
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


class myListWidgetItem(QtGui.QListWidgetItem):
    def __init__(self,name, listView):
        super(myListWidgetItem,self).__init__(name, listView)
        self.param = ''
        self.liste = listView