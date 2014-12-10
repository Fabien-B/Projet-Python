class Equipment():
    def __init__(self):
        self.quartier=''
        self.name=''
        self.adresse=''
        self.type=''
        self.activities={}          #dictionnary of possible activities. Par ex: {'bad':2,'foot':1,}
        self.revetement=[]          #par ex: gazon, ciment, ...
        self.size=None              #(x,y)
        self.eclairage=None         # 0 ou 1
        self.arrosage=None          #0 ou 1
        self.vestiaire=[]           # [nb pr joueurs, pr arbitres]
        self.sanitaires=None        #1 <=> oui mais nombre inconnu, un nombre: le nombre...
        self.douches=[]             # [nb individuelles, nb collectives]
        self.capaMax=0              #0<=> non applicable / pas de données
        self.tribunes=0             # nb de places: 0<=> N/A / no data
        self.clubHouse=0            #0/1
        self.categorie=0            # 0<=> N/A / no data
        self.date=0                 # 0<=> N/A / no data
        self.accesHand=None         #0/1
        self.toilettesHand=None     #0/1
        self.coords = None          #(latitude, longitude)

