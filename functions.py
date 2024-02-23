import pyautogui
import os
import time
from PIL import Image
from threading import *
import numpy as np

import bot

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def ask_for_direction():
    direction = input("Would you like your character to run up and down (ud) or left and right (lr)?: ").lower()
    if direction != "ud" and direction != "lr":
        print(direction)
        print("Please enter either \"ud\" or \"lr\" without quotations")
        return ""
    else:
        return direction


def take_screenshot():
    my_screenshot = pyautogui.screenshot()
    # print(ROOT_DIR + "\Scrreenshots\Screenshot.png")
    my_screenshot.save(ROOT_DIR + "\\Screenshots\\Screenshot.png")


def up_and_down():
    # pyautogui.keyDown("Z")
    pyautogui.keyDown("p")
    pyautogui.keyDown("w")
    time.sleep(0.15)
    pyautogui.keyUp("w")
    pyautogui.keyDown("s")
    time.sleep(0.15)
    pyautogui.keyUp("s")
    pyautogui.keyUp("p")
    # pyautogui.keyUp("Z")


def left_and_right():
    # pyautogui.keyDown("Z")
    pyautogui.keyDown("p")
    pyautogui.keyDown("a")
    time.sleep(0.15)
    pyautogui.keyUp("a")
    pyautogui.keyDown("d")
    time.sleep(0.15)
    pyautogui.keyUp("d")
    pyautogui.keyUp("p")
    # pyautogui.keyUp("Z")


def check_pixel(r, g, b, x, y):
    img = Image.open(ROOT_DIR + "\\Screenshots\\Screenshot.png").convert("RGB")
    pixel_info = img.getpixel((x, y))
    pixel_to_find = (r, g, b)
    if pixel_to_find == pixel_info:
        return True


def found_shiny():
    channelID = 929288419908153394
    user_id = 342830408800534529  # Replace with the actual User ID of Izokia
    msg = f'<@{user_id}> Check the stream you got a shiny!'  # Mention the user by their ID
    # TOKEN = 'MTE5MTY0NzM2NzMyMjE1MzAwMA.GBks-w.on91B2RCmJbIJm4QojYR9DQT6fKDcv7TGh2jLc'
    # bot_instance = bot.PokemonDiscordBot(TOKEN)
    # asyncio.run(bot_instance.send_notification(channelID, msg))
    print("FOUND SHINY")
    discord = Thread(target = bot.run_discord_bot())
    discord.start()
    exit(0)


def in_fight():
    print("Found condition indicating you are in a battle")
    # pyautogui.keyDown("q")
    time.sleep(1.55)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(2)
    take_screenshot()
    canRun = check_pixel(0, 0, 0, 922, 836)
    if not canRun:
        found_shiny()
        exit(0)
    time.sleep(1)




def run_from_battle():
    print("Found condition to run from battle")
    pyautogui.keyDown("q")
    pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    time.sleep(0.1)
    pyautogui.keyDown("d")
    pyautogui.keyUp("d")
    time.sleep(0.1)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.1)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    pyautogui.keyUp("q")


def reset_game():
    # print("Failed to run or detected a phone call, Resetting the game")
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("r")
    pyautogui.keyUp("r")
    pyautogui.keyUp("ctrl")
    pyautogui.keyDown("q")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    pyautogui.keyUp("q")
    # print("DONE RESETTING")
    # time.sleep(1)


# def delete_screenshot():
#     for f in os.listdir(ROOT_DIR + "\\Screenshots"):
#         os.remove(os.path.join(ROOT_DIR + "\\Screenshots", f))


def increase_enounter(today):
    with open('Data.txt', 'r+') as file:
        # read a list of all lines into data
        data = file.readlines()
        # lines = file.read()  # redudant, but I do overwriting in data (preference)
        # first = lines.split('\n', 1)[0]
        try:
            encounters = data[0].split(':')[1]
        except IndexError:
            encounters = 0
        try:
            resetCount = int(encounters) + 1
        except ValueError:
            resetCount = 2
        # print("ResetCount is : ", resetCount)
        # lines = lines.replace(first, "Total Resets: " + str(resetCount))
        data[0] = "Total Encounters: " + str(resetCount) + "\n"
        # print(lines)
    # with open('ResetData', 'w') as file:
    #     file.writelines(data)

    set_date_tracking(today, data)


def set_date_tracking(today, data):
    # with open('Data', 'r+') as file:
    #     data = file.readlines()

    lineDate = str(data[-1]).split(':', 1)[0]
    lineValue = str(data[-1]).split(':', 1)[1]
    # print("Last Date: ", lineDate, "compared to: ", today.strftime("%B %d, %Y"))
    if lineDate != today.strftime("%B %d, %Y"):
        with open("Data.txt", "a") as file:
            file.write("\n" + today.strftime("%B %d, %Y") + ": 1")
            print("newDate to file : ", today.strftime("%B %d, %Y"))
    else:
        try:
            val = int(lineValue) + 1
        except ValueError:
            val = 1
        data[-1] = today.strftime("%B %d, %Y") + ": " + str(val)
        with open('Data.txt', 'w') as file:
            print(data[0])
            file.writelines(data)


def StarterHuntKeyBinds():
    time.sleep(1.5)
    pyautogui.keyDown("q")
    time.sleep(.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(0.2)
    pyautogui.keyDown(".")
    pyautogui.keyUp(".")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.2)
    pyautogui.keyUp("q")
    take_screenshot()
    if not check_pixel(248, 216, 0, 585, 240):
        print("SHINY FOUND!")
        exit(0)
    elif check_pixel(248, 216, 0, 585, 240):
        reset_game()


def GCBinds():
    time.sleep(1.5)
    pyautogui.keyDown("q")
    time.sleep(.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(.2)
    pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    time.sleep(.2)
    pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    time.sleep(.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    time.sleep(.2)
    pyautogui.keyDown(".")
    pyautogui.keyUp(".")
    time.sleep(.2)
    pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    time.sleep(.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(.2)
    pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    time.sleep(.2)
    pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    time.sleep(.2)
    pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    time.sleep(.2)
    pyautogui.keyDown("s")
    pyautogui.keyUp("s")
    time.sleep(.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(.2)
    pyautogui.keyDown("o")
    pyautogui.keyUp("o")
    time.sleep(0.4)
    pyautogui.keyUp("q")
    take_screenshot()
    if not check_pixel(40, 88, 192, 520, 345):
        print("SHINY FOUND!")
        exit(0)
    elif check_pixel(40, 88, 192, 520, 345):
        reset_game()


# Have fun handling inputs :)ZZ
