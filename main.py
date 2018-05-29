from bge import logic, events, texture, types
import random
import time

cont = logic.getCurrentController()
own = cont.owner
sc = logic.getCurrentScene()
obl = sc.objects
mouse = logic.mouse

txt1 = obl['txt_1_npc_1']
ans1 = obl['ans_1_npc_1']
but1 = obl['click_ans_1']
but2 = obl['click_ans_2']
ans2 = obl['ans_2_npc_1']
npc1 = obl['npc_1']

def un():
    #bloquer le personnage
    txt1['Text'] = 'Hi. How are you ?'
    but1['vis'] = True #make the overlight active
    ans1['Text'] = 'Fine and you ?'
    but2['vis'] = True #make the overlight active
    ans2['Text'] = 'Go fuck yourself'
    

def deux():
    if but1['selAns'] is True:
        #reset buttons
        but1['selAns'] = False
        but2['selAns'] = False
        
        txt1['Text'] = 'Am good thanks'
        but1['vis'] = True #make the overlight active
        ans1['Text'] = 'Bye'
        but2['vis'] = False #make the overlight inactive
        ans2['Text'] = ''
        
    elif but2['selAns'] is True:
        #reset buttons
        but1['selAns'] = False
        but2['selAns'] = False
        
        txt1['Text'] = 'Oh'
        but1['vis'] = True #make the overlight active
        ans1['Text'] = 'See you'
        but2['vis'] = False #make the overlight inactive
        ans2['Text'] = ''

if npc1['ended'] is True:
    txt1['Text'] = 'I told you to go away.'
    ans1['Text'] = ''
    ans2['Text'] = ''
    but1['vis'] = False
    but2['vis'] = False
    npc1['ended'] = True
elif npc1['script'] == 1:
    un()
elif npc1['script'] == 2:
    deux()
elif npc1['script'] == 3:
    txt1['Text'] = 'Go away now.'
    ans1['Text'] = ''
    ans2['Text'] = ''
    but1['vis'] = False
    but2['vis'] = False
    npc1['ended'] = True