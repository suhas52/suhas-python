import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width = 500, height = 300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

def clicked():
    my_label.config(text="button clicked")



def get_entry_value():
    value = input.get()
    my_label.config(text=value)

button = tkinter.Button(text="Click me!", command=get_entry_value)
button.pack(side="top")

input = tkinter.Entry()
input.pack()















window.mainloop()