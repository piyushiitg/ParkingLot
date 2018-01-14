#!/usr/bin/python
import os, sys
import parking

class ParkingCommands(object):

    def __init__(self):
        self.parking = parking.Parking()

    def process_file(self, given_file):
        if not os.path.exists(given_file):
            print "Given file %s does not exist" % given_file

        file_obj = open(given_file)
        try:
            while True:
                line = file_obj.next()
                if line.endswith('\n'): line = line[:-1]
                if line == '': continue
                self.process_command(line)
        except StopIteration:
            file_obj.close()
        except Exception as ex:
            print "Error occured while processing file %s" % ex

    def process_input(self):
        try:
            while True:
                stdin_input = raw_input("Enter command: ")
                self.process_command(stdin_input)
        except (KeyboardInterrupt, SystemExit):
            return
        except Exception as ex:
            print "Error occured while processing input %s" % ex


    def process_command(self, stdin_input):
        inputs = stdin_input.split()
        command = inputs[0]
        params = inputs[1:]
        if hasattr(self.parking, command):
            command_function = getattr(self.parking, command)
            command_function(*params)
        else:
            print "Got wrong command."


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        pk_command = ParkingCommands()
        pk_command.process_input()
    elif len(args) == 2:
        pk_command = ParkingCommands()
        pk_command.process_file(args[1])
    else:
        print "Wrong number of arguments.\n" \
                "Usage:\n" \
                "./parking_lot.py <filename> OR \n" \
                "./parking_lot.py"

