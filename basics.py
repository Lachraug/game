import random 
import pygame as py
from GUI_widgets import *

py.init()

gimmick_adj = ['Cheerful', 'Aggressive', 'Sadistic', 'Angry', 'Dazzling', 'Fabulous', 'Charming', 'Slimey', 'Friendly', 'Loyal', 'Hardworking', 'Moody', 'Mysterious', 'Petty', 'Ass Kissing', 'Lazy', 'Sexy', 'Disillusioned', 'Under Appreciated', 'Over Rated', 'Shy', 'Insane', 'Fun Loving', 'Cute', 'Psychotic', 'Magical', 'Evil', 'Holy', 'Sweaty', 'Idiotic', 'Goofy', 'Stoic', 'Earnest', 'Relatable', 'Angelic', 'Unrelatable', 'Annoying', 'Ditzy', 'Compassionate', 'Disturbed', 'Nervous', 'Quiet', 'Clever', 'Vain', 'Clumsy', 'Sleepy', 'Plucky', 'Ambitious', 'Calm']
gimmick_noun = ['Pirate', 'Underdog', 'MMA Fighter', 'Rockstar', 'Prodigy', 'Taxi Driver', 'Daredevil', 'Demon', 'Theater Kid', 'Stoner', 'Gamer', 'Conspiracy Theorist', 'Talk Radio Host', 'Mail Man', 'Movie Star', 'Rebel', 'Punk', 'Emo', 'Ex Marine', 'Ghost', 'Everyman', 'Legacy Child', 'Influencer', 'Mean Girl', 'Rebel', 'Politician', 'Big Guy', 'Small Guy', 'Hacker', 'Furry', 'Olympian', 'Maniac', 'Nerd', 'Elon Musk type', 'Super Hero', 'Cowboy', 'Sheriff', 'Cop', 'Anarchist', 'Neoliberal', 'Philosopher', 'NYT Writer', 'Royalty', 'Orphan', 'Preacher', 'Hunk', 'Lady\'s Man', 'Nate Silver Type', 'Loner', 'Living Statue', 'Monk', 'Dancer', 'Warrior', 'Miser', 'Gig Worker', 'Leader', 'CEO', 'Priest', 'Knight', 'Comedian', 'Super Hero', 'Weeb', 'Undead', 'Plumber']



wrestlerFirstName=['Thunder', 'Bob', 'Big', 'Henry', 'Street', 'Boy', 'Dastardly', 'Billy', 'Marco', 'Sammy', 'Beastly', 'Brett', 'Brian', 'Lamar', 'Muscles', 'Strong-arm', 'Beef', 'Nails', 'Hammer', 'Throck', 'Pal', 'Miles', 'Smiley', 'Fatty', '4 Eyed', 'Slapper', 'Arnold', 'Monk', 'Jim', 'Pirate', 'Mark', 'Peter', 'Greg', 'Smashin\'', 'Beefy', 'Jason', 'Greg', 'Bill', 'Harry', 'Homer', 'Ripley', 'Bandit', 'Crunch', 'Hair', 'King', 'Quail', 'Cowboy', 'Snake']
wrestlerLastName=['Jaw', 'Fisher', 'Slappin', 'ol Boy', 'Jones', 'Slayer', 'Guiles', 'Nasty', 'Young Gun', 'Steel', 'Jones', 'Gregory', 'Malone', 'Masher', 'Grunt', 'Thrustmaster', 'Soto', 'Knight', 'Day', 'O’Houlihan', 'The Slammer', 'Hooligan', 'Destroyer', 'Powers', 'Farmer', 'Jams', 'Bond', 'Snow', 'Powerhouse', 'Ray', 'Grimes', 'Green', 'Twist', 'Cannon', 'Clash', 'Sawyer', 'Giant', 'Red', 'Thighs', 'Dog', 'Slayer', 'Demon', 'The Fist', 'Money', 'The Ringer']

styles=['Strong Style', 'Lucha Libre', 'Catch', 'Striker', 'Technician']
match_types=['No DQ', 'Cage', 'Dog Collar', 'Ladder', 'Falls Anywhere', 'Last Man Standing']

plot_beats_list = ['Run In', 'Injury', 'Prematch Fight', 'Beat Down', 'Rally', 'Disqualified', 'Match Start', 'Match End']

