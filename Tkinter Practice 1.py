#imports from the tkinter library, and because it's *, it imports everything. Later we can go ahead and include specific also
from tkinter import *
#defines the root function
root = Tk()
#creating a Label Widget
myLabel = Label(root, text="Hello World!")
#shoving it into the screen. The pack basically creates a screen as big as the content.
myLabel.pack()
#defines the loop because of which the GUI actually remains
root.mainloop()

