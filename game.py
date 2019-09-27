#!/usr/bin/env python
# encoding: utf-8

import npyscreen
from items import *

GAME_NAME: str = "Allonsy"
game_time = 0


class Room:
    def __init__(self):
        self.contents = []
        self.name = "FIXME"

    def empty(self, dims):
        self.contents = [[None for _ in range(0, dims[1])] for _ in range(0, dims[0])]

    def render(self):
        result = ""
        for y, row in enumerate(self.contents):
            for x, thing in enumerate(row):
                result += " " if not thing else thing.render() + " "
            result += "\n"
        return result


class TimeDisplay:
    def __init__(self):
        global game_time
        self.time = game_time
        # Intent of the following is to provide x,y location for the time portion of the HUD
        # TODO: fill the rest out
        self.locx = 0
        self.locy = 0
        self.label = f"TIME: {game_time:4.0f}"


td = TimeDisplay()


class HP:
    def __init__(self):
        consequences = []


hp = HP()


def travel_time():
    # Adjust this as necessary for travel time between rooms?
    global game_time
    game_time = game_time + 0.25
    TimeDisplay.label = f"TIME: {game_time:4.0f}"


def minor_action_time():
    # Examine, take something from inventory, small interactions
    global game_time
    game_time = game_time + 1


def major_action_time():
    # Solve a puzzle?
    global game_time
    game_time = game_time + 5


def make_rooms():
    rooms = []

    # TODO randomly link rooms together
    reactor_room = Room()
    reactor_room.name = "Reactor Room"
    reactor_room.empty([5, 5])
    rooms.append(reactor_room)

    return rooms


active_room = Room()
active_room.empty([5, 7])
active_room.name = "Test Room"
inv = PCInventory()

def draw_game_ui():
    npyscreen.Form.FIX_MINIMUM_SIZE_WHEN_CREATED = True
    form = npyscreen.Form(
        name=f"Welcome to {GAME_NAME}", FIX_MINIMUM_SIZE_WHEN_CREATED=True
    )
    time = form.add(
        npyscreen.TitleText,
        name=f"Time: {td.label}\tLocation: {active_room.name}",
    )

    ml = form.add(npyscreen.MultiLineEdit, value=active_room.render(), max_height=10)

    form.edit()


class TestApp(npyscreen.NPSApp):
    def main(self):
        while True:
            draw_game_ui()
            return
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F = npyscreen.Form(name=f"Welcome to {GAME_NAME}")
        t = F.add(npyscreen.TitleText, name="Text:")
        fn = F.add(npyscreen.TitleFilename, name="Filename:")
        fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        dt = F.add(npyscreen.TitleDateCombo, name="Date:")
        s = F.add(npyscreen.TitleSlider, out_of=4, name="Slider")
        ml = F.add(
            npyscreen.MultiLineEdit,
            value="""try typing here!\nMultiline text, press ^R to reformat.\n""",
            max_height=5,
            rely=9,
        )
        ms = F.add(
            npyscreen.TitleSelectOne,
            max_height=4,
            value=[1],
            name="Pick One",
            values=["Option1", "Option2", "Option3"],
            scroll_exit=True,
        )
        ms2 = F.add(
            npyscreen.TitleMultiSelect,
            max_height=-2,
            value=[1],
            name="Pick Several",
            values=["Option1", "Option2", "Option3"],
            scroll_exit=True,
        )

        # This lets the user interact with the Form.
        F.edit()

        print(ms.get_selected_objects())


if __name__ == "__main__":
    App = TestApp()
    App.run()
