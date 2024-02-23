import functions
import time
from datetime import date

sceneTransition = False
today = date.today()
TOKEN = 'MTE5MTY0NzM2NzMyMjE1MzAwMA.GBks-w.on91B2RCmJbIJm4QojYR9DQT6fKDcv7TGh2jLc'

def AskType():
    ans = input("What would you like to do?\n1)Shiny Starter Hunt\n2)Shiny Wild Grass Hunt\n3)Static Pokemon Shiny Hunt\n4)Game Corner Shiny\nYour Input: ")
    if ans.isdigit() and 0 < int(ans) <= 4:
        return int(ans)
    else:
        return -1

def GameCornerHunt():
    while (True):
        functions.GCBinds()
        functions.increase_enounter(today)


def StarterHunt():
    while(True):
        functions.StarterHuntKeyBinds()
        functions.increase_enounter(today)

def WildHunt():
    direction = functions.ask_for_direction()
    while direction == "":
        direction = functions.ask_for_direction()

    while True:
        functions.take_screenshot()
        # if functions.check_pixel(0, 0, 0, 224, 1022):
        #     sceneTransition = True
        #     print("SCENE TRANSITION STARTED")

        if direction == "ud":
            functions.up_and_down()
        elif direction == "lr":
            functions.left_and_right()
        inbattle_check = functions.check_pixel(248, 248, 248, 980, 465)
        if inbattle_check:
            functions.in_fight()

        while inbattle_check:
            functions.take_screenshot()
            run_from_battle = functions.check_pixel(0, 0, 0, 935, 835)
            # phone_call_check = functions.check_pixel(224, 8, 8, 1495, 943)
            if run_from_battle:
                functions.run_from_battle()
                # do operation for encounterCount
                functions.increase_enounter(today)
                inbattle_check = False
                time.sleep(1)
                functions.take_screenshot()
                run_check = functions.check_pixel(0, 184, 0, 700, 180)
                if run_check:
                    functions.reset_game()
                    # do operation for Reset Count
            # elif phone_call_check:
            # inbattle_check = False
            # functions.reset_game()


def main_process():
    # Create a thread to run the Discord bot
    huntType = AskType()
    while not huntType > 0:
        huntType = AskType()

    if huntType == 1:
        StarterHunt()
    elif huntType == 2:
        WildHunt()
    elif huntType == 3:
        print("Still a work in progress")
        exit(0)
    elif huntType == 4:
        GameCornerHunt()


if __name__ == '__main__':
    main_process()