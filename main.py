# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# SCLPin=17
# SDOPin=22

# HALF_BIT_TIME=.001
# CHARACTER_DELAY=5*HALF_BIT_TIME

# NUM_BITS=16

# GPIO.setup(SCLPin,GPIO.OUT)
# GPIO.setup(SDOPin,GPIO.IN)

# GPIO.output(SCLPin,GPIO.HIGH)
# time.sleep(HALF_BIT_TIME)

# # Initialize the previous key pressed
# prevKeyPressed = 0
# DEBOUNCE_DELAY = 0.2

# # Represents the mathematical expression
# expressionString = ''
# try:
# 	while True:
# 		button=1
# 		time.sleep(CHARACTER_DELAY)

# 		# Represents the first value the user inputs before pressing the mathematical operation
#         # Initialize button pressed boolean and first and s3econd val
		
# 		while button < 17:
# 			print_button=button
# 			if (print_button==17):
# 				print_button=1

# 			GPIO.output(SCLPin,GPIO.LOW)
			
# 			keyval=GPIO.input(SDOPin)
# 			if not keyval and not buttonPressed:
# 				# If 
# 				if prevKeyPressed in [4, 8, 12, 16]:
# 					print('operation:', print_button)
# 				else:
# 					expressionString += str(print_button)
# 				buttonPressed=True
# 				prevKeyPressed=button
# 				print('value:', expressionString)
# 				# Delay to now allow a value to be registered more than once if only clicking the button once
# 				time.sleep(DEBOUNCE_DELAY)

# 			GPIO.output(SCLPin,GPIO.HIGH)
			

# 			button+=1
# 		buttonPressed=False

# except KeyboardInterrupt:
# 	pass
# 	GPIO.cleanup
from controller import Controller
def main():
    INPUT_PIN = 22
    OUTPUT_PIN = 17
    
    controller = Controller(INPUT_PIN, OUTPUT_PIN)
    
    controller.run()
    return

if __name__ == "__main__":
    main()