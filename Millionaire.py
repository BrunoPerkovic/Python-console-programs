import random
from collections import Counter


class Question:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    def list_answers(self):
        print("a) " + self.answers[0])
        print("b) " + self.answers[1])
        print("c) " + self.answers[2])
        print("d) " + self.answers[3])

    def check_correct_answer(self, user_answer):
        answer_dict = {
            "a": self.answers[0],
            "b": self.answers[1],
            "c": self.answers[2],
            "d": self.answers[3]
        }

        user_is_correct = answer_dict[user_answer] == self.correct_answer
        return user_is_correct


class Level:
    def __init__(self, question_list, current_level, prize):
        self.question_list = question_list
        self.current_level = current_level
        self.prize = prize


class Jokers:

    def __init__(self):
        self.half_flag = False
        self.public_flag = False
        self.call_flag = False

    def half(self, answers, correct_answer):
        if self.half_flag:
            print("Joker HALF-HALF has already been used. ")
            return None
        answers.pop(answers.index(correct_answer))
        new_list = (random.choices(answers, weights=[1, 1, 1], k=1))
        new_list.append(correct_answer)
        self.half_flag = True
        print("Joker HALF-HALF has been used." + str(new_list))
        return new_list

    def public(self, answers):
        public_weights = []
        if self.public_flag:
            print("Joker ASK PUBLIC has already been used. ")
            return None
        if len(answers) == 2:
            public_weights = [1, 0.9]
        else:
            public_weights = [1.2, 1.1, 1, 0.9]
        new_list = Counter(random.choices(answers, weights=public_weights, k=100))
        for key, value in new_list.items():
            print(str(value) + " people voted for " + key)
        self.public_flag = True
        return new_list

    def call(self, answers):
        call_weights = []
        if self.call_flag:
            print("Joker CALL has already been used. ")
            return None
        if len(answers) == 2:
            call_weights = [1, 0.9]
        else:
            call_weights = [1, 1, 1, 1]
        new_list = random.choices(answers, weights=call_weights, k=1)
        self.call_flag = True
        print("Called person thinks the correct answer is " + str(new_list))
        return new_list


joker = Jokers()


def intro_message():
    print("""
Dobrodošli u kviz milijunaš.
Igra se sastoji od 15 pitanja. Prvo se pročita pitanje potom mogući odgovori.
Bodovni prag je sljedeći:
1 -100 kn (€13)
2 -200 kn (€26)
3 -300 kn (€39)
4 -500 kn (€65)
5 -1,000 kn (€130)*
6 -2,000 kn (€260)
7 -4,000 kn (€520)
8 -8,000 kn (€1,040)
9 -16,000 kn (€2,080)
10 -32,000 kn (€4,160)*
11 -64,000 kn (€8,320)
12 -125,000 kn (€16,250)
13 -250,000 kn (€32,500)
14 -500,000 kn (€65,000)
15 -1,000,000 kn (€130,000)*
Nakon svakog odgovora možete odustati i otići s osvojenom svotom novca.
Zvjezdicom označen novčani prag garantira osvojenu svotu prilikom pogrešnog odgovora.
Ako želite pozvati džoker pola-pola, stisnite h.
Ako želite pozvati džoker publiku, stisnite p.
Ako želite pozvati džoker zovi, stisnite z.
Ako želite odustati, stisnite q.
Sretno
""")


def play_again():
    repeat = input("Do you want to play: yes or no ?").lower().startswith("y")
    while repeat:
        main_game(levels)
        repeat = input("Do you want to play again: yes or no?").lower().startswith("y")
    print("Bye! ")


def quit_game():
    quit_me = input("Do you want to quit playing and collect guaranteed sum which is " + str(
        guaranteed_money) + " ?: Click q if you want to quit: ").lower()
    if quit_me == "q":
        print("Congratulations, your prize is " + str(guaranteed_money))


questions1 = [
    Question("Question1: What is the symbol of Hydrogen?", ["H", "B", "C", "E"], "H"),
    Question("Question1: What is the symbol of Oxygen? ", ["O", "P", "I", "U"], "O"),
    Question("Question1: What is the symbol of Nitrogen? ", ["M", "N", "LJ", "F"], "N")
]

questions2 = [
    Question("Question2: What sort of animal is Walt Disney's Dumbo?", ["Deer", "Rabbit", "Snake", "Elephant"],
             "Elephant"),
    Question("Question2: What kind of prince of Bel Air was Will Smith?", ["Ugly", "Stinky", "Fresh", "Tall"], "Fresh"),
    Question("Question2: Which car is famous for its red color and prancing horse logo?",
             ["Lotus", "Porsche", "Ferrari", "Lamborghini"], "Ferrari")
]