types_of_DQ = ['Illegal Weapon', 'Outside Help', 'Illegal Move', 'Arguing With Ref']

match_times = ['Squash', 'Short', 'Medium', 'Long', 'Epic']


personality = ['Cowardly', 'Brave', 'Humble', 'Arrogant', 'smart', 'stupid', 'mysterious']

irl_personalities = ['Egotist', 'Helping Hand', 'Workaholic', 'Spot Light Seaker']


fans = [0, 1, 2]


def make_style(lst=styles):
    style=[]
    style.append(random.choice(lst))
    style.append(random.choice(lst))
    return style


def make_name(first_lst=wrestlerFirstName, last_lst=wrestlerLastName):
    first=random.choice(first_lst)
    last=random.choice(last_lst)
    name=first + ' ' + last
    return name

def make_gimmick(adj_lst = gimmick_adj, noun_lst = gimmick_noun):
    adj = random.choice(adj_lst)
    noun = random.choice(noun_lst)
    lst = [adj, noun]
    return lst

def main(Surface,Player):
    game_event_loop(Player)
    Surface.fill(0)
    Player.update(Surface)

class MatchReview:
    def __init__(self, match, wrestler):
        self.wrestler = wrestler
        self.match = match
        self.heat = {}
        self.injury = [self.wrestler.injury]
        self.overness = {}
        self.boredom = {}
        self.botch = False

