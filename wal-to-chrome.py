import json

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

# def pass_to_json(json_arr,in_name,in_val):
# 	json_arr.append("\""+in_name+"\": ")	#name
# 	json_arr.append("["+str(in_val[0])+",")	#R
# 	json_arr.append(" "+ str(in_val[1])+",")	#G
# 	json_arr.append(" "+ str(in_val[2]))	#B
# 	if in_name == "button_background":
# 		json_arr.append(", 1")	#transparency
# 	json_arr.append("],\n")
# 	return json_arr

waltocrx = {'special.background': 'theme.colors.ntpbackground',
	'special.foreground': 'theme.colors.frame',
	'colors.color1': 'theme.colors.button_background',
	'colors.color2': 'theme.colors.ntp_text',
	'colors.color3': 'theme.colors.tab_background_text',
	'colors.color4': 'theme.colors.tab_text',
	'special.cursor': 'theme.colors.toolbar'}

with open(walfile, "r") as read_file:
	data = json.load(read_file)

with open(dest_file, "r") as read_file:
	data2 = json.load(read_file)

# do this in a loop
with open(dest_file, 'r+') as f:
	data2 = json.load(f)
	for key in waltocrx:
		hexcolor = data[key.split('.')[0]][key.split('.')[1]]
		rgbcolor = hex_to_rgb(hexcolor)
		rgbcolor = list(rgbcolor)
		data2[waltocrx[key].split('.')[0]][waltocrx[key].split('.')[1]][waltocrx[key].split('.')[2]] = rgbcolor		# f.seek(0)        # <--- should reset file position to the beginning.
		json.dump(data, f, indent=4)
		f.truncate()     # remove remaining part

# for key in waltocrx:
# 	hexcolor = data[key.split('.')[0]][key.split('.')[1]]
# 	# hexcolor = data["special"]["background"]
# 	rgbcolor = hex_to_rgb(hexcolor)
# 	rgbcolor = list(rgbcolor)
# 	data2[waltocrx[key].split('.')[0]][waltocrx[key].split('.')[1]][waltocrx[key].split('.')[2]] = rgbcolor
# 	# data2["theme"]["colors"]["ntp_background"] = rgbcolor

# with open(dest_file, "w") as jsonFile:
#     json.dump(data2, jsonFile)

#manifest.json should be updated now, proceed as normal packing .crx
# this can be done from CLI as well, additional feature
