#! /usr/bin/python

#MemeMonster

from tkinter import Tk, Label, Button, filedialog, simpledialog, Entry
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


# gui class

class memeMonsterGUI:
    def __init__(self, master):
    
       
        self.master = master
        master.title("memeMonster")
        
        
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        
        # adjust dimensions to middle of screen and make room for box
        
        xLocation = screenWidth / 2 - 245
        yLocation = screenHeight / 2 - 95    
        
        # have to convert to int because geometry doesn't like floats
        
        xLocation = int(xLocation)
        yLocation = int(yLocation)
        
        # specify geometry, must make coords a string normally looks like "490x190+220+200"
        
        root.geometry("600x240+"+str(xLocation)+"+"+str(yLocation))        

        # using grid rather than pack to set buttons in correct spot

		# image width dialogue

        self.label = Label(master, text="Max Image Width:  ")        
        self.label.grid(column=0,row=0)
        
        self.imageWidth = Entry(master)
        self.imageWidth.grid(column=1,row=0)

        self.label = Label(master, text="(pixels)")        
        self.label.grid(column=2,row=0)

        self.pixelSize = Label(master, text="Your Pixel Size:  ")
        self.pixelSize.grid(column=0,row=1)       

		# top words dialogue

        self.label = Label(master, text="Input Top Meme Words:  ")        
        self.label.grid(column=0,row=2)

        self.label = Label(master, text="(11 char max)")        
        self.label.grid(column=2,row=2)
        
        self.memeWordsTop = Entry(master)
        self.memeWordsTop.grid(column=1,row=2)

        self.memeWordsTopShow = Label(master, text="Your Top Meme Words:  ")
        self.memeWordsTopShow.grid(column=0,row=3)

		# bottom words dialogue

        self.label = Label(master, text="Input Bottom Meme Words:  ")        
        self.label.grid(column=0,row=4)

        self.label = Label(master, text="(11 char max)")        
        self.label.grid(column=2,row=4)
        
        self.memeWordsBottom = Entry(master)
        self.memeWordsBottom.grid(column=1,row=4)

        self.memeWordsShowBottom = Label(master, text="Your Bottom Meme Words:  ")
        self.memeWordsShowBottom.grid(column=0,row=5)

       	# directory selection
        
        self.path1 = Label(master, text="Your Chosen Directory:  ")
        self.path1.grid(column=0,row=6)    
        
        self.pathLookup_button = Button(master, text="Select Directory", command=self.pathLookup)
        self.pathLookup_button.grid(column=1,row=8)

        self.buffer1 = Label(master, text="       ") 
        self.buffer1.grid(column=0,row=7)


        self.buffer2 = Label(master, text="       ")
        self.buffer2.grid(column=0,row=8)   
       
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(column=6,row=9)
        
        self.processDir = Button(master, text="Process Folder", command= self.doWork)
        self.processDir.grid(column=0, row=9)
        

       
    def pathLookup(self):
        global folderpath
        folderpath = filedialog.askdirectory()
        #print(str(folderpath)) 
        
        # give us some dots if it's too long and truncate
        folderpathString = folderpath

        if (len(folderpathString) > 37):
            folderpathString = folderpathString[:36] + "..."
            
        else:
            folderpathString = folderpath

        memeTextTop = self.memeWordsTop.get()
        memeTextBottom = self.memeWordsBottom.get()

        pixels = self.imageWidth.get()

        self.pathLabel = Label(self.master, text=pixels,width=40,anchor='center')
        self.pathLabel.grid(column=1,row=1)

        self.pathLabel = Label(self.master, text=memeTextTop,width=40,anchor='center')
        self.pathLabel.grid(column=1,row=3)     
       
        self.pathLabel = Label(self.master, text=memeTextBottom,width=40,anchor='center')
        self.pathLabel.grid(column=1,row=5)            

  
        self.memeWordsShowLabel = Label(self.master, text=folderpathString,anchor='w')
        self.memeWordsShowLabel.grid(column=1,row=6)                
        

        return folderpath

        
        
    def completed(self,pixels):
        self.buffer3 = Label(self.master, text= "memeFiles Dir Created",anchor='w')
        self.buffer3.grid(column=1,row=10)             
        
    def doWork(self):
        
        # get pixel data
        pixels = self.imageWidth.get()

        # get meme text
        memeTextTop = self.memeWordsTop.get()
        memeTextBottom = self.memeWordsBottom.get()

        # change dir
        os.chdir(folderpath)
        # process functions
        pixelSize(pixels)
        makeDir(pixels)
        processPics(pixels,memeTextTop, memeTextBottom)
        self.completed(pixels)
        self.completeLabel = Label(self.master, text="Images are located in the memeFiles directory.",anchor='w')
        self.completeLabel.grid(column=1,row=9)    
     
           
        



