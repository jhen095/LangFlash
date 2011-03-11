#!/usr/bin/env python

import sys
import random

def load():
    # One day these will be populated from an external file. Probably XML.
    verbs.insert(0, VocabObj('iru', 'いる', 'exists (a)'))
    verbs.insert(1, VocabObj('aru', 'ある', 'exists (i)'))
    verbs.insert(2, VocabObj('motsu', 'もつ', 'carry'))
    verbs.insert(3, VocabObj('suru', 'する', 'do'))
    verbs.insert(4, VocabObj('tsukuru', 'つくる', 'make'))
    verbs.insert(5, VocabObj('dekiru', 'できる', 'able'))
    verbs.insert(6, VocabObj('iu', 'いう', 'say'))
    verbs.insert(7, VocabObj('iku', 'いく', 'go'))
    verbs.insert(8, VocabObj('miru', 'みる', 'see'))
    verbs.insert(9, VocabObj('ageru', 'あげる', 'give'))
    verbs.insert(10, VocabObj('taberu', 'たべる', 'eat'))
    verbs.insert(11, VocabObj('shiru', 'しる', 'know'))
    verbs.insert(12, VocabObj('hoshii', 'ほしい', 'want'))
    verbs.insert(13, VocabObj('kuru', 'くる', 'come'))
    verbs.insert(14, VocabObj('tsukeru', 'つける', 'put on'))
    verbs.insert(15, VocabObj('oku', 'おく', 'put'))
    verbs.insert(16, VocabObj('shinjiru', 'しんじる', 'believe'))
    verbs.insert(17, VocabObj('hanasu', 'はなす', 'speak'))
    verbs.insert(18, VocabObj('yomu', 'よむ', 'read'))
    verbs.insert(19, VocabObj('neru', 'ねる', 'sleep'))
    verbs.insert(20, VocabObj('mitsukeru', 'みつける', 'find'))
    verbs.insert(21, VocabObj('yobu', 'よぶ', 'call'))
    verbs.insert(22, VocabObj('oyogu', 'およぐ', 'swim'))
    verbs.insert(23, VocabObj('hajimeru', 'はじめる', 'begin (t)'))
    verbs.insert(24, VocabObj('kangaeru', 'かんがえる', 'consider'))
    verbs.insert(25, VocabObj('oshieru', 'おしえる', 'teach'))
    verbs.insert(26, VocabObj('utau', 'うたう', 'sing'))
    verbs.insert(27, VocabObj('wakaru', 'わかる', 'understand'))
    verbs.insert(28, VocabObj('warau', 'わらう', 'laugh'))
    verbs.insert(29, VocabObj('tatsu', 'たつ', 'stand'))
    verbs.insert(30, VocabObj('tomaru', 'とまる', 'stop'))
    verbs.insert(31, VocabObj('tsuku', 'つく', 'arrive'))
    verbs.insert(32, VocabObj('uru', 'うる', 'sell'))
    verbs.insert(33, VocabObj('omou', 'おもう', 'think'))
    verbs.insert(34, VocabObj('suwaru', 'すわる', 'sit'))
    verbs.insert(35, VocabObj('narau', 'ならう', 'learn'))
    verbs.insert(36, VocabObj('nomu', 'のむ', 'drink'))
    verbs.insert(37, VocabObj('okuru', 'おくる', 'send'))
    verbs.insert(38, VocabObj('kaku', 'かく', 'write'))
    verbs.insert(39, VocabObj('hairu', 'はいる', 'enter'))
    verbs.insert(40, VocabObj('kau', 'かう', 'buy'))
    verbs.insert(41, VocabObj('kiku', 'きく', 'listen'))
    verbs.insert(42, VocabObj('matsu', 'まつ', 'wait'))
    verbs.insert(43, VocabObj('hajimaru', 'はじまる', 'begin (i)'))
    verbs.insert(44, VocabObj('kaeru', 'かえる', 'return'))
    verbs.insert(45, VocabObj('kakaru', 'かかる', 'take'))
    verbs.insert(46, VocabObj('aruku', 'あるく', 'walk'))
    verbs.insert(47, VocabObj('asobu', 'あそぶ', 'play'))
    verbs.insert(48, VocabObj('au', 'あう', 'meet'))


class VocabObj:
    """A simple vocabulary object"""
    def __init__(self, romaji_vocab, hirigana_vocab, english_meaning):
        self.romaji_vocab = romaji_vocab
        self.hirigana_vocab = hirigana_vocab
        self.english_meaning = english_meaning

# main
correctCount = 0
bContinue = True
verbs = []
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
