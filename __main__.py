'''A main logic for Raspberry Pi with GPIO(gpiozero).'''

import argparse
import GCodeModule

# Parse the arguments
PARSER_OBJ = argparse.ArgumentParser()
PARSER_OBJ.add_argument('input_file', type=str, nargs='?')
PARSER_ARG = PARSER_OBJ.parse_args()

# Process
def proc_main():
    """Main procedure of gcode-pi"""
    import pprint

    with open(PARSER_ARG.input_file, 'r') as file_stream:
        string = file_stream.read()

        gcode_tuple = GCodeModule.GCodeProcedure.GCodeParser(string).run()
        pprint.pprint(gcode_tuple)

if __name__ == '__main__':
    proc_main()
