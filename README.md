## Usage

python csv\_pixel\_art inputfile outputfile

there are several options for the inputfile type

the easiest is a png/jpg/jpeg file (transparency supported) with the correct size

in my case I usually use a size of around 20x20

## CSV

I started this for compiling csv files but it just way to inconvenient in comparison to the above

Using actual csv files as input you have to check the settings.py:

delimiter/quotechar: delimiter as per csv setting/dialect; by defailt ',' and '"'

## Experimental

setting adjust=True will make that the program will try to scale down to width, height

the scaling is rather naive, but you do have the option, if you so wish, results may vary

## Some other settings

there's also a few variables that affect the output independent of inputfile type

output\_delimiter: delimiter of rows; by default '\n'

linebegin/lineend: puts some custom string in front and in the end of each line

ratio\_multiplier: since the ratio between height and width is 1:2 for terminals need to
multiple (by default with 2) so pixel art comes out right. can only be integer


## Requirements

python: ast, sys, numpy, csv, os, PIL

## Display the art

make sure the output file can be executed with: chmod +x outputfile

if that doesn't work you can try adding '#!/bin/bash' in line 1

if you want to display some art when starting your terminal you can for instance add
path/to/outputfile to ~/.bashrc

i also have a script that chooses a random pixel art from /.config/bash_pixel_art that you can find 
under the name random_bash_pixels i put in examples


## Example and Credit

for the example pixel art of Emil from Nier

i copied Emil from user 'jehuty': https://kandipatterns.com/patterns/characters/emil-nier-35822

also i have copied and adjusted some pixel art from here of a chatot: https://www.birdiestitching.com/product/pokemon-chatot-2/

Emil being 25x25 and compiled from csv, while chatot is 20x20 and compiled from png

