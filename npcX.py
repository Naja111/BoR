from bge import logic, events, texture, types
import random
import time

cont = logic.getCurrentController()
own = cont.owner
sc = logic.getCurrentScene()
obl = sc.objects
mouse = logic.mouse

txt1 = obl['txt_1_npc_2']
ans1 = obl['ans_1_npc_2']
but1 = obl['click_ans_1_npc_2']
but2 = obl['click_ans_2_npc_2']
ans2 = obl['ans_2_npc_2']
npc2 = obl['npc_2']

char = obl['char']
glb = obl['global']

inv = [glb['slot1'],glb['slot2'],glb['slot3']] #list of all inventory slots

def un():
    txt1['Text'] = 'Hi. I need some help !\nDo you have a minute ?'
    but1['vis'] = True #make the overlight active
    ans1['Text'] = 'Yes, what is it ?'
    but2['vis'] = True #make the overlight active
    ans2['Text'] = 'No, I am in a hurry.'
    
def deux():
    if but1['selAns'] is True:
        #reset buttons
        but1['selAns'] = False
        but2['selAns'] = False
        
        txt1['Text'] = 'I could really use a ITEM2,\nplease bring one to me.'

        for i,ii in enumerate(inv): #itterate the list of slots, searching for a item2
            if inv[i] == 'item2': #if it founds one :
                npc2['got'] = True
                break
            else:
                npc2['got'] = False

        if npc2['got'] is True:
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
        if npc2['got'] is True:
            but1['selAns'] = False
            but2['selAns'] = False

            txt1['Text'] = 'Oh thanks !\nTake this reward.'
            but1['vis'] = True
            but2['vis'] = False
            ans1['Text'] = '(Take the reward)'
            ans2['Text'] = ''

        elif npc2['got'] is False:
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

if npc2['script'] == 0:
    pass
elif npc2['ended'] is True:
    txt1['Text'] = 'Thanks for your help !'
    ans1['Text'] = ''
    ans2['Text'] = ''
    but1['vis'] = False
    but2['vis'] = False
    npc2['ended'] = True
elif npc2['script'] == 1:
    un()
elif npc2['script'] == 2:
    deux()
elif npc2['script'] == 3:
    trois()
elif npc2['script'] == 4:
    npc2['ended'] = True
