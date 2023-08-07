from tkinter import *
import main as m

root = Tk()
root.title('Lexical Analyzer')
root.geometry('2000x2000')
root.config(bg='#AEBDCA')

frame1 = Frame(root, padx=10)
frame1.pack(side=LEFT, anchor="w")

frame2 = Frame(root, padx=10)
frame2.pack(side=RIGHT, anchor="e")

v1 = Scrollbar(frame1, orient='vertical')
v2 = Scrollbar(frame2, orient='vertical')

text_box1 = Text(frame1, height=30, width=70, yscrollcommand=v1.set)
v1.config(command=text_box1.yview)
v1.pack(side=RIGHT, fill='y')
text_box1.pack(side=LEFT, padx=40, pady=50)

text_box2 = Text(frame2, height=30, width=70, yscrollcommand=v2.set)
v2.config(command=text_box2.yview)
v2.pack(side=RIGHT, fill='y')
text_box2.pack(side=RIGHT, padx=40, pady=50, expand=1, fill=BOTH)


def take_input():  # Run and Generates Lexeme Token Pair
    m.string = text_box1.get(1.0, "end-1c")
    # print(m.string)
    m.lexeme_token(m.string)
    length = len(m.tokens)
    for i in range(0, length):
        text_box2.insert(INSERT, m.tokens[i])
        text_box2.insert(INSERT, "\n")
    # print(m.tokens)


def clearTextWidget():  # Clear Both Text Widgets
    text_box1.delete("1.0", "end")
    text_box2.delete("1.0", "end")


Run_button = Button(text="Run", font="Helvetica 10 bold italic", command=take_input)
Run_button.place(x=550, y=670)

Clear_button = Button(text="Clear", font="Helvetica 10 bold italic", command=clearTextWidget)
Clear_button.place(x=650, y=670)

Close_button = Button(text="Close", font="Helvetica 10 bold italic", command=root.destroy)
Close_button.place(x=750, y=670)

root.mainloop()
