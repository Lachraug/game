import pygame as py

from GenStats import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SILVER = (192,192,192)
GOLD = (255,215,0)
LGTRED = (255, 51, 51)
DARKGREY = (100,100,100)
LGTBLUE = (173, 207, 230)
DARKRED = (139,0,0)
LGTGREEN = (51, 225, 51)
YELLOW = (255,255,0)
DRKYELLOW = (224,165,38)

fans = []

stats = GenStats()

py.init()

pos = py.mouse.get_pos()
surf = py.display.set_mode((1400, 800), 0, 32)

class Text():
    def __init__(self, x, y, text, txtsize = 40, color = (0, 0, 0)):
        self.x = x
        self.y = y
        self.text = text
        self.size = txtsize
        self.color = color

    def draw(self, win):
        font = py.font.SysFont('comicsans', self.size)
        text = font.render(self.text, 1, self.color)
        font.render(self.text, 1, self.color)
        win.blit(text, (self.x, self.y))


class Txt_Left_Button():

    def __init__(self, color, x,y,width,height, text = [], txtsize = 60, metadata=False, text_color = (0,0,0)):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.txtsize = txtsize
        self.metadata = metadata
        self.text_color = text_color

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

    def draw(self, win, outline = True):

        if outline:
            py.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        py.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
 
        liney = self.y

        if isinstance(self.text, str):
            font = py.font.SysFont('comicsans', self.txtsize)
            text = font.render(self.text, 1, self.text_color)
            font.render(self.text, 1, self.text_color)
            win.blit(text, (self.x, self.y))

        elif len(self.text) > 1:
 
            for line in self.text:

                font = py.font.SysFont('comicsans', self.txtsize)
                text = font.render(line, 1, self.text_color)
                font.render(line, 1, self.text_color)
                win.blit(text, (self.x, liney))
                liney += self.txtsize - 5
        
    def hover(self, pos, text, update = False):
        if self.isOver(pos):
            button = Txt_Left_Button(BLACK, pos[0], pos[1], 300, 150, text, 20, False, (225, 225, 225))
            button.draw(surf, True)

            if update == True:
                py.display.update(pos[0]-100, pos[1]-100, pos[0]+375, pos[1]+250)

class Button():
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


class Scroll_List():
    def __init__(self, color, x, y, num_of_boxes, text, metadata = False, text_size = 25):
        self.x = x
        self.y = y
        self.num_of_boxes = num_of_boxes
        self.text = text
        self.outline = Button(WHITE, self.x, self.y, 350, (60*num_of_boxes+10))
        self.up_button = Button(WHITE, (self.x + 355), self.y, 30, 30, 'UP', 20)
        self.down_button = Button(WHITE, (self.x + 355), (self.y + ((num_of_boxes*60)-20)), 30, 30, 'Down', 20)
        self.click_list = []
        self.draw_list = []

        self.text_size = text_size
        self.metadata = metadata
        self.place_in_list = 0
        self.color = color

        

    #this is to create a list to draw for the UI
    def create_list(self):
        self.draw_list = self.text[self.place_in_list:(self.num_of_boxes+self.place_in_list)]


    def draw(self, surf):
        self.click_list = []
        self.outline.draw(surf, True)
        self.up_button.draw(surf, True)
        self.down_button.draw(surf, True)

        #Y point
        counter = self.y + 5

        #when the list needs to stop
        break_point = self.y + 100 + (self.num_of_boxes*60)

        for x in self.draw_list:
            button = Button(self.color, self.x + 5, counter + 5, 340, 50, x.name, self.text_size, x)
            button.draw(surf, True)
            counter += 60
            self.click_list.append(button)

            #if counter > break_point:
            #    break

class Scroll_List_Custom():
    def __init__(self, color, x, y, width, height, num_of_boxes, text, metadata = False, text_size = 25):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.num_of_boxes = num_of_boxes
        self.text = text
        self.outline = Button(WHITE, self.x, self.y, self.width + 10, (self.height*num_of_boxes + 5*self.num_of_boxes + 10))
        self.up_button = Button(WHITE, (self.x + self.width + 10), self.y, 30, 30, 'UP', 20)
        self.down_button = Button(WHITE, (self.x + self.width +10), (self.y + (num_of_boxes*self.height)), 30, 30, 'Down', 20)
        self.click_list = []
        self.draw_list = []


        self.text_size = text_size
        self.metadata = metadata
        self.place_in_list = 0
        self.color = color

        

    #this is to create a list to draw for the UI
    def create_list(self):
        self.draw_list = self.text[self.place_in_list:(self.num_of_boxes+self.place_in_list)]


    def draw(self, surf):
        self.click_list = []
        self.outline.draw(surf, True)
        self.up_button.draw(surf, True)
        self.down_button.draw(surf, True)

        #Y point
        counter = self.y + 5

        #when the list needs to stop
        break_point = self.y + 100 + (self.num_of_boxes*60)

        for x in self.draw_list:
            button = Button(self.color, self.x + 5, counter + 5, self.width, self.height, x.name, self.text_size, x)
            button.draw(surf, True)
            counter += self.height+5
            self.click_list.append(button)

            #if counter > break_point:
            #    break

