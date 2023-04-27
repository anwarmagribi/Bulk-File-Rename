import os
from pathlib import Path
from tkinter import *
from tkinter.ttk import Separator
from tkinter.filedialog import askopenfilename, askdirectory

root = Tk()
root.title('Bulk Rename')
root.geometry("")
root.resizable(True, True)


def getDir():
    global directoryName
    directoryName = askdirectory()
    dirName = Label(root, text=directoryName, relief=SUNKEN).grid(column=1,row=1,columnspan=2,padx=(0,10),pady=(0,10))
    root.wm_geometry("")
    # Checks if a directory has been selected and enables the buttons
    if directoryName:
        appendEntry.config(state=NORMAL)
        appendButton.config(state=NORMAL)
        prependEntry.config(state=NORMAL)
        prependButton.config(state=NORMAL)
        removeEntry.config(state=NORMAL)
        remvoeButton.config(state=NORMAL)
        addNumberButton.config(state=NORMAL)
        findEntry.config(state=NORMAL)
        replaceEntry.config(state=NORMAL)
        replaceButton.config(state=NORMAL)
        makeUppercaseButton.config(state=NORMAL)
        makeLowercaseButton.config(state=NORMAL)
        makeTitleButton.config(state=NORMAL)
        showDirectoryButton.config(state=NORMAL)
        '''
        If a directory has already been chosen the 'Open' button
        will move to the bottom and be named 'Open New'
        '''
        getDirectory.grid_forget()
        getDirectory.config(text="Open New")
        getDirectory.grid(row=14, column=0)
            
                   
def append():
    path = Path(directoryName).glob('*')
    text2add = appendEntry.get()  
    for i in path:
        newName = i.name.split(".")[0] + text2add + "." + i.name.split(".")[1]
        newFilePath = i.parent / newName
        os.rename(str(i), str(newFilePath))
        
def prepend():
    path = Path(directoryName).glob('*')
    text2prepend = prependEntry.get()
    for i in path:
        newName = text2prepend + i.name
        newFilePath = i.parent / newName
        os.rename(str(i), str(newFilePath))
            
def remove():
    path = Path(directoryName).glob('*')
    text2remove = removeEntry.get()
    for i in path:
       if text2remove in str(i):
         os.rename(str(i), str(i).replace(text2remove,""))
         
# Function to open a new window that shows the directory of files.        
def openWindow():
    path = Path(directoryName).glob('*')
    newWindow = Toplevel(root)
    newWindow.title("Directory of Files")
    newWindow.resizable(False, False)
    paddingLeft = Label(newWindow, text="").grid(row=0,column=0, padx=20)
    listOfFiles = []
    for i in path:
        listOfFiles.append(str(i.name))
    files = "\n".join(listOfFiles)
    fileDisplay = Label(newWindow, text=files).grid(row=1, column=1)
    paddingRight = Label(newWindow, text="").grid(row=0,column=2, padx=20)   
    
def addNumbers():
    path = Path(directoryName).glob('*')
    num = 1
    for i in path:
        os.rename(str(i), str(i).split('.')[0] + str(num) + f".{str(i).split('.')[1]}")
        num += 1
        
def findAndReplace():
    findText = findEntry.get()
    replaceText = replaceEntry.get()
    path = Path(directoryName).glob('*')
    for i in path:
        if str(findText) in str(i):
            os.rename(str(i), str(i).replace(findText,replaceText))
            
def makeUppercase():
    path = Path(directoryName).glob('*')
    for i in path:
        newName = i.name.split(".")[0].upper() + "." + i.name.split(".")[1]
        newFilePath = i.parent / newName
        os.rename(str(i),str(newFilePath))
        
def makeLowercase():
    path = Path(directoryName).glob('*')
    for i in path:
        newName = i.name.split(".")[0].lower() + "." + i.name.split(".")[1]
        newFilePath = i.parent / newName
        os.rename(str(i),str(newFilePath))
        
def makeTitle():
    path = Path(directoryName).glob('*')
    for i in path:
        newName = newName = i.name.split(".")[0].title() + "." + i.name.split(".")[1]
        newFilePath = i.parent / newName
        os.rename(str(i),str(newFilePath))
        
        
        
separator1 = Separator(root, orient=HORIZONTAL)
separator1.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky='we')
        
chooseDir = Label(root, text="CHOOSE DIRECTORY:",justify=LEFT, anchor="w").grid(sticky=W, column=0,row=1,padx=(20,0))
getDirectory = Button(root, text="Open", command=getDir, width=10)
getDirectory.grid(column=2,row=1,pady=20, padx=(0,50))

#----------------------------------------------------------------------------------------------------------

appendLabel = Label(root, text="APPEND", justify=LEFT, anchor="w").grid(sticky=W, padx=(20, 0), column=0,row=2)

appendEntry = Entry(root, state=DISABLED)
appendEntry.grid(column=1, row=2, columnspan=3, padx=(0,20), pady=(10,10), sticky='w')


