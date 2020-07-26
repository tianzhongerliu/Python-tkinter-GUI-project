from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

filename = ''

def noodbook():
    # 作者信息
    def author():
        showinfo('作者信息', '本软件由XXX完成')

    # 版权信息
    def about():
        showinfo('版权信息.Copyright', '本软件版权归属为XXX')

    # 打开文件
    def openfile():
        global filename
        filename = askopenfilename(defaultextension='.txt')
        if filename == '':
            filename = None
        else:
            root.title('FileName:' + os.path.basename(filename))
            textPad.delete(1.0, END)
            f = open(filename, 'r')
            textPad.insert(1.0, f.read())
            f.close()

    # 新建文件
    def newfile():
        global filename
        root.title('未命名文件')
        filename = None
        textPad.delete(1.0, END)

    # 保存文件
    def savefile():
        global filename
        try:
            f = open(filename, 'w')
            msg = textPad.get(1.0, END)
            f.write(msg)
            f.close()
        except:
            saveasfile()

    # 另存文件
    def saveasfile():
        f = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
        global filename
        filename = f
        fh = open(f, 'w')
        msg = textPad.get(1.0, END)
        fh.write(msg)
        fh.close()
        root.title('FileName:' + os.path.basename(f))

    # 剪切文件
    def cutfile():
        textPad.event_generate('<<Cut>>')

    # 复制文件
    def copyfile():
        textPad.event_generate('<<Copy>>')

    # 粘贴文件
    def pastefile():
        textPad.event_generate('<<Paste>>')

    # 重做文件
    def redofile():
        textPad.event_generate('<<Redo>>')

    # 撤销文件
    def undofile():
        textPad.event_generate('<<Undo>>')

    # 全选文件
    def selectAll():
        textPad.tag_add('sel', '1.0', END)

    # 查找
    def search():
        topsearch = Toplevel(root)
        topsearch.geometry('300x30+200+250')
        label1 = Label(topsearch, text='Find')
        label1.grid(row=0, column=0, padx=5)
        entry1 = Entry(topsearch, width=20)
        entry1.grid(row=0, column=1, padx=5)
        button1 = Button(topsearch, text='查找')
        button1.grid(row=0, column=2)

    root = Tk()
    root.title("记事本")
    root.geometry("800x500+100+100")

    # 创建菜单
    menubar = Menu(root)
    root.config(menu=menubar)

    filemenu = Menu(menubar)
    filemenu.add_command(label='新建', accelerator='Ctrl+N', command=newfile)
    filemenu.add_command(label='打开', accelerator='Ctrl+O', command=openfile)
    filemenu.add_command(label='保存', accelerator='Ctrl+S', command=savefile)
    filemenu.add_command(label='另存为', accelerator='Ctrl+Shift+S', command=saveasfile)
    menubar.add_cascade(label='文件', menu=filemenu)

    editmenu = Menu(menubar)
    editmenu.add_command(label='撤销', accelerator='Ctrl+Z', command=undofile)
    editmenu.add_command(label='重做', accelerator='Ct rl+Y', command=redofile)
    editmenu.add_separator()
    editmenu.add_command(label='剪切', accelerator='Ctrl+X', command=cutfile)
    editmenu.add_command(label='复制', accelerator='Ctrl+C', command=copyfile)
    editmenu.add_command(label='粘贴', accelerator='Ctrl+V', command=pastefile)
    editmenu.add_separator()
    editmenu.add_command(label='查找', accelerator='Ctrl+F', command=search)
    editmenu.add_command(label='全选', accelerator='Ctrl+A', command=selectAll)
    menubar.add_cascade(label='编辑', menu=editmenu)

    aboutmenu = Menu(menubar)
    aboutmenu.add_command(label='作者', command=author)
    aboutmenu.add_command(label='版权', command=about)
    menubar.add_cascade(label='关于', menu=aboutmenu)

    # 创建按钮开关
    toolbar = Frame(root, height=25, bg='light sea green')
    shortButton = Button(toolbar, text='打开', command=openfile)
    shortButton.pack(side=LEFT, padx=5, pady=5)
    shortButton = Button(toolbar, text='保存', command=savefile)
    shortButton.pack(side=LEFT)
    toolbar.pack(expand=NO, fill=X)

    # 创建状态栏
    status = Label(root, text='Ln20', bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)

    # 创建正文编辑区域linenumber&text
    lnlabel = Label(root, width=2, bg='antique white')
    lnlabel.pack(side=LEFT, fill=Y)

    textPad = Text(root, undo=True)
    textPad.pack(expand=YES, fill=BOTH)

    scroll = Scrollbar(textPad)
    textPad.config(yscrollcommand=scroll.set)
    scroll.config(command=textPad.yview)
    scroll.pack(side=RIGHT, fill=Y)

    root.mainloop()
