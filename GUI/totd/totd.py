import tkinter as tk
import random
import time
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 500)
canvas1.pack()
root.eval('tk::PlaceWindow . center')
root.overrideredirect(True)

def hello ():  
    thoughts=["The book of life has many chapters,\n try to read them all.",
    "Put out positive vibes to the universe and \n watch the universe respond in kindness.",
    "If young people are not taught that violence \n is never the answer, the cycle of abuse will continue.",
    "At the end of the day, the most important \n question is: Did you try your best?",
    "Life is a succession of lessons which \n must be lived to be understood",
    "Laugh at yourself often, admit your imperfections,\n and work against taking yourself too seriously."]
    choice = random.randrange(0,len(thoughts))
    label1 = tk.Label(root, text= thoughts[choice], fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(250, 250, window=label1)
    
# button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
hello()

# canvas1.create_window(150, 150, window=button1)
root.after(5000, lambda: root.destroy()) # Destroy the widget after 30 seconds
root.mainloop()