def pixelSize(pixels):

    print("Your images are processed and are located in the memeFiles directory.")

def makeDir(pixels):
    if os.path.exists( "memeFiles"):
        pass
    else:
       os.mkdir(( "memeFiles"))



def processPics(pixels, memeTextTop, memeTextBottom):
    for file in os.listdir('.'):

        #this function creates the images and tosses them in the folder    
        def imageProcess():
            image = Image.open(file)
            filename, file_extension = os.path.splitext(file)
            # have to make a tuple out of pixels because of PIL requirements
            listSize = [int(pixels),int(pixels)]
            imageSize = tuple(listSize)
            image.thumbnail(imageSize)

            # need to calculate number of pixels to the right of center of text and subtract that from full pixel size

			# figure out text size and turn into an int (can't do partial pixels)
            textSize = int(pixels) * .15
            textSize = int(textSize)
            textPixel = textSize * 1.21
            textPixel = int(textPixel)
            # calc y location - center the center point of the text 
            yLoc = (int(pixels) - (int((textPixel) * len(memeTextTop)/2)))/2
            


            # calc xLoc for top
            xLoc = int(pixels) - (int(pixels)-10)

            print("top loc = ",xLoc)

            # font = ImageFont.truetype(<font-file>, <font-size>)

            font1 = ImageFont.truetype("../Hack-Bold.ttf", textSize)
            font2 = ImageFont.truetype("../Hack-Bold.ttf", textSize)
            # draw.text((x, y),"Sample Text",(r,g,b))
            draw = ImageDraw.Draw(image)


            
            #black border - must write the characters with pixel offsets to get boarder properly
            draw.text((yLoc+3, xLoc),memeTextTop,(0,0,0),font=font2)
            draw.text((yLoc, xLoc+3),memeTextTop,(0,0,0),font=font2)
            draw.text((yLoc, xLoc-3),memeTextTop,(0,0,0),font=font2)
            draw.text((yLoc-3, xLoc),memeTextTop,(0,0,0),font=font2)


            # white text
            draw.text((yLoc, xLoc),memeTextTop,(255,255,255),font=font1)


			# bottom text

            # calc y location - center the center point of the text 
            yLoc = (int(pixels) - (int((textPixel) * len(memeTextBottom)/2)))/2
            
            # calc xLoc for bottom
            xLoc = int(pixels) - (10 + textSize)
			
            print("bottom loc = ",xLoc)

            # font = ImageFont.truetype(<font-file>, <font-size>)

            font1 = ImageFont.truetype("../Hack-Bold.ttf", textSize)
            font2 = ImageFont.truetype("../Hack-Bold.ttf", textSize)
            # draw.text((x, y),"Sample Text",(r,g,b))
            draw = ImageDraw.Draw(image)


            
            #black border - must write the characters with pixel offsets to get boarder properly
            draw.text((yLoc+3, xLoc),memeTextBottom,(0,0,0),font=font2)
            draw.text((yLoc, xLoc+3),memeTextBottom,(0,0,0),font=font2)
            draw.text((yLoc, xLoc-3),memeTextBottom,(0,0,0),font=font2)
            draw.text((yLoc-3, xLoc),memeTextBottom,(0,0,0),font=font2)


            # white text
            draw.text((yLoc, xLoc),memeTextBottom,(255,255,255),font=font1)


            image.save( 'memeFiles/{}_{}{}'.format(filename, pixels, file_extension))


        #do it only for image file types
        if file.endswith('.jpg'):
            imageProcess()
 
        elif file.endswith('.jpeg'):
            imageProcess()

        elif file.endswith('.png'):
            imageProcess()

    

# display gui and loop it    
if __name__ == "__main__":        
    root = Tk()
    my_gui = memeMonsterGUI(root)
    root.mainloop() 
