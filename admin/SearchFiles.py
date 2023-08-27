import os
from datetime import datetime
import time

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

# Definition of constants representing the column names
NAME      = 'Name'           # Filename
DEEP_NAME = 'Indented name'  # Filename, preceded by spaces based on the depth of the directory
PATH      = 'Path'           # Path
REL_PATH  = 'Relative path'  # Path relative to the search path
SIZE      = 'Size'           # Filesize
CREATED   = 'Created'        # Create date
MODIFIED  = 'Modified'       # Last modified
ACCESSED  = 'Accessed'       # Last accessed
IS_DIR    = 'Is directory'   # Is this a file or a directory


# STEP 1: Where to start the search
#START_LOCATION = os.getcwd()
START_LOCATION = r'C:\Users\henkj\IOT\DesigningHousingsInFreeCAD'
#START_LOCATION = r'C:\Users\hjvanderpol\OneDrive\03 HenkJan\18 FreeCad'
#START_LOCATION = r'C:\Users\hjvanderpol\OneDrive\03 HenkJan\18 FreeCad\Bruidstaart Iris en Abbout'
#START_LOCATION = r'C:\Users\hjvanderpol'
#START_LOCATION = r'C:\Users\hjvanderpol\OneDrive - Bond3D'
#START_LOCATION = r'C:\Users\hjvanderpol\OneDrive - Bond3D\Pictures'
#START_LOCATION = r'F:\\'
#START_LOCATION = r'C:\Windows'
#START_LOCATION = r'F:\Patents'
#START_LOCATION = r'S:\#8062'
#START_LOCATION = r'C:\Users\hjvanderpol\OneDrive\03HenkJan\18 FreeCad'
#START_LOCATION = r'C:\Users\hjvanderpol\AppData\Local\Arduino15'

# STEP 2: How deep do we want the search to be?
#MAX_DEPTH = 1
MAX_DEPTH = 999

# STEP 3: Filter the files that were found
def Requirement(direntry):
	#return True
	return direntry.name.lower().endswith('md')
	#return ('ultimaker' in direntry.name)
	#return direntry.is_dir(follow_symlinks=False)
	#return not(direntry.is_dir(follow_symlinks=False))
	#return ('fast' in direntry.path.lower() or 'mould' in direntry.path.lower()) and direntry.name.lower().endswith('docx') 
	#return direntry.name.lower().startswith('d')  and direntry.name.lower().endswith('pdf') 
	#return 'test' in direntry.path.lower() and direntry.name.lower().endswith('pptx') 
	#return direntry.name.lower().endswith('step')
	#return direntry.name.lower().endswith('stl')
	#return direntry.name.lower().endswith('pdf')
	#return direntry.name.lower().endswith('gcode')
	#return direntry.name.lower().endswith('dotx')
	#return direntry.name.lower().endswith('svg')
	#return direntry.name.lower().endswith('pptx')
	#return 'eps' in direntry.path.lower() and direntry.name.lower().endswith('docx')
	#return 'printing material for' in direntry.path.lower() and direntry.name.lower().endswith('pdf')
	#return 'bump' in direntry.path.lower() and direntry.name.lower().endswith('svg')
	#return direntry.name.lower().endswith('fcstd')
	#return 'benchy' in direntry.name.lower()
	#return 'model' in direntry.path.lower() and direntry.name.lower().endswith('svg')
	#return 'coor' in direntry.path.lower() and direntry.name.lower().endswith('svg')
	#return '' in direntry.name.lower() and direntry.name.lower().endswith('svg') and datetime.fromtimestamp(direntry.stat().st_ctime).strftime('%Y-%m') in ('2019-03', '2019-04')
	#return direntry.name.lower().endswith('xlsx') and datetime.fromtimestamp(direntry.stat().st_ctime).strftime('%Y') in ('2020')
	#return 'astm' in direntry.name.lower()


# STEP 4: Sort the files in a certain order
SORT = PATH
#SORT = MODIFIED
#SORT_REVERSE = True
SORT_REVERSE = False


# STEP 5: Define which COLUMNS in the report, in what order
#COLUMNS = [NAME, PATH, SIZE, CREATED, MODIFIED, ACCESSED]
#COLUMNS = [IS_DIR,DEEP_NAME, PATH]
COLUMNS = [PATH]
#COLUMNS = [NAME, PATH]
#COLUMNS = [NAME]
#COLUMNS = [REL_PATH, MODIFIED, SIZE]

# Fields to choose from in the COLUMNS (can be extended)
TAGS = { 
	NAME:      lambda de: de.name,
	DEEP_NAME: lambda de: '  '*(len(de.path[len(START_LOCATION)+1:].split('\\'))-1)+de.name,
	PATH:      lambda de: de.path,
	REL_PATH:  lambda de: de.path[len(START_LOCATION)+1:],
	SIZE:      lambda de: '%d' % de.stat().st_size,
	CREATED:   lambda de: datetime.fromtimestamp(de.stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
	MODIFIED:  lambda de: datetime.fromtimestamp(de.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'), 
	ACCESSED:  lambda de: datetime.fromtimestamp(de.stat().st_atime).strftime('%Y-%m-%d %H:%M:%S'),
	IS_DIR:    lambda de: {False:'File', True: 'Directory'}[de.is_dir()]
}

# Recursive function that scans the disk and add relevant files to the selection
def AddToSelection(baseDir, selection, requirement, level):
	#print('{level}) {path}'.format(level=level, path=baseDir))
	files = os.scandir(baseDir)
	for de in files:
		if requirement(de):
			selection.append(de)
		if de.is_dir(follow_symlinks=False) and level<MAX_DEPTH:
			AddToSelection(de.path, selection, requirement, level+1)

# PREPS DONE. THE ACTUAL PROGRAM STARTS HERE
# Retrieve files
selection = []
AddToSelection(START_LOCATION, selection, Requirement, level=0)

# Sort the files
selection.sort(key= TAGS[SORT], reverse=SORT_REVERSE)

# Print the first couple of filenames
print('\n'.join([de.name for de in selection[:8]]))
if len(selection)>8: print('...')

# Export file results
try:
	results='\n'.join(['\t'.join(COLUMNS)]+['\t'.join([TAGS[k](de) for k in COLUMNS]) for de in selection])
except:
	print(selection)

# Copy to clipboard		
import pyperclip
pyperclip.copy(results)
print('Results of {num:d} files copied to clipboard'.format(num=len(selection)))
