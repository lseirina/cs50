# YOUR PRINCESS

    #### Video Demo:  <URL HERE>

    #### Description


    YOUR PRINCESS is my final project for CS50's Introduction to Programming with Python. This project is a quiz, where based on user's answers programm chooses a correspomding disney princess.

    #### Folder Contents

    * project.py: This is the file which contains my main function and the other functions necessary to implement the game.
    * princess.csv: This file stores the princesses' names and their charactiristics.
    * requirements.txt: All pip-installable libraries that I used for this project are listed here.
    * test_project.py: This file contains my test functions for project.py.

    #### Libraries Used

    * sys : collects a user's name from the list that contains command line arguments in command line interface.
    * re : validats input name that it contains alphabetical characters only.
    * fontstyle : adds colors, font weights to output of the programm.
    * random:  implements pseudo-random choice of colour for output.
    * emoji: for edding emoji of princess
    * pytest : for testing functions

    #### How to use

    After downloading the Project.py file and csv file into the same directory, you just need to run the code to iniciate it.

    In general, all menus use an input system that gets the option you type in and uses that to give you your result. If you type an invalid option, the programm will prompt you for input again. 

    To start you need to write your name in command line interface. 
    If the user does not specify exactly one command-line argument the programm will exit via sys.exit:
    "Too few command-line arguments" or "Too many command-line arguments" will be printed in interface if there is not anough or too many arguments respectively.
    Otherwise the programm will continue and, adress to you by name, ask if you want to play:
    "Hello {sys.argv[1]}, would you like to know what princess you are? "
    The code will ignore any leading whitespace in the user’s answer, and treat the user’s answer case-insensitively. But the answer must be: "Yes" or "No". If it does not, you'll be reprompted continuously until the required answer is entered. 

    if you answer "Yes" the programm will ask you questions. Each question requires correct ancwer selection out of five options proposed. The answers are characteristics of princesses, which are read, using DictReader, from csv file "Princess.csv" . There is a" while True loop" and If the answer is not from the list of options, the programm will ask user to try again and repeat the question. The programm compares the answer of the user to the data of csv file and based on it chooses the name of princess and adds it to the list.

    Then the programm counts the number of references of each princess's name and outputs the result:
    "Your princess is Avrora" (for example)

    The output is printed in colour with "princess" emoji.

    ####Functions
    My final project has main function and four additional functions.
    * main()
    The main function does not take any parameters, it's purpose is to take control of the program's flux, and call all other functions. The main function  has 6 questions and compares the users answer with the charactiristics in csv file. The function enters a "while True" loop, and it keeps running until the users chooses the right answer of the options offerd. Each question also has a "while True" loop, which will be reprompted continuously until a correct option of answer is entered.
    * check_argv():
     checks if command line arguments contains the required number of arguments. Also I use regular expression to check that the name of the user does not include punctuations or numbers. if name does not meet the requirements the program exit via sys.exit.
    * count_princess(l): 
    counts names of princesses in the list and depending on numbers of references princess's name outputs what princess chose user.
    * text_emoji(s):
    adds emoji of princess to the output, depending on which princess is chosen.
    * text_font(t):
    adds font to the output using random choice.
    
    
    
    
