class Equipment():
    def __init__(self):
        self.quartier = ''
        self.name = ''
        self.adresse = ''
        self.type = ''
        self.activities = {}          #dictionnary of possible activities. Par ex: {'bad':2,'foot':1,}
        self.revetement = []          #par ex: gazon, ciment, ...
        self.size = None              #(x,y)
        self.eclairage = 0         # 0 ou 1
        self.arrosage = 0          #0 ou 1
        self.vestiaire = []           # [nb pr joueurs, pr arbitres]
        self.sanitaires = None        #1 <=> oui mais nombre inconnu, un nombre: le nombre...
        self.douches = []             # [nb individuelles, nb collectives]
        self.capaMax = 0              #0<=> non applicable / pas de données
        self.tribunes = 0             # nb de places: 0<=> N/A / no data
        self.clubHouse = 0            #0/1
        self.categorie = 0            # 0<=> N/A / no data
        self.date = 0                 # 0<=> N/A / no data
        self.accesHand = 0         #0/1
        self.toilettesHand = 0     #0/1
        self.coords = None            #(latitude, longitude)
        # Les filtreas doivent modifier cette valeur, et appeler appli.update_affichage_equipements() pour mettre,à jour la carte.

    def __repr__(self):
        text = '  '.join([self.name, self.type, str(self.coords)])
        return text
