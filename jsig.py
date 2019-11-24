#!/usr/bin/python

# TODO:
# - choose between static thumbnail height or width, currently only static height is supported
# - check if imagemagick is not available
# - ask original picture folder name for URL
# - create thumbnail folder if needed
# - add missing slashes to folder name and remove duplicates
# - user defined css for html elements
# - make some parameters required in argparse / show help if missing

# FIXME:
# - Ctrl-C cancels external convert program but not this script

import os
import argparse

def create_thumbnail():
	command = "convert -auto-orient -strip -quality " + quality + " -resize x" + args.height + " " + filename + " " + args.thumbdir + "/" + filename
	if args.verbose:
		print (command)
	os.system(command)

programName = "JSIG - JaPeK's static image gallery"
programVersion = "0.035"

# Read command line parameters:
parser = argparse.ArgumentParser(description = programName + " " + programVersion)
parser.add_argument('-a', '--append', action='store_true', help='do not recreate / overwrite old thumbnails')
parser.add_argument('-p', '--htmlpage', action='store_true', help='make full stand alone html page instead of includeable snippet')
parser.add_argument('-t', '--thumbdir', help='folder to save thumbnails')
parser.add_argument('-f', '--htmlfile', help='file to save html code')
parser.add_argument('-u', '--urlpath', help='optional path for image folder in URL')
parser.add_argument('-y', '--height', help='y resolution for thumbnails')
parser.add_argument('-v', '--verbose', action='store_true', help='show progress during execution')

args = parser.parse_args()

html = ""

if args.htmlpage:
	html = "<html>\n"

html += "<div class=\"bordered\" style=\"text-align: center;\">\n"

quality = "100"

url_path = ""

if args.urlpath != None:
	url_path = args.urlpath + "/"

if args.htmlfile != None and args.thumbdir == None:
	print("ERROR: Thumbnail directory not defined.")
	quit()

if args.height == None:
	print("ERROR: Height for thumbnails not defined.")
	quit()

for filename in os.listdir("."):
	if filename.lower().endswith(".png") or filename.lower().endswith(".jpg"):
		if args.thumbdir != None:
			if os.path.exists(args.thumbdir + "/" + filename):
				if not args.append:
					create_thumbnail()
				elif args.verbose:
					print ("Preserving old thumbnail: " + filename)
			else:
				create_thumbnail()
		if args.htmlfile != None:
			html += "<a href=\"" + url_path + filename + "\"><img src=\"" + url_path + args.thumbdir + "/" + filename + "\"></a>\n"

html += "</div>\n"

if args.htmlpage:
	html += "</html>"

if args.htmlfile != None:
	file_htm = open(args.htmlfile, "w")
	file_htm.write(html)
	file_htm.close()
	if args.verbose:
		print ("Saved HTML file: " + args.htmlfile)
