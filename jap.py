#!/usr/bin/env python

import sys
import argparse
import random

def load():

    f = open("verbs", "r", encoding="utf-8")
    for line in f:
        currLineSplit = line.split('\t')
        verbs.append(VerbQuestion(currLineSplit[0].strip(), currLineSplit[1].strip(), currLineSplit[2].strip()))
    f.close()

class Question:
    """Super class for all questions"""
    def __init__(self):
        pass

    def ask():
        self.asked += 1

    def resolve_answer(answer):
        pass

class VocabQuestion(Question):
    """A simple vocabulary object"""
    def __init__(self, romaji_vocab, hirigana_vocab, english_meaning):
        self.romaji_vocab = romaji_vocab
        self.hirigana_vocab = hirigana_vocab
        self.english_meaning = english_meaning

class VerbQuestion(VocabQuestion):
    """"""
    def __init__(self, romaji_vocab, hirigana_vocab, english_meaning):
        super(VerbQuestion, self).__init__(romaji_vocab, hirigana_vocab, english_meaning)

class AdjectiveQuestion(VocabQuestion):
    """"""
    def __init__(self, romaji_vocab, hirigana_vocab, english_meaning):
        super(VerbQuestion, self).__init__(romaji_vocab, hirigana_vocab, english_meaning)
        

def main():
    parser = argparse.ArgumentParser(description='Japanese flashcards')
    parser.add_argument('-q', '--question-mode', dest='questionMode', choices=['japanese', 'english', 'both'], default='both', help='')
    parser.add_argument('-t', '--text-mode', dest='textMode', choices=['katakana', 'romaji'], default='katakana', help='')
    args = parser.parse_args()
#    args = parser.parse_args(['-q', 'english'])
#    args = parser.parse_args(['-q', 'english', '-t', 'romaji'])
#    args = parser.parse_args(['-q', 'japanese'])

    correctCount = 0
    bContinue = True
    chanceOfAskWrong = .33
    askWrong = []
    load()

    while bContinue:
        # determine question/answer & print question
        currCorrectAns = ''
        #ask wrong
        if len(askWrong) > 0 and chanceOfAskWrong > random.random():
            if args.questionMode == 'japanese' or (args.questionMode == 'both' and random.randint(0,1)):
                currVerbObj = askWrong[random.randint(0, len(askWrong) - 1)]
                print('Japanese for: ' + currVerbObj.english_meaning)
                currCorrectAns = currVerbObj.hirigana_vocab
            elif args.questionMode == 'english' or args.questionMode == 'both':
                currVerbObj = askWrong[random.randint(0, len(askWrong) - 1)]
                if args.textMode == 'katakana':
                    print('English for: ' + currVerbObj.hirigana_vocab)
                else:
                    print('English for: ' + currVerbObj.romaji_vocab)
                currCorrectAns = currVerbObj.english_meaning
        #ask new
        else:
            if args.questionMode == 'japanese' or (args.questionMode == 'both' and random.randint(0,1)):
                currVerbObj = verbs[random.randint(0, len(verbs) - 1)]
                print('Japanese for: ' + currVerbObj.english_meaning)
                currCorrectAns = currVerbObj.hirigana_vocab
            elif args.questionMode == 'english' or args.questionMode == 'both':
                currVerbObj = verbs[random.randint(0, len(verbs) - 1)]
                if args.textMode == 'katakana':
                    print('English for: ' + currVerbObj.hirigana_vocab)
                else:
                    print('English for: ' + currVerbObj.romaji_vocab)
                currCorrectAns = currVerbObj.english_meaning
    
        # get user answer
        currUserAns = input()
    	
        # check for exit
        if(currUserAns == 'x' or currUserAns == 'X' or currUserAns == 'q' or currUserAns == 'Q'):
            bContinue = False
            continue
    	
        # check & print result
        if(currCorrectAns.split('|').count(currUserAns) > 0):
            correctCount+=1
            print('CORRECT - Correct Count = ' + str(correctCount) + '\n\n')
            if askWrong.count(currVerbObj) > 0:
                askWrong.remove(currVerbObj)
        else:
            print('WRONG - Correct answer is : ' + currCorrectAns + '\n\n')
            askWrong.append(currVerbObj)
            
    print('Thanks for playing. Bye!')


verbs = []
main()
