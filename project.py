import csv
import fontstyle
import re
import sys
import random
import emoji

def main():
    
    check_argv()
    while True:
        try:
            start = input(f"Hello {sys.argv[1]}, would you like to know what princess you are? ").strip().title()
            if start == "Yes":
                princesses = []
                with open("princess.csv", "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        princesses.append(row)

                output = []
                while True:
                    try:
                        print("kindness,", "courage,", "patience,", "intelligence,", "curiosity")
                        que1 = input("What is your best quality? ")
                        for row in princesses:
                            if que1 == row["quality"]:
                                output.append(row["name"])
                                
                        if que1 not in [
                            princesses[0]["quality"],
                            princesses[1]["quality"],
                            princesses[2]["quality"],
                            princesses[3]["quality"],
                            princesses[4]["quality"]
                            ]:
                            print("Choose from the list!")
                        else:
                            break
                    except ValueError:
                        pass
                while True:
                    try:
                        print("pink,", "green,", "blue,", "yellow,", "light pink")
                        que2 = input("What colour whould your princess dress be? ")       
                        for row in princesses:
                            if que2 == row["dress"]:
                                output.append(row["name"])
                        if que2 not in [
                            princesses[0]["dress"],
                            princesses[1]["dress"],
                            princesses[2]["dress"],
                            princesses[3]["dress"],
                            princesses[4]["dress"]
                            ]:
                            print("Choose from the list!")
                        else:
                            break
                    except ValueError:
                        pass
                while True:
                    try:
                        print("gold,", "cherry blossom,", "silver,", "stone,", "corals")
                        que3 = input("What would your crown be made from? ")       
                        for row in princesses:
                            if que3 == row["crown"]:
                                output.append(row["name"]) 
                        if que3 not in [
                            princesses[0]["crown"],
                            princesses[1]["crown"],
                            princesses[2]["crown"],
                            princesses[3]["crown"],
                            princesses[4]["crown"]
                            ]:
                            print("Choose from the list!")
                        else:
                            break
                    except ValueError:
                        pass
                while True:
                    try:
                        print("walking,", "fighting,", "cleaning up,", "reading,", "swiming")
                        que4 = input("What do you enjoy the most? ")       
                        for row in princesses:
                            if que4 == row["enjoy"]:
                                output.append(row["name"])
                        if que4 not in [
                            princesses[0]["enjoy"],
                            princesses[1]["enjoy"],
                            princesses[2]["enjoy"],
                            princesses[3]["enjoy"],
                            princesses[4]["enjoy"]
                            ]:
                            print("Choose from the list!")
                        else:
                            break
                    except ValueError:
                        pass
                while True:
                    try:
                        print("woods,", "mountains,", "castle,", "library,", "sea")
                        que5 = input("What kind of places do you like? ")       
                        for row in princesses:
                            if que5 == row["place"]:
                                output.append(row["name"])
                        if que5 not in [
                            princesses[0]["place"],
                            princesses[1]["place"],
                            princesses[2]["place"],
                            princesses[3]["place"],
                            princesses[4]["place"]
                            ]:
                            print("Choose from the list!")
                        else:
                            break
                    except ValueError:
                        pass
                while True:
                    try:
                        print("naiv,", "stubborn,", "weak,", "loner,", "careless")
                        que6 = input("What's your greatest weakness? ")       
                        for row in princesses:
                            if que6 == row["weakness"]:
                                output.append(row["name"])
                        if que6 not in [
                            princesses[0]["weakness"],
                            princesses[1]["weakness"],
                            princesses[2]["weakness"],
                            princesses[3]["weakness"],
                            princesses[4]["weakness"]
                            ]:
                            print("Choose from the list!")
                        else:
                            break
                    except ValueError:
                        pass
                choice = count_princess(output)
                tex_emoji = text_emoji(choice)
                tex_color = text_font(tex_emoji)
                print(tex_color)
            elif start == "No":
                print("OK, maybe next time:)") 
            if start not in ["Yes", "No"]:
                print("Yes or No")
            else:
                break         
        except: 
            pass
    
def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    matches = re.search(r"^[a-zA-Z]+$", sys.argv[1])
    if matches:
        return sys.argv[1]
    else:
        sys.exit("Invalid name")


def count_princess(l):
    princess_count1 = l.count("Avrora")
    princess_count2 = l.count("Mulan")
    princess_count3 = l.count("Cinderella")
    princess_count4 = l.count("Bell")
    princess_count5 = l.count("Ariel")


    list_of_princess = [princess_count1, princess_count2, princess_count3, princess_count4, princess_count5]
    max_num = max(list_of_princess)
    if max_num == princess_count1:
        tex = "Your princess is Avrora"
    elif max_num == princess_count2:
        tex = "Your princess is Mulan"
    elif max_num == princess_count3:
        tex = "Your princess is Cinderella"
    elif max_num == princess_count4:
        tex = "Your princess is Bell"
    elif max_num == princess_count5:
        tex = "Your princess is Ariel"
    
    return tex

def text_emoji(s):
    if "Mulan" in s:
        return emoji.emojize(f"{s} :princess:")
    elif "Avrora" in s:
        return emoji.emojize(f"{s} :princess_light_skin_tone:")
    elif "Bell" in s:
        return emoji.emojize(f"{s} :princess_medium-dark_skin_tone:")
    elif "Cinderella" in s:
        return emoji.emojize(f"{s} :princess_medium-light_skin_tone:")
    elif "Ariel" in s:
        return emoji.emojize(f"{s} :princess:")

def text_font(t):
    colors = [
    "bold/Italic/UNDERLINE/PURPLE_BG",
    "bold/Italic/UNDERLINE/GREEN_BG",
    "bold/Italic/UNDERLINE/BLUE_BG",
    "bold/Italic/UNDERLINE/YELLOW_BG",
    "bold/Italic/UNDERLINE/RED_BG"
    ]
    t_color = fontstyle.apply(t, random.choice(colors))
    
    return t_color

if __name__ == "__main__":
    main()

