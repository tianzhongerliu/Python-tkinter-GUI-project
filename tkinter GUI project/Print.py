import tkinter as tk
import tkinter.messagebox

class Canvas():
    def __init__(self, window):
        root = tk.Toplevel(window)
        root.title('Print')
        root.geometry('800x600')

        self.status = 0  # 在myButton类的事件处理函数中改变
        self.draw = 0  # 一次操作完成的标志位

        self.board = tk.Canvas(root, width = 800, height = 600)
        self.board.pack()
        self.board.bind('<B1-Motion>', self.print)
        self.board.bind('<ButtonRelease-3>', self.Draw)  # 鼠标左键释放

        menubar = tk.Menu(root)
        menubar.add_command(label='Empty', command=self.board_empty)

        Graphicsmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Graphics', menu=Graphicsmenu)
        Graphicsmenu.add_command(label='Line', command=lambda : self.SetStatus(0))
        Graphicsmenu.add_command(label='arc', command=lambda : self.SetStatus(1))
        Graphicsmenu.add_command(label='rectangle', command=lambda : self.SetStatus(2))
        Graphicsmenu.add_command(label='oval', command=lambda : self.SetStatus(3))

        menubar.add_command(label='Help', command=self.help)

        root.config(menu = menubar)

    def Draw(self, event):
        if self.draw == 0:
            # 两点确定一个图形,所以此处获取第一个点坐标
            self.x = event.x  # 动态增加MyCanvas实例属性
            self.y = event.y  # 相对于窗口，鼠标光标当前的位置
            self.draw = 1
        else:  # 当点击第二次时,draw标志位改为1进入else判断子句,获取第二个点坐标进行画图
            if self.status == 0:
                self.board.create_line(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 1:
                self.board.create_arc(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 2:
                self.board.create_rectangle(self.x, self.y, event.x, event.y)
                self.draw = 0
            else:
                self.board.create_oval(self.x, self.y, event.x, event.y)
                self.draw = 0

    def SetStatus(self, status):
        self.status = status

    def print(self, event):
        x1, y1 = (event.x-1), (event.y-1)
        x2, y2 = (event.x+1), (event.y+1)
        self.board.create_oval(x1,y1,x2,y2, fill = 'black', tag = '0')

    def create_line(self, event):
        pass

    def back(self):
        self.board.delete('0')

    def board_empty(self):
        self.board.delete('all')

    def help(self):
        tk.messagebox.showinfo(title='Help', message='Left click to use brush, right click to add graphics.')

