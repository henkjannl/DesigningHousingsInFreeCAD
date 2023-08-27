import os
from datetime import datetime
from shutil import copyfile
from PIL import Image

"""
This script:
- retrieves directory data
- filters and sorts files
- formats the output
- puts the result on the clipboard so it can be pasted in a spreadsheet

Useful links:
https://docs.python.org/3/library/os.html#os.stat_result
https://docs.python.org/3/library/os.html#os.DirEntry

To do:
- created, modified, accessed not always makes sense (e.g. accessed 
  older than created)
"""


# STEP 1: Where to start the search
START_LOCATION = os.getcwd()
#START_LOCATION = "C:\\Users\\henkj\\OneDrive\\Documents\\eclipse"
#START_LOCATION = "C:\\"
#START_LOCATION = "C:\\Users\\henkj\\Dropbox\\Foto's\\2019\\Vakantie Balkan, RAW en filmpjes"

# STEP 2: Filter the files that were found
def Requirement(direntry):
	#return True
	#return ('arduino' in direntry.name.lower()) and direntry.name.lower().endswith('svg')
	#return direntry.name.lower().endswith('arw') or \
	#	   direntry.name.lower().endswith('jpg') or \
	#	   direntry.name.lower().endswith('mp4') 
	return direntry.name.lower().endswith('png')
	#return ('linux' in direntry.name.lower()) and direntry.name.lower().endswith('fb.h')
	#return 'stratasys' in direntry.name.lower()


# STEP 3: Sort the files in a certain order
SORT = 'path'
#SORT = 'date'
SORT_REVERSE = False


# STEP 4: Define which COLUMNS in the report, in what order
#COLUMNS = ['name', 'path', 'size', 'created', 'modified', 'accessed', 'width', 'height']
COLUMNS = ['name', 'path', 'width', 'height']

# Fields to choose from in the COLUMNS (can be extended)
TAGS = { 
	'Name': 	 lambda de: de.name,
	'Path': 	 lambda de: de.path,
	'Size':		 lambda de: '%d' % de.stat().st_size,
	'Created':	 lambda de: datetime.fromtimestamp(de.stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
	'Modified':	 lambda de: datetime.fromtimestamp(de.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'), 
	'Accessed':	 lambda de: datetime.fromtimestamp(de.stat().st_atime).strftime('%Y-%m-%d %H:%M:%S'),
	'Width':     lambda de: f'{Image.open(de.path).size[0]}',
	'Height':    lambda de: f'{Image.open(de.path).size[1]}',
}


# Recursive function that scans the disk and add relevant files to the 
# selection
def AddToSelection(baseDir, selection, requirement):

	try:
		files = os.scandir(baseDir)
		
		for de in files:
			
			if requirement(de):
				selection.append(de)
				
			if de.is_dir(follow_symlinks=False):
				AddToSelection(de.path, selection, requirement)
	except:
		pass


# Retrieve files
selection = []
AddToSelection(START_LOCATION, selection, Requirement)

# Sort the files
if SORT.lower()=='name':
	selection.sort( key= lambda de: de.name )
elif SORT.lower()=='path':
	selection.sort( key= lambda de: de.path )
elif SORT.lower()=='date':
	selection.sort( key= lambda de: de.stat().st_ctime )
elif SORT.lower()=='size':
	selection.sort( key= lambda de: de.stat().st_size )

if SORT_REVERSE:
	selection = list(reversed(selection))


# Prepare the headers
results=''
for i,k in enumerate(COLUMNS):

	for l in TAGS.keys():

		if k.strip().upper() == l.strip().upper():
			results+=l+'\t'

			# Correct spelling mistakes in COLUMNS list
			COLUMNS[i]=l 
results+='\n'

# Export file results
lines=[]
for i,de in enumerate(selection):
		
	lines.append('\t'.join( [TAGS[k](de) for k in COLUMNS]))
	
	# Only print the first 20 lines
	if i<20: print(de.name)

	
if len(selection)>=20:
	print(':')

results+='\n'.join(lines)
	
print('\nTotal of {cnt:d} files'.format(cnt=len(selection)))

import pyperclip
pyperclip.copy(results)