import json
import random
import re
import readline

def load_words():
    with open("words_dictionary.json") as wf:
        all_words = json.load(wf)
        six_words = []
        for word in all_words.keys():
            if len(word) == 5:
                six_words.append(word)

    return six_words

def contains(char, words, pos=None, negate=False):
    cleaned_list = []
    if pos == None:
        for word in words:
            if negate:
                if not char in word:
                    cleaned_list.append(word)
            elif char in word:
                cleaned_list.append(word)
    else:
        for word in words:
            if negate:
                if word.find(char, pos, pos+1) == -1:
                    cleaned_list.append(word)
            elif word.find(char, pos, pos+1) != -1:
                    cleaned_list.append(word)
    return cleaned_list

def left_words(english_words):
    length = len(english_words)
    if length > 10:
        return "You have {} words left".format(length)
    else:
        return "This is your words list: {}".format(english_words)

def example(request):
    if request == "example":
        print("Try: {}".format(english_words[random.randrange(0, len(english_words))]))
    elif request == "all":
        if len(english_words) <= 20:
            print("Ok: {}".format(english_words))
        else:
            to_print = []
            for i in range(0, 20):
                to_print.append(english_words[i])
            print("Ok: {}".format(to_print))

def router(request):
    if request == "example" or request == "all":
        example(request)
    elif request.startswith("has"):
        pass
        if request.startswith("has not at"):
            pass
        elif request.startswith("has at"):
            pass
        elif request.startswith("has not"):
            pass
        else:
            pass
    else:
        print("example, has X")

if __name__ == '__main__':
    english_words = load_words()
    pattern = re.compile(r'has ([a-z]+)')
    pattern2 = re.compile(r'has at ([a-z]) (\d)')
    pattern3 = re.compile(r'has not at ([a-z]) (\d)')
    pattern4 = re.compile(r'has not ([a-z]+)')
    try:
        while True:
            request = input()
            if request == "example":
                print("Try: {}".format(english_words[random.randrange(0, len(english_words))]))
            elif request == "all":
                if len(english_words) <= 20:
                    print("Ok: {}".format(english_words))
                else:
                    to_print = []
                    for i in range(0, 20):
                        to_print.append(english_words[i])
                    print("Ok: {}".format(to_print))
            elif request.startswith("has"):
                if request.startswith("has not at"):
                    try:
                        valid_chars = re.match(pattern3, request)
                        pos = int(valid_chars[2]) - 1
                        print("Ok you don't have {} at {} in your word".format(valid_chars[1], pos+1))
                    except TypeError:
                        print("Format has not at x [1-5]")
                    if pos >= 5 or pos <= -1:
                        print("Format has not at x [1-5]")
                    else:
                        english_words = contains(valid_chars[1], english_words, pos, negate=True)
                        print(left_words(english_words))
                elif request.startswith("has at"):
                    try:
                        valid_chars = re.match(pattern2, request)
                        pos = int(valid_chars[2]) - 1
                        print("Ok you have {} at {} in your word".format(valid_chars[1], pos+1))
                    except TypeError:
                        print("Format has at x [1-5]")
                    if pos >= 5 or pos <= -1:
                        print("Format has at x [1-5]")
                    else:
                        english_words = contains(valid_chars[1], english_words, pos)
                        print(left_words(english_words))   
                elif request.startswith("has not"):
                    try:
                        valid_chars = re.match(pattern4, request)
                        print("Ok you don't have {} in your word".format(valid_chars[1]))
                    except TypeError:
                        print("You need to provide one or more characters!")
                    for char in valid_chars[1]:
                        english_words = contains(char, english_words, negate=True)
                        print(left_words(english_words))
                else:
                    try:
                        valid_chars = re.match(pattern, request)
                        print("Ok you have {} in your word".format(valid_chars[1]))
                    except TypeError:
                        print("You need to provide one or more characters!")
                    for char in valid_chars[1]:
                        english_words = contains(char, english_words)
                        print(left_words(english_words))
            else:
                print("example, has X")
    except KeyboardInterrupt as e:
        print("You had {} words left.\nBye!".format(len(english_words)))
    