class Header_Button():
    
    def __init__(self, color_one, color_two, x, y, width, height, text_one, text_two, txtsize = 40, txtsize_two = 40, metadata = False, text_color_one = (0,0,0), text_color_two = (0,0,0)):
        self.color_one = color_one
        self.color_two = color_two
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_one = text_one
        self.text_two =text_two
        self.txtsize = txtsize
        self.txtsize_two = txtsize_two
        self.metadata = metadata
        self.text_color_one = text_color_one
        self.text_color_two = text_color_two
        self.top  = Button(self.color_one, self.x, self.y, self.width, self.height, self.text_one, self.txtsize, False, self.text_color_one)
        self.bottom  = Button(self.color_two, self.x, (self.y + self.height + 5), self.width, self.height, self.text_two, self.txtsize_two, self.metadata, self.text_color_two)


    def draw(self,win):
        
        self.top.draw(win, False)
        self.bottom.draw(win, True)
        #Call this method to draw the button on the screen

class Scroll_List_Detailed_Wrestlers():
    def __init__(self, color, x, y, width, height, num_of_boxes, data, metadata = False, text_size = 25, text_color = (0, 0, 0)):
        self.x = x
        self.y = y
        self.num_of_boxes = num_of_boxes
        self.data = data
        self.width = width
        self.height = height
        self.outline = Button(WHITE, self.x, self.y, self.width + 10, (self.height*num_of_boxes + 5*self.num_of_boxes + 10))
        self.up_button = Button(WHITE, (self.x + self.width + 10), self.y, 30, 30, 'UP', 20)
        self.down_button = Button(WHITE, (self.x + self.width +10), (self.y + (num_of_boxes*self.height)), 30, 30, 'Down', 20)
        self.click_list = []
        self.draw_list = []
        self.text_color = text_color

        self.text_size = text_size
        self.metadata = metadata
        self.place_in_list = 0
        self.color = color

        

    #this is to create a list to draw for the UI
    def create_list(self):
        self.draw_list = self.data[self.place_in_list:(self.num_of_boxes+self.place_in_list)]


    def draw(self, surf):
        self.click_list = []
        self.outline.draw(surf, True)
        self.up_button.draw(surf, True)
        self.down_button.draw(surf, True)

        #Y point
        counter = self.y + 5

        #when the list needs to stop

        for x in self.draw_list:
            button = Txt_Left_Button(self.color, self.x + 5, counter + 5, self.width, self.height, x.display, self.text_size, x, self.text_color)
            button.draw(surf, True)
            counter += self.height + 5
            self.click_list.append(button)

class FanGraph:
    def __init__(self, x, y, stat, fans, wrestler = False):
        self.x = x
        self.y = y
        self.stat = stat
        self.fans = fans
        self.wrestler = wrestler
    
    def draw(self, surf, stats):
        counter = self.y
        outline = ((self.x-5, self.y -5), (295, (20*len(self.fans) + 5)))
        py.draw.rect(surf, BLACK, outline, 2)

        if self.wrestler:
            wrestler_name = Button(WHITE, self.x + 147, self.y - 15, 0, 0, self.stat + ': ' + self.wrestler.name, 23)
            wrestler_name.draw(surf)

        for fan in self.fans:
            if self.stat == 'heat':
                heat = fan.wrestler_heat.get(self.wrestler)
                style = Text(self.x, counter, fan.style + ': ' + str(heat), 15)
                style.draw(surf)
                rect = ((self.x + 85, counter), (heat * 2, 15))
                py.draw.rect(surf, BLUE, rect)

            if self.stat == 'over':
                over = fan.wrestlers_pop.get(self.wrestler)
                style = Text(self.x, counter, fan.style + ': ' + str(over), 15)
                style.draw(surf)
                rect = ((self.x + 85, counter), (over * 2, 15))
                py.draw.rect(surf, BLUE, rect)

            if self.stat == 'bored':
                bored = fan.wrestler_bored.get(self.wrestler)
                style = Text(self.x, counter, fan.style + ': ' + str(bored), 15)
                style.draw(surf)
                rect = ((self.x + 85, counter), (bored * 10, 15))
                py.draw.rect(surf, BLUE, rect)  

               #draw little colored circles for warnings 

                color = fan.frequency_of_wrestler(self.wrestler, stats)

                if color == 'warning':
                    py.draw.circle(surf, DRKYELLOW, (self.x - 12, counter + 5), 7)
                if color == 'danger':
                    py.draw.circle(surf, RED, (self.x - 12, counter + 5), 7)
            counter += 20
    
