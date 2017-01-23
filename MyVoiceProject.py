import Leap, sys, math, time
from Leap import SwipeGesture
# CircleGesture, KeyTapGesture, ScreenTapGesture
# create a list to store the msgs
s=[]
import pyttsx
engine = pyttsx.init()
engine.say('Greetings!')
engine.say('MyVoice is Activated')
engine.say('Please use hand gestures to communicate.')
#engine.say('How are you today?')
engine.runAndWait()

class LeapMotionListener(Leap.Listener):
	
	def on_connect(self,controller):
		print "Motion Sensor Connected"
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
		
	def on_exit(self, controller):
		print "Exited"
		#engine.say('Motion Controls Deactivated')
		#engine.runAndWait()		
		
def main():	
	listener = LeapMotionListener()
	controller = Leap.Controller()
	controller.add_listener(listener)
	
	cRightMove=0
	cLeftMove=0
	cUpMove=0
	cDownMove=0
	
	loopCount=0
	
	start = time.time()	
	while True:
		global s, engine, exit_thing
		exit_thing = False
		
		frame = controller.frame(0)
		motionSinceLastFrame=frame.translation(controller.frame(1))
		
		
		hand = frame.hands.rightmost
		position = hand.palm_position	
					
		x=position[0]
		y=position[1]
		z=position[2]	
		
		#print frame.current_frames_per_second
		canmove= x>-80 and x<80 and z<60 and z>-60
			
		
		
		if motionSinceLastFrame.x >20.0 and canmove:
			cRightMove+=1
		else:
			cRightMove=0
		if motionSinceLastFrame.x <-20.0 and canmove:
			cLeftMove+=1
		else:
			cLeftMove=0
		if motionSinceLastFrame.y >20.0 and canmove:
			cUpMove+=1
		else:
			cUpMove=0
		if motionSinceLastFrame.y <-20.0 and canmove:
			cDownMove+=1
		else:
			cDownMove=0
		
		
		if(cRightMove>=800):
			if len(s)==0 or s[len(s)-1]!="right":
			# add "right" to end of the list
				s.append("right")
		elif (cUpMove>=800):
			if len(s) == 0 or s[len(s) - 1] != "up":
				s.append("up")			
		elif (cLeftMove>=800):
			if len(s) == 0 or s[len(s) - 1] != "left":
				s.append("left")
		elif (cDownMove>=800):
			if len(s) == 0 or s[len(s) - 1] != "down":
				s.append("down")		
			
		
		
			# make list into str(join)
		#print "".join(s)
			# if s is right and up
		if("".join(s)=="rightup"):
			engine.say('Hello!')
			engine.runAndWait()
			del s[:]
			start=time.time()
			
		elif ("".join(s)=="leftup"):
			engine.say("See you later")
			engine.runAndWait()
			del s[:]
			start=time.time()
				
		elif ("".join(s)=="updown"):
			engine.say("Yes")
			engine.runAndWait()
			del s[:]
			start=time.time()
			
		elif ("".join(s)=="leftright"):
			engine.say("No not at all")
			engine.runAndWait()
			del s[:]
			start=time.time()
				
		elif ("".join(s)=="upleft"):
			engine.say("Thank you very much")
			engine.runAndWait()
			del s[:]
			start=time.time()
				
		elif ("".join(s)=="downleft"):
			engine.say("Sorry about that")
			engine.runAndWait()
			del s[:]
			start=time.time()
				
		elif ("".join(s)=="rightdown"):
			engine.say("My Voice is now Deactivated")
			engine.runAndWait()
			del s[:]
			start=time.time()
			exit_thing = True
				
		if exit_thing == True:
			print("Motion controls are now off")
			break
				
			# if length of s is more than 5, clear
		if(len(s)>=2):
			del s[:]
			loopCount=0
			#print "clear"
			
		end = time.time()
		if(len(s)>0 and (end-start)>2):
			del s[:]
			start=time.time()		
			
	#exit		
	controller.remove_listener(listener)

if __name__ == "__main__":
	main()