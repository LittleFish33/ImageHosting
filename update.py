import os
import datetime
# if is's a image
def isImage(str,list):
	# all the format of the image that the markdown support
	postfixs = [".jpg",".bmp",".png",".gif",".JPG",".BMP",".PNG",".GIF",".JPEG",".jpeg",".jpng",".JPNG",".svg",".SVG",".TIFF",".tiff",".webp",".WEBP"]
	for postfix in postfixs:
		if(str.endswith(postfix)):
			list.append(str)
			return;
	return


os.system("git add *")
os.system("git status")
f = os.popen("git status")
mystr = f.read() # get the string output
f.close()
os.system("git commit -m \"update" + datetime.datetime.now().strftime('%Y-%m-%d') + "\"")
os.system("git pull")
os.system("git push origin master")
strArr = mystr.split()
list = []
for str in strArr:
	isImage(str,list)
prefix = "https://raw.githubusercontent.com/LittleFish33/ImageHosting/master/"
for image in list:
	print prefix + image
if(len(list) == 1):
	os.system("echo" + prefix + list[0] +  "|clip")
str = input("input anything to continue")