## Usage

python csv\_pixel\_art inputfile outputfile

there are several options for source, the input 

you can input csv fies for this it's important to set the following variables in settings.py:

delimiter/quotechar: delimiter as per csv setting/dialect; by defailt ',' and '"'



also an option is inputing images of either png, jpg or jpeg.
For these the following variable settings apply:

adjust, width, height

by default adjust will be false. Setting it to true will cause the program to use
an experimental function that will scale the image down to the defined width and height.
the scale down is naive and might produce unexpected results not resembling the image.

for images that already have the correct size just use adjust=False


there's also a few variables that affect the output independent of inputfile type

output\_delimiter: delimiter of rows; by default '\n'

linebegin/lineend: puts some custom string in front and in the end of each line

ratio\_multiplier: since the ratio between height and width is 1:2 for terminals need to
multiple (by default with 2) so pixel art comes out right. can only be integer


## Requirements

python: ast, sys, numpy, csv, os, PIL

## Example and Credit

For the example pixel art of Emil from Nier

I copied it from user 'jehuty': https://kandipatterns.com/patterns/characters/emil-nier-35822



To inspect the picture in the command line make sure the file is executable with chmod +x output

then run ./output; if that doesn't work add '#!/bin/bash' to first line of the file
