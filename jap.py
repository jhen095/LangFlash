import random

verbs = {'iru': 'exists (animate)'}
verbs['aru'] = 'exists (inanimate)'
verbs['motsu'] = 'carry'
verbs['suru'] = 'do'
verbs['tsukuru'] = 'make'
verbs['dekiru'] = 'be able to'
verbs['iu'] = 'say'
verbs['iku'] = 'go'
verbs['miru'] = 'see'
verbs['ageru'] = 'give'
verbs['taberu'] = 'eat'
verbs['shiru'] = 'know'
verbs['hoshii'] = 'want'
verbs['kuru'] = 'come'
verbs['tsukeru'] = 'put on'
verbs['oku'] = 'put'
verbs['shinjiru'] = 'believe'
verbs['hanasu'] = 'speak'
verbs['yomu'] = 'read'
verbs['neru'] = 'sleep'
verbs['mitsukeru'] = 'find'
verbs['yobu'] = 'call'

correctCount = 0

bContinue = True
while bContinue:
	currVerbKey = list(verbs.keys())[random.randint(0, len(verbs)-1)]
	currVerbVal = verbs[currVerbKey]
	
	if(random.randint(0,1)):
		ansEng = False
		print('Japanese for: ' + currVerbVal)
	else:
		ansEng = True
		print('English for: ' + currVerbKey)
	
	currAns = input()
	
	if(currAns == 'x' or currAns == 'X' or currAns == 'q' or currAns == 'Q'):
		bContinue = False
		continue
	
	result = False;
	correctAns = ''
	if(ansEng):
		currCorrectAns = currVerbVal
	else:
		currCorrectAns = currVerbKey
			
	if(currAns == currCorrectAns):
		result = True			
			
	if(result):
		correctCount+=1
		print('CORRECT - Correct Count = ' + str(correctCount) + '\n\n')
	else:
		print('WRONG - Correct answer is : ' + currCorrectAns + '\n\n')
	
print('Thanks for playing. Bye!')