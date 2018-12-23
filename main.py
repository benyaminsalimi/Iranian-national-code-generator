#!/usr/bin/python
import getopt
import json
import re
import sys
from ir_national_code import *

national_code_object = ir_national_code()

def main(argv):
    state = ''
    output = ''
    try:
        opts, args = getopt.getopt(argv,"hs:o:",["state=","output="])
    except getopt.GetoptError:
        print('main.py -s <state name> -o <output file name>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('main.py -s <state name> -o <output file name>')
            sys.exit()
        elif opt in ("-s",'--state'):
            state = arg
        elif opt in ("-o",'--output'):
            output = arg
    
    if output == '':
        output = state
    
    # open outputfile
    outputfile = open(output, 'a')
    
    # i dont use national_code_object.by_state() because of memory issues 
    # searching the city
    counter = 0
    for city in national_code_object.city_codes:
        if state == national_code_object.city_codes[city][0]:
            # generate 0000000 to 9999999
            for x in range(10000000, 19999999):
                # each national code
                code = str(city + str(x)[1:])
                if national_code_object.validator(code):
                    # write to file
                    outputfile.write(code + '\n')
                    counter += 1
    print("Total number of exported code : ",counter)
    
                    

if __name__ == "__main__":
    main(sys.argv[1:])
