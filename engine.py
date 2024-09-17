# Import the Engine class
from sensors_actuators.engine import Engine

# Instantiate the engine object
engine = Engine()

def control_motor():
    while True:
        print("\nMotor Control Options:")
        print("1. Start Left Motor")
        print("2. Start Right Motor")
        print("3. Stop Left Motor")
        print("4. Stop Right Motor")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            power = int(input("Enter power percentage for left motor (-100 to 100): "))
            engine.start_left(power)
            print(f"Left motor started with {power}% power.")
        
        elif choice == '2':
            power = int(input("Enter power percentage for right motor (-100 to 100): "))
            engine.start_right(power)
            print(f"Right motor started with {power}% power.")
        
        elif choice == '3':
            engine.stop_left()
            print("Left motor stopped.")
        
        elif choice == '4':
            engine.stop_right()
            print("Right motor stopped.")
        
        elif choice == '5':
            print("Exiting motor control.")
            break
        
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    control_motor()