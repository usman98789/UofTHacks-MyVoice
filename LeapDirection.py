import Leap, sys, math, time
from Leap import SwipeGesture
# CircleGesture, KeyTapGesture, ScreenTapGesture

# create a list to store the msgs
s=[]
import pyttsx
engine = pyttsx.init()
engine.say('Greetings!')
engine.say('How are you today?')
engine.runAndWait()

class LeapMotionListener(Leap.Listener):
	
	

	def on_connect(self,controller):
		print "Motion Sensor Connected"
		engine.say('Motion Sensor is Connected')
		engine.runAndWait()
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
		
	
def main():
	listener = LeapMotionListener()
	controller = Leap.Controller()

	controller.add_listener(listener)
	while True:
		global s, engine
	
		frame = controller.frame()
	
		for gesture in frame.gestures():
			# check if gesture is swipe
			if gesture.type == Leap.Gesture.TYPE_SWIPE:
				swipe = SwipeGesture(gesture)
				swipeDir = swipe.direction
					# if x>0 and x>y (right)
				if(swipeDir.x > 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
					# if length is 0 or last element is not left, add right
					if len(s)==0 or s[len(s)-1]!="right":
						# add "right" to end of the list
						s.append("right")
					# else x<0 and x>y (left)
				elif(swipeDir.x < 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
					if len(s)==0 or s[len(s)-1]!="left":
						s.append("left")
					# else y>0 and x<y (up)
				elif(swipeDir.y > 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
					if len(s) == 0 or s[len(s) - 1] != "up":
						s.append("up")
					# else y<0 and x<y (down)
				elif(swipeDir.y < 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
					if len(s) == 0 or s[len(s) - 1] != "down":
						s.append("down")
		
			# make list into str(join)
			print s, ":  ", "".join(s)
			# if s is right and up
			if("".join(s)=="rightup"):
				engine.say('Hello!')
				engine.runAndWait()
				s=[]
				
				# pause for a sec
				time.sleep(1)
	
			if ("".join(s)=="leftup"):
				engine.say("Bye")
				engine.runAndWait()
				s=[]
				time.sleep(1)
				
			# if length of s is more than 5, clear
			if(len(s)>=2):
				s=[]
				time.sleep(1)
				print "clear"
				
				
	
	print "Press enter to quit"
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		controller.remove_listener(listener)



if __name__ == "__main__":
	main()