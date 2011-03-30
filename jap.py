#!/usr/bin/env python

import sys
import argparse
import random

def load():
    # load verbs
    curr_category = ''
    f = open("verbs", "r", encoding="utf-8")
    for line in f:
        if line[:2] == '##':
            continue
        if line[0] == '#':
            curr_category = line[1:].strip()
            continue
        curr_line_split = line.split('\t')
        verbs.append(VerbQuestion(curr_category, curr_line_split[0].strip(), curr_line_split[1].strip(), curr_line_split[2].strip()))
    f.close()

    # load adjectives
    curr_category = ''
    f = open("adjectives", "r", encoding="utf-8")
    for line in f:
        if line[:2] == '##':
            continue
        if line[0] == '#':
            curr_category = line[1:].strip()
            continue
        curr_line_split = line.split('\t')
        adjectives.append(AdjectiveQuestion(curr_category, curr_line_split[0].strip(), curr_line_split[1].strip(), curr_line_split[2].strip()))
    f.close()

class VerbQuestion:
    """"""
    def __init__(self, category, romaji_vocab, hiragana_vocab, english_meaning):
        self.category = category
        self.romaji_vocab = romaji_vocab
        self.hiragana_vocab = hiragana_vocab
        self.english_meaning = english_meaning
        self.last_asked_in = False

    def ask_in_english(self):
        self.last_asked_in = 'english'
        print('Japanese for: ' + self.english_meaning)

    def ask_in_japanese(self):
        self.last_asked_in = 'japanese'
        if hiragana:
            print('English for: ' + self.hiragana_vocab)
        else:
            print('English for: ' + self.romaji_vocab)

    def resolve_answer(self, user_answer):
        ret_value = False
        if self.last_asked_in == 'english' and hiragana:
            answer = self.hiragana_vocab
        elif self.last_asked_in == 'english':
            answer = self.romaji_vocab
        else:
            answer = self.english_meaning

        if answer.split('|').count(user_answer) > 0:
            print('CORRECT')
            ret_value = True
        else:
            print('WRONG')
            ret_value = False

        print(' - correct answer is : ' + answer)

        return ret_value

class AdjectiveQuestion:
    """"""
    def __init__(self, category, romaji_vocab, hiragana_vocab, english_meaning):
        self.category = category
        self.romaji_vocab = romaji_vocab
        self.hiragana_vocab = hiragana_vocab
        self.english_meaning = english_meaning
        self.last_asked_in = False

    def ask_in_english(self):
        self.last_asked_in = 'english'
        print('Japanese for: ' + self.english_meaning)

    def ask_in_japanese(self):
        self.last_asked_in = 'japanese'
        if hiragana:
            print('English for: ' + self.hiragana_vocab)
        else:
            print('English for: ' + self.romaji_vocab)

    def resolve_answer(self, user_answer):
        ret_value = False
        if self.last_asked_in == 'english' and hiragana:
            answer = self.hiragana_vocab
        elif self.last_asked_in == 'english':
            answer = self.romaji_vocab
        else:
            answer = self.english_meaning

        if answer.split('|').count(user_answer) > 0:
            print('CORRECT')
            ret_value = True
        else:
            print('WRONG')
            ret_value = False

        print(' - correct answer is : ' + answer)

        return ret_value

def main():
    parser = argparse.ArgumentParser(description='Japanese flashcards')
    parser.add_argument('-q', '--question-mode', dest='question_mode', choices=['japanese', 'english', 'both'], default='both', help='What language you are asked to give the answers in. Default is \'both\'')
    parser.add_argument('-hm', '--hiragana-mode', dest='hiragana_mode', choices=['True', 'False'], default='True', help='If you cannot display hiragana characters in your terminal, set this to False. Default is \'True\'')
    parser.add_argument('-v', '--verb-mode', dest='verb_mode', choices=['True', 'False'], default='True', help='Questions regarding verbs are asked. Default is \'True\'')
    parser.add_argument('-a', '--adjective-mode', dest='adjective_mode', choices=['True', 'False'], default='True', help='Questions regarding adjectives are asked. Default is \'True\'')
    args = parser.parse_args()
#    args = parser.parse_args(['-q', 'english'])
#    args = parser.parse_args(['-q', 'english', '-hm', 'False'])
#    args = parser.parse_args(['-q', 'japanese', '-hm', 'False', '-a', 'False'])

    # interpret arguments
    hiragana = args.hiragana_mode == 'True'
    verb_mode = args.verb_mode == 'True'
    adjective_mode = args.adjective_mode == 'True'

    correct_count = 0
    b_continue = True
    original_chance_of_ask_wrong = .2
    chance_of_ask_wrong = original_chance_of_ask_wrong
    ask_wrong = []
    load()

    while b_continue:
        # determine question
        if len(ask_wrong) > 0 and chance_of_ask_wrong > random.random():
            chance_of_ask_wrong = original_chance_of_ask_wrong
            curr_question = ask_wrong[random.randint(0, len(ask_wrong) - 1)]
        elif verb_mode and adjective_mode:
            if random.random() < 0.5:
                curr_question = verbs[random.randint(0, len(verbs) - 1)]
            else:
                curr_question = adjectives[random.randint(0, len(adjectives) - 1)]
        elif verb_mode:
            curr_question = verbs[random.randint(0, len(verbs) - 1)]
        elif adjective_mode:
            curr_question = adjectives[random.randint(0, len(adjectives) - 1)]

        # ask question
        if args.question_mode == 'japanese' or (args.question_mode == 'both' and random.randint(0,1)):
            curr_question.ask_in_english()
        elif args.question_mode == 'english' or args.question_mode == 'both':
            curr_question.ask_in_japanese()

        # get user answer
        curr_user_ans = input()
    	
        # check for exit
        if(curr_user_ans == 'x' or curr_user_ans == 'X' or curr_user_ans == 'q' or curr_user_ans == 'Q'):
            b_continue = False
            continue

        if len(ask_wrong) > 0:
            chance_of_ask_wrong += 0.1
    	
        # check & print result
        if curr_question.resolve_answer(curr_user_ans):
            correct_count += 1
            print(' - correct count = ' + str(correct_count))
            if ask_wrong.count(curr_question) > 0:
                ask_wrong.remove(curr_question)
        else:
            ask_wrong.append(curr_question)
            ask_wrong.append(curr_question)

        print()
            
    print('\nThanks for playing. Bye!\n')

verbs = []
adjectives = []
hiragana = True
verb_mode = True
adjective_mode = True
main()
