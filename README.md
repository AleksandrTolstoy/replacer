# replacer-CLI-utility
CLI program to replace text in files

With its help, you can do something similar to this.
It is useful to use if you need to replace some template text in large files

# Example
~ command
python3 replacer.py -o Ukraine -n SOLO --file test_data1 --insertion CONGO

~ input file
Ukraine sjdnfhj kwjbr wfb rrr SOLO jdfn Ukraine kwdnfkne SOLO
apple Ukraine samsung
google week
sample dictUkraine
nskjnjf wnns sdd SOLO

~ output file 
UkraineCONGOSOLO jdfn UkraineCONGOSOLO
apple UkraineCONGOSOLO