appendButton = Button(root, text="Append",state=DISABLED,command=append, width=10)
appendButton.grid(column=2,row=2, padx=(0,50),pady=(0,10))

#----------------------------------------------------------------------------------------------------------

prependLabel = Label(root, text="PREPEND", justify=LEFT, anchor="w").grid(sticky=W, column=0,row=3,pady=20, padx=(20, 0))

prependEntry = Entry(root, state=DISABLED)
prependEntry.grid(column=1,row=3, padx=(0,20), pady=(10,10), sticky='w')

prependButton = Button(root, text="Prepend",state=DISABLED, command=prepend, width=10)
prependButton.grid(column=2,row=3,pady=20,padx=(0,50))

#----------------------------------------------------------------------------------------------------------

removeLabel = Label(root, text="REMOVE", justify=LEFT, anchor="nw").grid(sticky=NW, column=0, row=4,  padx=(20, 0), pady=(10,0))

removeEntry = Entry(root, state=DISABLED)
removeEntry.grid(column=1, row=4, padx=(0,20), pady=(10,30), sticky='w')

remvoeButton = Button(root, text="Remove",state=DISABLED, command=remove, width=10)
remvoeButton.grid(column=2,row=4, pady=(0,10),padx=(0,50))

#----------------------------------------------------------------------------------------------------------

separator3 = Separator(root, orient=HORIZONTAL)
separator3.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky='we')


#----------------------------------------------------------------------------------------------------------

findAndLabel = Label(root, text="FIND",justify=LEFT, anchor="nw").grid(sticky=NW, padx=(20, 0),pady=(10,0), column=0, row=6)
findEntry = Entry(root, state=DISABLED)
findEntry.grid(column=1, row=6, padx=(0,20), sticky='w')

replaceLabel = Label(root, text="REPLACE",justify=LEFT, anchor="w").grid(sticky=W,padx=(20, 0),column=0, row=7)
replaceEntry = Entry(root, state=DISABLED)
replaceEntry.grid(column=1, row=7, padx=(0,20), sticky='w')
replaceButton = Button(root, text="Repalce", state=DISABLED, command=findAndReplace, width=10)
replaceButton.grid(column=2, row=7,padx=(0,50),pady=(0,10))


separator2 = Separator(root, orient=HORIZONTAL)
separator2.grid(row=8, column=0, columnspan=3, padx=20, pady=10, sticky='we')


addNumber = Label(root, text="ADD NUMBER", anchor='w').grid(sticky=W, column=0,row=9, padx=(20, 0))
addNumberExample = Label(root, text="eg: myfile1, myfile2, myfile3", font=("Segoe UI",8),anchor='w')
addNumberExample.grid(column=1, row=9, padx=(0, 20), sticky=W)

addNumberButton = Button(root, text="Apply",state=DISABLED, command=addNumbers, width=10)
addNumberButton.grid(column=2,row=9,padx=(0,50),pady=(0,10))

#----------------------------------------------------------------------------------------------------------

makeCapital = Label(root, text="CAPITALIZE", anchor='w').grid(sticky=W, column=0,row=10,padx=(20,0))
makeUppercaseExample = Label(root, text="program.txt --> PROGRAM.txt", font=("Segoe UI",8),anchor='w')
makeUppercaseExample.grid(column=1, row=10, padx=(0, 20), sticky=W)
makeUppercaseButton = Button(root, text="Apply",state=DISABLED, command=makeUppercase, width=10)
makeUppercaseButton.grid(column=2, row=10, padx=(0,50),pady=(0,10))

#----------------------------------------------------------------------------------------------------------

makeLower = Label(root, text="LOWERCASE", anchor='w').grid(sticky=W, column=0,row=11,padx=(20,0))
makeLowercaseExample = Label(root, text="PROGRAM.txt --> program.txt", font=("Segoe UI",8),anchor='w')
makeLowercaseExample.grid(column=1, row=11, padx=(0, 20), sticky=W)

makeLowercaseButton = Button(root, text="Apply",state=DISABLED, command=makeLowercase, width=10)
makeLowercaseButton.grid(column=2, row=11, padx=(0,50),pady=(0,10))

#----------------------------------------------------------------------------------------------------------

titlelze = Label(root, text="MAKE TITLE", anchor='w').grid(sticky=W,column=0,row=12,padx=(20,0))
makeTitleExample = Label(root, text="file1.txt --> File1.txt", anchor='w')
makeTitleExample.grid(column=1, row=12, padx=(0, 20), sticky=W)

makeTitleButton = Button(root, text="Apply",state=DISABLED, command=makeTitle, width=10)
makeTitleButton.grid(row=12, column=2, padx=(0,50), pady=(0,10))

separator4 = Separator(root, orient=HORIZONTAL)
separator4.grid(row=13, column=0, columnspan=3, padx=20, pady=10, sticky='we')

showDirectoryButton = Button(root, text="Show Changes",state=DISABLED,command=openWindow, width=10)
showDirectoryButton.grid(row=14, column=2, pady=20,padx=(0,50))

root.mainloop()
