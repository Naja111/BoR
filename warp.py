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


goTO = obl[own['warpTO']] #set destination name in goTO property by copying it from the "warpTO" prop of the object controlling the script

#The three necessary logic bricks on the object controlling the script are :
E = cont.sensors['E'] # a keayboard sensors named E
Near = cont.sensors['Near'] # a near sensor named Near
camSwitch = cont.actuators['Cam'] # a Scene actuator named Cam

#The controlling object also need a string property named "warpTO" containing the name of the destination
#Dont forget to select the new camera to use after warping by selecting with the scene actuator (Cam)
#This script also use a timer variable (called "warpTime") starting at zero on a object called "global" as a cooldown

#WARP :
if E.positive and Near.positive and glb['warpTime'] > 0.5: #check if the [E] touch of the keyboard is pressed and the character is in the trigger zone usin logics sensors named E and Near
	glb['warpTime'] = 0 #reset warp time cooldown
	warp = goTO.position #grab the warp's point global position
	print('warp to :',warp,goTO) #print warp position, not really usefull
	char.position = warp #warp the character to finale position
	cont.activate(camSwitch) #activate the actuator responsable for switching to the new camera