from tkinter import *
from tkinter import messagebox
import googletrans
from googletrans import Translator


class GUI():
    root = Tk()
    mainmenu_frame = Frame(root)
    translate_frame = Frame(root, bg='#5584AC')
    history_frame = Frame(root)

    #----------mainmenu frame----------
    mainmenu_frame_title = Label(mainmenu_frame, text='WELCOME TO TRANSLATOR')
    translate_btn = Button(mainmenu_frame, text='Translate')
    history_btn = Button(mainmenu_frame, text='History')
    exit_btn = Button(mainmenu_frame, text='Exit')


    #------------translate frame-----------
    translate_frame_title = Label(translate_frame,text="TRANSLATOR", font=('Cooper Black','50','bold'),fg='#42C2FF', bg='#5584AC')
    enter_lbl = Label(translate_frame, text='ENTER', font=('Lilita One', '32', 'bold'), fg='#42C2FF', bg='#5584AC')
    enter_text = Text(translate_frame, font=('Casterllar', '18', 'bold'), width=37, height=4, bd=4, relief=GROOVE, wrap='word')
    meaning_lbl = Label(translate_frame, text='TRANSLATE', font=('Lilita One', '32', 'bold'), fg='#42C2FF', bg='#5584AC')
    meaning_text = Text(translate_frame, font=('Casterllar', '18', 'bold'), width=37, height=4, bd=4, relief=GROOVE, wrap='word')
    trans_img = PhotoImage(file='trans.png')
    trans_btn = Button(translate_frame, image=trans_img, bd=0, bg='#5584AC', activebackground="whitesmoke")
    clear_img = PhotoImage(file='delete.png')
    clear_btn = Button(translate_frame, image=clear_img, bd=0, bg='#5584AC', activebackground="whitesmoke")
    return_img = PhotoImage(file='home.png')
    return_btn = Button(translate_frame, image=return_img, bd=0, bg='#5584AC', activebackground="whitesmoke")
    frame_option = LabelFrame(translate_frame, text="Option", bg='#5584AC', fg='#42C2FF', font=('Allura', '15', 'bold'))
    lang = ["English to Vietnamese", "Vietnamese to English"]
    x = IntVar()
    x.set("0")

    #------------history frame----------
    history_frame_title = Label(history_frame, text='History')
    history_text = Text(history_frame, width=50, height=5, bd=4, relief=GROOVE, wrap='word')
    showhis_btn = Button(history_frame, text='Show History')
    frame3_btn2 = Button(history_frame, text='Return to main menu')

    def __init__(self):
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.state('zoomed')
        self.root.title('TRANSLATOR')
        self.root.configure(bg='#4A4A4A')
        self.root.iconbitmap('logo.ico')
        for frame in (self.mainmenu_frame, self.translate_frame, self.history_frame):
            frame.grid(row=0, column=0, sticky='nsew')


        #---------main menu frame--------
        self.mainmenu_frame_title.pack()
        self.translate_btn.pack(pady=10)
        self.translate_btn['command'] = lambda: self.show_frame(self.translate_frame)
        self.history_btn.pack(pady=10)
        self.history_btn['command'] = lambda: self.show_frame(self.history_frame)
        self.exit_btn.pack(pady=10)
        self.exit_btn['command'] = self.exit

        #-----------translate frame------------------
        self.translate_frame_title.pack()
        self.enter_lbl.pack(pady=20)
        self.enter_text.pack()
        self.enter_text.focus_set()  # vitri con tro
        self.frame_option.pack(pady=30)
        for index in range(len(self.lang)):
            radiobutton = Radiobutton(self.frame_option, bg='#5584AC', text=self.lang[index], variable=self.x, value=index,
                                      fg='#42C2FF', font=("Mulish ExtraLight", '13', 'bold'))
            radiobutton.pack(anchor=W)
        self.meaning_lbl.pack(pady=20)
        self.meaning_text.pack()
        self.trans_btn.place(x=640, y=700)
        self.trans_btn['command'] = self.trans
        self.clear_btn.place(x=740, y=700)
        self.clear_btn['command'] = self.clear
        #self.exit_btn.place(x=840, y=700)
        #self.exit_btn['command'] = self.exit
        self.return_btn.place(x=840, y=700)
        self.return_btn['command'] = lambda: self.show_frame(self.mainmenu_frame)


        #-------------history frame-----------
        self.history_frame_title.pack()
        self.history_text.pack(pady=10)
        self.showhis_btn.pack(pady=10)
        self.frame3_btn2.pack(pady=10)
        self.showhis_btn['command'] = self.show_history
        self.frame3_btn2['command'] = lambda: self.show_frame(self.mainmenu_frame)


        self.show_frame(self.mainmenu_frame)
        self.root.mainloop()

    def show_frame(self, frame):
        frame.tkraise()


    def trans(self):
        src_lang = " en "
        dest_lang = "vi"
        if (self.x.get()) == 0:
            src_lang = "en"
            dest_lang = "vi"
        elif (self.x.get()) == 1:
            src_lang = "vi"
            dest_lang = "en"
        else:
            pass
        in_put = self.enter_text.get(1.0, END)
        tran_slate = Translator()
        out_put = tran_slate.translate(text=in_put, src=src_lang, dest=dest_lang)
        self.meaning_text.delete(1.0, END)
        self.meaning_text.insert(END, out_put.text)

        #lưu các từ đã nhập vào file
        fh = open('history.txt', 'a')
        fh.write(in_put)
        fh.close()

    def clear(self):
        self.enter_text.delete(1.0, END)
        self.meaning_text.delete(1.0, END)

    def show_history(self):
        fh = open('history.txt', 'r')
        text = fh.read()
        self.history_text.delete(1.0, END)
        self.history_text.insert(END, text)
        fh.close()

    def exit(self): #xác nhận lại có muốn đóng cửa sổ
        res = messagebox.askyesno('Confirm','Do you want to exit?')
        if res == TRUE:
            self.root.destroy()
        else:
            pass


if __name__ == '__main__':
    test = GUI()

