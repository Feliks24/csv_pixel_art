import ast
import sys
import numpy as np
import csv
import os

#our file
from settings import *



def hex_to_rgb(hex_color):
    """Converts a hexadecimal color code to RGB (decimal)."""
    hex_color = hex_color.lstrip('#')
    return [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]

def string_to_rgb(rgb_string):
    return ast.literal_eval(rgb_string)

def ansi(rgb_array):
    #ansi escape character for setting the color
    return f'\\e[48;2;{rgb_array[0]};{rgb_array[1]};{rgb_array[2]}m '

def csv_format(inputfile, outputfile):
    """does all the work"""
    with open(inputfile, newline='') as csvfile:

        reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)

        #find unique colors
        colors = set()
        for row in reader:
            colors.update(row)
        define_colors = dict()
        colorcode_RGB = (0,0,0)

        #define the unique colors and convert to readable colorcode

        print(f'define colorcodes for colors either in:\n hex #000000 - #FFFFFF\n rgb [0,0,0] - [255,255,255]\n transparent: \'transparent\' or -1')
        for color in colors:
            print(f'define {color}:')
            colorcode = input()
            if colorcode[:1] == '!':
                #only for testing
                colorcode_RGB = colorcode
            elif colorcode == 'transparent' or colorcode == '-1':
                colorcode_RGB ='\\e[0m '
            elif colorcode[:1] == '#':
                colorcode_RGB = ansi(hex_to_rgb(colorcode))
            elif colorcode[:1] == '[':
                colorcode_RGB = ansi(string_to_rgb(colorcode))
            else:
                print('colorcode not recognized')
                return
            define_colors[color] = ratio_multiplier*colorcode_RGB

    #if file not available/overwrites previous file
    if not os.path.exists(outputfile):
        open(outputfile, 'w').close()
    #write into new file
    with open(inputfile, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        with open(outputfile, 'w') as writefile:
            for row in reader:
                writefile.write(linebegin)
                for element in row:
                    writefile.write(str(define_colors[element]))
                #resets the background color
                writefile.write('\\e[0m ')
                #custom linened + row delimiter
                writefile.write(lineend)
                writefile.write(output_delimiter)



if __name__ == "__main__":
    try:
        inputfile = sys.argv[1]
        outputfile = sys.argv[2]
    except:
        print("not enough arguments")
        print("$csv_pixel_art inputfile outputfile")
        sys.exit()
    if (not inputfile[(len(inputfile)-4):] == '.csv'):
        print('File is not csv, might cause unexpected behaviour')
    
    csv_format(inputfile, outputfile)
