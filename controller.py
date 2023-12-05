import RPi.GPIO as GPIO
import time
from calculator import Calculator

class Controller:
    def __init__(self, inputPin, outputPin) -> None:
        self.SCLPin = outputPin
        self.SDOPin = inputPin

        # Get the calculator object
        self.calculator = Calculator()

        # Set GPIO Pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.SCLPin,GPIO.OUT)
        GPIO.setup(self.SDOPin,GPIO.IN)
        GPIO.output(self.SCLPin,GPIO.HIGH)
        # String that represents mathematical expression
        self.expressionString = ''
        self.operationAlreadyUsed = False
        # Constants
        self.NUM_BITS = 16
        self.DEBOUNCE_DELAY = 0.2
        self.BIT_DELAY = 0.005

        time.sleep(self.BIT_DELAY)

    '''
        Will run the program to get input from the number pad and use the calculator to compute the string expression
    '''
    def run(self):
        try:
            print('--------------------------------------------')
            print("Welcome to the Calculator Program!")
            print("Please enter numerical values and mathematical operations.")
            print("You can enter a series of values and one operation. The program will calculate the result.")
            print("Only one operation is allowed in each calculation.")
            print("Press Ctrl+C to exit the program.")
            print('--------------------------------------------')
            while True:
                # Set button to 1 after every iteration
                button=1
                time.sleep(self.BIT_DELAY)

                while button < 17:
                    correctButton=button
                    if (correctButton==17):
                        correctButton=1

                    GPIO.output(self.SCLPin,GPIO.LOW)
                    keyval=GPIO.input(self.SDOPin)
                 
                    # When button is pressed
                    if not keyval and not buttonPressed:
                        if(correctButton == 15):
                            # When 15 (clear) is pressed, clear the expression
                            self.clear()
                        elif(correctButton == 16):
                            print('Calculating expression...')
                            # When 16 (enter) is pressed, evaluate the expression
                            result = self.calculator.evaluateExpression(self.expressionString)
                            print('--------------------------------------------')
                            print(f'Calculated result: {result}')
                            print('Continue entering numerical values and mathematical operations if you would like to calculate another expression!')
                            print('--------------------------------------------')
                            self.clear()
                        elif(correctButton in [11, 12, 13, 14]): # Any operation button selected
                            # If operation symbol already in expression string
                            if(self.operationAlreadyUsed):
                                print('You cannot use more than 1 operation symbol! Please try again.\n')
                            else:
                                # Transform the number of the button pressed to a operation symbol
                                operationSymbol = self.transformNumToOperationSymbol(correctButton)
                                self.operationAlreadyUsed = True
                                self.expressionString += str(operationSymbol)
                        elif(correctButton == 10):
                            # If 10 is selected, make it add a 0 instead of 10
                            self.expressionString += '0'
                        else:
                            self.expressionString += str(correctButton)
                       
                        buttonPressed=True
                        print('Your expression:', self.expressionString)

                        # Delay to now allow a value to be registered more than once if only clicking the button once
                        time.sleep(self.DEBOUNCE_DELAY)

                    GPIO.output(self.SCLPin,GPIO.HIGH)

                    button+=1
                buttonPressed=False

        except KeyboardInterrupt:
            self.cleanup()
    
    def transformNumToOperationSymbol(self, buttonNumber):
        operation_mapping = {
            11: '+',  # Plus
            12: '-',  # Minus
            13: '*',  # Multiply
            14: '/',  # Divide
        }

        # Return the operation symbol or None if not found
        return operation_mapping.get(buttonNumber)

    '''
        Function to clear the current expression
    '''
    def clear(self):
        self.operationAlreadyUsed = False
        self.expressionString = ''

    def cleanup(self):
        GPIO.cleanup
