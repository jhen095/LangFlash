#!/usr/bin/env python

import sys
import random

def load():
    # One day these will be populated from an external file. Probably XML.
    verbs.insert(0, VerbQuestion('iru', 'いる', 'exists (a)'))
    verbs.insert(1, VerbQuestion('aru', 'ある', 'exists (i)'))
    verbs.insert(2, VerbQuestion('motsu', 'もつ', 'carry'))
    verbs.insert(3, VerbQuestion('suru', 'する', 'do'))
    verbs.insert(4, VerbQuestion('tsukuru', 'つくる', 'make'))
    verbs.insert(5, VerbQuestion('dekiru', 'できる', 'able'))
    verbs.insert(6, VerbQuestion('iu', 'いう', 'say'))
    verbs.insert(7, VerbQuestion('iku', 'いく', 'go'))
    verbs.insert(8, VerbQuestion('miru', 'みる', 'see'))
    verbs.insert(9, VerbQuestion('ageru', 'あげる', 'give'))
    verbs.insert(10, VerbQuestion('taberu', 'たべる', 'eat'))
    verbs.insert(11, VerbQuestion('shiru', 'しる', 'know'))
    verbs.insert(12, VerbQuestion('hoshii', 'ほしい', 'want'))
    verbs.insert(13, VerbQuestion('kuru', 'くる', 'come'))
    verbs.insert(14, VerbQuestion('tsukeru', 'つける', 'put on'))
    verbs.insert(15, VerbQuestion('oku', 'おく', 'put'))
    verbs.insert(16, VerbQuestion('shinjiru', 'しんじる', 'believe'))
    verbs.insert(17, VerbQuestion('hanasu', 'はなす', 'speak'))
    verbs.insert(18, VerbQuestion('yomu', 'よむ', 'read'))
    verbs.insert(19, VerbQuestion('neru', 'ねる', 'sleep'))
    verbs.insert(20, VerbQuestion('mitsukeru', 'みつける', 'find'))
    verbs.insert(21, VerbQuestion('yobu', 'よぶ', 'call'))
    verbs.insert(22, VerbQuestion('oyogu', 'およぐ', 'swim'))
    verbs.insert(23, VerbQuestion('hajimeru', 'はじめる', 'begin (t)'))
    verbs.insert(24, VerbQuestion('kangaeru', 'かんがえる', 'consider'))
    verbs.insert(25, VerbQuestion('oshieru', 'おしえる', 'teach'))
    verbs.insert(26, VerbQuestion('utau', 'うたう', 'sing'))
    verbs.insert(27, VerbQuestion('wakaru', 'わかる', 'understand'))
    verbs.insert(28, VerbQuestion('warau', 'わらう', 'laugh'))
    verbs.insert(29, VerbQuestion('tatsu', 'たつ', 'stand'))
    verbs.insert(30, VerbQuestion('tomaru', 'とまる', 'stop'))
    verbs.insert(31, VerbQuestion('tsuku', 'つく', 'arrive'))
    verbs.insert(32, VerbQuestion('uru', 'うる', 'sell'))
    verbs.insert(33, VerbQuestion('omou', 'おもう', 'think'))
    verbs.insert(34, VerbQuestion('suwaru', 'すわる', 'sit'))
    verbs.insert(35, VerbQuestion('narau', 'ならう', 'learn'))
    verbs.insert(36, VerbQuestion('nomu', 'のむ', 'drink'))
    verbs.insert(37, VerbQuestion('okuru', 'おくる', 'send'))
    verbs.insert(38, VerbQuestion('kaku', 'かく', 'write'))
    verbs.insert(39, VerbQuestion('hairu', 'はいる', 'enter'))
    verbs.insert(40, VerbQuestion('kau', 'かう', 'buy'))
    verbs.insert(41, VerbQuestion('kiku', 'きく', 'listen'))
    verbs.insert(42, VerbQuestion('matsu', 'まつ', 'wait'))
    verbs.insert(43, VerbQuestion('hajimaru', 'はじまる', 'begin (i)'))
    verbs.insert(44, VerbQuestion('kaeru', 'かえる', 'return'))
    verbs.insert(45, VerbQuestion('kakaru', 'かかる', 'take'))
    verbs.insert(46, VerbQuestion('aruku', 'あるく', 'walk'))
    verbs.insert(47, VerbQuestion('asobu', 'あそぶ', 'play'))
    verbs.insert(48, VerbQuestion('au', 'あう', 'meet'))

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
    correctCount = 0
    bContinue = True    
    load()

    while bContinue:
        # determine question/answer & print question
        currCorrectAns = ''
        if(random.randint(0,1)):
            currVerbObj = verbs[random.randint(0, len(verbs) - 1)]
            print('Japanese for: ' + currVerbObj.english_meaning)
            currCorrectAns = currVerbObj.hirigana_vocab
        else:
            currVerbObj = verbs[random.randint(0, len(verbs) - 1)]
            print('English for: ' + currVerbObj.hirigana_vocab)
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
        else:
            print('WRONG - Correct answer is : ' + currCorrectAns + '\n\n')
            
    print('Thanks for playing. Bye!')


verbs = []
main()
