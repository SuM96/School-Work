from tkinter import *
import tkinter.simpledialog

'''
This class takes in a title and a summary. 
Private variables don't exist in python
Accessor: memo.title
Mutator: momo.title = "Something"
'''
class Notepad:
    def __init__(self, name, summary = "", font = "Arial", fontSize = 14):
        self.name = name
        self.summary = summary
        self.font = font
        self.fontSize = fontSize

class NotepadGUI:
    def __init__(self, notepad):
        self.notepad = notepad

    def manageInfo(self, state = 0):
        self.memo_window = Tk()
        self.memo_window.geometry("400x400")
        self.memo_window.title(self.notepad.name)
        
        self.nameTitleLabel = Label(self.memo_window, text = self.notepad.name, font = (self.notepad.font, self.notepad.fontSize))
        self.nameTitleLabel.place(x = 20, y = 5)

        #Add Scroll bar if I have time 
        fixedHeight = IntVar()
        fixedWidth = IntVar()
        # Arial and Large
        if(self.notepad.font == "Arial" and self.notepad.fontSize == 16):
            fixedHeight.set(13)
            fixedWidth.set(29)
        elif(self.notepad.font == "Times New Roman" and self.notepad.fontSize == 14):
            fixedHeight.set(14)
            fixedWidth.set(39)
        elif(self.notepad.font == "Times New Roman" and self.notepad.fontSize == 16):
            fixedHeight.set(13)
            fixedWidth.set(33)
        # Default: Arial and Small
        #else:
        #    fixedHeight.set(14)
        #    fixedWidth.set(32)
        # Text height and text width is determined by the characters. Not the pixels
        self.summaryText = Text(self.memo_window, height = fixedHeight.get(), width = fixedWidth.get(), wrap = WORD, font = (self.notepad.font, self.notepad.fontSize))
        # state 0 is the default state. In this state, it will just show the text without anyway to do anything
        if(state == 0):
            self.displayText()
        # state 1 will let you edit the text
        elif(state == 1):
            self.editText()
        self.summaryText.place(x = 20, y = 40)

    def displayText(self):
        # Make the code to be able to be programmed in
        self.summaryText.config(state = NORMAL)
        # Delete Everything from the textbox
        self.summaryText.delete(1.0, END)
        # Insert the text
        self.summaryText.insert(INSERT, self.notepad.summary)
        # This function will disable the ability to write text into the file
        self.summaryText.config(state = DISABLED)
        self.quitButton = Button(self.memo_window, text = "Quit", command = self.memo_window.destroy)
        self.quitButton.place(x = 350, y = 360)

    def editText(self):
        self.summaryText.config(state = NORMAL)
        self.summaryText.delete(1.0)
        self.summaryText.insert(INSERT, self.notepad.summary)
        self.saveButton = Button(self.memo_window, text = "Save", command = self.setText)
        self.saveButton.place(x = 300, y = 360)
        self.quitButton = Button(self.memo_window, text = "Quit", command = self.memo_window.destroy)
        self.quitButton.place(x = 350, y = 360)

    def setText(self):
        self.notepad.summary = self.summaryText.get(1.0, END)
        self.memo_window.destroy()

class Memos:
    def __init__(self):
        self.notepadList1 = list()
        self.main_window = Tk()
        self.main_window.title("Memos")
        self.main_window.geometry("300x300")

        self.titleFrame = Frame(self.main_window, height = 50, width = 300)
        self.titleFrame.place(x = 0, y = 0)
        self.titleLabel = Label(self.titleFrame, text = "Memo Read/Write", font = ("Times New Roman", 26))
        self.titleLabel.place(x = 12, y = 0)

        self.customizeFrame = Frame(self.main_window, height = 50, width = 300)
        self.customizeFrame.place(x = 0, y = 50)
        self.rbFont = StringVar()
        self.rbFont.set("Arial")
        self.rbFontSize = IntVar()
        self.rbFont.set(14)
        # Radio buttons need commands
        self.rbArial = Radiobutton(self.customizeFrame, text = "Arial", variable = self.rbFont, value = "Arial")
        self.rbArial.place(x = 10, y = 0)
        self.rbTNR = Radiobutton(self.customizeFrame, text = "Times New Roman", variable = self.rbFont, value = "Times New Roman")
        self.rbTNR.place(x = 10, y = 25)
        self.rbFontSmall = Radiobutton(self.customizeFrame, text = "Small", variable = self.rbFontSize, value = 14)
        self.rbFontSmall.place(x = 150, y = 0)
        self.rbFontLarge = Radiobutton(self.customizeFrame, text = "Large", variable = self.rbFontSize, value = 16)
        self.rbFontLarge.place(x = 150, y = 25)

        self.buttonFrame = Frame(self.main_window, height = 200, width = 100)
        self.buttonFrame.place(x = 200, y = 100)
        self.buttonRead = Button(self.buttonFrame, text = "Read", compound = CENTER, width = 7, command = self.read)
        self.buttonRead.place(x = 20, y = 10)
        # Remember to add something for New
        self.buttonNew = Button(self.buttonFrame, text = "New", compound = CENTER, width = 7, command = self.new)
        self.buttonNew.place(x = 20, y = 45)
        self.buttonEdit = Button(self.buttonFrame, text = "Edit", compound = CENTER, width = 7, command = self.edit)
        self.buttonEdit.place(x = 20, y = 80)
        self.buttonDelete = Button(self.buttonFrame, text = "Delete", compound = CENTER, width = 7, command = self.delete)
        self.buttonDelete.place(x = 20, y = 115)
        self.buttonQuit = Button(self.buttonFrame, text = "Quit", compound = CENTER, width = 7, command = self.main_window.destroy)
        self.buttonQuit.place(x = 20, y = 150)

        self.listboxFrame = Frame(self.main_window, width = 200, height = 200)
        self.listboxFrame.place(x = 0, y = 100)
        self.lbEntry1 = Listbox(self.listboxFrame, width = 29, height = 11, selectmode = SINGLE)
        self.lbEntry1.place(x = 10, y = 10)

        self.main_window.mainloop()
    
    def new(self):
        newTitle = tkinter.simpledialog.askstring("New Title", "Please enter a title") 
        newNotepad = NotepadGUI(Notepad(newTitle, "", self.rbFont.get(), self.rbFontSize.get()))
        newNotepad.manageInfo(1)
        self.notepadList1.append(newNotepad)
        self.lbEntry1.insert(END, newTitle)
        
    def read(self):
        self.notepadList1[self.lbEntry1.curselection()[0]].manageInfo()

    def edit(self):
        self.notepadList1[self.lbEntry1.curselection()[0]].manageInfo(1)

    def delete(self):
        self.notepadList1.pop(self.lbEntry1.curselection()[0])
        self.lbEntry1.delete(self.lbEntry1.curselection()[0])

Memos()