class Wrestler_overview:
    def __init__(self, x, y, wrestler):
        self.x = x
        self.y = y
        self.wrestler = wrestler
        self.over = Header_Button(DARKGREY, LGTBLUE, self.x + 200, self.y+70, 30, 30, 'Over', str(self.wrestler.overness), 25, 25, self.wrestler.overness, WHITE, BLACK)
        self.heat = Header_Button(DARKGREY, LGTBLUE, self.x + 320, self.y + 140, 30, 30, 'Heat', str(self.wrestler.heat), 25, 25, self.wrestler.heat, WHITE, BLACK)


    def draw(self, surf):
        
        header = Button(DARKGREY, self.x + 200, self.y+20, 0, 0, self.wrestler.name, 45, False, WHITE)
        gimmick = Button(DARKGREY, self.x + 180, self.y+45, 0, 0, 'Gimmick:    ' + self.wrestler.gimmick.display, 25, False, WHITE)
        background_right = Button(DARKGREY, self.x, self.y, 400, 500)
        happy_title = Header_Button(DARKGREY, LGTBLUE, self.x + 25, self.y+70, 30, 30, 'Happy', str(self.wrestler.happy), 25, 25, self.wrestler.happy, WHITE, BLACK)
        pay_title = Header_Button(DARKGREY, LGTBLUE, self.x + 100, self.y+70, 30, 30, 'Pay', str(self.wrestler.pay), 25, 25, self.wrestler.pay, WHITE, BLACK)
        char_skill = Header_Button(DARKGREY, LGTBLUE, self.x + 320, self.y+70, 30, 30, 'Character Work', str(self.wrestler.chrctr_work), 25, 25, self.wrestler.chrctr_work, WHITE, BLACK)
        heel_face = Header_Button(DARKGREY, LGTBLUE, self.x + 30, self.y+140, 30, 30, 'Heel/Face', str(self.wrestler.heel_face), 25, 25, self.wrestler.heel_face, WHITE, BLACK)
        ring_skill = Header_Button(DARKGREY, LGTBLUE, self.x + 155, self.y+140, 30, 30, 'In Ring Skill', str(self.wrestler.skill), 25, 25, self.wrestler.skill, WHITE, BLACK)   
        personality = Button(DARKGREY, self.x + 200, self.y + 480, 0, 0, 'Personality: ' + self.wrestler.personality, 25, self.wrestler.personality, WHITE)
        energy = Header_Button(DARKGREY, LGTBLUE, self.x + 155, self.y+210, 30, 30, 'Energy', str(self.wrestler.energy), 25, 25, self.wrestler.energy, WHITE, BLACK)
        style = Button(DARKGREY, self.x + 200, self.y + 450, 0, 0, 'Style: ' + self.wrestler.style.display, 25, self.wrestler.style, WHITE)

                
        background_right.draw(surf, True)
        header.draw(surf)     
        gimmick.draw(surf)
        heel_face.draw(surf)
        char_skill.draw(surf)
        ring_skill.draw(surf)
        energy.draw(surf)
        self.over.draw(surf)
        pay_title.draw(surf)
        happy_title.draw(surf)
        personality.draw(surf)
        style.draw(surf)
        self.heat.draw(surf)


    def update(self):
        py.display.update(self.x - 5 , self.y - 5, 410, 510)
    
    def display_over_info(self, pos, fans):

        txt = []
        for fan in fans:
            wrestler = self.wrestler
            over = fan.wrestlers_pop.get(wrestler)
            txt.append(fan.style + ' overness: ' + str(over))

        tool_tip = Txt_Left_Button(GREEN, pos[0] + 5, pos[1] + 5, 200, 200, txt, 20)
        tool_tip.draw(surf, True)

    def display_heat_info(self, pos, fans):
        txt = []
        for fan in fans:
            wrestler = self.wrestler
            heat = fan.wrestler_heat.get(wrestler)
            txt.append(fan.style + ' heat: ' + str(heat))

        tool_tip = Txt_Left_Button(GREEN, pos[0] + 5, pos[1] + 5, 200, 200, txt, 20)
        tool_tip.draw(surf, True)

