import tkinter as tk
import tkinter.messagebox
import pickle
import Noodbook
import Greedy_snake
import Calculator
import Print
import Music
import GUI.VideoPlayer as Video
import Tetris
import MineSweeping
import ManAndMachine

image_file = None
image_file2 = None
image_file3 = None
image_file4 = None
image_file5 = None
image_file6 = None
image_file7 = None
image_file8 = None
image_file9 = None
image_file10 = None
image_file11 = None
image_file12 = None

class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry('600x400')

        loadface(self.root)


class loadface():
    def __init__(self, master):
        self.master = master
        self.master.title('Loaging')
        # 登录界面
        self.loadpage = tk.Frame(self.master, height=400, width=600)
        self.loadpage.place(x=0, y=0)

        global image_file
        image_file = tk.PhotoImage(file='2.gif')
        canvas = tk.Canvas(self.loadpage, height=400, width=600)
        image = canvas.create_image(0, 0, anchor='nw', image=image_file)
        canvas.place(x=0, y=0)

        tk.Label(self.loadpage, text='Welcome', font=('Arial', 20)).place(x=270, y=70)

        tk.Label(self.loadpage, text='User name：  ', font=('Arial', 12)).place(x=180, y=150)
        tk.Label(self.loadpage, text='Password：', font=('Arial', 12)).place(x=180, y=200)

        self.var_user_name = tk.StringVar()
        entry_user_name = tk.Entry(self.loadpage, textvariable=self.var_user_name, font=('Arial', 12))
        entry_user_name.place(x=270, y=150)

        self.var_user_pwd = tk.StringVar()
        entry_user_pwd = tk.Entry(self.loadpage, textvariable=self.var_user_pwd, font=('Arial', 12), show='*')
        entry_user_pwd.place(x=270, y=200)

        but_login = tk.Button(self.loadpage, text='Login', command=self.change_login)
        but_login.place(x=270, y=250)

        but_sign_up = tk.Button(self.loadpage, text='Sign up', command=self.change_sign_up)
        but_sign_up.place(x=350, y=250)

    def change_sign_up(self, ):
        self.loadpage.destroy()
        signpage(self.master)

    def change_login(self):
        user_name = self.var_user_name.get()
        user_pwd = self.var_user_pwd.get()
        try:
            with open('users_info.pickle', 'rb') as user_file:
                user_info = pickle.load(user_file)
        except FileNotFoundError:
            with open('users_info.pickle', 'wb') as user_file:
                user_info = {'admin': 'admin'}
                pickle.dump(user_info, user_file)

        if user_name in user_info:
            if user_pwd == user_info[user_name]:
                self.loadpage.destroy()
                userpage(self.master, self.var_user_name)
            else:
                tk.messagebox.showerror(message='Error,your password is wrong, try again.')
        else:
            is_sign_up = tk.messagebox.askyesno(title='Welcome', message='You have not sign up yet. Sign up now?')
            if is_sign_up:
                self.loadpage.destroy()
                signpage(self.master)

class signpage():
    def __init__(self, master):
        self.master = master
        self.master.title('Sign up')
        self.signpage = tk.Frame(self.master, height=400, width=600)
        self.signpage.place(x=0, y=0)

        global image_file
        image_file = tk.PhotoImage(file='2.gif')
        canvas = tk.Canvas(self.signpage, height=400, width=600)
        image = canvas.create_image(0, 0, anchor='nw', image=image_file)
        canvas.place(x=0, y=0)

        tk.Label(self.signpage, text='Welcome to sign up!', font=('Arial', 18)).place(x=200, y=50)
        self.new_name = tk.StringVar()
        tk.Label(self.signpage, text='User name:', font=('Arial', 12)).place(x=200, y=130)
        entry_user_name = tk.Entry(self.signpage, textvariable=self.new_name)
        entry_user_name.place(x=300, y=130)

        self.new_pwd = tk.StringVar()
        tk.Label(self.signpage, text='Password:', font=('Arial', 12)).place(x=205, y=180)
        entry_user_pwd = tk.Entry(self.signpage, textvariable=self.new_pwd, show='*')
        entry_user_pwd.place(x=300, y=180)

        self.new_pwd_confirm = tk.StringVar()
        tk.Label(self.signpage, text='Confirm password:', font=('Arial', 12)).place(x=150, y=230)
        entry_new_pwd_confirm = tk.Entry(self.signpage, textvariable=self.new_pwd_confirm, show='*')
        entry_new_pwd_confirm.place(x=300, y=230)

        confirm_button = tk.Button(self.signpage, text='determine', command=self.sign_up)
        confirm_button.place(x=230, y=300)

        cancel_button = tk.Button(self.signpage, text='  cancel  ', command=self.back_loading)
        cancel_button.place(x=350, y=300)

    def sign_up(self):
        nn = self.new_name.get()
        np = self.new_pwd.get()
        ncf = self.new_pwd_confirm.get()
        with open('users_info.pickle', 'rb') as user_file:
            exist_user_info = pickle.load(user_file)
        if np != ncf:
            tk.messagebox.showerror(title='Error', message='Password and confirm password must be same!')
        elif nn in exist_user_info:
            tk.messagebox.showerror(title='Error', message='This name has been used!')
        else:
            exist_user_info[nn] = np
            with open('users_info.pickle', 'wb') as user_file:
                pickle.dump(exist_user_info, user_file)
            tk.messagebox.showinfo(title='Welcome', message='You have successfully signed up!')
            self.signpage.destroy()
            loadface(self.master)

    def back_loading(self):
        self.signpage.destroy()
        loadface(self.master)