questions3 = [
    Question("Question3: What is name of the band whose front man was Freddie Mercury?",
             ["Prince", "Queen", "Count", "Majesty"], "Queen"),
    Question("Question3: What is the capital of USA?", ["Los Angeles", "Dallas", "New York", "Washington"],
             "Washington"),
    Question("Question3: What sport is played with puck?", ["Baseball", "Hockey", "Football", "Lacrosse"], "Hockey")
]

questions4 = [
    Question("Question4: What is the name of professional American basketball league?", ["NBA", "NFL", "NHL", "MBL"],
             "NBA"),
    Question("Question4: What is the name of Spanish professional football league?",
             ["Serie A", "Premier League", "La Liga", "Bundes Liga"], "La Liga"),
    Question("Question4: What colors are used in chess?", ["Black/Yellow", "White/Yellow", "Green/Gold", "Black/White"],
             "Black/White")
]

questions5 = [
    Question("Question5: What food does mice like to eat?", ["Ham", "Cheese", "Mold", "Mushroom"], "Cheese"),
    Question("Question5: What food rabbits like to eat?", ["Carrot", "Cabbage", "Zucchini", "Cucumber"], "Carrot"),
    Question("Question5: Which of 4 foods melt quickly while exposed to sun?", ["Ice Cream", "Pizza", "Egg", "Potato"],
             "Ice Cream")
]

questions6 = [
    Question("Question6: Most countries use Celsius as temperature measurement. What other measurement is used?",
             ["Zeitheit", "Mole", "Fahrenheit", "Bar"], "Fahrenheit"),
    Question("Question6: Who is leading knights of the round table?", ["Percival", "Arthur", "Ringo", "Bingo"],
             "Arthur"),
    Question("Question6: What country has flag similar to Pepsi logo?",
             ["North Korea", "Japan", "Thailand", "South Korea"], "South Korea")
]

questions7 = [
    Question("Question7: Which fighter was known as Gracie Killer?",
             ["Kazushi Sakuraba", "Takanori Gomi", "Hayato Sakurai", "Shinya Aoki"], "Kazushi Sakuraba"),
    Question("Question7: Who was first African American World Heavyweight champion in boxing?",
             ["Joe Louis", "Jack Johnson", "Jack Dempsey", "John Sullivan"], "Jack Johnson"),
    Question("Question7: Which boxer was known as Sweet pea?",
             ["Rocky Marciano", "Floyd Patterson", "Pernell Whitaker", "Roger Mayweather"], "Pernell Whitaker")
]

