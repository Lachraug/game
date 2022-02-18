import pygame as py
import random
from basics import *
from pprint import pprint
from screens import *
from GUI_widgets import *

from test_screen_class import *
from match_plot_beats import *

LEFT = 1
RIGHT = 3


surf = py.display.set_mode((1400, 800), 0, 32)

guy = Wrestler()
guytwo = Wrestler()

stats.add_roster(guy)
stats.add_roster(guytwo)

for x in range(10):
    bob = Wrestler()
    guy.add_friend(bob)
for x in range(10):
    bob = Wrestler()
    guy.add_enemy(bob)
for x in range(10):
    bob = Wrestler()
    guytwo.add_enemy(bob)
for x in range(10):
    bob = Wrestler()
    guytwo.add_friend(bob)

for x in range(20):
    stats.add_roster(Wrestler())


for fan in fans:
    for wrestler in stats.roster:
        num = random.randrange(100)
        fan.wrestlers_pop[wrestler] = num
        fan.wrestler_heat[wrestler] = 0
        fan.wrestler_bored[wrestler] = 0

for wrestler in stats.roster:
    wrestler.average_overness(fans)






py.init()

pos=py.mouse.get_pos()
click = []

first_guy_check = False
second_guy_check = False

contender_one = Button(LGTRED, 605, 155, 340, 50, 40)
contender_two = Button(LGTRED, 605, 155, 340, 50, 40)

splashImg = py.image.load(r'C:\Users\Peter\Desktop\Wrestlinggame\pics\splash.jpg')
dollar = py.image.load(r'C:\Users\Peter\Desktop\Wrestlinggame\pics\dollar_sign.png')
dollar = py.transform.scale(dollar, (150, 150))

imgx = 200
imgy = 200

match = Match()

place_in_list = 0

dragbutton = Button(RED, 500, 400, 120, 120, 'drag')
play = Button(BLACK, 620, 500, 100, 100, 'play!')





