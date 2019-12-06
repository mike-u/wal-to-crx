### Project to integrate with Pywal to generate a matching Chrome theme


### Todos:
* Make the script just look at the most recent Chrome Extension directory to modify, or make it able to generate its own theme (better method)
* CLI Chrome theme packing
* Make the script part of Pywal somehow, or run when Pywal runs
* Apply the Chrome theme when Pywal updates
* Choose the Pywal color -> Chrome theme colors conversion, I guessed at one to start testing but it'll probably have to change later

### General notes:
use `wal -i "path/to/img.jpg"` to generate a colorscheme

color profile is then in `"~/.cache/wal/colors.sh"`
* easier way to access is `"~/.cache/wal/colors"`
	* basic text file of 16 hex colors

Need to write a Python script that reads this file and puts it into a manifest.json
* .cache/wal/colors.json is already in json format

Need to decide how to translate colors.json format to chrome themes
* convert hex to RGB, should be easy with Python

colors.json:
	special.background -> theme.colors.ntpbackground
	special.foreground -> theme.colors.frame
	colors.color0 already background
	colors.color1 = theme.colors.button_background
	colors.color2 = theme.colors.ntp_text
	colors.color3 = theme.colors.tab_background_text
	colors.color4 = theme.tab_text
	special.cursor = theme.toolbar

tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
 this will handle converting hex to rgb

button_background needs 4 digits, 1 at the end for transparency
