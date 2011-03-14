#!/usr/bin/env python

import sys
import argparse
import random

def load():
    # One day these will be populated from an external file. Probably XML.
    verbs.append(VerbQuestion('iru', 'いる', 'exists (a)'))
    verbs.append(VerbQuestion('aru', 'ある', 'exists (i)'))
    verbs.append(VerbQuestion('motsu', 'もつ', 'carry'))
    verbs.append(VerbQuestion('suru', 'する', 'do'))
    verbs.append(VerbQuestion('tsukuru', 'つくる', 'make'))
    verbs.append(VerbQuestion('dekiru', 'できる', 'able'))
    verbs.append(VerbQuestion('iu', 'いう', 'say'))
    verbs.append(VerbQuestion('iku', 'いく', 'go'))
    verbs.append(VerbQuestion('miru', 'みる', 'see'))
    verbs.append(VerbQuestion('ageru', 'あげる', 'give'))
    verbs.append(VerbQuestion('taberu', 'たべる', 'eat'))
    verbs.append(VerbQuestion('shiru', 'しる', 'know'))
    verbs.append(VerbQuestion('hoshii', 'ほしい', 'want'))
    verbs.append(VerbQuestion('kuru', 'くる', 'come'))
    verbs.append(VerbQuestion('tsukeru', 'つける', 'put on'))
    verbs.append(VerbQuestion('oku', 'おく', 'put'))
    verbs.append(VerbQuestion('shinjiru', 'しんじる', 'believe'))
    verbs.append(VerbQuestion('hanasu', 'はなす', 'speak'))
    verbs.append(VerbQuestion('yomu', 'よむ', 'read'))
    verbs.append(VerbQuestion('neru', 'ねる', 'sleep'))
    verbs.append(VerbQuestion('mitsukeru', 'みつける', 'find'))
    verbs.append(VerbQuestion('yobu', 'よぶ', 'call'))
    verbs.append(VerbQuestion('oyogu', 'およぐ', 'swim'))
    verbs.append(VerbQuestion('hajimeru', 'はじめる', 'begin (t)'))
    verbs.append(VerbQuestion('kangaeru', 'かんがえる', 'consider'))
    verbs.append(VerbQuestion('oshieru', 'おしえる', 'teach'))
    verbs.append(VerbQuestion('utau', 'うたう', 'sing'))
    verbs.append(VerbQuestion('wakaru', 'わかる', 'understand'))
    verbs.append(VerbQuestion('warau', 'わらう', 'laugh'))
    verbs.append(VerbQuestion('tatsu', 'たつ', 'stand'))
    verbs.append(VerbQuestion('tomaru', 'とまる', 'stop'))
    verbs.append(VerbQuestion('tsuku', 'つく', 'arrive'))
    verbs.append(VerbQuestion('uru', 'うる', 'sell'))
    verbs.append(VerbQuestion('omou', 'おもう', 'think'))
    verbs.append(VerbQuestion('suwaru', 'すわる', 'sit'))
    verbs.append(VerbQuestion('narau', 'ならう', 'learn'))
    verbs.append(VerbQuestion('nomu', 'のむ', 'drink'))
    verbs.append(VerbQuestion('okuru', 'おくる', 'send'))
    verbs.append(VerbQuestion('kaku', 'かく', 'write'))
    verbs.append(VerbQuestion('hairu', 'はいる', 'enter'))
    verbs.append(VerbQuestion('kau', 'かう', 'buy'))
    verbs.append(VerbQuestion('kiku', 'きく', 'listen'))
    verbs.append(VerbQuestion('matsu', 'まつ', 'wait'))
    verbs.append(VerbQuestion('hajimaru', 'はじまる', 'begin (i)'))
    verbs.append(VerbQuestion('kaeru', 'かえる', 'return'))
    verbs.append(VerbQuestion('kakaru', 'かかる', 'take'))
    verbs.append(VerbQuestion('aruku', 'あるく', 'walk'))
    verbs.append(VerbQuestion('asobu', 'あそぶ', 'play'))
    verbs.append(VerbQuestion('au', 'あう', 'meet'))

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
        if(currUserAns == currCorrectAns):
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