class Button:
    def __init__(self, color, x, y, width, height, text='', txtsize = 60, metadata=False, text_color = (0,0,0)):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.txtsize = txtsize
        self.metadata = metadata
        self.text_color = text_color



    def draw(self,win, outline=None):

        #Call this method to draw the button on the screen
        if outline:
            py.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        py.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = py.font.SysFont('comicsans', self.txtsize)
            text = font.render(self.text, 1, self.text_color)
            font.render(self.text, 1, self.text_color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
    
    
    def hover(self, pos, text, update = False):
        if self.isOver(pos):
            button = Txt_Left_Button(BLACK, pos[0], pos[1], 300, 150, text, 20, False, (225, 225, 225))
            button.draw(surf, True)

            if update == True:
                py.display.update(pos[0]-100, pos[1]-100, pos[0]+375, pos[1]+250)

class Gimmick:
    def __init__(self):
        self.lst = make_gimmick()
        self.main_adjective = self.lst[0]
        self.main_noun = self.lst[1]
        self.side_adjectives = []
        self.side_nouns = []
        self.display = self.lst[0] + ' ' + self.lst[1]

class Style:
    def __init__(self):
        self.lst = make_style()
        self.main = self.lst[0]
        self.secondary = self.lst[1]
        self.display = self.lst[0] + ', ' + self.lst[1]

class Wrestler:
    def __init__(self):
        self.name = make_name()
        self.style = Style()
        self.gimmick = Gimmick()
        self.chrctr_work=random.randrange(20)
        self.skill = random.randrange(100)
        self.pay=random.randrange(20)
        self.overness = 0
        self.happy = 100
        self.title = ''
        self.energy = 100
        self.heel_face = random.randrange(10)
        self.legs_health = 0
        self.arms_health = 0
        self.torso_health= 0
        self.head_health= 0
        self.injury = 0
        self.heat = 0
        
        self.personality = random.choice(irl_personalities)
        self.friends = []
        self.enemies = []
        self.past_matches = []
        
        

        self.match_history = []
        self.display = [self.name, 'Style: ' + self.style.lst[0] + ', ' + self.style.lst[1], 'Overness: ' + str(self.overness), 'Tired: ' + str(self.energy)]
        self.feud = False
        self.past_feud = []
        self.long_term_feud = False
        
    
    def calculate_heat(self, match, fans):
        outcomes = []
        for fan in fans:

            if wrap_up != False:
                outcomes.append(wrap_up)
        
        return wrap_up

    def average_heat(self, fans):
        self.heat = 0
        num = 0
        fan_pop = 0
        percent = 0
        
        for fan in fans:
            fan_pop += fan.size
            
        for fan in fans:
            percent = fan.size/fan_pop

            num = percent * fan.wrestler_heat.get(self)
            
            self.heat += num

        num = round(self.heat, 2)
        self.heat = num


    def add_friend(self, wrestler):
        self.friends.append(wrestler)

    def add_enemy(self, wrestler):
        self.enemies.append(wrestler) 

    def average_overness(self, fans):
        self.overness = 0
        num = 0
        fan_pop = 0
        percent = 0
        
        for fan in fans:
            fan_pop += fan.size
        for fan in fans:
            percent = fan.size/fan_pop
            
            num = percent * fan.wrestlers_pop.get(self)
            self.overness += num
        num = round(self.overness, 2)
        self.overness = num

    def summary(self):
        pass

    def quick_summary(self):
        friends = ''
        enemies = ''
        health = 'healthy'
        last_match = ''
        lst_of_info =[]

        if len(self.friends) == 0:
            friends = 'No Current Friends'
        elif len(self.friends) == 1:
            friends = 'Top Friends: ' + self.friends[0].name
        elif len(self.friends) > 1:
            friends = 'Top Friends: ' + self.friends[0].name + ', ' + self.friends[1].name


        if len(self.enemies) == 0:
            enemies = 'No Current Enemies'
        elif len(self.enemies) == 1:
            enemies = 'Top Enemies: ' + self.enemies[0].name 
        elif len(self.enemies) > 1:
            enemies = 'Top Enemies: ' + self.enemies[0].name + ', ' + self.enemies[1].name



        if self.legs_health or self.torso_health or self.arms_health or self.head_health < 3:
            health = 'Not Injured' 
        elif self.legs_health or self.torso_health or self.arms_health or self.head_health > 2 and self.legs_health or self.torso_health or self.arms_health or self.head_health < 5:
            health = 'Mild Injury'
        elif self.legs_health or self.torso_health or self.arms_health or self.head_health > 4 and self.legs_health or self.torso_health or self.arms_health or self.head_health < 8:
            health = 'Injured'
        elif self.legs_health or self.torso_health or self.arms_health or self.head_health > 7 and self.legs_health or self.torso_health or self.arms_health or self.head_health < 11:
            health = 'Sever Injury'

        if len(self.match_history) > 0:
            last_match = 'Last Match: ' + self.match_history[-1].name
        elif len(self.match_history) == 0:
            last_match = 'No Past Matches'

        styl = 'Style: ' + self.style.lst[0] + ', ' + self.style.lst[1]


        lst_of_info.append('Current Championship: ' + self.title)
        lst_of_info.append(friends)
        lst_of_info.append(enemies)
        lst_of_info.append(health)
        lst_of_info.append(last_match)
        lst_of_info.append(styl)


        return lst_of_info

    def injured(self):

        injury = random.randrange(4)
        injury_pnt = random.randrange(20)

        if injury == 1:
            self.legs_health += injury_pnt
        if injury == 2:
            self.arms_health += injury_pnt
        if injury == 3:
            self.torso_health += injury_pnt
        if injury == 4:
            self.head_health += injury_pnt

    def over(self, x):
        self.overness += x

class Fans:
    def __init__(self, style):
        self.fav_wrst = []
        self.wrestlers_pop = {}
        self.style = style
        self.desired_match = {}
        self.happy = 0
        self.size = 50
        self.wrestler_heat = {}
        self.wrestler_support = {}
        self.wrestler_bored = {}

    def calculate_heat_match_outcome(self, match):
        difference = self.wrestlers_pop.get(match.loser) - self.wrestlers_pop.get(match.winner)
        winner = match.winner
        review_to_edit = match.review.get(match.winner)
        
        if self.style in match.loser.style.lst and self.style not in match.winner.style.lst:
            self.wrestler_heat[match.winner] += .5
            if difference > 20:
                roll = random.randrange(3)
                self.wrestler_heat[match.winner] += roll

                #putting in numbers in the match review
                review_to_edit.heat[self.style] = (roll + .5)

                return (self.style + ' fans are slightly heated that ' + match.winner.name + ' beat ' + match.loser.name)
        elif difference > 30:
            roll = random.randrange(3)
            self.wrestler_heat[winner] += (roll + .5)
            
                #putting in numbers in the match review
            review_to_edit.heat[self.style] = (roll + .5)


            return (self.style + ' fans are slightly heated that ' + match.winner.name + ' beat ' + match.loser.name)
        else:
            
            review_to_edit.heat[self.style] = 0
            return False
        
    def make_roster(self, stats):
        for wrestler in stats.roster:
            self.wrestlers[wrestler] = wrestler.overness

    def roll_for_overness(self, match, spots, botch):
        #variable change is for the sake of logging the change
        change = {}
        performance = 0

        for wrestler in match.wrestlers:
            performance += wrestler.skill
            change[wrestler] = self.wrestlers_pop.get(wrestler)


        performance -= botch

        if botch == 0:
            performance += spots

        roll = random.randrange(100 * len(match.wrestlers))


        win_over = self.wrestlers_pop.get(match.winner)
        los_over = self.wrestlers_pop.get(match.loser)

        #putting over another wrestler costs the person who has a lot of overness but it does give 'em a bump
        if los_over > win_over:
            difference = los_over - win_over
            if difference > 29:
                self.wrestlers_pop[match.loser] -= 1
                self.wrestlers_pop[match.winner] += 1
            elif difference > 49:
                self.wrestlers_pop[match.loser] += 2
                self.wrestlers_pop[match.winner] -= 5

        #if you fail the first roll, you have to get under your current overness to go down
        if performance < roll:
            for wrestler in match.wrestlers:
                overness = self.wrestlers_pop.get(wrestler)
                roll = random.randrange(100)
                if roll < overness:
                    self.wrestlers_pop[wrestler] -= 1
                    if botch > 0:
                        self.wrestlers_pop[wrestler] -= 1
                        #if the wrestler is the correct style and its only a minor botch you counter the botch minus
                        if self.style in wrestler.style.lst:
                            if botch == 5:
                                self.wrestlers_pop[wrestler] += 1

        elif performance > roll:
            for wrestler in match.wrestlers:
                overness = self.wrestlers_pop.get(wrestler)
                roll = random.randrange(100)
                if roll > overness:
                    self.wrestlers_pop[wrestler] += 1

                    if self.style in wrestler.style.lst:
                        self.wrestlers_pop[wrestler] += 1

                if self.style in wrestler.style.lst:
                    self.wrestlers_pop[wrestler] += 1
                if self.wrestlers_pop[wrestler] > 100:
                    self.wrestlers_pop[wrestler] = 100
        
        for wrestler in match.wrestlers:
            if self.wrestlers_pop[wrestler] <= 0:
                self.wrestlers_pop[wrestler] = 0

            #calculating for review
            before_match_number = change.get(wrestler)

            after_match_number = self.wrestlers_pop.get(wrestler)
            overall_change = before_match_number - after_match_number

            wrestler_review = match.review.get(wrestler)
            wrestler_review.overness[self.style] = overall_change


    def calculate_heat_over_other(self, match):
        retun = False
        winner = match.winner
        loser = match.loser

        win_over = self.wrestlers_pop.get(winner)
        win_heat = self.wrestler_heat.get(winner)

        los_over = self.wrestlers_pop.get(loser)
        los_heat = self.wrestler_heat.get(loser)


#        if win_over > los_over:
#            if los_heat > los_over * 1.5:
#                modified_los_heat = los_heat/2
#                self.wrestler_heat[loser] = modified_los_heat
#                return True
        return retun

    def frequency_of_wrestler(self, wrestler, stats):
        
        overness = self.wrestlers_pop.get(wrestler)
        heat = self.wrestler_heat.get(wrestler)
        count = 0
        if overness > 80:
            if len(stats.past_shows) < 10:
                for show in stats.past_shows:
                    if wrestler in show.wrestlers:
                        
                        count +=1
                        
            else: 
                for show in stats.past_shows[-10:]:
                    if wrestler in show.wrestlers:
                        
                        count += 1
            if count > 7:
                return 'danger'
            if count == 7:
                return 'warning'

        elif overness > 60:
            if len(stats.past_shows) < 8:
                for show in stats.past_shows:
                    if wrestler in show.wrestlers:
                        
                        count +=1          
            else: 
                for show in stats.past_shows[-8:]:
                    if wrestler in show.wrestlers:
                        
                        count += 1
            if count > 4:
                return 'danger'
            if count == 4:
                return 'warning'
        
        elif overness > 40:
            
            if len(stats.past_shows) < 6:
                for show in stats.past_shows:
                    if wrestler in show.wrestlers:
                        
                        count +=1        
            else: 
                for show in stats.past_shows[-6:]:
                    if wrestler in show.wrestlers:
                        
                        count += 1
            if count > 3:
                return 'danger'
            if count == 3:
                return 'warning'
        
        elif overness >= 0:
            if len(stats.past_shows) < 3:
                for show in stats.past_shows:

                    if wrestler in show.wrestlers:
                        
                        count +=1    
            else: 
                for show in stats.past_shows[-3:]:
                    if wrestler in show.wrestlers:
                        
                        count += 1
            if count > 1:
                return 'danger'
            if count == 0:
                return  'warning'

    def adjust_boredom(self, wrestler, stats):
        if self.frequency_of_wrestler(wrestler, stats) == 'danger':
            if wrestler in self.wrestler_bored:
                flip = random.randrange(2)
                print('got here')
                if flip == 1:
                    self.wrestler_bored[wrestler] += 1
                    print(wrestler.name + 'should adjust his boreddom')

    def bored_impact(self, match):
        confirm = False

        for wrestler in match.wrestlers:
            bored = self.wrestler_bored.get(wrestler)
            if bored == 1:
                roll = random.randrange(2)
                if roll == 1:
                    confirm = True
                    break
        
        if confirm == True:
            for wrestler in match.wrestlers:
                print(self.wrestler_heat.get(wrestler))
                self.wrestler_heat[wrestler] -= 2
                if self.wrestler_heat[wrestler] < 1:
                    self.wrestler_heat[wrestler] = 0
                    print(self.wrestler_heat.get(wrestler))

for style in styles:
    new = Fans(style)
    fans.append(new)

class Show:
    def __init__(self):
        self.matches = []
        self.venue = 'venue'
        self.promos = []
        self.timeline = []
        self.wrap_up = []
        self.name = 'PPV'
        self.wrestlers = []

    def add_match(self, wrestlers):
        self.matches.append(wrestlers)

    def get_wrap_up():
        for event in timeline:
            event.calculate_match()
            self.wrap_up.append(event.wrap_up)

class Disqualification:
    def __init__(self, type_of_dq):
        self.DQed = False
        self.type_of_DQ = False
        self.name = type_of_dq
        self.type = 'DQ'

class Promo:
    def __init__(self):
        self.wrestler_one = False
        self.wrestler_two = False
        self.type = ''

class Run_In:
    def __init__(self, run_iner, connected_wrestler, other, connection):
        self.first_party = run_iner
        self.second_party = connected_wrestler
        self.third_party = other

        #options are 'Friends of: ' or 'Enemies of: '
        self.connection = connection
        self.type = 'run in'
        self.display = []
    
    def make_display(self):

        if self.connection == 'friend':
            relation = 'assist'
        if self.connection == 'enemy':
            relation = 'attack'
        self.display = [self.first_party.name, 'will ' + relation, self.second_party.name]
    
class Injury:
    def __init__(self, wrestler, bodypart, severity):
        self.wrestler = wrestler
        self.bodypart = bodypart
        self.severity = severity
        self.type = 'injury'
        self.display = []
    
    def make_display(self):
        self.display = [self.wrestler.name, 'injures ' + self.bodypart, self.severity]

class Feuds:
    def __init__(self):
        self.wrestlers = []
        self.matches = []
        self.segments = []
        self.events = []
        self.fan_approval = 0
        self.origin = False
        self.type = ''
        self.length = ''

Feud_catagories = ['Heroic', 'Evil', 'Supernatural']

stats = GenStats()

class Feud_Evil(Feuds):
    def __init__(self):
        super().__init__
        self.type = 'Evil'
        self.name = ''
        


class Match:
    def __init__(self):
        self.wrestlers= []
        self.others = []
        self.winner = False
        self.loser = False
        self.name = ''
        self.risk= 0
        self.time= 0
        self.weapons = []
        self.overness = 0
        self.type = ''
        self.plot = []
        self.plot_visuals = []
        self.feud = False
        self.wrap_up = []
        self.spots = ''
        self.length = ''
        self.feud = False
        self.show = False
        self.review = {}


    def add_wrestlers(self, wrestlerOne, wrestlerTwo):
        self.wrestlers.append(wrestlerOne)
        self.wrestlers.append(wrestlerTwo)
        self.name = self.wrestlers[0].name + ' vs ' + self.wrestlers[1].name
        
    def plan_type(self, match_type):
        self.type = match_type

    def create_reviews(self):
        for wrestler in self.wrestlers:
            self.review[wrestler] = MatchReview(self, wrestler)


    def calculate_botch(self, wrestler, num):
        roll = random.randrange(101)
        if roll > wrestler.skill:
            botch_roll = random.randrange(11)

            if botch_roll < 7:
                #self.review[num].botch = 'Minor'
                self.wrap_up.append(wrestler.name + ' did a minor botch.')
                return 5

            if botch_roll == 7 or 8 or 9:
                #self.review[num].botch = 'Medium'
                self.wrap_up.append(wrestler.name + ' botched.')
                return 15

            if botch_roll == 10:
                #self.review[num].botch = 'Big'
                self.wrap_up.append(wrestler.name + ' did a major botch.')
                return 30
        else: 
            return 0

    def calculate_spots(self):   
        performance = 0     
        if self.spots == 'Low':
            performance = 3
        if self.spots == 'Medium':
            performance = 6
        if self.spots == 'High':
            performance = 12
        
        return performance

    def calculate_fan_response(self, fans):
        #setting up variables to plug into the fan rolls
        wrestler_for_botch_roll = random.randrange(len(self.wrestlers) - 1)
        botch = self.calculate_botch(self.wrestlers[wrestler_for_botch_roll], wrestler_for_botch_roll)
        spots = self.calculate_spots()


        pop_before = []
        #to be compared afterwards
        for wrestler in self.wrestlers:
            pop_before.append(wrestler.overness)


        wrestler_one = self.wrestlers[0].overness
        wrestler_two = self.wrestlers[1].overness

        for fan in fans:
            fan.roll_for_overness(self, spots, botch)
            fan.calculate_heat_match_outcome(self)

        for wrestler in self.wrestlers:
            wrestler.average_overness(fans)

            

        # for num in range((len(self.wrestlers))):

        #     if self.wrestlers[num].overness > pop_before[num]:
        #         self.wrap_up.append(self.wrestlers[num].name + ' seems to have lost some fan\'s interest')
        #         self.review[num].overness = self.wrestlers[num].overness - pop_before[num]

        #     if self.wrestlers[num].overness < pop_before[num]:
        #         self.wrap_up.append(self.wrestlers[num].name + ' seems to have gained some fan\'s interest')
        #         self.review[num].overness = self.wrestlers[num].overness - pop_before[num]

 

    def calc_happiness(self):

        def winner_over_loser(self):

            difference = self.winner.overness - self.loser.overness
            if difference > 59:
                self.loser.happy += 3
                self.winner.happy -= 5
            elif difference > 39:
                self.loser.happy += 2
                self.winner.happy -= 3
            elif difference > 19:
                self.loser.happy += 1

        def loser_over_winner(self):
            difference = self.loser.overness - self.winner.overness
            if difference > 59:
                self.loser.happy -= 10
                self.winner.happy += 5
            elif difference > 39:
                self.loser.happy -= 7
                self.winner.happy += 4
            elif difference > 15: 
                self.loser.happy -= 5
                self.winner.happy += 3



        if self.loser.personality == 'Egotist':
            if self.loser.overness < self.winner.overness:
                difference = self.loser.overness - self.winner.overness
                if difference > 59:
                    self.loser.happy -= 15
                    self.winner.happy += 5
                elif difference > 39:
                    self.loser.happy -= 10
                    self.winner.happy += 4
                elif difference > 15: 
                    self.loser.happy -= 8
                    self.winner.happy += 3
            
            if self.winner.overness > self.loser.overness:
                self.loser_over_winner()
            

        elif self.loser.personality == 'Helping Hand':
            if self.winner.overness < self.loser.overness:
                difference = self.loser.overness - self.winner.overness
                if difference > 59:
                    self.winner.happy += 5
                elif difference > 39:
                    self.winner.happy += 4
                elif difference > 15: 
                    self.winner.happy += 3
            
            elif self.winner.overness > self.loser.overness:
                self.winner_over_loser()

    def catalogue_event(self):
        for wrestler in self.wrestlers:
            wrestler.match_history.append(self)
        if self.feud:
            for wrestler in self.wrestlers:
                wrestler.feud.matches.append(self)
                wrestler.feud.events.append(self)

    def calculate_risk(self):
        num_of_wrestlers = len(self.wrestlers)
        risk = 0
        for wrestler in self.wrestlers:
            risk += wrestler.skill
            risk -= wrestler.energy
        
        if self.spots == 'Low':
            risk -= 5
        if self.spots == 'Medium':
            risk -= 10
        if self.spots == 'High':
            risk -= 20


        roll = random.randrange(100 * num_of_wrestlers)
        if roll > risk:
            return True
    
    def calculate_injury(self):
        coin_flip = random.randrange(len(self.wrestlers))
        injury_amount = random.randrange(30)
        if random.randrange(30) == 0:
            self.wrestlers[coin_flip].injury == 100
            return self.wrestlers[coin_flip].name + ' was injured'
        
        else:
            self.wrestlers[coin_flip].injury += injury_amount
            if self.wrestlers[coin_flip].injury > 99:
                return self.wrestlers[coin_flip].name + ' was injured'
            else:
                return self.wrestlers[coin_flip].name + ' got a bit battered up'

    def calculate_event(self, fans):
        
        self.calculate_fan_response(fans)
        for fan in fans:
            wrap_up = fan.calculate_heat_match_outcome(self)


        if self.calculate_risk():
            injury = self.calculate_injury()
            self.wrap_up.append(injury)



            if wrap_up:
                self.wrap_up.append(wrap_up)
    
    def calculate_boredom(self, fans):
        for fan in fans:
            for wrestler in self.wrestlers:
                if fan.frequency_of_wrestler(wrestler, stats):
                    print('returned true')
                    fan.adjust_boredom(wrestler)
        
    def draw_match(self):
        name = Txt_Left_Button(SILVER, 1000, 160, 230, 65, [self.winner.name, 'def', self.loser.name], 25)
        counter = 240

        name.draw(surf, True)
        for event in self.wrap_up:

            nxt = Button(WHITE, 1100, counter, 0, 0, event, 25)
            counter += 25
            nxt.draw(surf, False)
            
            if counter == 685:
                break  

    def calculate_energy(self):
        for wrestler in self.wrestlers:
            if self.length == 'long':
                wrestler.energy -= 12
                if self.type != '':
                    wrestler.energy -= 8
            elif self.length == 'medium':
                wrestler.energy -= 10
                if self.type != '':
                    wrestler.energy -= 5
            elif self.length == 'short':
                wrestler.energy -= 7
                if self.type != '':
                    wrestler.energy -= 3










plot_beats_list = ['Run In', 'Injury', 'Prematch Fight', 'Beat Down', 'Rally', 'Grab Mic/Promo', 'Argue w/ Ref', 'Slap Off', 'Table Spot', 'Illegal Weapon']

types_of_DQ = ['Illegal Weapon', 'Outside Help', 'Illegal Move', 'Arguing With Ref']

weapon = Disqualification('Illegal Weapon')
outside_help = Disqualification('Outside Help')
illegal_move = Disqualification('Illegal Move')
arguing_with_ref = Disqualification('Arguing w/ Ref')


feud_architypes = ['Jealousy', 'Title Chase', 'Superior', 'Revenge']




types_of_DQ = [weapon, outside_help, illegal_move, arguing_with_ref]





fans = []
for style in styles:
    new = Fans(style)
    fans.append(new)

#images
check_mark = dollar = py.image.load(r'C:\Users\Peter\Desktop\Wrestlinggame\pics\check_mark.png')
check_mark_resized = py.transform.scale(check_mark,(40,40))
check_mark_smaller = py.transform.scale(check_mark, (25, 25))

bob= Wrestler()

dob = Wrestler()

lob = Wrestler()

bob.title = 'The Cool Championship'

print('hi')

spots_selection = ['None', 'Low', 'Medium', 'High']