import math

ethnicityPrompts = [
    "English", "Spanish", "German", "French", "Italian"
]

backGroundSettings = ["a taxi at an airport", "supermarket"]

backGroundImagePrompts = [
    "Generate a pixel-art image of"
]

occupations = [
    "taxi driver", "supermarket cashier", "supermarket manager"
]


def prompt(settingNumber: int, occupationNumber: int):
    randomIndex = math.floor(math.random() * ethnicityPrompts.length)
    return backGroundImagePrompts + backGroundSettings[settingNumber] + "with a" + ethnicityPrompts[randomIndex] + " " + occupations[occupationNumber] + "."
