class GenStats:
    def __init__(self):
        #personal
        self.money = 0
        self.roster = []
        self.roster_names = []
        self.equiptment = []
        self.sorted_list = []
        self.feuds = []
        self.past_feuds = []
        self.oppertunities = []
        self.past_shows = []
    
    def adjust_money(self, x):
        self.money+=x

    def add_roster(self, wrestler):
        self.roster.append(wrestler)
        self.roster_names.append(wrestler.name)



    def pay_roster(self):
        for wrestler in self.roster:
            self.money-=wrestler.pay