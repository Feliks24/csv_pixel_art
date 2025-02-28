## Usage

python csv\_pixel\_art inputfile outputfile

a few variables are set in the settings.py file:

delimiter/quotechar: delimiter as per csv setting/dialect; by defailt ',' and '"'

output\_delimiter: delimiter of rows; by default '\n'

linebegin/lineend: puts some custom string in front and in the end of each line

ratio\_multiplier: since the ratio between height and width is 1:2 for terminals need to
multiple (by default with 2) so pixel art comes out right. can only be integer

will overwrite outputfile


## Requirements

python: ast, sys, numpy, csv, os

## Example and Credit

For the example pixel art of Emil from Nier

I copied it from user 'jehuty': https://kandipatterns.com/patterns/characters/emil-nier-35822



To inspect the picture in the command line make sure the file is executable with chmod +x output

then run ./output; if that doesn't work add '#!/bin/bash' to first line of the file
