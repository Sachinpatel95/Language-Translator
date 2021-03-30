from tkinter import *
from tkinter import ttk
from google_trans_new import google_translator

root = Tk()

root.geometry("650x600")
root.title("Language Translator")

tittle = Label(root, text='Language Translator', bd=8, relief=GROOVE, font = ("times new roman", 30, "bold"), bg='#3498DB', fg='black')
tittle.pack(side=TOP, fill=X)

in_frame = Frame(root, bd=3, relief = RIDGE, bg='#3498DB')
in_frame.place(x=10, y=70, width = 630, height = 520)

label1 = Label(in_frame, text = 'Enter Text', font = ("times new roman", 20, "bold"), bg='#3498DB', fg='white')
label1.pack()

text = Text(in_frame, width=50, height=4, font = ("times new roman", 15), bd=5, relief=GROOVE)
text.pack()

label2 = Label(in_frame, text = 'Choose Language To Translate: ', font = ("times new roman", 20, "bold"), bg='#3498DB', fg='white')
label2.place(y=170)

langs = ttk.Combobox(in_frame, font = ("times new roman", 13, "bold"), state='readonly')
langs['values'] = ('Arabic', 'Bulgarian', 'Chinese', 'French', 'Greek', 'Gujarati', 'Hindi', 'Punjabi', 'Malayalam', 'Irish', 'Italian', 'Japanese', 'Korean', 'Latin', 'Russian', 'Spanish', 'Telugu', 'Urdu', 'Zulu')
langs.place(x=400,y=175)


def get_output():
    Dict={'Arabic':'ar', 'Bulgarian':'bg', 'Chinese':'zh-cn', 'French':'fr', 'Greek':'el', 'Gujarati':'gu', 'Hindi':'hi','Punjabi':'pa', 'Malayalam':'ml', 'Irish':'ga', 'Italian':'it', 'Japanese':'ja', 'Korean':'ko', 'Latin':'la', 'Russian':'ru', 'Spanish':'es', 'Telugu':'te', 'Urdu':'ur', 'Zulu':'zu'}
    output.delete('1.0', 'end')
    translator=google_translator()
    txt = text.get('1.0', 'end')
    ans=translator.translate(txt, lang_tgt=Dict[langs.get()])
    output.insert(0.0, ans)


translate_btn = Button(in_frame, text = 'TRANSLATE', command=get_output, font = ("times new roman", 15, "bold"))
translate_btn.place(x=250, y=250)


label3 = Label(in_frame, text = 'Translated Text', font = ("times new roman", 20, "bold"), bg='#3498DB', fg='white')
label3.place(x=220, y=320)

output = Text(in_frame, width=46, height=4, font = ("arial", 15), bd=5, relief=GROOVE, pady=10)
output.place(x=50, y=360)

root.mainloop()