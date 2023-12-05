from controller import Controller

def main():
    INPUT_PIN = 22
    OUTPUT_PIN = 17
    
    controller = Controller(INPUT_PIN, OUTPUT_PIN)
    
    controller.run()
    return

if __name__ == "__main__":
    main()