class Gamestate():
    def __init__(self):
        self.state = 'main'
        self.first_frame = True
        self.match = Match()
        self.show = Show()

        self.roster_displayed = False


        self.holder_of_data = False
        #list
        self.list_one = []
        self.list_two = []
        self.list_three = []
        self.list_four = []
        self.list_five = []
        self.list_six = []

        #checks
        self.check_one = False
        self.check_two = False
        self.check_three = False
        self.check_four = False
        self.check_five = False

        #more checks
        self.other_check_one = False
        self.other_check_two = False
        self.other_check_three = False
        self.other_check_four = False

        #lists
        self.class_object_one = False
        self.class_object_two = False
        self.class_object_three = False
        self.class_object_four = False

        #Make a show
        self.pick_promo = False
        self.pick_match = False

        #planning match
        self.winner_one = False
        self.winner_two = False
        self.big_spots = False

        #run ins
        self.friends_one = False
        self.enemies_one = False

        self.friends_two = False
        self.enemies_two = False

        self.benefit_first_guy = False
        self.benefit_second_guy = False
        self.chosen_wrestler = False

        self.for_display = []

        #for wrestler management
        self.main_list = False

        #injury
        self.injured = False
        self.injured_bodypart = False
        self.severity = False

        #DQ
        self.dqed_wrestler = False
        self.dq_method = False

        #beatdown
        self.beaten_down = False
        self.beater = False
        self.list_of_others = []

        #plot beats
        self.edit_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
            #to save your place when you edit something so it can then store it on the proper part in edit list
        self.indx_placeholder = 0

        #display current wrestlers
        self.display_wrestler_one = False
        self.display_wrestler_two = False

        self.current_display_friend = False
        self.current_display_enemy = False

        #end of show
        self.counter = 0
        self.unused_roster = stats.roster.copy()
        
        #review shows
        self.list_of_shows = False
        self.viewed_show = False

        #fans
        self.heat_fan_graph = False
        self.over_fan_graph = False
        self.bored_fan_graph = False
        
    def clear_checks(self):
        self.check_one = False
        self.check_two = False
        self.check_three = False
        self.check_four = False
        self.check_five = False

    def clear_lists(self):
        self.list_one = []
        self.list_two = []
        self.list_three = []
        self.list_four = []
        self.list_five = []

    def reset_all(self):
        self.clear_lists()
        self.clear_checks()
        self.first_frame = True

    def clear_all_shit(self):
        self.state = 'main'
        self.first_frame = True
        self.match = Match()
        self.show = Show()

        self.roster_displayed = False

        #list
        self.list_one = []
        self.list_two = []
        self.list_three = []
        self.list_four = []
        self.list_five = []
        self.list_six = []

        #checks
        self.check_one = False
        self.check_two = False
        self.check_three = False
        self.check_four = False
        self.check_five = False

        #more checks
        self.other_check_one = False
        self.other_check_two = False
        self.other_check_three = False
        self.other_check_four = False

        #lists
        self.class_object_one = False
        self.class_object_two = False
        self.class_object_three = False
        self.class_object_four = False

        #Make a show
        self.pick_promo = False
        self.pick_match = False

        #planning match
        self.winner_one = False
        self.winner_two = False
        self.big_spots = False

        #run ins
        self.friends_one = False
        self.enemies_one = False

        self.friends_two = False
        self.enemies_two = False

        self.benefit_first_guy = False
        self.benefit_second_guy = False
        self.chosen_wrestler = False

        self.for_display = []

        #for wrestler management
        self.main_list = False

        #injury
        self.injured = False
        self.injured_bodypart = False
        self.severity = False

        #DQ
        self.dqed_wrestler = False
        self.dq_method = False

        #beatdown
        self.beaten_down = False
        self.beater = False
        self.list_of_others = []

        #plot beats
        self.edit_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
            
        self.indx_placeholder = 0

        #display current wrestlers
        self.display_wrestler_one = False
        self.display_wrestler_two = False

        self.current_display_friend = False
        self.current_display_enemy = False

        #end of show
        self.counter = 0
        

        #past shows
        self.list_of_shows = False
        self.viewed_show = False

    def intro(self):
        intro = Intro()

    def main(self):
        #buttons
        wrestlerbttn = Button(RED, 50, 50, 200, 50, 'Wrestlers')
        agents = Button(BLUE, 50, 200, 250, 50, 'Free Agents')
        feuds = Button(GREEN, 50, 350, 330, 50, 'Feuds and Plots')
        eqptmnt = Button(SILVER, 50, 500, 250, 50, 'Equipment')
        underline = Button(BLACK, 600, 630, 500, 10)
        show = Button(GOLD, 600, 150, 300, 100, 'Make a Show!')
        screenspl = Button(WHITE, 600, 50, 1, 1, 'Manage your shit!')
        past_shows = Button(YELLOW, 1100, 200, 160, 50, 'Past Shows', 40)
        fans = Button(BLUE, 50, 600, 150, 50, 'Fans')
        
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if show.isOver(pos) == True:
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.first_frame = True
                    self.state = 'show'

            if wrestlerbttn.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.first_frame = True
                    self.state = 'wrestlers'
                    return
            
            if feuds.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.first_frame = True
                    self.state = 'feuds'
                    return
        
            if past_shows.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.first_frame = True
                    self.state = 'past shows'
                    return
                
            if fans.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.first_frame = True
                    self.state = 'fans'
                    return
                    
        surf.fill(WHITE)
        surf.blit(dollar, (500, 500))
        underline.draw(surf)
        past_shows.draw(surf, True)
        show.draw(surf, True)
        feuds.draw(surf, True)
        wrestlerbttn.draw(surf, True)
        agents.draw(surf, True)
        eqptmnt.draw(surf, True)
        screenspl.draw(surf)
        fans.draw(surf)

        #dragbutton.draw(surf)

        if self.first_frame == True:
            py.display.update()
            self.first_frame = False

    def fans(self):
        surf.fill(WHITE)
        counter = 50
        fan_click_list = []
        for fan in fans:
            new = Button(LGTBLUE, counter, 75, 200, 50, fan.style + ' Fans', 30, fan)
            counter += 250
            new.draw(surf, True)
            fan_click_list.append(fan)

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

        
        py.display.update()

    def make_show(self):
        global click

        global place_in_list
        #definitions
        #venue = Button()
        card = Button(WHITE, 775, 50, 2, 2, 'Card', 100)
        venue = Button(LGTRED, 50, 100, 70, 50, 'Venue', 30)
        addmatch = Button(GREEN, 600, 100, 175, 50, 'Add a Match', 40)
        addsegment = Button(LGTBLUE, 900, 100, 185, 50, 'Add Segment', 40)

        #add match window buttons
        window = Button(BLACK, 400, 200, 600, 300)
        pickmatch = Button(BLACK, 600, 320, 0, 0, 'Use existing feud?', 60, False, WHITE)
        feud = Button(RED, 500, 400, 200, 60, 'Existing Feud', 40)
        notfeud = Button(RED, 700, 400, 150, 60, 'New Match', 40)

        #add segment window buttons
        picksegment = Button(BLACK, 600, 320, 0, 0, 'Segment or Promo?', 60, False, WHITE)
        segment = Button(RED, 500, 400, 160, 60, 'Segment', 40)
        promo = Button(RED, 700, 400, 150, 60, 'Promo', 40)

        confirm = Button(GREEN, 1200, 740, 140, 50, 'Confirm', 30)
        back = Button(RED, 1200, 25, 80, 50, 'Back', 30)
        run_show = Button(GREEN, 1200, 600, 170, 40, 'Manage time line', 30)

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if addmatch.isOver(pos) == True:
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.pick_match = True
            if addsegment.isOver(pos) == True:
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.pick_promo = True

            #buttons for the window if 'add match' was selected
            if notfeud.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    if self.pick_match == True:
                        self.pick_promo = False
                        self.pick_match = False
                        self.state = 'add match'
                        place_in_list = 0
                        self.first_frame = True
            if feud.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    if self.pick_match == True:
                        self.pick_promo = False
                        self.pick_match = False
                        self.state = 'add match'
                        place_in_list = 0
                        self.first_frame = True

            #buttons for the window if 'add segment' was selected
            if segment.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    if self.pick_promo == True:
                        self.pick_promo = False
                        self.pick_match = False
                        self.state = 'add match'
                        place_in_list = 0
                        self.first_frame = True

            if notfeud.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    if self.pick_promo == True:
                        self.pick_promo = False
                        self.pick_match = False
                        self.state = 'add match'
                        place_in_list = 0
                        self.first_frame = True            
          
            if confirm.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    if len(self.show.matches) > 0:
                        self.first_frame = True
                        self.state = 'show results'
                        self.run_show()
                        return
        
        #draw
        surf.fill(WHITE)

        y = 190

        for match in self.show.matches:

            nxt = Txt_Left_Button(SILVER, 610, y, 230, 60, [match.winner.name, 'def', match.loser.name], 25)
            y += 70
            nxt.draw(surf, True)
            click.append(nxt)
            if y == 685:
                break  

        card.draw(surf, True)
        addmatch.draw(surf, True)
        venue.draw(surf, True)
        addsegment.draw(surf, True)

        #drawing if 'add match' was selected
        if self.pick_match == True:

            window.draw(surf, False)
            pickmatch.draw(surf, False)
            feud.draw(surf, True)
            notfeud.draw(surf, True)

            self.pick_promo = False
        #drawing if 'add segment' was selected
        if self.pick_promo == True:

            window.draw(surf, False)
            picksegment.draw(surf, True)
            segment.draw(surf, True)
            promo.draw(surf, True)
            self.pick_match = False

        back.draw(surf, True)
        run_show.draw(surf, True)
        confirm.draw(surf, True)

        py.display.update()

    def make_match(self):

        #all this shit I need because I don't know how to do it any other way
        #making list for scrolling

        global first_guy_check
        global second_guy_check

        self.roster_displayed.create_list()

        #buttons
        first_guy = Button(WHITE, 1095, 150, 200, 70)
        second_guy = Button(WHITE, 1095, 350, 200, 70)
        vs = Button(WHITE, 1180, 290, 0, 0, 'VS', 50)
        top_close = Button(WHITE, 1300, 150, 10, 10, 'X', 15)
        bottom_close = Button(WHITE, 1300, 350, 10, 10, 'X', 15)
        confirm = Button(GREEN, 1200, 740, 140, 50, 'Confirm', 30)
        back = Button(RED, 1200, 25, 80, 50, 'Back', 30)
        back_wrestler = Button(RED, 500, 75, 40, 40, '<-', 30)

        friends = Button(WHITE, 485, 610, 0, 0, 'Friends', 35)
        enemies = Button(WHITE, 790, 610, 0, 0, 'Enemies', 35)




        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        
            if back.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.state = 'show'
                    self.first_frame = True
                    return
            
            if confirm.isOver(pos):
                if event.type ==  py.MOUSEBUTTONDOWN and event.button == LEFT:
                    if first_guy_check != False and second_guy_check != False:
                        self.match.add_wrestlers(first_guy_check, second_guy_check)

                        #reset for next time
                        first_guy_check = False
                        second_guy_check = False
                        self.first_frame = True
                        self.state = 'plan match'
                        return


        #this is so the menus scroll
            if self.roster_displayed.up_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    if self.roster_displayed.place_in_list != 0:
                        self.roster_displayed.place_in_list -= 1
            if self.roster_displayed.down_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.roster_displayed.place_in_list != len(stats.roster):
                        self.roster_displayed.place_in_list += 1

            if self.current_display_friend != False:
                if self.current_display_friend.up_button.isOver(pos):
                    if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                        if self.current_display_friend.place_in_list != 0:
                            self.current_display_friend.place_in_list -= 1
                if self.current_display_friend.down_button.isOver(pos):
                    if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                        if self.current_display_friend.place_in_list != len(stats.roster):
                            self.current_display_friend.place_in_list += 1

            if self.current_display_enemy != False:
                if self.current_display_enemy.up_button.isOver(pos):
                    if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                        if self.current_display_enemy.place_in_list != 0:
                            self.current_display_enemy.place_in_list -= 1
                if self.current_display_enemy.down_button.isOver(pos):
                    if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                        if self.current_display_enemy.place_in_list != len(stats.roster):
                            self.current_display_enemy.place_in_list += 1

            #selecting a friend or enemy from the bottom lists
            if self.current_display_friend != False:
                for item in self.current_display_friend.click_list:
                    if item.isOver(pos):
                        if event.type == py.MOUSEBUTTONDOWN and event.button == RIGHT:
                            self.display_wrestler_one = Wrestler_overview(500, 70, item.metadata)
                            self.current_display_friend = Scroll_List_Custom(LGTRED, 400, 650, 190, 30, 3, item.metadata.friends)
                            self.current_display_enemy = Scroll_List_Custom(LGTRED, 700, 650, 190, 30, 3, item.metadata.enemies)
                            self.list_five.append(item.metadata)
            if self.current_display_enemy != False:
                for item in self.current_display_enemy.click_list:
                    if item.isOver(pos):
                        if event.type == py.MOUSEBUTTONDOWN and event.button == RIGHT:
                            self.display_wrestler_one = Wrestler_overview(500, 70, item.metadata)
                            self.current_display_friend = Scroll_List_Custom(LGTRED, 400, 650, 190, 30, 3, item.metadata.friends)
                            self.current_display_enemy = Scroll_List_Custom(LGTRED, 700, 650, 190, 30, 3, item.metadata.enemies)
                            self.list_five.append(item.metadata)

            #the back button for wrestler statistics
            if back_wrestler.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    if len(self.list_five) > 1:
                        self.list_five.pop()
                        self.display_wrestler_one = Wrestler_overview(500, 70, self.list_five[-1])
                        self.current_display_friend = Scroll_List_Custom(LGTRED, 400, 650, 190, 30, 3, self.list_five[-1].friends)
                        self.current_display_enemy = Scroll_List_Custom(LGTRED, 700, 650, 190, 30, 3, self.list_five[-1].enemies)
                            

        #close buttons for wrestlers if you want to cancel the one you selected
            if top_close.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    if first_guy_check != False:
                        first_guy_check = False
                        py.display.update(1095, 150, 210, 60)


            if bottom_close.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                    if second_guy_check != False:
                        second_guy_check = False
                        py.display.update(1095, 350, 210, 60)



        #selecting the wrestlers you want
            for item in self.roster_displayed.click_list:
                if item.isOver(pos):

                    if event.type == py.MOUSEBUTTONDOWN and event.button == LEFT:
                        if first_guy_check == False:
                            #GUI update
                            new = Button(LGTRED, 1100, 155, 190, 50, item.text[0], 25, item.metadata)
                            new.draw(surf, True)
                            py.display.update((1095, 150, 200, 100))
                            #store wrestler information
                            first_guy_check = item.metadata


                            break

                        elif second_guy_check == False:
                            #GUI update
                            anotherFuckingButton = Button(LGTRED, 1100, 355, 190, 50, item.text[0], 25, item)
                            anotherFuckingButton.draw(surf, True)
                            py.display.update((1095, 350, 200, 100))
                            #store wrestler information
                            second_guy_check = item.metadata
                            break
            
            #hovering toolbox info
            #the for loop is causing it to stutter i think, find out a way around this


            for button in self.roster_displayed.click_list:
                if button.isOver(pos):
                    if event.type == py.MOUSEBUTTONDOWN and event.button == RIGHT:
                        self.display_wrestler_one = Wrestler_overview(500, 70, button.metadata)
                        self.current_display_friend = Scroll_List_Custom(LGTRED, 400, 650, 190, 30, 3, button.metadata.friends)
                        self.current_display_enemy = Scroll_List_Custom(LGTRED, 700, 650, 190, 30, 3, button.metadata.enemies)
                        self.list_five.append(button.metadata)



        surf.fill(WHITE)

        first_guy.draw(surf, True)
        second_guy.draw(surf, True)
        vs.draw(surf, True)
        top_close.draw(surf, True)
        bottom_close.draw(surf, True)
        confirm.draw(surf, True)
        back.draw(surf, True)

        

        self.roster_displayed.draw(surf)
        if self.display_wrestler_one != False:
            self.display_wrestler_one.draw(surf)
            self.current_display_enemy.create_list()
            self.current_display_friend.create_list()


            back_wrestler.draw(surf, False)
            self.current_display_friend.draw(surf)
            self.current_display_enemy.draw(surf)
            if self.display_wrestler_one.over.bottom.isOver(pos):
                self.display_wrestler_one.display_over_info(pos, fans)
            if self.display_wrestler_one.heat.bottom.isOver(pos):
                self.display_wrestler_one.display_heat_info(pos, fans)
            friends.draw(surf, False)
            enemies.draw(surf, False)
            
            

        #setting up list of wrestlers

        py.display.update(50, 50, 1000, 800)




        #to update for the first frame only
        if self.first_frame == True:
            self.first_frame = False
            self.match = Match()
            py.display.update()
        

        
        #always updating list of names

    def plan_match(self):
        #things to bring in
        
        #buttons and shit
        planning = Button(WHITE, 750, 25, 0, 0, 'Match Planning')
        match_type = Button(SILVER, 120, 75, 160, 50, 'Match Type', 40)
        plot_beats = Button(SILVER, 120, 145, 160, 50, 'Plot Beats', 40)    
        length = Button(SILVER, 120, 215, 160, 50, 'Length', 40)    
        winner = Button(WHITE, 430, 600, 0, 0, 'Winner', 50)
        winner_choice_one = Button(LGTRED, 80, 650, 340, 50, self.match.wrestlers[0].name, 30, self.match.wrestlers[0])
        winner_choice_two = Button(LGTRED, 430, 650, 340, 50, self.match.wrestlers[1].name, 30, self.match.wrestlers[1])
        order_of_plot = Button(GREEN, 920, 85, 150, 40, 'Order', 30)
        confirm = Button(GREEN, 1200, 740, 170, 50, 'Confirm', 40)
        back = Button(RED, 1200, 25, 100, 50, 'Back', 40)

        display_length = Button(WHITE, 350, 240, 0, 0, 'Length:', 40)
        display_type = Button(WHITE, 350, 180, 0, 0, 'Type:', 40)
        wpns_to_be_used = Button(RED, 1100, 100, 150, 50, 'Weapons', 40)

        big_spots = Button(SILVER, 120, 285, 160, 50, 'Big Spots', 40) 


        self.roster_displayed.create_list()
        
        


        #match type UI on the right hand side
        
        right_side_outline = Button(DARKGREY, 700, 75, 600, 550)




        #game loop
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if winner_choice_one.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.match.winner = self.match.wrestlers[0]
                    self.match.loser = self.match.wrestlers[1]
            
            if winner_choice_two.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.match.winner = self.match.wrestlers[1]
                    self.match.loser = self.match.wrestlers[0]
            



            #buttons on left being clicked
            if match_type.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.clear_checks()
                    self.check_one = True

            if plot_beats.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.clear_lists()
                    self.first_frame = True
                    self.state= 'plot'
                    return

            if length.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.clear_checks()
                    self.check_three = True

            if big_spots.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.clear_checks()
                    self.check_four = True    


            #buttons on right being clicked
                #match type
            if self.check_one == True:
                for item in self.list_one:
                    if item.isOver(pos):
                        if event.type == py.MOUSEBUTTONDOWN:
                            self.match.type = item.metadata
                            button = Txt_Left_Button(WHITE, 390, 165, 0, 0, item.metadata, 40)
                            button.draw(surf, False)
                            py.display.update(390, 165, 500, 210)

            if self.check_four == True:
                for item in self.list_four:
                    if item.isOver(pos):
                        if event.type == py.MOUSEBUTTONDOWN:
                            self.match.spots = item
                            button = Txt_Left_Button(WHITE, 390, 165, 0, 0, item, 40)
                            button.draw(surf, False)
                            py.display.update(390, 165, 500, 210)

                #time
            if self.check_three == True:
                for item in self.list_three:
                    if item.isOver(pos):
                        if event.type == py.MOUSEBUTTONDOWN:
                            self.match.time = item.metadata
                            button = Txt_Left_Button(WHITE, 405, 230, 0, 0, item.metadata, 40)
                            button.draw(surf, False)
                            py.display.update(400, 225, 500, 280)


            if confirm.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:

                    self.first_frame == True
                    made_match = self.match
                    self.show.matches.append(made_match)

                    for wrestler in self.match.wrestlers:
                        if wrestler in self.unused_roster:
                            indx = self.unused_roster.index(wrestler)
                            self.unused_roster.pop(indx)


                    self.match = Match()
                    
                    self.state = 'show'
                    return

        




        #draw
        surf.fill(WHITE)
        right_side_outline.draw(surf, True)
        plot_beats.draw(surf, True)
        planning.draw(surf, False)
        match_type.draw(surf, True)
        winner.draw(surf, False)
        winner_choice_one.draw(surf, True)
        winner_choice_two.draw(surf, True)
        length.draw(surf, True)
        display_length.draw(surf, False)
        display_type.draw(surf, False)
        confirm.draw(surf, True)
        big_spots.draw(surf, True)

        #drawing the winner check mark
        if self.match.winner == self.match.wrestlers[0]:
            surf.blit(check_mark_resized, (78, 630))
            py.display.update(50, 600, 600, 800)
        
        if self.match.winner == self.match.wrestlers[1]:
            surf.blit(check_mark_resized, (428, 630))
            py.display.update(50, 600, 600, 800)     

        #making right side buttons appear
            #match type
        if self.check_one == True:
            self.list_one = []
            counter = 85
            for x in match_types:
                button = Button(LGTBLUE, 730, counter, 255, 50, x, 40, x)
                counter += 60
                button.draw(surf, True)
                self.list_one.append(button)
            py.display.update(700, 75, 600, 550)
            
        if self.check_four == True:
            self.list_two = []
            counter = 85
            for x in spots_selection:
                button = Button(LGTBLUE, 730, counter, 255, 50, x, 40, x)
                counter += 60
                button.draw(surf, True)
                self.list_one.append(button)
            py.display.update(700, 75, 600, 550)

            #length
        if self.check_three == True:
            self.list_three = []
            counter = 85
            for x in match_times:
                button = Button(LGTBLUE, 705, counter, 200, 50, x, 40, x)
                counter += 60 
                button.draw(surf, True)
                self.list_three.append(button)
            py.display.update(700, 75, 600, 550)


        if self.first_frame == True:
            self.check_one = False
            self.first_frame = False
            py.display.update()

    def run_in(self):
        if self.first_frame == True:
            self.first_frame = False

            #scroll lists



        
        #buttons
        run_in = Button(WHITE, 750, 25, 0, 0, 'Run In Planning')
        in_favor_of = Button(WHITE, 400, 75, 0, 0, 'Run In Will Benefit...', 40)
        winner_choice_one = Button(LGTRED, 80, 120, 340, 50, self.match.wrestlers[0].name, 30, self.match.wrestlers[0])
        winner_choice_two = Button(LGTRED, 430, 120, 340, 50, self.match.wrestlers[1].name, 30, self.match.wrestlers[1])
        friends = Button(WHITE, 200, 210, 0, 0, 'Friends of: ' , 30)
        enemies = Button(WHITE, 700, 210, 0, 0, 'Enemies of: ', 30)
        back = Button(RED, 1200, 50, 120, 50, 'Back')
        confirm = Button(GREEN, 1100, 700, 165, 50, 'Confirm')
        
        
        #scroll lists

        #game loop
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if winner_choice_one.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
       
                    self.benefit_first_guy = True
                    self.benefit_second_guy = False

            if winner_choice_two.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.benefit_second_guy = True
                    self.benefit_first_guy = False
            

            if back.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.first_frame = True

                    self.state = 'plot'
                    return
            
            if confirm.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    new = Run_In(self.chosen_wrestler[0], self.chosen_wrestler[1], self.chosen_wrestler[2], self.chosen_wrestler[3])

                    self.edit_list[self.indx_placeholder] = new

                    self.match.others.append(self.chosen_wrestler[0])
                    self.chosen_wrestler = False
                    self.first_frame = True
                    self.state = 'plot'
                    return


            #scroll up interactions for friends and enemies list
            if self.friends_one.up_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.friends_one.place_in_list > 0:
                        self.friends_one.place_in_list -= 1

            if self.friends_two.up_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.friends_two.place_in_list > 0:
                        self.friends_two.place_in_list -= 1

            if self.enemies_one.up_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.enemies_one.place_in_list > 0:
                        self.enemies_one.place_in_list -= 1

            if self.enemies_two.up_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.enemies_two.place_in_list > 0:
                        self.enemies_two.place_in_list -= 1

            #scroll down for lists
            if self.friends_one.down_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.friends_one.place_in_list += 1

            if self.friends_two.down_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.friends_two.place_in_list += 1

            if self.enemies_one.down_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.enemies_one.place_in_list += 1

            if self.enemies_two.down_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.enemies_two.place_in_list += 1
            
        


            #clicking list
            for button in self.friends_one.click_list:
                if button.isOver(pos):
                    if self.benefit_first_guy == True:
                        if event.type == py.MOUSEBUTTONDOWN:

                            self.chosen_wrestler = [button.metadata, self.match.wrestlers[0], self.match.wrestlers[1], 'friend']
                            self.for_display = [button.metadata.name, 'will assist', self.match.wrestlers[0].name]


            
            for button in self.enemies_one.click_list:
                if button.isOver(pos):
                    if self.benefit_first_guy == True:
                        if event.type == py.MOUSEBUTTONDOWN:

                            self.chosen_wrestler = [button.metadata, self.match.wrestlers[1], self.match.wrestlers[0], 'enemy']
                            self.for_display = [button.metadata.name, 'will attack', self.match.wrestlers[1].name]



            for button in self.friends_two.click_list:
                if button.isOver(pos):
                    if self.benefit_second_guy == True:
                        if event.type == py.MOUSEBUTTONDOWN:

                            self.chosen_wrestler = [button.metadata, self.match.wrestlers[1], self.match.wrestlers[0], 'friend']
                            self.for_display = [button.metadata.name, 'will assist', self.match.wrestlers[1].name]




            for button in self.enemies_two.click_list:
                if button.isOver(pos):
                    if self.benefit_second_guy == True:
                        if event.type == py.MOUSEBUTTONDOWN:

                            self.chosen_wrestler = [button.metadata, self.match.wrestlers[0], self.match.wrestlers[1], 'enemy']
                            self.for_display = [button.metadata.name, 'will attack', self.match.wrestlers[0].name]



        #draw
        surf.fill(WHITE)
        run_in.draw(surf, False)
        in_favor_of.draw(surf, False)
        winner_choice_one.draw(surf, True)
        winner_choice_two.draw(surf, True)
        friends.draw(surf, False)
        enemies.draw(surf, False)
        back.draw(surf, True)


        if self.benefit_first_guy == True:

            name_helped = Txt_Left_Button(WHITE, 255, 200, 0, 0, self.match.wrestlers[0].name, 30)
            name_hurt = Txt_Left_Button(WHITE, 765, 200, 0, 0, self.match.wrestlers[1].name, 30)

            name_hurt.draw(surf, False)
            name_helped.draw(surf, False)

            self.friends_one.create_list()
            self.friends_one.draw(surf)

            self.enemies_one.create_list()
            self.enemies_one.draw(surf)
            py.display.update()



        
        #if the second wrestler is chosen this is drawn
        if self.benefit_second_guy == True:
            name_helped = Txt_Left_Button(WHITE, 255, 200, 0, 0, self.match.wrestlers[1].name, 30)
            name_hurt = Txt_Left_Button(WHITE, 765, 200, 0, 0, self.match.wrestlers[0].name, 30)

            self.friends_two.create_list()
            self.friends_two.draw(surf)

            self.enemies_two.create_list()
            self.enemies_two.draw(surf)

            name_hurt.draw(surf, False)
            name_helped.draw(surf, False)
            

        if self.chosen_wrestler != False:
            info = Txt_Left_Button(WHITE, 1000, 400, 0, 0, self.for_display)
            info.draw(surf, False)


            confirm.draw(surf, True)

        if self.first_frame == True:
            self.first_frame = False

            py.display.update()


        py.display.update()

    def feuds(self):

        planning = Button(WHITE, 750, 25, 0, 0, 'Feud Management')
        running_feuds = Button(WHITE, 75, 75, 0, 0, 'Current Feuds')
        new_feud = Button(GREEN, 700, 75, 150, 40, 'New Feud', 40)

        surf.fill(WHITE)
        planning.draw(surf, False)
        running_feuds.draw(surf, False)
        new_feud.draw(surf, True)



        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()


        py.display.update()
        if self.first_frame == True:
            self.first_frame = False

    def wrstler_management(self):
        #buttons
        surf.fill(WHITE)
        friends = Button(WHITE, 375, 600, 150, 40, 'Friends', 25)
        enemies = Button(WHITE, 640, 600, 150, 50, 'Enemies', 25)
        feuds = Button(SILVER, 475, 345, 150, 50, 'Feuds', 35)
        past_matches = Button(SILVER, 475, 465, 180, 50, 'Past Matches', 35)
        possiblities = Button(SILVER, 475, 595, 180, 50, 'Possibilities', 35)
        
        header = Button(WHITE, 800, 30, 0, 0, 'Wrestler Management', 50)
        back = Button(RED, 1200, 25, 100, 50, 'Back', 40)
        past_matches = Button(GOLD, 80, 700, 200, 50, 'Past Matches', 30)




        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            
            if self.main_list.down_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.main_list.place_in_list += 1
                    self.main_list.create_list()
                    self.main_list.draw(surf)   
                    py.display.update(50, 100, 400, 800)             

            if self.main_list.up_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.main_list.place_in_list > 0:
                        self.main_list.place_in_list -= 1
                        py.display.update(50, 100, 400, 800) 

            for button in self.main_list.click_list:
                if button.isOver(pos):
                    if event.type == py.MOUSEBUTTONDOWN:
                        self.holder_of_data = button.metadata
                        self.display_wrestler_one = Wrestler_overview(950, 120, button.metadata)
                        self.heat_fan_graph = FanGraph(650, 150, 'heat', fans, button.metadata)
                        self.over_fan_graph = FanGraph(650, 280, 'over', fans, button.metadata)
                        self.bored_fan_graph = FanGraph(650, 410, 'bored', fans, button.metadata)
                        self.current_display_friend = Scroll_List_Custom(LGTRED, 340, 635, 200, 30, 4, button.metadata.friends, button.metadata.friends, 18)
                        self.current_display_enemy = Scroll_List_Custom(LGTRED, 600, 635, 200, 30, 4, button.metadata.enemies, button.metadata.enemies, 18)

            if self.display_wrestler_one != False:
                if past_matches.isOver(pos):
                    if event.type == py.MOUSEBUTTONDOWN:
                        print(self.holder_of_data.past_matches)


            if back.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.first_frame = True
                    self.state = 'main'
                    return



        
        header.draw(surf, False)
        friends.draw(surf)
        enemies.draw(surf)
        #fueds.draw(surf, True)
        #past_matches.draw(surf, True)
        #possiblities.draw(surf, True)
        #background_right.draw(surf, True)
        back.draw(surf, True)

        self.main_list.create_list()
        self.main_list.draw(surf)

        if self.display_wrestler_one != False:
            past_matches.draw(surf, True)
            self.display_wrestler_one.draw(surf)
            #self.display_wrestler_one.update()
            self.heat_fan_graph.draw(surf, stats)
            self.over_fan_graph.draw(surf, stats)
            self.bored_fan_graph.draw(surf, stats)

            #make list for friends and enemies
            self.current_display_friend.create_list()
            self.current_display_enemy.create_list()

            self.current_display_friend.draw(surf)
            self.current_display_enemy.draw(surf)
            
            py.display.update()

        if self.first_frame == True:
            py.display.update()
            self.first_frame = False
        
    def injury(self):
        #buttons
        header = Button(WHITE, 750, 25, 0, 0, 'Injury Planning')

        wrestler_choice_one = Button(LGTRED, 80, 120, 340, 50, self.match.wrestlers[0].name, 30, self.match.wrestlers[0])
        wrestler_choice_two = Button(LGTRED, 430, 120, 340, 50, self.match.wrestlers[1].name, 30, self.match.wrestlers[1])
        who_injured = Button(WHITE, 450, 75, 0, 0, 'Who Is Kayfabe Injured?', 50)
        seriousness = Button(WHITE, 340, 200, 0, 0, 'Seriousness', 40)

        #injury buttons
        leg = Button(DARKRED, 110, 250, 95, 40, 'Leg', 40, 'leg', WHITE)
        arm = Button(DARKRED, 110, 300, 95, 40, 'Arm', 40, 'arm', WHITE)
        chest = Button(DARKRED, 110, 350, 95, 40, 'Chest', 40, 'chest', WHITE)
        head = Button(DARKRED, 110, 400, 95, 40, 'Head', 40, 'head', WHITE)

        #severity
        minor = Button(LGTGREEN, 300, 270, 105, 40, 'Minor', 40, 'minor')
        bad = Button(YELLOW, 300, 330, 105, 40, 'Bad', 40, 'bad')
        serious = Button(LGTRED, 300, 390, 105, 40, 'Serious', 40, 'serious')

        confirm = Button(GREEN, 1200, 740, 170, 50, 'Confirm', 40)
        back = Button(RED, 1200, 25, 100, 50, 'Back', 40)

        

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if back.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.state = 'plot'
                    return
            
            if confirm.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.state = 'plot'
                    self.first_frame = True

                    injured = self.injured
                    body_part = self.injured_bodypart
                    severity = self.severity

                    self.injured = False
                    self.injured_bodypart = False
                    self.severity = False

                    new = Injury(injured, body_part, severity)
                    self.edit_list[self.indx_placeholder] = new
                    return


            if wrestler_choice_one.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    surf.blit(check_mark_resized, (75, 105))
                    py.display.update(70, 50, 500, 130)
                    self.injured = wrestler_choice_one.metadata
            
            if wrestler_choice_two.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    surf.blit(check_mark_resized, (430, 105))
                    py.display.update(70, 50, 500, 130)
                    self.injured = wrestler_choice_two.metadata


            #make bodypart buttons function
            if leg.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.injured_bodypart = 'leg'
            if arm.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.injured_bodypart = 'arm'
            if chest.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.injured_bodypart = 'chest'
            if head.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.injured_bodypart = 'head'

            #severity buttons
            if minor.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.severity = 'minor'
            if bad.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.severity = 'bad'            
            if serious.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.severity = 'serious'

            

        if self.injured != False and self.injured_bodypart == False:
            leg.draw(surf, True)
            arm.draw(surf, True)
            chest.draw(surf, True)
            head.draw(surf, True)
            seriousness.draw(surf, False)
            py.display.update(50, 150, 500, 420)

        #checkmark for injury selected
        if self.injured_bodypart != False:
            minor.draw(surf, True)
            bad.draw(surf, True)
            serious.draw(surf, True)
            py.display.update(260, 220, 450, 500)


            if self.injured_bodypart == 'head':
                surf.blit(check_mark_smaller, (70, 400))
                py.display.update(50, 150, 58, 420)

            if self.injured_bodypart == 'chest':
                surf.blit(check_mark_smaller, (70, 350))
                py.display.update(50, 150, 58, 420)
            if self.injured_bodypart == 'leg':
                surf.blit(check_mark_smaller, (70, 250))
                py.display.update(50, 150, 58, 420)
            if self.injured_bodypart == 'arm':
                surf.blit(check_mark_smaller, (70, 300))
                py.display.update(50, 150, 58, 420)

        if self.severity == 'minor':
            surf.blit(check_mark_smaller, (250, 270))
            py.display.update(210, 250, 270, 500)
        if self.severity == 'bad':
            surf.blit(check_mark_smaller, (250, 330))
            py.display.update(210, 250, 270, 500)
        if self.severity == 'serious':
            surf.blit(check_mark_smaller, (250, 390))
            py.display.update(210, 250, 270, 500)

        if self.severity != False:
            if self.injured != False:
                if self.injured_bodypart != False:
                    confirm.draw(surf, True)
                    py.display.update(1000, 500, 1150, 600)


                    



        surf.fill(WHITE)
        back.draw(surf, False)
        header.draw(surf, False)
        wrestler_choice_one.draw(surf, True)
        wrestler_choice_two.draw(surf, True)
        who_injured.draw(surf, True)

        if self.first_frame == True:
            py.display.update()
            self.first_frame = False

    def disqualification(self):
        #buttons
        header = Button(WHITE, 750, 25, 0, 0, 'DQ Planning')
        wrestler_choice_one = Button(LGTRED, 80, 120, 340, 50, self.match.wrestlers[0].name, 30, self.match.wrestlers[0])
        wrestler_choice_two = Button(LGTRED, 430, 120, 340, 50, self.match.wrestlers[1].name, 30, self.match.wrestlers[1])
        who_dq = Button(WHITE, 450, 75, 0, 0, 'Who Is Disqualified?', 50)

        self.main_list.create_list()

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            #choosing wrestler
            if wrestler_choice_one.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    surf.blit(check_mark_resized, (75, 105))
                    py.display.update(70, 50, 500, 130)
                    self.injured = wrestler_choice_one.metadata
            
            if wrestler_choice_two.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    surf.blit(check_mark_resized, (430, 105))
                    py.display.update(70, 50, 500, 130)
                    self.injured = wrestler_choice_two
        
            #list scroll buttons
            if self.main_list.up_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.friends_two.place_in_list > 0:
                        self.friends_two.place_in_list -= 1

            if self.main_list.down_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.enemies_one.place_in_list += 1

            for button in self.main_list.click_list:
                if button.isOver(pos):
                    if event.type == py.MOUSEBUTTONDOWN:
                        self.dq_method = button.metadata

        surf.fill(WHITE)
        self.main_list.draw(surf)
        py.display.update()
        header.draw(surf, False)
        wrestler_choice_one.draw(surf, True)
        wrestler_choice_two.draw(surf, True)
        who_dq.draw(surf, False)

        if self.first_frame == True:
            py.display.update()
            self.first_frame == False

    def plot_beats(self):
        surf.fill(WHITE)
        self.match.time = 'long'
        header = Button(WHITE, 750, 25, 0, 0, 'Plot Planning')
        #wrestler_choice_one = Button(LGTRED, 80, 120, 340, 50, self.match.wrestlers[0].name, 30, self.match.wrestlers[0])
        #wrestler_choice_two = Button(LGTRED, 430, 120, 340, 50, self.match.wrestlers[1].name, 30, self.match.wrestlers[1])
        empty_slot = Button (WHITE, 500, 100, 220, 60)
        match_start = Button(RED, 500, 170, 220, 50, 'Match Start', 40, 'start')
        edit = Button(DARKRED, 740, 110, 75, 40, 'Edit', 35, False, WHITE)
        confirm = Button(GREEN, 1200, 740, 170, 50, 'Confirm', 40)
        back = Button(RED, 1200, 25, 100, 50, 'Back', 40)
        

        #have to draw this first so dragging stuff looks good
        counter = 170
        empty_slot.draw(surf, True)
        match_start.draw(surf, True)


        time = []

        if self.match.time == 'short':
            time = [1, 2, 1]
        if self.match.time == 'medium':
            time = [1, 3, 2]
        if self.match.time == 'long':
            time = [1, 4, 2]
        
        self.list_two = []
        self.list_three = []   

        for x in range(time[1]):

            counter += 70
            new = Button(WHITE, 500, counter, 220, 50)
            new.draw(surf, True)
            self.list_two.append(new)

        counter += 70
        match_end = Button(RED, 500, counter, 220, 50, 'Match End', 40)
        match_end.draw(surf, True)

        for x in range(time[2]):
            counter += 70
            new = Button(WHITE, 500, counter, 220, 50)
            new.draw(surf, True)
            self.list_three.append(new)

        #for edit buttons to be drawn and store which one is which
        slots = time[0] + time[1] + time[2] + 2
        counter = 110

        self.list_six = []
        
        for num in range(slots):
            new = Button(DARKRED, 740, counter, 75, 40, 'Edit', 35, False, WHITE)
            self.list_six.append(new)
            counter += 70
            new.draw(surf, True)



        #game loop
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            for button in self.list_one:
                if button.isOver(pos):
                    if event.type == py.MOUSEBUTTONDOWN:
                        self.check_one = True
                        self.class_object_one = button
                        self.class_object_one.x = pos[0]
                        self.class_object_one.y = pos[1]

            if confirm.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.match.plot = self.edit_list
                    self.state = 'plan match'
                    self.first_frame = True
                    return

            if back.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.state = 'plan match'
                    self.first_frame = True
                    return
            


            #making sure things will release when put over an outline
            if empty_slot.isOver(pos):
                if event.type == py.MOUSEBUTTONUP:
                    if self.check_one == True:
                        
                        button = Button(LGTBLUE, empty_slot.x, empty_slot.y, empty_slot.width, empty_slot.height, self.class_object_one.metadata, 40, self.class_object_one.metadata)
                        self.list_four.append(button)
                        self.edit_list[0] = self.class_object_one.metadata

                        self.indx_placeholder = 0
                        self.check_one = False
                        self.class_object_one = False

            
            counter = 0
            for outline in self.list_two:
                counter += 1
                if outline.isOver(pos):
                    if event.type == py.MOUSEBUTTONUP:
                        if self.check_one == True:

                            button = Button(LGTBLUE, outline.x, outline.y, outline.width, outline.height, self.class_object_one.metadata, 40, self.class_object_one.metadata)
                            self.list_four.append(button)
                            self.edit_list[counter+1] = self.class_object_one.metadata

                            self.indx_placeholder = counter + 1
                            self.class_object_two = button
                            self.check_one = False
                            self.class_object_one = False



            for outline in self.list_three:
                counter += 1
                if outline.isOver(pos):
                    if event.type == py.MOUSEBUTTONUP:
                        if self.check_one == True:

                            button = Button(LGTBLUE, outline.x, outline.y, outline.width, outline.height, self.class_object_one.metadata, 40, self.class_object_one.metadata)
                            self.list_four.append(button)
                            self.edit_list[counter+2] = self.class_object_one.metadata

                            self.indx_placeholder = counter + 2
                            self.check_one = False
                            self.class_object_one = False
                

            if self.check_one == True:
                if event.type == py.MOUSEBUTTONUP:
                    self.class_object_one = False
                    self.check_one = False

            #clicking on an edit button         
            counter = 0
            for button in self.list_six:
                if button.isOver(pos):
                    if event.type == py.MOUSEBUTTONUP:
                        indx = self.list_six.index(button)
                        inpt = self.edit_list[indx]
                        if self.cycle_thro_for_event_editing(inpt) == True:
                            return

            

        if self.class_object_two != False:
            self.class_object_two.draw(surf, True)
        for button in self.list_four:
            button.draw(surf, True)
            #        for button in self.list_five:
            #            button.draw(surf, True)

        counter = 110

        for event in self.edit_list:
            if isinstance(event, str) == False:
                event.make_display()
                text = event.display
                new = Txt_Left_Button(WHITE, 840, counter, 0, 0, text, 22)
                new.draw(surf, False)
            counter += 60

        confirm.draw(surf, True)
        back.draw(surf, True)


        header.draw(surf, False)
        counter = 85

        #list of plot points
        for x in plot_beats_list:
            button = Button(LGTBLUE, 100, counter, 210, 50, x, 40, x)
            counter += 60 
            button.draw(surf, True)
            self.list_one.append(button)

        #list of plot stuff used
        counter = 85

        #for drawing the dragged stuff around
        if self.check_one == True:
            self.class_object_one.x = pos[0]
            self.class_object_one.y = pos[1]
            self.class_object_one.draw(surf, True)



        if self.first_frame == True:
            self.first_frame = False

        edit.draw(surf, True)
 
        py.display.update()

    def beat_down(self):
        #buttons
        header = Button(WHITE, 750, 25, 0, 0, 'Injury Planning')
        wrestler_choice_one = Button(LGTRED, 80, 120, 340, 50, self.match.wrestlers[0].name, 30, self.match.wrestlers[0])
        wrestler_choice_two = Button(LGTRED, 430, 120, 340, 50, self.match.wrestlers[1].name, 30, self.match.wrestlers[1])
        confirm = Button(GREEN, 1200, 740, 170, 50, 'Confirm', 40)
        back = Button(RED, 1200, 25, 100, 50, 'Back', 40)
        self.list_of_others.create_list()

        #game loop
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()        

            #picking who will get beaten down
            if wrestler_choice_one.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    surf.blit(check_mark_resized, (75, 105))
                    py.display.update(70, 50, 500, 130)
                    self.beater = wrestler_choice_one.metadata
                    self.beaten_down = wrestler_choice_two.metadata
            
            if wrestler_choice_two.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    surf.blit(check_mark_resized, (430, 105))
                    py.display.update(70, 50, 500, 130)
                    self.beater = wrestler_choice_two.metadata
                    self.beaten_down = wrestler_choice_one.metadata
            
            #changing screens, adding in the new plot
            if confirm.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.state = 'plot'
                    self.first_frame = True
                    new = BeatDown(self.beaten_down, self.beater)
                    self.edit_list[self.indx_placeholder] = new
                    return

        
        surf.fill(WHITE)

        #once the beaten down person is picked, pick who will beat them up
        if self.beaten_down != False:
            display = Button(WHITE, 400, 250, 0, 0, 'Other people who will beat down ' + self.beaten_down.name, 30)
            display.draw(surf, False)
            self.list_of_others.draw(surf)
            py.display.update(50, 200, 800, 800)


        header.draw(surf, False)
        wrestler_choice_one.draw(surf, True)
        wrestler_choice_two.draw(surf, True)
        back.draw(surf, True)
        confirm.draw(surf, True)

        if self.first_frame == True:
            self.first_frame = False
            py.display.update()

    def cycle_thro_for_event_editing(self, event):
        if event == 'Run In':
            self.state = 'Run In'
            self.first_frame = True
            return True
        if event == 'Injury':
            self.state = 'Injury'
            self.first_frame = True
            return True
        if event == 'Prematch Fight':
            self.state = 'Prematch Fight'
            self.first_frame = True
            return True
        if event == 'Beat Down':
            self.state = 'beat down'
            self.first_frame = True
            return True
        if event == 'Rally':
            self.state = 'Rally'
            self.first_frame = True
        if event == 'Disqualified':
            self.state = 'DC'
            self.first_frame = True
        if event == 'Grab Mic/Promo':
            self.state = 'promo'
            self.first_frame = True            

    def check_event_type(self, plot):
        test = []
        if plot == '-':
            text = []

        elif plot.type == 'run in': 
            if plot.connection == 'Friends of: ':
                relation = 'assist'
            if plot.connection == 'Enemies of: ':
                relation = 'attack'
            text = [self.first_party.name, 'will ' + relation, self.second_party]
    
        elif plot.type == 'injury':
            text = [plot.wrestler, 'injures ' + plot.bodypart, self.severity]
        
        return text

    def promos(self):
        header = Button(WHITE, 750, 25, 0, 0, 'Promos')
 




        self.roster_displayed.draw(surf)

    def show_results(self):
        header = Button(WHITE, 750, 25, 0, 0, 'Show Results')
        name_of_show = Button(WHITE, 750, 70, 0, 0, self.show.name)
        next_event = Button(GREEN, 1150, 120, 120, 30, 'Next', 30)
        previous_event = Button(RED, 950, 120, 120, 30, 'Previous', 30) 
        confirm = Button(GREEN, 1200, 740, 170, 50, 'All Done', 40)


        surf.fill(WHITE)

        counter = 80
        list_of_summaries = []
        for wrestler in self.show.matches[self.counter].wrestlers:
            display = Wrestler_overview_min(100, counter, wrestler)
            display.draw(surf)
            list_of_summaries.append(display)
            counter += 350        

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if next_event.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.counter < len(self.show.matches) - 1:
                        self.counter += 1

            if previous_event.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.counter > 0:
                        self.counter -= 1

            if confirm.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    stats.past_shows.append(self.show)

                    self.clear_checks()
                    self.clear_lists()
                    self.match = False
                    self.unused_roster_show_cleanup()



                    self.clear_all_shit()

                    
                    return
            


        self.show.matches[self.counter].draw_match()



        header.draw(surf, True)
        name_of_show.draw(surf, True)
        next_event.draw(surf, True)
        previous_event.draw(surf, True)
        confirm.draw(surf, True)

        for item in list_of_summaries:
            if item.heat.bottom.isOver(pos):
                item.display_heat_info(pos, fans) 
            if item.over.bottom.isOver(pos):
                item.display_over_info(pos, fans)
        py.display.update()
        if self.first_frame == True:
            self.first_frame = False

    def past_shows(self):
        
        header = Button(WHITE, 750, 25, 0, 0, 'Past Shows')
        next_event = Button(GREEN, 1150, 120, 120, 30, 'Next', 30)
        previous_event = Button(RED, 950, 120, 120, 30, 'Previous', 30) 


        surf.fill(WHITE)
        self.list_of_shows.create_list()

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if self.list_of_shows.down_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    self.list_of_shows.place_in_list += 1
                    self.list_of_shows.create_list()
                    self.list_of_shows.draw(surf)   
                    py.display.update(50, 100, 420, 900)             

            if self.list_of_shows.up_button.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.list_of_shows.place_in_list > 0:
                        self.list_of_shows.place_in_list -= 1
                        py.display.update(50, 100, 420, 900) 

            for button in self.list_of_shows.click_list:
                if button.isOver(pos):
                    if event.type == py.MOUSEBUTTONDOWN:
                        self.viewed_show = button.metadata
                        self.counter = 0
                        
            if next_event.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.counter < len(self.viewed_show.matches) - 1:
                        self.counter += 1

            if previous_event.isOver(pos):
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.counter > 0:
                        self.counter -= 1


        if self.viewed_show != False:

            
            name_of_show = Button(WHITE, 750, 75, 0, 0, self.viewed_show.name, 45)         

            name_of_show.draw(surf)


            next_event.draw(surf, True)
            previous_event.draw(surf, True)
            self.viewed_show.matches[self.counter].draw_match()

            counter = 100
            for wrestler in self.viewed_show.matches[self.counter].wrestlers:
                display = Wrestler_overview_min(400, counter, wrestler)
                display.draw(surf)
                
                counter += 350
            py.display.update(400, 55, 1100, 900)


        header.draw(surf, True)
        self.list_of_shows.draw(surf)
        


        if self.first_frame == True:
            py.display.update()
            self.first_frame = False
            
    def stateManager(self):
        if self.state == 'intro':
            self.intro()

        if self.state == 'main':
            
            self.main()

        if self.state == 'fans':
            self.fans()

        if self.state == 'wrestlers':
            if self.first_frame == True: 
                self.main_list = Scroll_List_Custom(LGTRED, 25, 50, 210, 30, 13, stats.roster, stats.roster, 20)

            self.wrstler_management()

        if self.state == 'feuds':
            self.feuds()

        if self.state == 'equiptment':
            self.equiptment()

        if self.state == 'show':
            if self.first_frame == True:
                self.clear_checks()
                self.pick_promo = False
                self.pick_match = False

            self.make_show()
            

        if self.state == 'add match':
            if self.first_frame == True:
                self.display_wrestler_one = False
                self.roster_displayed = Scroll_List_Detailed_Wrestlers(LGTRED, 100, 75, 200, 70, 8, stats.roster, stats.roster, 20)

            self.make_match()

        if self.state == 'plan match':
            self.plan_match()

        if self.state == 'Run In':
            if self.first_frame == True:
                for_display =[]
                self.friends_one = Scroll_List(LGTRED, 100, 250, 7, self.match.wrestlers[0].friends, self.match.wrestlers[0].friends)
                self.enemies_one = Scroll_List(LGTRED, 600 ,250,7, self.match.wrestlers[0].enemies, self.match.wrestlers[0].enemies)

                self.friends_two = Scroll_List(LGTRED, 100, 250, 7, self.match.wrestlers[1].friends, self.match.wrestlers[1].friends)
                self.enemies_two = Scroll_List(LGTRED, 600 ,250,7, self.match.wrestlers[1].enemies, self.match.wrestlers[1].enemies)


            self.run_in()
        if self.state == 'Injury':
            self.injury()

        if self.state == 'DQ':
            if self.first_frame == True:
                self.main_list = Scroll_List(LGTGREEN, 200, 200, 6, types_of_DQ, types_of_DQ)
            self.disqualification()

        if self.state == 'plot':
            if self.first_frame == True:
                
                self.first_frame == False
            self.plot_beats()

        if self.state == 'beat down':
            if self.first_frame == True:
                self.list_of_others = Scroll_List_Detailed_Wrestlers(LGTRED, 100, 75, 200, 70, 8, stats.roster, stats.roster, 20)
            self.beat_down()
        
        if self.state == 'promos':
            if self.first_frame == True:
                self.roster_displayed = Scroll_List_Detailed_Wrestlers(LGTRED, 100, 75, 200, 70, 8, stats.roster, stats.roster, 20)

        if self.state == 'show results':
            self.show_results()

        if self.state == 'past shows':
            if self.first_frame == True:
                self.list_of_shows = Scroll_List_Custom(YELLOW, 30, 60, 300, 50, 10, stats.past_shows)
            self.past_shows()
            
    def run_show(self):

        

        print('\n \n \n \n')
        cal_boredom = False
        #calculate events of the matches
        for event in self.show.matches:
            event.create_reviews()
            event.calculate_event(fans)

            for wrestler in event.wrestlers:
                wrestler.past_matches.append(event)

        


            #each match we calculate boredom

