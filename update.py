import os

# if is's a image
def isImage(str,list):
	# all the format of the image that the markdown support
	postfixs = [".jpg",".bmp",".png",".gif",".JPG",".BMP",".PNG",".GIF",".JPEG",".jpeg",".jpng",".JPNG",".svg",".SVG",".TIFF",".tiff",".webp",".WEBP"]
	for postfix in postfixs:
		if(str.endswith(postfix)):
			list.append(str)
			return;
	return

os.popen("git add *")
mystr = os.popen("git status")
str = os.popen("git commit -m \"update\"")
print (str)
str = os.popen("git pull")
print (str)
str = os.popen("git push origin master")
print (str)
mystr = mystr.read() # get the string output
strArr = mystr.split()
list = []
for str in strArr:
	isImage(str,list)
prefix = "https://raw.githubusercontent.com/LittleFish33/ImageHosting/master/"
for image in list:
	print prefix + image