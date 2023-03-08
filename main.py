# Generate a new day of the Pathfinder Adeventure Path Skull & Shackles using the 2e conversion values found here:
# https://drive.google.com/drive/folders/1ghVbvZcKh54Gb8n4zXuibMC1OGed7WPg?usp=sharing
import random

if __name__ == '__main__':
    riggerTasks = ["*RIGGING REPAIR* - (DC 13 Athletics, DC 13 Sailing Lore/Acrobatics):\nThe ship’s rigging "
                   "frequently gets damaged and must be repaired. Climb and repair it\n",

                   "*LINE WORK* - (DC 13 Sailing Lore/Acrobatics, DC 17 Fort Save vs Fatigue):\n Hard work hoisting "
                   "and lowering sails.\n",

                   "*UPPER RIGGING WORK* - (DC 13 Athletics, DC 13 Sailing Lore/Acrobatics):\nWork in the upper "
                   "rigging.\n",

                   "*ROPE WORK* - (DC 13 Sailing Lore/Acrobatics):\nHandling the ship’s ropes, including coiling them, "
                   "stowing them, and securing them to cleats and single and double bollards.\n",

                   "*LOOKOUT* - (DC 13 Athletics, DC 13 Perception):\nA climb to the crow's nest 60 feet up.\n",

                   "*MAINSAIL DUTIES* - (DC 13 Sailing Lore/Athletics, DC 17 Fort Save vs Fatigue):\nTough work raising"
                   " and lowering the mainsail.\n"]

    cookTasks = ["*COOKING* - (DC 13 Cooking Lore/Intelligence (IF FISHGUTS IS DRUNK)):\nAssist Fishguts in cooking "
                 "for the day. If he is sober, no check is required.\n",

                 "*COOKING* - (DC 13 Cooking Lore/Intelligence (IF FISHGUTS IS DRUNK)):\nAssist Fishguts in cooking "
                 "for the day. If he is sober, no check is required.\n",

                 "*FISHING* - (DC 13 Fishing Lore/Survival, FAILURE = BILGES NEXT DAY):\nCatch dinner for the night "
                 "using the ship's nets.\n",

                 "*TURTLE HUNTING* - (DC 13 Fishing Lore/Survival, FAILURE = BILGES NEXT DAY):\nHunting leatherback "
                 "sea turtles with harpoons, hooks, and nets.\n",

                 "*BULL SESSION* - (N/A):\nDrink with Ambrose 'Fishguts' Kroop and listen to his stories. You must "
                 "drink and additional rum ration, but may take an additional ship action during the day.\n",

                 "*SPECIAL OCCASION* - (DC 13 Cooking Lore/Survival, DC 17 Cooking Lore/Intelligence IF DRUNK):\nThe "
                 "Captain is celebrating some special event today and wants a pig butchered and cooked for dinner. "
                 "Slaughter the animal and help Fishguts clean and prepare it.\n"]

    swabTasks = ["*MAN THE BILGES* - (DC 17 Athletics, DC 17 Fort Save vs Fatigue):\nVile and sweaty work in the "
                 "bilges (A11).\n",

                 "*RAT CATCHER* - (DC 13 Stealth/Survival):\nCatch rats and other vermin belowdeck.\n",

                 "*SWAB THE DECKS* - (DC 13 Athletics/DC 13 Fort vs Fatigue):\nMop and scrub the decks with mops "
                 "and big sandstone blocks called holystones. Either choose the Athletics check or Fort save.\n",

                 "*HAULING ROPE AND KNOT WORK* - (DC 13 Sailing Lore/Athletics, DC 13 Fort Save vs Fatigue):\nTying "
                 "and untying knots in the ship's ropes and moving coils around.\n",

                 "*RUNNER* - (DC 13 Acrobatics, DC 13 Fort Save vs Fatigue):\nPassing messages to the crew and officers"
                 " of the Wormwood everywhere except for the officer's cabins.\n",

                 "*REPAIRS* - (DC 13 Sailing Lore/Crafting):\nThings are constantly breaking. Repairing sails, rope, "
                 "wood, etc.\n"]

    while 1:
        pause = input("Press Enter to generate a new day!\n")

        print("\n--------------------------NEW DAY------------------------------\n")

        fishgutsDrunk = True if random.randint(0, 1) == 0 else False

        spiderAttack = True if random.randint(0, 3) == 0 else False

        riggerTask = riggerTasks[random.randint(0, 5)]

        cookTask = cookTasks[random.randint(0, 5)]

        swabTask1 = swabTasks[random.randint(0, 5)]

        swabTask2 = swabTasks[random.randint(0, 5)]

        swabTask3 = swabTasks[random.randint(0, 5)]

        print(f'Good morning Krusty Krew! Here are the results for the day!\n\n'
              f'Is Fishguts capable of helping out today? {fishgutsDrunk}\n\n'
              f'Will a spider bite somebody working in the bilge today? {spiderAttack}\n\n'
              f'+++Cook Daily Task+++\n{cookTask}\n'
              f'+++Rigger Daily Task+++\n{riggerTask}\n'
              f'+++First Swab Task+++\n{swabTask1}\n'
              f'+++Second Swab Task+++\n{swabTask2}\n'
              f'+++Third Swab Task+++\n{swabTask3}')

        print("---------------------------------------------------------------\n")