class userpage():
    def __init__(self, master, name):
        self.master = master
        self.master.title('user page')

        self.userpage = tk.Frame(self.master, height=400, width=600)
        self.userpage.place(x=0, y=0)

        global image_file8
        image_file8 = tk.PhotoImage(file='10.gif')
        canvas = tk.Canvas(self.userpage, height=400, width=600)
        image = canvas.create_image(0, 0, anchor='nw', image=image_file8)
        canvas.place(x=0, y=0)

        self.name = name
        self.user_name = name.get()
        # print(self.user_name)
        l = tk.Label(self.userpage, text = '')
        l.config(text = 'welcome: '+ self.user_name)
        l.place(x=10, y=5)

        global image_file2
        image_file2 = tk.PhotoImage(file='4.gif')
        nootbook = tk.Button(self.userpage, command=self.ab_nootbook, activebackground='grey', relief='raised', image = image_file2, bd=1)
        nootbook.place(x=50, y=40)
        tk.Label(self.userpage, text = 'Nootbook', font=('Arial', 10)).place(x=95, y=155)

        global image_file3
        image_file3 = tk.PhotoImage(file='5.gif')
        nootbook = tk.Button(self.userpage, command=self.ab_calculator, activebackground='grey', relief='raised', image=image_file3, bd=1)
        nootbook.place(x=225, y=40)
        tk.Label(self.userpage, text='Calculator', font=('Arial', 10)).place(x=275, y=155)

        global image_file4
        image_file4 = tk.PhotoImage(file='6.gif')
        game = tk.Button(self.userpage, command=self.ab_game, activebackground='grey', relief='raised', image=image_file4, bd=1)
        game.place(x=400, y=40)
        tk.Label(self.userpage, text='Game', font=('Arial', 10)).place(x=450, y=155)

        global image_file5
        image_file5 = tk.PhotoImage(file='7.gif')
        game = tk.Button(self.userpage, command=self.ab_video, activebackground='grey', relief='raised', image=image_file5, bd=1)
        game.place(x=50, y=200)
        tk.Label(self.userpage, text='Video', font=('Arial', 10)).place(x=105, y=315)

        global image_file6
        image_file6 = tk.PhotoImage(file='8.gif')
        game = tk.Button(self.userpage, command=self.ab_print, activebackground='grey', relief='raised', image=image_file6, bd=1)
        game.place(x=225, y=200)
        tk.Label(self.userpage, text='Print', font=('Arial', 10)).place(x=285, y=315)

        global image_file7
        image_file7 = tk.PhotoImage(file='9.gif')
        game = tk.Button(self.userpage, command=self.ab_music, activebackground='grey', relief='raised', image=image_file7, bd=1)
        game.place(x=400, y=200)
        tk.Label(self.userpage, text='Music', font=('Arial', 10)).place(x=460, y=315)

        quit_button = tk.Button(self.userpage, text = 'Quit', command = self.back_to_loading).place(x=550, y=360)

    def back_to_loading(self):
        self.userpage.destroy()
        loadface(self.master)

    def ab_nootbook(self):
        Noodbook.noodbook()

    def ab_calculator(self):
        Calculator.calculator_run(self.userpage)

    def ab_game(self):
        self.userpage.destroy()
        gamepage(self.master, self.name)

    def ab_video(self):
        Video.videoplayer_run(self.userpage)

    def ab_print(self):
        Print.Canvas(self.userpage)

    def ab_music(self):
        Music.music_run(self.userpage)

class gamepage():
    def __init__(self, master, name):
        self.master = master
        self.master.title('game page')

        self.name = name
        self.gamepage = tk.Frame(self.master, height=400, width=600)
        self.gamepage.place(x=0, y=0)

        global image_file9
        image_file9 = tk.PhotoImage(file='11.gif')
        canvas = tk.Canvas(self.gamepage, height=400, width=600)
        image = canvas.create_image(0, 0, anchor='nw', image=image_file9)
        canvas.place(x=0, y=0)

        global image_file10
        image_file10 = tk.PhotoImage(file='12.gif')
        canvas.create_image(-30, 70, anchor='nw', image=image_file10)
        global image_file11
        image_file11 = tk.PhotoImage(file='13.gif')
        canvas.create_image(380, 40, anchor='nw', image=image_file11)
        global image_file12
        image_file12 = tk.PhotoImage(file='14.gif')
        canvas.create_image(10, 10, anchor='nw', image=image_file12)

        back = tk.Button(self.gamepage, text = 'Back', command = self.back_userpage).place(x=40, y=10)
        game1 = tk.Button(self.gamepage, text = '1.贪吃蛇', command = Greedy_snake.run, font=('Arial', 16), relief='raised', bd=1)
        game1.place(x=250, y=70)

        game2 = tk.Button(self.gamepage, text='2.俄罗斯方块', command=Tetris.main, font=('Arial', 16), relief='raised', bd=1)
        game2.place(x=250, y=120)

        game3 = tk.Button(self.gamepage, text='3.扫雷', command=MineSweeping.main, font=('Arial', 16), relief='raised', bd=1)
        game3.place(x=250, y=170)

        game4 = tk.Button(self.gamepage, text='4.五子棋', command=ManAndMachine.main, font=('Arial', 16), relief='raised', bd=1)
        game4.place(x=250, y=220)

    def back_userpage(self):
        self.gamepage.destroy()
        userpage(self.master, self.name)

if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.mainloop()

