# jsig
Create static picture gallery web page from image folder.
Requires imagemagick.

Example use:
python jsig.py -p -y 10 -v -f gallery.html -t thumbs -u pics

This will create a stand alone web page called gallery.html that has thumbnail image links to pictures residing in folder called "pics" in your URL. Thumbnails will be 64 pixels high and read from "pics/thumbs" in the URL.

Full size pictures are read from current working directory and thumbnail folder has to reside there also.

Better documentation coming later.

For now, see: jsig.py --help
