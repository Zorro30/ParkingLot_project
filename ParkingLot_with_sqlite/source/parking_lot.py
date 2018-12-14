#!/usr/bin/python
import os, sys
import parking

class ParkingCommands(object):

    def __init__(self):
        self.parking = parking.Parking()

    print('*'*20+'Parking Project'+'*'*20)
    print('hint-> Type Bye or press Enter to quit')

    def process_input(self):
        try:
            while True:
                text = input('Enter command: ')
                if text == 'Bye':
                    return
                else:
                    self.process_command(text)
        except (KeyboardInterrupt, SystemExit):
            return
        except Exception as ex:
            print('Thanks for using Parking App')

    def process_command(self, text):
        inputs = text.split()
        command = inputs[0]
        params = inputs[1:]
        if hasattr(self.parking, command):    #checks if the command is present in the parking.py file.
            command_function = getattr(self.parking, command)
            command_function(*params)
        else:
            print ("Got wrong command.")

if __name__ == "__main__":
    pk_command = ParkingCommands()
    pk_command.process_input()