questions8 = [
    Question("Question8: Who was first person in space?",
             ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Sally Ride"], "Yuri Gagarin"),
    Question("Question8: In Albert Einsteins famous equation E=mc2, what does the c represent?",
             ["Gravity", "Time", "Matter", "Speed of light"], "Speed of light"),
    Question("Question8: Which planet is called Fire Planet?", ["Pluto", "Saturn", "Venus", "Mercury"], "Venus")
]

questions9 = [
    Question("Question9: Which famous rock band shares the name of the song Jailbreak with AC/DC?",
             ["Van Halen", "Led Zeppelin", "Thin Lizzy", "Aerosmith"], "Thin Lizzy"),
    Question("Question9: Which singer did Kanye West mention on stage when he interrupted Taylor Swift on VMAs?",
             ["Beyonce", "Rihanna", "Nicki Minaj", "Ciara"], "Beyonce"),
    Question("Question9: Name of Michael Jacksons mansion Neverland is inspired by which cartoon?",
             ["Hercules", "Aladin", "Shrek", "Peter Pan"], "Peter Pan")
]

questions10 = [
    Question("Question10: What car did OJ Simpson used as a getaway car when he was fleeing from police ?",
             ["Ford Ranger", "Ford Bronco", "Dodge Ram", "Ford F150"], "Ford Bronco"),
    Question("Question10: What does E means in Mercedes Benz E class?",
             ["Einspritzmotor", "Einstellung", "Einkumplug", "Elektroniks"], "Einspritzmotor"),
    Question("Question10: In what year was first automatic car released?", ["1948", "1958", "1978", "1984"], "1948")
]

questions11 = [
    Question("Question11: What Kawasaki bike did Tom Cruise as Maverick ride in movie Top Gun?",
             ["GPZ900R", "GPZ1100E", "GPZ600R", "GPZ250R"], "GPZ900R"),
    Question("Question11: What actor appeared both in Kill Bill and Once upon a time in hollywood?",
             ["Michael Madsen", "Michael Parks", "David Carradine", "Quentin Tarantino"], "Michael Madsen"),
    Question("Question11: Which of the four named movies didnt win the big five?",
             ["It Happend One Night", "One Flew Over the Cuckoos Nest", "Gone with the Wind",
              "The Silence of the Lambs"], "The Silence of the Lambs")
]

questions12 = [
    Question(
        "Question12: While J. R. R. Tolkien was an Oxford professor, he founded a literary club. What was the name?",
        ["Inklings", "Book worms", "Read Club", "Between the lies"], "Inklings"),
    Question("Question12: In Carlo Collodi’s Pinocchio, what are all the bad boys on Pleasure Island changed into?",
             ["Monkey", "Donkey", "Horse", "Dog"], "Donkey"),
    Question("Question12: In which state do Mark Twain’s characters Tom Sawyer and Huckleberry Finn live?",
             ["Missouri", "Mississippi", "Tennessee", "Alabama"], "Missouri")
]

questions13 = [
    Question("Question13: Which constitutional amendment allowed the right to vote regardless of race in USA?",
             ["10th", "12th", "15th", "18th"], "15th"),
    Question("Question13: Who was the first King in England?", ["Henry", "Arthur", "Michael", "Egbert"], "Egbert"),
    Question("Question13: Which ancient civilization invented the wheel?",
             ["Egypt", "Greece", "Mesopotamia", "Phoenicians"], "Mesopotamia")
]

questions14 = [
    Question("Question14: Construction of which of these famous landmarks was completed first?",
             ["Empire State Building", "Royal Albert Hall", "Eiffel Tower", "Big Ben Clock Tower"],
             "Big Ben Clock Tower"),
    Question("Question14: Which of these cetaceans is classified as a 'toothed whale'?",
             ["Gray Whale", "Minke Whale", "Sperm Whale", "Humpback Whale"], "Sperm Whale"),
    Question("Question14: Oberon is the satellite of which planet?", ["Mercury", "Neptune", "Uranus", "Mars"], "Uranus")
]

questions15 = [
    Question("Question15: In 1718, which pirate died in battle off the coast of what is now North Carolina?",
             ["Calico Jack", "Blackbeard", "Bartholomew Roberts", "Captain Kidd"], "Blackbeard"),
    Question("Question15: The Earth is approximately how many miles away from the Sun?", ["9.3m", "39m", "93m", "193m"],
             "93m"),
    Question("Question15: Which insect shorted out an early supercomputer and inspired the term computer bug?",
             ["Moth", "Roach", "Spider", "Japanese beetle"], "Moth")
]

levels = [
    Level(questions1, 1, 100),
    Level(questions2, 2, 200),
    Level(questions3, 3, 300),
    Level(questions4, 4, 500),
    Level(questions5, 5, 1000),
    Level(questions6, 6, 2000),
    Level(questions7, 7, 4000),
    Level(questions8, 8, 8000),
    Level(questions9, 9, 16000),
    Level(questions10, 10, 32000),
    Level(questions11, 11, 64000),
    Level(questions12, 12, 125000),
    Level(questions13, 13, 250000),
    Level(questions14, 14, 500000),
    Level(questions15, 15, 1000000)
]


global current_money
global half_answers
global half_used_level


def main_game(levels):
    global guaranteed_money
    guaranteed_money = 0
    half_answers = []
    half_used_level = 0
    intro_message()
    answer = ""

    for level in levels:
        if answer == "q":
            quit_game()
            break

        if answer == "lose":
            break
        else:
            pass

        current_question = level.question_list[random.randint(0, 2)]
        print(current_question.question)
        current_question.list_answers()

        while True:
            try:
                answer = input("Please choose one of following answers: ")

                if answer not in ("a", "b", "c", "d", "h", "p", "z", "q"):
                    print("Please enter one of allowed letters! ")

                if answer == "q":
                    break

                elif answer == "p":
                    if half_used_level == level.current_level:
                        joker.public(half_answers)
                    else:
                        joker.public(current_question.answers)

                elif answer == "h":
                    half_answers = joker.half(current_question.answers.copy(), current_question.correct_answer)
                    half_used_level = level.current_level

                elif answer == "z":
                    if half_used_level == level.current_level:
                        joker.call(half_answers)
                    else:
                        joker.call(current_question.answers)

                else:
                    if current_question.check_correct_answer(answer):
                        if level.current_level % 15 == 0:
                            guaranteed_money = level.prize
                            print("CONGRATULATIONS!!! YOU ARE NOW A MILLIONAIRE ! :) :) :) YOUR PRIZE IS {} kuna".format(guaranteed_money))
                            play_again()
                        elif level.current_level % 5 == 0:
                            guaranteed_money = level.prize
                            print("Your answer is correct. You are now guaranteed {} kuna".format(guaranteed_money))
                        else:
                            current_money = level.prize
                            print("Your answer is correct. Your current award is {} kuna".format(current_money))
                        break

                    else:
                        print("Unfortunately, the correct answer is {}. You win {} kuna".format(current_question.correct_answer, guaranteed_money))
                        answer = "lose"
                        break
            except KeyError:
                pass

play_again()
