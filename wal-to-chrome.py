import json, os

waldir = "~/.cache/wal/"
dest_file = "manifest.json"
walfile = "colors.json"
new_colors=[]

def hex_to_rgb(hexin):
	hexin = hexin.lstrip("#")
	rgb_out = tuple(int(hexin[i:i+2], 16) for i in (0, 2, 4))
	#rgb_out is like (255, 255, 255)
	# need to convert it to something like [255, 255, 255]
	return rgb_out

waltocrx = {'special.background': 'theme.colors.ntpbackground',
	'special.foreground': 'theme.colors.frame',
	'colors.color1': 'theme.colors.button_background',
	'colors.color2': 'theme.colors.ntp_text',
	'colors.color3': 'theme.colors.tab_background_text',
	'colors.color4': 'theme.colors.tab_text',
	'special.cursor': 'theme.colors.toolbar'}

# read wal's colors
with open(walfile, "r") as read_file:
	wal_colors = json.load(read_file)
	
# read manifest's colors
with open(dest_file, "r") as read_file:
	chrome_colors = json.load(read_file)

#loop through each key, read wal's color, and put it in manifest's json
with open(dest_file, 'r+') as f:
	chrome_colors = json.load(f)
	for key in waltocrx:
		hexcolor = wal_colors[key.split('.')[0]][key.split('.')[1]]
		rgbcolor = hex_to_rgb(hexcolor)
		rgbcolor = list(rgbcolor)
		chrome_colors[waltocrx[key].split('.')[0]][waltocrx[key].split('.')[1]][waltocrx[key].split('.')[2]] = rgbcolor		# f.seek(0)        # <--- should reset file position to the beginning.

os.remove(dest_file)	#need to overwrite it, might be better ways
with open(dest_file, "w+") as f:	
	json.dump(chrome_colors, f, indent=None)
	f.truncate()     # remove remaining part

#manifest.json should be updated now, proceed as normal packing .crx
# this can be done from CLI as well, additional feature
