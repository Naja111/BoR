from bge import logic, events, texture, types
import random
import time

#basic set-up things and aliases
cont = logic.getCurrentController()
own = cont.owner
sc = logic.getCurrentScene()
obl = sc.objects
mouse = logic.mouse

char = obl['char']
glb = obl['global']

#sl1,sl2,sl3 = obl['slot1'],obl['slot2'],obl['slot3'] ##########

E = cont.sensors['E'] # a keayboard sensors named E
Near = cont.sensors['Near'] # a near sensor named Near

inv = [glb['slot1'],glb['slot2'],glb['slot3']]
freeslot = False

if E.positive and Near.positive:
	picking = own
	print('picking:',picking)

	for i,ii in enumerate(inv):
		if inv[i] == '':
			print('slot',i+1,' is avalaible')
			freeslot = True
			free = str('slot{}'.format(i+1))
			glb[free] = str(picking) #add the item in the slot
			
			#create visual
			obl
			slotpos = obl[free].position
			
			
			break
		else:
			pass

	if freeslot is False:
		print('No free slot')
	else:
pass
