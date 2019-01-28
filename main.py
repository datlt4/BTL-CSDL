from tkinter import  *
import sqlite3
from sqlite3 import Error
from tkinter import messagebox

database_path = ".\\db_tra_cuu.db"

def create_connection(db_file):
    """ create a database connection to a SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return  None
conn = create_connection(database_path)

def listNameFood(conn):
    sql =   """select ten_tp from thuc_pham
            """
    cur = conn.cursor()
    cur.execute(sql)
    listName = [row[0] for row in cur.fetchall()]
    return listName

def listNameNutrition(conn):
    sql =   """select ten_dd from dinh_duong
            """
    cur = conn.cursor()
    cur.execute(sql)
    listName = [row[0] for row in cur.fetchall()]
    return listName

def listNamePathology(conn):
    sql =   """select ten_bl from benh_ly
            """
    cur = conn.cursor()
    cur.execute(sql)
    listName = [row[0] for row in cur.fetchall()]
    return listName

def tc_tp_mota(conn, ten_thuc_pham):
    sql =   """select mo_ta_tp from thuc_pham where ten_tp = (?)
            """
    cur = conn.cursor()
    cur.execute(sql, (ten_thuc_pham,))
    return cur.fetchall()

def tc_tp_dd(conn, ten_thuc_pham):
    sql ="""
        select ten_dd, ham_luong
            from(
                    (select id_tp
                        from thuc_pham
                            where(ten_tp = (?))
                    )
                    natural join(
                                select id_dd, ten_dd
                                    from dinh_duong
                                )
                    natural join tp_vs_dd
                )
        """
    cur = conn.cursor()
    cur.execute(sql, (ten_thuc_pham,))

    return cur.fetchall()

def tc_tp_bl(conn, ten_thuc_pham):
    sql =   """
            select ten_bl, khuyen_dung
                from(
                        (select id_tp
                            from thuc_pham
                                where(ten_tp = (?))
                        )
                        natural join(
                                    select id_bl, ten_bl
                                        from benh_ly
                                    )
                        natural join tp_vs_bl
                    )
            """
    cur = conn.cursor()
    cur.execute(sql, (ten_thuc_pham,))
    return cur.fetchall()

def tc_dd_mota(conn, ten_dinh_duong):
    sql = """select mo_ta_dd from dinh_duong where ten_dd = (?)"""
    cur = conn.cursor()
    cur.execute(sql, (ten_dinh_duong,))
    return cur.fetchall()

def tc_dd_tp(conn, ten_dinh_duong):
    sql =   """
            select ten_tp, ham_luong
                from(
                        (select id_dd
                            from dinh_duong
                                where(ten_dd = (?))
                        )
                        natural join(
                                    select id_tp, ten_tp
                                        from thuc_pham
                                    )
                        natural join tp_vs_dd                                    
                    )
            """
    cur = conn.cursor()
    cur.execute(sql, (ten_dinh_duong,))
    return cur.fetchall()

def tc_dd_bl(conn, ten_dinh_duong):
    sql =   """
            select ten_bl, phu_hop
                from(
                        (select id_dd
                            from dinh_duong
                                where(ten_dd = (?))
                        )
                        natural join(
                                    select id_bl, ten_bl
                                        from benh_ly
                                    )
                        natural join dd_vs_bl                                    
                    )
            """
    cur = conn.cursor()
    cur.execute(sql, (ten_dinh_duong,))
    return cur.fetchall()

def tc_bl_mota(conn, ten_benh_ly):
    sql = """select mo_ta_bl from benh_ly where ten_bl = (?)"""
    cur = conn.cursor()
    cur.execute(sql, (ten_benh_ly,))
    return cur.fetchall()

def tc_bl_tp(conn, ten_benh_ly):
    sql =   """
            select ten_tp, khuyen_dung
                from(
                        (select id_bl
                            from benh_ly
                                where(ten_bl = (?))
                        )
                        natural join(
                                    select id_tp, ten_tp
                                        from thuc_pham
                                    )
                        natural join tp_vs_bl                                    
                    )
            """
    cur = conn.cursor()
    cur.execute(sql, (ten_benh_ly,))
    return cur.fetchall()

def tc_bl_dd(conn, ten_benh_ly):
    sql =   """
            select ten_dd, phu_hop
                from(
                        (select id_bl
                            from benh_ly
                                where(ten_bl = (?))
                        )
                        natural join(
                                    select id_dd, ten_dd
                                        from dinh_duong
                                    )
                        natural join dd_vs_bl                                    
                    )
            """
    cur = conn.cursor()
    cur.execute(sql, (ten_benh_ly,))
    return cur.fetchall()

""" Auto Complete User input"""
class AutoCompleteEntry(Entry):
    def __init__(self, lista, *args, **kwargs):
        
        Entry.__init__(self, *args, **kwargs)
        self.lista = lista        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        
        self.lb_up = False

    def changed(self, name, index, mode):  

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True
                
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]

def design_gui():
    #create window object
    window = Tk()
    window.title('Tra cứu thông tin thực phẩm và các bệnh lý liên quan')

    # screen_width = window.winfo_screenwidth()
    # screen_height = window.winfo_screenheight()
    # screen_resolution = str(screen_width) + 'x' + str(screen_height)
    # window.geometry(screen_resolution)

    # define three labels
    #-------------------------------------------------------------------
    str_input = StringVar()

    str_out_mota = StringVar()
    str_out_kq1  = StringVar()
    str_out_kq2  = StringVar()

    str_success  = StringVar()
    str_name_kq1 = StringVar()
    str_name_kq2 = StringVar()
    #-------------------------------------------------------------------
    listFood = listNameFood(conn)
    listNutrition = listNameNutrition(conn)
    listPathology = listNamePathology(conn)
    bigList = listFood + listNutrition + listPathology
    e_in = AutoCompleteEntry(bigList, window, width = 50, borderwidth = 3)
    e_in.pack()
    str_input = e_in
    e_in.grid(row = 1, column = 1, columnspan = 3)
    e_in.focus()

    text_success = Label(window, textvariable = str_success)
    text_success.grid(row = 3, column = 0,columnspan = 1, sticky = S)
    # ------------------ Radiobutton -------------------------------------------
    var_radio = IntVar()
    R1 = Radiobutton(window, text="Thực phẩm", variable=var_radio, value=1, anchor = CENTER, width = 50)
    R1.grid(row = 0, column = 0)
    R1.select()

    R2 = Radiobutton(window, text="Dinh dưỡng", variable=var_radio, value=2, anchor = CENTER, width = 50)
    R2.grid(row = 0, column = 2)

    R3 = Radiobutton(window, text="Bệnh lý", variable=var_radio, value=3, anchor = CENTER, width = 50)
    R3.grid(row = 0, column = 4)
    #-------------------------------------------------------------------------------

    l_mo_ta=Label(window, text = 'Mô tả')
    l_mo_ta.grid(row = 4, column = 0, sticky = S)

    scrolly1 = Scrollbar(window, orient=VERTICAL)
    scrolly1.grid(row = 5, column = 1, sticky = N+S+W)

    text_out_mota = Text(window,bg = "white", width = 50, height = 30,  wrap= WORD, yscrollcommand = scrolly1.set)
    text_out_mota.grid(row = 5, column = 0, columnspan = 1, rowspan = 1, sticky = W)

    scrolly1.config( command =text_out_mota.yview )
    #------------------ hien thi ket qua-------------------------------------------

    text_kq1 = Label(window, textvariable = str_name_kq1)
    text_kq1.grid(row = 4, column = 2, columnspan = 1, sticky = S)

    scrolly2 = Scrollbar(window, orient=VERTICAL)
    scrolly2.grid(row = 5, column = 3, sticky = N+S+W)

    text_out_kq1 = Text(window,bg = "white", width = 50, height = 30,  wrap= WORD, yscrollcommand = scrolly2.set)
    text_out_kq1.grid(row = 5, column = 2, columnspan = 1, rowspan = 1, sticky = E+W )

    scrolly2.config( command =text_out_kq1.yview )
    #-------------------------------------------------------------------

    text_kq2 = Label(window, textvariable = str_name_kq2)
    text_kq2.grid(row = 4, column = 4, columnspan = 1, sticky = S)

    scrolly3 = Scrollbar(window, orient=VERTICAL)
    scrolly3.grid(row = 5, column = 5, sticky = N+S+W)

    text_out_kq2 = Text(window,bg = "white", width = 50, height = 30,  wrap= WORD, yscrollcommand = scrolly3.set)
    text_out_kq2.grid(row = 5, column = 4,columnspan = 1, rowspan = 1)

    scrolly3.config( command =text_out_kq2.yview )
    #--------------------------- handler button --------------------------------------
    def handler_but():
        str_success.set("")
        str_out_kq1.set("")
        str_out_kq1.set("")
        str_out_kq2.set("")

        text_out_mota.delete(1.0, END)
        text_out_kq1.delete(1.0, END)
        text_out_kq2.delete(1.0, END)

        i = var_radio.get()

        if i == 1 :
            str_name_kq1.set("Dinh dưỡng trong 100g")
            str_name_kq2.set("Bệnh lý")

            row = tc_tp_mota(conn, str_input.get().strip())
            if row :
                str_out_mota.set("%s" % (row[0]))
                for row in tc_tp_dd(conn, str_input.get().strip()):
                    str_out_kq1.set( str_out_kq1.get() + "%-20s : %s\n" % (row[0],row[1]) )
                for row in tc_tp_bl(conn, str_input.get()):
                    str_out_kq2.set( str_out_kq2.get() + "Lời khuyên: %s cho bệnh: %s\n" % (row[1],row[0]) )

                text_out_mota.insert(INSERT, str_out_mota.get().strip())
                text_out_kq1.insert(INSERT, str_out_kq1.get())
                text_out_kq2.insert(INSERT, str_out_kq2.get())
            else:
                messagebox.showwarning("Warning","Tên này chưa có trong cơ sở dữ liệu")
                str_success.set(" Lỗi! Tên này chưa có trong cơ sở dữ liệu")
        elif i == 2:
            str_name_kq1.set("Thực phẩm trong 100g")
            str_name_kq2.set("Bệnh lý")

            row = tc_dd_mota(conn, str_input.get().strip())
            if row :
                str_out_mota.set("%s" % (row[0]))
                for row in tc_dd_tp(conn, str_input.get().strip()):
                    str_out_kq1.set(str_out_kq1.get() + "%-20s : %s\n" % (row[0], row[1]))
                for row in tc_dd_bl(conn, str_input.get().strip()):
                    str_out_kq2.set(str_out_kq2.get() + "Bệnh       : %s\nLời khuyên : %s\n" % (row[0], row[1]))

                text_out_mota.insert(INSERT, str_out_mota.get())
                text_out_kq1.insert(INSERT, str_out_kq1.get())
                text_out_kq2.insert(INSERT, str_out_kq2.get())
            else:
                messagebox.showwarning("Warning","Tên này chưa có trong cơ sở dữ liệu")
                str_success.set(" Lỗi! Tên này chưa có trong cơ sở dữ liệu")
        elif i == 3:
            str_name_kq1.set("Thực phẩm")
            str_name_kq2.set("Dinh dưỡng")

            row = tc_bl_mota(conn, str_input.get().strip())
            if row:
                str_out_mota.set("%s" % (row[0]))
                for row in tc_bl_tp(conn, str_input.get().strip()):
                    str_out_kq1.set( str_out_kq1.get() + "%-15s Khuyên dùng:%s\n" % (row[0],row[1]) )
                for row in tc_bl_dd(conn, str_input.get().strip()):
                    str_out_kq2.set( str_out_kq2.get() + "%-15s Lời khuyên:%s\n" % (row[0],row[1]) )

                text_out_mota.insert(INSERT, str_out_mota.get())
                text_out_kq1.insert(INSERT, str_out_kq1.get())
                text_out_kq2.insert(INSERT, str_out_kq2.get())
            else:
                messagebox.showwarning("Warning","Tên này chưa có trong cơ sở dữ liệu")
                str_success.set(" Lỗi! Tên này chưa có trong cơ sở dữ liệu")
    #-------------------------------------------------------------------

    but = Button(window, text = 'Tìm kiếm', command = handler_but)
    but.grid(row = 1, column = 4, sticky = N+W)
    #-------------------------------------------------------------------
    #event enter:
    def func(event):
        handler_but()
    window.bind('<Return>', func)

    window.mainloop()

if __name__ == '__main__':

    design_gui()