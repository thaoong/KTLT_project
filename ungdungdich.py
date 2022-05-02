from tkinter import *
from tkinter import messagebox
import googletrans
from googletrans import Translator


class GUI():
    root = Tk()
    mainmenu_frame = Frame(root, bg='#D3F4FF')
    translate_frame = Frame(root, bg='#D3F4FF')
    history_frame = Frame(root, bg='#D3F4FF')

    #----------mainmenu frame----------
    mainmenu_frame_title = Label(mainmenu_frame, text='WELCOME TO TRANSLATOR', font=('Cooper Black','65','bold'), fg='#1F3C88', bg='#D3F4FF')
    translate_btn = Button(mainmenu_frame, text='Translate', font=('Orelega One', '30'), width=30, height=1, fg='#FFFFFF', bg='#1EAFED', bd=7)
    history_btn = Button(mainmenu_frame, text='History', font=('Orelega One', '30'), width=30, height=1, fg='#FFFFFF', bg='#1EAFED', bd=7)
    exit_btn = Button(mainmenu_frame, text='Exit', font=('Orelega One', '30'), width=30, height=1, fg='#FFFFFF', bg='#1EAFED', bd=7)


    #------------translate frame-----------
    translate_frame_title = Label(translate_frame, text='TRANSLATOR', font=('Cooper Black','70','bold'), fg='#1F3C88', bg='#D3F4FF')
    frame1 = Frame(translate_frame, bg='#D3F4FF')
    enter_lbl = Label(frame1, text='ENTER', font=('Lilita One', '32', 'bold'), fg='#1F3C88', bg='#D3F4FF')
    enter_text = Text(frame1, font=('Casterllar', '18', 'bold'), width=40, height=7, bd=6, relief=GROOVE, wrap='word')
    meaning_lbl = Label(frame1, text='TRANSLATE', font=('Lilita One', '32', 'bold'), fg='#1F3C88', bg='#D3F4FF')
    meaning_text = Text(frame1, font=('Casterllar', '18', 'bold'), width=40, height=7, bd=6, relief=GROOVE, wrap='word')
    button_frame = Frame(translate_frame, bg='#D3F4FF')
    trans_img = PhotoImage(file='trans.png')
    trans_btn = Button(button_frame, image=trans_img, bd=0, bg='#D3F4FF', activebackground="whitesmoke")
    clear_img = PhotoImage(file='delete.png')
    clear_btn = Button(button_frame, image=clear_img, bd=0, bg='#D3F4FF', activebackground="whitesmoke")
    return_img = PhotoImage(file='home.png')
    return_btn = Button(button_frame, image=return_img, bd=0, bg='#D3F4FF', activebackground="whitesmoke")
    frame_option = LabelFrame(translate_frame, text="Option", bg='#1F3C88', fg='#FFFFFF', font=('Allura', '15', 'bold'))
    lang = ["English to Vietnamese", "Vietnamese to English"]
    x = IntVar()
    x.set("0")

    #------------history frame----------
    history_frame_title = Label(history_frame, text='History', font=('Cooper Black', '70', 'bold'), fg='#1F3C88', bg='#D3F4FF')
    history_text = Text(history_frame, width=100, height=18, bd=8, relief=GROOVE, wrap='word')
    hisbtn_frame = Frame(history_frame, bg='#D3F4FF')
    showhis_img = PhotoImage(file='showhistory.png')
    showhis_btn = Button(hisbtn_frame, text='Show History', image=showhis_img, bd=0, bg='#D3F4FF', activebackground="whitesmoke")
    back_img = PhotoImage(file='back.png')
    back_btn = Button(hisbtn_frame, image=back_img, bd=0, bg='#D3F4FF', activebackground="whitesmoke")
    back_btn = Button(hisbtn_frame, image=back_img, bd=0, bg='#D3F4FF', activebackground="whitesmoke")
    clear_his_btn = Button(hisbtn_frame, image=clear_img, bd=0, bg='#D3F4FF', activebackground="whitesmoke")

    def __init__(self):
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.state('zoomed')
        self.root.title('TRANSLATOR')
        self.root.iconbitmap('logo.ico')
        for frame in (self.mainmenu_frame, self.translate_frame, self.history_frame):
            frame.grid(row=0, column=0, sticky='nsew')


        #---------main menu frame--------
        self.mainmenu_frame_title.pack(pady=30)
        self.translate_btn.pack(pady=50)
        self.translate_btn['command'] = lambda: self.show_frame(self.translate_frame)
        self.history_btn.pack(pady=50)
        self.history_btn['command'] = lambda: self.show_frame(self.history_frame)
        self.exit_btn.pack(pady=50)
        self.exit_btn['command'] = self.exit

        #-----------translate frame------------------
        self.translate_frame_title.pack(pady=20)
        self.frame1.pack(pady=30)
        self.enter_lbl.grid(row=0, column=1, pady=20)
        self.enter_text.grid(row=1, column=1, padx=30)
        self.enter_text.focus_set()
        self.meaning_lbl.grid(row=0, column=2, pady=20)
        self.meaning_text.grid(row=1, column=2, padx=30)
        self.frame_option.pack(pady=15)
        for index in range(len(self.lang)):
            radiobutton = Radiobutton(self.frame_option, bg='#9FE8FA', text=self.lang[index], variable=self.x, value=index,
                                      fg='black', font=("Mulish ExtraLight", '13', 'bold'))
            radiobutton.pack(anchor=W)
        self.button_frame.pack(pady=30)
        self.trans_btn.pack(side='left', padx=15)
        self.trans_btn['command'] = self.trans
        self.clear_btn.pack(side='left', padx=15)
        self.clear_btn['command'] = self.clear
        self.return_btn.pack(side='left', padx=15)
        self.return_btn['command'] = lambda: self.show_frame(self.mainmenu_frame)


        #-------------history frame-----------
        self.history_frame_title.pack(pady=20)
        self.history_text.pack(pady=30)
        self.hisbtn_frame.pack(pady=25)
        self.showhis_btn.pack(side='left', padx=15)
        self.showhis_btn['command'] = self.show_history
        self.back_btn.pack(side='left', padx=15)
        self.back_btn['command'] = lambda: self.show_frame(self.mainmenu_frame)
        self.clear_his_btn.pack(side='left', padx=15)
        self.clear_his_btn['command'] = self.clear_history

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
        fh = open('history.txt', 'a', encoding='utf-8')
        fh.write(in_put)
        fh.close()

    def clear(self):
        self.enter_text.delete(1.0, END)
        self.meaning_text.delete(1.0, END)

    def show_history(self):
        fh = open('history.txt', 'r', encoding='utf-8')
        text = fh.read()
        self.history_text.delete(1.0, END)
        self.history_text.insert(END, text)
        fh.close()

    def clear_history(self):
        fh = open('history.txt', 'r+', encoding='utf-8')
        fh.truncate(0)
        self.history_text.delete(1.0, END)
        fh.close()

    def exit(self): #xác nhận lại có muốn đóng cửa sổ
        res = messagebox.askyesno('Confirm', 'Do you want to exit?')
        if res == TRUE:
            self.root.destroy()
        else:
            pass


if __name__ == '__main__':
    test = GUI()

