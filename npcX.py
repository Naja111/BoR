from bge import logic, events, texture, types
import random
import time

cont = logic.getCurrentController()
own = cont.owner
sc = logic.getCurrentScene()
obl = sc.objects
mouse = logic.mouse

txt1 = obl['txt_1_npc_3']
ans1 = obl['ans_1_npc_3']
but1 = obl['click_ans_1_npc_3']
but2 = obl['click_ans_2_npc_3']
ans2 = obl['ans_2_npc_3']
npc = obl['npc_3']

char = obl['char']
glb = obl['global']

inv = [glb['slot1'],glb['slot2'],glb['slot3']] #list of all inventory slots

def un():
    if npc['talked'] is True:
        txt1['Text'] = 'Ho, its you again. Want something ?'
    else:
        txt1['Text'] = 'Hello stranger. Need a drink ?'
        
    but1['vis'] = True #make the overlight active
    but2['vis'] = True #make the overlight active
    
    if glb['barQuest'] >= 1:
        ans1['Text'] = 'Do you know a William ?'
    else:
        ans1['Text'] = 'Any news from the city ?'
    
    ans2['Text'] = 'No, I am in a hurry.'
    
def deux():
    if but1['selAns'] is True:
        #reset buttons
        but1['selAns'] = False
        but2['selAns'] = False
        
        txt1['Text'] = 'I could really use a ITEM2,\nplease bring one to me.'

        for i,ii in enumerate(inv): #itterate the list of slots, searching for a item2
            if inv[i] == 'item2': #if it founds one :
                npc['got'] = True
                break
            else:
                npc['got'] = False

        if npc['got'] is True:
            but1['vis'] = True
            ans1['Text'] = '(Give it to him)'
            but2['vis'] = True
            ans2['Text'] = 'No thanks.'
        else:
            but1['vis'] = True
            ans1['Text'] = 'I will go get one for you.'
            but2['vis'] = True
            ans2['Text'] = 'No thanks.'
    elif but2['selAns'] is True:

        but1['selAns'] = False
        but2['selAns'] = False

        txt1['Text'] = 'Oh ok too bad.'
        but1['vis'] = False
        but2['vis'] = False
        ans1['Text'] = ''
        ans2['Text'] = ''
    else:
        pass

def trois():
    if but1['selAns'] is True:
        if npc['got'] is True:
            but1['selAns'] = False
            but2['selAns'] = False

            txt1['Text'] = 'Oh thanks !\nTake this reward.'
            but1['vis'] = True
            but2['vis'] = False
            ans1['Text'] = '(Take the reward)'
            ans2['Text'] = ''

        elif npc['got'] is False:
            but1['selAns'] = False
            but2['selAns'] = False

            txt1['Text'] = 'I will wait here for you then.'
            but1['selAns'] = False
            but2['selAns'] = False
            but1['vis'] = False
            but2['vis'] = False
            ans1['Text'] = ''
            ans2['Text'] = ''

    elif but2['selAns'] is True:
        txt1['Text'] = 'I will get it myself then.'
        but1['selAns'] = False
        but2['selAns'] = False
        but1['vis'] = False
        but2['vis'] = False
        ans1['Text'] = ''
        ans2['Text'] = ''
    else:
        pass

if npc['script'] == 0:
    pass
elif npc['ended'] is True:
    txt1['Text'] = 'Thanks for your help !'
    ans1['Text'] = ''
    ans2['Text'] = ''
    but1['vis'] = False
    but2['vis'] = False
    npc['ended'] = True
elif npc['script'] == 1:
    un()
elif npc['script'] == 2:
    deux()
elif npc['script'] == 3:
    trois()
elif npc['script'] == 4:
    npc['ended'] = True
