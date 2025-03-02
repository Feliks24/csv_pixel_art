#!/usr/bin/python

import ast
import sys
import numpy as np
import csv
import os
from PIL import Image

#our file
from settings import *

def hex_to_rgb(hex_color):
    """Converts a hexadecimal color code to RGB (decimal)."""
    hex_color = hex_color.lstrip('#')
    return [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]

def string_to_rgb(rgb_string):
    #perhaps dangerous, TODO: make sure its good
    return ast.literal_eval(rgb_string)

def ansi(rgb_array):
    #ansi escape character for setting the color
    if rgb_array[0] == -1 or rgb_array[0] == 300:
        return '\\e[0m '
    return f'\\e[48;2;{rgb_array[0]};{rgb_array[1]};{rgb_array[2]}m '

def csv_format(inputfile):
    """does all the work"""
    data = []
    with open(inputfile, newline='') as csvfile:

        reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        #find unique colors and get matrix
        colors = set()
        for row in reader:
            colors.update(row)
            data.append(row)
    matrix = np.array(data,dtype='<U25')

    colorcode_RGB = (0,0,0)
    define_colors = {}

    #define the unique colors and convert to readable colorcode
    print(f'define colorcodes for colors either in:\n hex #000000 - #FFFFFF\n rgb [0,0,0] - [255,255,255]\n transparent: \'transparent\' or -1')
    for color in colors:
        print(f'define {color}:')
            #if str(color) == '-1':
                #colorcode_RGB ='\\e[0m '
            #else:
                #colorcode_RGB = ansi(string_to_rgb(color))
        colorcode = input()
        if colorcode[:1] == '!':
            #only for testing, to be removed later
            colorcode_RGB = colorcode
        elif colorcode == "":
            #special case, to be removed later
            colorcode_RGB = string_to_rgb(color)
        elif colorcode == 'transparent' or colorcode == '-1':
            colorcode_RGB = [-1,-1,-1]
        elif colorcode[:1] == '#':
            colorcode_RGB = hex_to_rgb(colorcode)
        elif colorcode[:1] == '[':
            colorcode_RGB = string_to_rgb(colorcode)
        else:
            print('colorcode not recognized')
            return
        define_colors[color] = ansi(colorcode_RGB)
            
    for w in range(matrix.shape[0]):
        for h in range(matrix.shape[1]):
            matrix[w,h] = define_colors[matrix[w,h]]
    return matrix

def image_format(inputfile):
    with Image.open(inputfile) as im:
        image_matrix = np.array(im)
    height, width, channels = image_matrix.shape
    if channels == 4:
        #this means that there is an alpha channel
        temp_matrix = image_matrix[:,:,:3]
        ansi_matrix = np.empty((height,width),dtype='<U25')
        for row in range(height):
            for col in range(width):
                if image_matrix[row,col,3] < 100:
                    ansi_matrix[row,col] = '\\e[0m '
                else:
                    ansi_matrix[row,col] = ansi(temp_matrix[row,col])
    elif channels == 3:
        ansi_matrix = np.empty((height,width,3),dtype='<U25')
        for row in range(height):
            for col in range(width):
                ansi_matrix[row,col] = ansi(image_matrix[row,col])
    else:
        print("an error with the image dimensions occurred")
        return [[[-1]]]
    #print(ansi_matrix)
    #print(ansi_matrix.shape)
    return ansi_matrix

def image_format_adjust(inputfile, width=width, height=height):
    #height and width defined in settings.py
    img = Image.open(inputfile).convert("RGB")
    img_w, img_h = img.size

    pixels_matrix = []

    for row in range(height):
        row_pixels = []
        for col in range(width):
            src_x = int((col/width)*img_w)
            src_y = int((row/height)*img_h)
            r,g,b = img.getpixel((src_x, src_y))

            row_pixels.append(ansi([r,g,b]))
        pixels_matrix.append(row_pixels)
    return pixels_matrix



def file_to_output(inputfile, outputfile, format_function):
    matrix = format_function(inputfile)
    if matrix[0][0] == -1:
        return 
    """
        its expected that the matrix is some size
        and has the characters already formatted
        in the correct string now to be printed in output
    """
    if not os.path.exists(outputfile):
        open(outputfile, 'w').close()

    with open(outputfile, 'w') as writefile:
        for row in matrix:
            writefile.write(linebegin)
            for element in row:
               writefile.write(ratio_multiplier*(element))
            #reset the terminal background + custom defined string
            writefile.write('\\e[0m '+lineend+output_delimiter)
    return

if __name__ == "__main__":
    try:
        inputfile = sys.argv[1]
        outputfile = sys.argv[2]
    except:
        print("not enough arguments")
        print("$csv_pixel_art inputfile outputfile")
        sys.exit()
    
    filetype = inputfile[(len(inputfile)-4):]
    if inputfile.endswith('.csv'):
        file_to_output(inputfile, outputfile, csv_format)
    elif inputfile.endswith(('.jpeg', '.png', '.jpg')):
        if adjust:
            file_to_output(inputfile, outputfile, image_format_adjust)
        else:
            file_to_output(inputfile, outputfile, image_format)
    else:
        print('invalid inputfile type')
        print('make sure file is either csv, png, jpg or jpeg')
