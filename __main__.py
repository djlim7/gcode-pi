'''A main logic for Raspberry Pi with GPIO(gpiozero).'''

import argparse
import GCodeModule

# Parse the arguments
PARSER_OBJ = argparse.ArgumentParser()
PARSER_OBJ.add_argument('input_file', type=str, nargs='?')
PARSER_ARG = PARSER_OBJ.parse_args()

# Process
with open(PARSER_ARG.input_file, 'r') as file_stream:
    S = file_stream.read()

CUSTOM_PARSER = GCodeModule.GCodeProcedure.GCodeParser(S)
CUSTOM_ELEMENT_TUPLE = GCodeModule.GCodeObject.GCodeElementHandler(CUSTOM_PARSER.parse_syntax())
print(CUSTOM_ELEMENT_TUPLE.bind_to_gcode())