class Wrestler_overview_min():
    def __init__(self, x, y, wrestler):
        self.x = x
        self.y = y
        self.wrestler = wrestler
        self.over = Header_Button(DARKGREY, LGTBLUE, self.x + 200, self.y+70, 40, 30, 'Over', str(self.wrestler.overness), 25, 25, self.wrestler.overness, WHITE, BLACK)
        self.heat = Header_Button(DARKGREY, LGTBLUE, self.x + 320, self.y + 140, 40, 30, 'Heat', str(self.wrestler.heat), 25, 25, self.wrestler.heat, WHITE, BLACK)


    def draw(self, surf):

        header = Button(DARKGREY, self.x + 200, self.y+20, 0, 0, self.wrestler.name, 45, False, WHITE)
        gimmick = Button(DARKGREY, self.x + 180, self.y+45, 0, 0, 'Gimmick:    ' + self.wrestler.gimmick.display, 25, False, WHITE)
        background_right = Button(DARKGREY, self.x, self.y, 400, 300)
        happy_title = Header_Button(DARKGREY, LGTBLUE, self.x + 25, self.y+70, 30, 30, 'Happy', str(self.wrestler.happy), 25, 25, self.wrestler.happy, WHITE, BLACK)
        pay_title = Header_Button(DARKGREY, LGTBLUE, self.x + 100, self.y+70, 30, 30, 'Pay', str(self.wrestler.pay), 25, 25, self.wrestler.pay, WHITE, BLACK)
        char_skill = Header_Button(DARKGREY, LGTBLUE, self.x + 320, self.y+70, 30, 30, 'Mic Work', str(self.wrestler.chrctr_work), 25, 25, self.wrestler.chrctr_work, WHITE, BLACK)
        heel_face = Header_Button(DARKGREY, LGTBLUE, self.x + 30, self.y+135, 30, 30, 'Heel/Face', str(self.wrestler.heel_face), 25, 25, self.wrestler.heel_face, WHITE, BLACK)
        ring_skill = Header_Button(DARKGREY, LGTBLUE, self.x + 155, self.y+135, 30, 30, 'In Ring Skill', str(self.wrestler.skill), 25, 25, self.wrestler.skill, WHITE, BLACK)
       

        background_right.draw(surf, True)
        header.draw(surf)     
        gimmick.draw(surf)
        heel_face.draw(surf)
        char_skill.draw(surf)
        ring_skill.draw(surf)
        pay_title.draw(surf)
        happy_title.draw(surf)


        self.heat.draw(surf)
        self.over.draw(surf)
        

    def update(self):
        py.display.update(self.x - 5 , self.y - 5, 410, 310)

    def display_over_info(self, pos, fans):

        txt = []
        for fan in fans:
            wrestler = self.wrestler
            over = fan.wrestlers_pop.get(wrestler)
            txt.append(fan.style + ' overness: ' + str(over))

        tool_tip = Txt_Left_Button(GREEN, pos[0] + 5, pos[1] + 5, 200, 200, txt, 20)
        tool_tip.draw(surf, True)

    def display_heat_info(self, pos, fans):
        txt = []
        for fan in fans:
            wrestler = self.wrestler
            heat = fan.wrestler_heat.get(wrestler)
            txt.append(fan.style + ' heat: ' + str(heat))

        tool_tip = Txt_Left_Button(GREEN, pos[0] + 5, pos[1] + 5, 200, 200, txt, 20)
        tool_tip.draw(surf, True)


class MatchPanel():
    def __init__(self, match, x, y):
        self.match = match
        self.y = y
        self.x = x
    
    def draw(self):
        background = Button(GOLD, self.x, self.y, 400, 200)
        name = Button()



class WrestlerPastMatches():
    def __init__(self, wrestler, x, y):
        self.wrestler = wrestler
        self.x = x
        self.y = y

    def draw(self):
        background = Button(WHITE, self.x, self.y, 600, 500)
        header = Button(WHITE, self.x + 300, self.y + 30, 0, 0, self.wrestler.name + '\'s past shows', 30)
        close = Button(BLACK, self.x + 570, self.y + 10, 20, 20, 'X', 20)



        background.draw(surf, True)
        background.draw(surf)


class PostMatchSummary():
    def __init__(self, summary):
        self.preheat = preheat