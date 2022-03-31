from tkinter import *
from tkinter import messagebox
class GUI():
    root = Tk()
    title_lbl = Label(root,text="TRANSLATOR",font=('Cooper Black','50','bold'),fg='#ECC602',bg='#4A4A4A')
    enter_lbl = Label(root, text='ENTER', font=('Lilita One', '29', 'bold'), fg='#ECC602', bg='#4A4A4A')
    enter_text= Text(root, font=('Casterllar', '18', 'bold'), width=37, height=3, bd=4, relief=GROOVE, wrap='word')
    meaning_lbl = Label(root, text='TRANSLATE', font=('Lilita One', '29', 'bold'), fg='#ECC602', bg='#4A4A4A')
    meaning_text = Text(root, font=('Casterllar', '18', 'bold'), width=37, height=3.5, bd=4, relief=GROOVE, wrap='word')
    search_img = PhotoImage(file='search.png')
    search_btn = Button(root, image=search_img, bd=0, bg='#4A4A4A', activebackground="whitesmoke")
    clear_img = PhotoImage(file='clear.png')
    clear_btn = Button(root, image=clear_img, bd=0, bg='#4A4A4A', activebackground="whitesmoke")
    exit_img = PhotoImage(file='exit.png')
    exit_btn = Button(root, image=exit_img, bd=0, bg='#4A4A4A', activebackground="whitesmoke")
    frame_option = LabelFrame(root, text="Option", bg='#4A4A4A', fg='#ECC602', font=('Allura', '15', 'bold'))
    lang = ["English to Vietnamese", "Vietnamese to English"]
    x = IntVar()
    x.set("0")

    def __init__(self):
        self.root.geometry('840x645')
        self.root.title('TRANSLATOR')
        self.root.configure(bg='#4A4A4A')
        self.root.resizable(0, 0)
        self.title_lbl.place(x=175, y=0)
        self.enter_lbl.place(x=365, y=100)
        self.enter_text.place(x=175, y=160)
        self.enter_text.focus_set()  # vitri con tro
        self.meaning_lbl.place(x=325, y=370)
        self.meaning_text.place(x=175, y=435)
        self.search_btn.place(x=290, y=570)
        self.clear_btn.place(x=390, y=570)
        self.exit_btn.place(x=490, y=570)
        self.exit_btn['command']=self.exit
        self.frame_option.place(x=320, y=270)
        for index in range(len(self.lang)):
            radiobutton = Radiobutton(self.frame_option, bg='#4A4A4A', text=self.lang[index], variable=self.x, value=index,
                                      fg='#ECC602', font=("Mulish ExtraLight", '13'))
            radiobutton.pack(anchor=W)
        self.root.mainloop()


    def exit(self): #xác nhận lại có muốn đóng cửa sổ
        res = messagebox.askyesno('Confirm','Do you want to exit?')
        if res==TRUE:
            self.root.destroy()
        else:
            pass


if __name__=='__main__':
    test=GUI()