#            for fan in fans:
#                #if someone isn't over a lot but people REALLY want to see them lose, this will stop them from getting boring
#                if fan.calculate_heat_over_other(event) == False:

                    #fan.adjust_boredom(event.loser, stats)
#                    fan.adjust_boredom(event.winner, stats)
            
#                fan.bored_impact(event)
        


        for wrestler in event.wrestlers:
            self.show.wrestlers.append(wrestler)
            review = event.review.get(wrestler)


            wrestler.average_heat(fans)
            print(review.heat)

        
            
    def show_timeline(self):

        header = Button(WHITE, 750, 25, 0, 0, 'Show Time Line')

    def unused_roster_show_cleanup(self):
        
        for wrestler in self.unused_roster:
            if wrestler.injured == False:
                if wrestler.personality == 'Workaholic':
                    if wrestler.energy > 39:
                        wrestler.happy -= 10
                elif wrestler.personality != 'Workaholic':
                    if wrestler.energy > 64:
                        wrestler.happy -= 10

            if wrestler.energy > 94:
                wrestler.energy = 100
            if wrestler.energy < 95:
                wrestler.energy += 5
        new_list = stats.roster.copy()

        self.unused_roster = new_list

    
    



def draw_window():
    frame = Button(BLACK, 400, 200, 600, 400)
    x_out = Button(WHITE, 1000, 200, 30, 30, 'X')
    frame.draw(surf, True)
    x_out.draw(surf, True)
    py.display.update(400, 200, 600, 400)

game_state = Gamestate()
surf = py.display.set_mode((1400, 800), 0, 32)


clock = py.time.Clock()

#Running game
while True:
    pos=py.mouse.get_pos()
    game_state.stateManager()

    clock.tick(30)


