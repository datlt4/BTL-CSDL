from tkinter import  *
import sqlite3
from sqlite3 import Error
from tkinter import messagebox

database_path = ".\\db_tra_cuu.db"

def createConnection(db_file):
    """ create a database connection to a SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return  None

def listNameFood(conn):
    cur = conn.cursor()
    cur.execute("select ten_tp from thuc_pham")
    listName = [row[0] for row in cur.fetchall()]
    return listName

def listNameNutrition(conn):
    cur = conn.cursor()
    cur.execute("select ten_dd from dinh_duong")
    listName = [row[0] for row in cur.fetchall()]
    return listName

def listNamePathology(conn):
    cur = conn.cursor()
    cur.execute("select ten_bl from benh_ly")
    listName = [row[0] for row in cur.fetchall()]
    return listName

def bigList(conn):
    listName_1 = listNameFood(conn)
    listName_2 = listNameNutrition(conn)
    listName_3 = listNamePathology(conn)
    listName = listName_1 + listName_2 + listName_3
    return listName

def queryID_Food(conn, _name):
    cur = conn.cursor()
    cur.execute("select id_tp from thuc_pham where ten_tp = (?)", (_name,))
    row = cur.fetchone()
    if row:
        return row[0]
    else:
        return 0

def queryDes_Food(conn, _name):
    cur = conn.cursor()
    cur.execute("select mo_ta_tp from thuc_pham where ten_tp = (?)", (_name,))
    row = cur.fetchone()
    return row[0]

def queryID_Nutrition(conn, _name):
    cur = conn.cursor()
    cur.execute("select id_dd from dinh_duong where ten_dd = (?)", (_name,))
    row = cur.fetchone()
    if row:
        return row[0]
    else:
        return 0

def queryDes_Nutrition(conn, _name):
    cur = conn.cursor()
    cur.execute("select mo_ta_dd from dinh_duong where ten_dd = (?)", (_name,))
    row = cur.fetchone()
    return row[0]

def queryID_Pathology(conn, _name):
    cur = conn.cursor()
    cur.execute("select id_bl from benh_ly where ten_bl = (?)", (_name,))
    row = cur.fetchone()
    if row:
        return row[0]
    else:
        return 0

def queryDes_Pathology(conn, _name):
    cur = conn.cursor()
    cur.execute("select mo_ta_bl from benh_ly where ten_bl = (?)", (_name,))
    row = cur.fetchone()
    return row[0]

def queryTable_tp_vs_dd(conn, _name1, _name2):
    cur = conn.cursor()
    cur.execute("select ham_luong from tp_vs_dd where id_tp = (?) and id_dd = (?)", (_name1, _name2))
    return cur.fetchone()

def queryTable_tp_vs_bl(conn, _name1, _name2):
    cur = conn.cursor()
    cur.execute("select khuyen_dung from tp_vs_bl where id_tp = (?) and id_bl = (?)", (_name1, _name2))
    return cur.fetchone()

def queryTable_dd_vs_bl(conn, _name1, _name2):
    cur = conn.cursor()
    cur.execute("select phu_hop from dd_vs_bl where id_dd = (?) and id_bl = (?)", (_name1, _name2))
    return cur.fetchone()

def insertToTable_tp_vs_dd (conn, _name1, _name2, _value):
    cur = conn.cursor()
    cur.execute("insert into tp_vs_dd values (?, ?, ?)", (_name1, _name2, _value))
    conn.commit()
    return None

def insertToTable_tp_vs_bl (conn, _name1, _name2, _value):
    cur = conn.cursor()
    cur.execute("insert into tp_vs_bl values (?, ?, ?)", (_name1, _name2, _value))
    conn.commit()
    return None

def insertToTable_dd_vs_bl (conn, _name1, _name2, _value):
    cur = conn.cursor()
    cur.execute("insert into dd_vs_bl values (?, ?, ?)", (_name1, _name2, _value))
    conn.commit()
    return None

def updateRow_tp_vs_dd (conn, _name1, _name2, _value):
    cur = conn.cursor()
    cur.execute("update tp_vs_dd set ham_luong = (?) where  id_tp = (?) and id_dd = (?)", (_value, _name1, _name2))
    conn.commit()
    return None

def updateRow_tp_vs_bl (conn, _name1, _name2, _value):
    cur = conn.cursor()
    cur.execute("update tp_vs_bl set khuyen_dung = (?) where  id_tp = (?) and id_bl = (?)", (_value, _name1, _name2))
    conn.commit()
    return None

def updateRow_dd_vs_bl (conn, _name1, _name2, _value):
    cur = conn.cursor()
    cur.execute("update dd_vs_bl set phu_hop = (?) where  id_dd = (?) and id_bl = (?)", (_value, _name1, _name2))
    conn.commit()
    return None

def insertToTable_thuc_pham(conn, _value1, _value2):
    cur = conn.cursor()
    cur.execute("insert into thuc_pham(ten_tp, mo_ta_tp) values (?, ?)", (_value1, _value2))
    conn.commit()
    return None

def insertToTable_dinh_duong(conn, _value1, _value2):
    cur = conn.cursor()
    cur.execute("insert into dinh_duong(ten_dd, mo_ta_dd) values (?, ?)", (_value1, _value2))
    conn.commit()
    return None

def insertToTable_benh_ly(conn, _value1, _value2):
    cur = conn.cursor()
    cur.execute("insert into benh_ly(ten_bl, mo_ta_bl) values (?, ?)", (_value1, _value2))
    conn.commit()
    return None

def updateRowTable_thuc_pham(conn, _value1, _value2):
    cur = conn.cursor()
    cur.execute("update thuc_pham set mo_ta_tp = (?) where  id_tp = (?)", (_value1, _value2))
    conn.commit()
    return None

def updateRowTable_dinh_duong(conn, _value1, _value2):
    cur = conn.cursor()
    cur.execute("update dinh_duong set mo_ta_dd = (?) where  id_dd = (?)", (_value1, _value2))
    conn.commit()
    return None

def updateRowTable_benh_ly(conn, _value1, _value2):
    cur = conn.cursor()
    cur.execute("update benh_ly set mo_ta_bl = (?) where  id_bl = (?)", (_value1, _value2))
    conn.commit()
    return None

def deleteRowTable_thuc_pham(conn, _value1):
    cur = conn.cursor()
    cur.execute("delete from thuc_pham where id_tp = (?)", (_value1,))
    conn.commit()
    return None

def deleteRowTable_dinh_duong(conn, _value1):
    cur = conn.cursor()
    cur.execute("delete from dinh_duong where id_dd = (?)", (_value1,))
    conn.commit()
    return None

def deleteRowTable_benh_ly(conn, _value1):
    cur = conn.cursor()
    cur.execute("delete from benh_ly where id_bl = (?)", (_value1,))
    conn.commit()
    return None

def delete_idTP_tp_vs_dd(conn, _value1):
    cur = conn.cursor()
    cur.execute("delete from tp_vs_dd where id_tp = (?)", (_value1,))
    conn.commit()
    return None

def delete_idTP_tp_vs_bl(conn, _value1):
    cur = conn.cursor()
    cur.execute("delete from tp_vs_bl where id_tp = (?)", (_value1,))
    conn.commit()
    return None

def delete_idDD_tp_vs_dd(conn, _value1):
    cur = conn.cursor()
    cur.execute("delete from tp_vs_dd where id_dd = (?)", (_value1,))
    conn.commit()
    return None

def delete_idDD_dd_vs_bl(conn, _value1):
    cur = conn.cursor()
    cur.execute("delete from dd_vs_bl where id_dd = (?)", (_value1,))
    conn.commit()
    return None

def delete_idBL_tp_vs_bl(conn, _value1):
    cur = conn.cursor()
    cur.execute("delete from tp_vs_bl where id_bl = (?)", (_value1,))
    conn.commit()
    return None

def delete_idBL_dd_vs_bl(conn, _value1):
    cur = conn.cursor()
    cur.execute("delete from dd_vs_bl where id_bl = (?)", (_value1,))
    conn.commit()
    return None


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


def designGUI():
    conn = createConnection(database_path)
    GUI = Tk()
    GUI.title('Thêm quan hệ giữa thực phẩm, dinh dưỡng và các bệnh lý liên quan')
    GUI.geometry('570x820')

    inputFood = StringVar()
    inputNutrition = StringVar()
    inputPathology = StringVar()

    idDD = IntVar()
    idTP = IntVar()
    idBL = IntVar()

    inputEntity = StringVar()
    inputDescription = StringVar()

    idEntity = IntVar()
    desEntity = StringVar()

    labelNo1 = Label(GUI, text = "Thực phẩm")
    labelNo1.grid(row = 0, column = 1, sticky = N)
    labelNo2 = Label(GUI, text = "Dinh dưỡng")
    labelNo2.grid(row = 0, column = 2, sticky = N)
    labelNo3 = Label(GUI, text = "Bệnh lý")
    labelNo3.grid(row = 0, column = 3, sticky = N)

    entryFood = AutoCompleteEntry(listNameFood(conn), GUI, width = 30, borderwidth = 1)
    inputFood = entryFood
    entryFood.grid(row = 1, column = 1, columnspan = 1)
    entryFood.focus()
    entryNutrition = AutoCompleteEntry(listNameNutrition(conn), GUI, width = 30, borderwidth = 1)
    inputNutrition = entryNutrition
    entryNutrition.grid(row = 1, column = 2, columnspan = 1)
    entryNutrition.focus()
    entryPathology = AutoCompleteEntry(listNamePathology(conn), GUI, width = 30, borderwidth = 1)
    inputPathology = entryPathology
    entryPathology.grid(row = 1, column = 3, columnspan = 1)
    entryPathology.focus()

    inputContent = StringVar()
    inputSuitability = StringVar()
    inputRecommendation = StringVar()

    labelNull1 = Label(GUI, text = "")
    labelNull1.grid(row = 2, column = 0)

    labelNo4 = Label(GUI, text = "Hàm lượng chất dinh dưỡng trong 100g thực phẩm:")
    labelNo4.grid(row = 3, column = 1, columnspan = 2, sticky = E)
    entryContent = Entry(GUI, textvariable = inputContent, width = 20, borderwidth = 1)
    entryContent.grid(row = 3, column = 3, rowspan = 1, sticky = W)
    entryContent.focus()

    labelNull2 = Label(GUI, text = "")
    labelNull2.grid(row = 4, column = 1)

    labelNo5 = Label(GUI, text = "Mức độ phù hợp của chất dinh dưỡng với bệnh lý:")
    labelNo5.grid(row = 5, column = 1, columnspan = 2, sticky = E)
    listNo1 = ['rất tốt', 'tốt', 'không tốt']
    entrySuitability = AutoCompleteEntry(listNo1, GUI, width = 20, borderwidth = 1)
    inputSuitability = entrySuitability
    entrySuitability.grid(row = 5, column = 3, sticky = W)
    entrySuitability.focus()

    labelNull3 = Label(GUI, text = "")
    labelNull3.grid(row = 6, column = 0)

    labelNo6 = Label(GUI, text = "Khuyến cáo thực phẩm với bệnh lý:")
    labelNo6.grid(row = 7, column = 1, columnspan = 2, sticky = E)
    listNo2 = ['nên ăn nhiều', 'nên ăn', 'hạn chế', 'kiêng ăn', 'không được ăn']
    entryRecommendation = AutoCompleteEntry(listNo2, GUI,width = 20, borderwidth = 1)
    inputRecommendation = entryRecommendation
    entryRecommendation.grid(row = 7, column = 3, sticky = W)
    entryRecommendation.focus()

    labelNull4 = Label(GUI, text = "")
    labelNull4.grid(row = 8, column = 0)
    
    #scrolly1 = Scrollbar(GUI, orient=VERTICAL)
    #scrolly1.grid(row = 9, column = 0, sticky = W)
    #', yscrollcommand = scrolly1.set'
    textOutput = Text(GUI, bg = "white", width = 45, height = 9,  wrap= WORD)
    textOutput.grid(row = 9, column = 1, columnspan = 2, rowspan = 1)

    labelNull8 = Label(GUI, text = "")
    labelNull8.grid(row = 10, column = 1)
    labelNull9 = Label(GUI, text = "")
    labelNull9.grid(row = 11, column = 1)

    varRadioButton = IntVar()
    R1 = Radiobutton(GUI, text="Thực phẩm", variable = varRadioButton, value = 1, anchor = S, width = 10)
    R1.grid(row = 12, column = 1)
    R1.select()

    R2 = Radiobutton(GUI, text="Dinh dưỡng", variable = varRadioButton, value = 2, anchor = S, width = 10)
    R2.grid(row = 12, column = 2)

    R3 = Radiobutton(GUI, text="Bệnh lý", variable = varRadioButton, value = 3, anchor = S, width = 0)
    R3.grid(row = 12, column = 3) 

    labelNo7 = Label(GUI, text = "Nhập tên:")
    labelNo7.grid(row = 13, column = 1, sticky = S)


    entryEntity = AutoCompleteEntry(bigList(conn), GUI, width = 60, borderwidth = 1)
    inputEntity = entryEntity
    entryEntity.grid(row = 13, column = 2, columnspan = 3, sticky = W)
    entryEntity.focus()
    
    labelNull5 = Label(GUI, text = "")
    labelNull5.grid(row = 14, column = 1)

    labelNo8 = Label(GUI, text = "Mô tả:")
    labelNo8.grid(row = 15, column = 1, sticky = S)

    entryDiscription = Entry(GUI, textvariable = inputDescription, width = 60, borderwidth = 1)
    entryDiscription.grid(row = 15, column = 2, columnspan = 3,  sticky = W)
    entryDiscription.focus()

    labelNull6 = Label(GUI, text = "")
    labelNull6.grid(row = 16, column = 1)

 
    textOutput_2 = Text(GUI, bg = "white", width = 60, height = 18,  wrap= WORD)
    textOutput_2.grid(row = 17, column = 0, columnspan = 4, rowspan = 1)


    def clickHandle_1():

        idTP = queryID_Food(conn, inputFood.get())
        if idTP == 0 and inputFood.get() != '':
            print(idTP)
            messagebox.showwarning("Không tồn tại dữ liệu","Tên này không phải tên thực phẩm hoặc chưa có trong cơ sở dữ liệu")
            flagFood = 0
        else:
            if inputFood.get() == '':
                flagFood = 1
            else:
                flagFood = 2

        idDD = queryID_Nutrition(conn, inputNutrition.get())
        if idDD == 0 and inputNutrition.get() != '':
            messagebox.showwarning("Không tồn tại dữ liệu","Tên này không phải chất dinh dưỡng hoặc chưa có trong cơ sở dữ liệu")
            flagNutrition = 0
        else:
            if inputNutrition.get() == '':
                flagNutrition = 1
            else:
                flagNutrition = 2

        idBL = queryID_Pathology(conn, inputPathology.get())
        if idBL == 0 and inputPathology.get() != '':
            messagebox.showwarning("Không tồn tại dữ liệu","Tên này không phải tên bệnh lý hoặc chưa có trong cơ sở dữ liệu")
            flagPathology = 0
        else:
            if inputPathology.get() == '':
                flagPathology = 1
            else:
                flagPathology = 2

        textOutput.delete(1.0, END)

        if flagFood == 2 and flagNutrition == 2:
            if (inputContent.get() != ''):
                row = queryTable_tp_vs_dd(conn, idTP, idDD)
                if row:
                    print('updateRow_tp_vs_dd')
                    updateRow_tp_vs_dd(conn, idTP, idDD, inputContent.get())
                else:
                    print('insertToTable_tp_vs_dd')
                    insertToTable_tp_vs_dd(conn, idTP, idDD, inputContent.get())
            textOutput.insert(INSERT, '- Hàm lượng ' + inputNutrition.get() + ' trong 100g ' + inputFood.get() + ' là: ' + inputContent.get() +'\n')

        if flagNutrition == 2 and flagPathology == 2:
            if (inputSuitability.get() != ''):
                row = queryTable_dd_vs_bl(conn, idDD, idBL)
                if row:
                    print('updateRow_dd_vs_bl')
                    updateRow_dd_vs_bl(conn, idDD, idBL, inputSuitability.get())
                else:
                    print("insertToTable_dd_vs_bl")
                    insertToTable_dd_vs_bl(conn, idDD, idBL, inputSuitability.get())
            textOutput.insert(INSERT, '- ' + inputNutrition.get() + ' ' + inputSuitability.get() + ' cho người mắc ' + inputPathology.get() +'\n')

        if flagFood == 2 and flagPathology == 2:
            if (inputRecommendation.get() != ''):
                row = queryTable_tp_vs_bl(conn, idTP, idBL)
                if row:
                    print('updateRow_tp_vs_bl')
                    updateRow_tp_vs_bl(conn, idTP, idBL, inputRecommendation.get())

                else:
                    print('insertToTable_tp_vs_bl')
                    insertToTable_tp_vs_bl(conn, idTP, idBL, inputRecommendation.get())
            textOutput.insert(INSERT, '- ' + 'Người mắc ' + inputPathology.get()+ ' ' + inputRecommendation.get() + ' ' + inputFood.get())

    def clickHandle_2():
        if(inputEntity.get() != ''):
            i = varRadioButton.get()
            if i == 1:
                idEntity = queryID_Food(conn, inputEntity.get())
                if idEntity:
                    desEntity = queryDes_Food(conn, inputEntity.get())
                    textOutput_2.delete(1.0, END)
                    textOutput_2.insert(INSERT, "Tên thực phẩm:\t " + inputEntity.get() + '\nMã số:\t\t' + str(idEntity) + '\nMô tả: ' + desEntity)
                else:
                    messagebox.showwarning("Dữ liệu không chính xác","Tên này không phải thực phẩm hoặc chưa có trong cơ sở dữ liệu")
            else:
                if i == 2:
                    idEntity = queryID_Nutrition(conn, inputEntity.get())
                    if idEntity:
                        desEntity = queryDes_Nutrition(conn, inputEntity.get())
                        textOutput_2.delete(1.0, END)
                        textOutput_2.insert(INSERT, "Tên dinh dưỡng:\t " + inputEntity.get() + '\nMã số:\t\t ' + str(idEntity) + '\nMô tả: ' + desEntity)
                    else:
                        messagebox.showwarning("Dữ liệu không chính xác","Tên này không phải chất dinh dưỡng hoặc chưa có trong cơ sở dữ liệu")
                else :
                    if i == 3:
                        idEntity = queryID_Pathology(conn, inputEntity.get())
                        if idEntity:
                            desEntity = queryDes_Pathology(conn, inputEntity.get())
                            textOutput_2.delete(1.0, END)
                            textOutput_2.insert(INSERT, "Tên bệnh lý:\t   " + inputEntity.get() + '\nMã số:\t\t' + str(idEntity) + '\nMô tả: ' + desEntity)            
                        else:
                            messagebox.showwarning("Dữ liệu không chính xác","Tên này không phải tên bệnh lý hoặc chưa có trong cơ sở dữ liệu")

    def clickHandle_3():
        if(inputEntity.get() != ''):
            if(inputDescription.get() != ''):
                i = varRadioButton.get()
                if i == 1:
                    idEntity = queryID_Food(conn, inputEntity.get())
                    if idEntity:
                        updateRowTable_thuc_pham(conn, inputDescription.get(), idEntity)
                    else:
                        insertToTable_thuc_pham(conn, inputEntity.get(), inputDescription.get())
                        idEntity = queryID_Food(conn, inputEntity.get())
                    textOutput_2.delete(1.0, END)
                    textOutput_2.insert(INSERT, "Tên thực phẩm:\t " + inputEntity.get() + '\nMã số:\t\t' + str(idEntity) + '\nMô tả: ' + inputDescription.get())
                else:
                    if i == 2:
                        idEntity = queryID_Nutrition(conn, inputEntity.get())
                        if idEntity:
                            updateRowTable_dinh_duong(conn, inputDescription.get(), idEntity)
                        else:
                            insertToTable_dinh_duong(conn, inputEntity.get(), inputDescription.get())
                            idEntity = queryID_Nutrition(conn, inputEntity.get())
                        textOutput_2.delete(1.0, END)
                        textOutput_2.insert(INSERT, "Tên dinh dưỡng:\t " + inputEntity.get() + '\nMã số:\t\t ' + str(idEntity) + '\nMô tả: ' + inputDescription.get())
                    else :
                        if i == 3:
                            idEntity = queryID_Pathology(conn, inputEntity.get())
                            if idEntity:
                                updateRowTable_benh_ly(conn, inputDescription.get(), idEntity)
                            else:
                                insertToTable_benh_ly(conn, inputEntity.get(), inputDescription.get())
                                idEntity = queryID_Pathology(conn, inputEntity.get())
                            textOutput_2.delete(1.0, END)
                            textOutput_2.insert(INSERT, "Tên bệnh lý:\t   " + inputEntity.get() + '\nMã số:\t\t' + str(idEntity) + '\nMô tả: ' + inputDescription.get())

    def clickHandle_4():
        if(inputEntity.get() != ''):
            i = varRadioButton.get()
            if i == 1:
                idEntity = queryID_Food(conn, inputEntity.get())
                if idEntity:
                    deleteRowTable_thuc_pham(conn, idEntity)
                    delete_idTP_tp_vs_bl(conn, idEntity)
                    delete_idTP_tp_vs_dd(conn, idEntity)
                    textOutput_2.delete(1.0, END)
                    textOutput_2.insert(INSERT, inputEntity.get() + ' đã bị xóa khỏi cơ sở dữ liệu')
                else:
                    messagebox.showwarning("Không thể xóa","Tên này không phải thực phẩm hoặc chưa có trong cơ sở dữ liệu")
            else:
                if i == 2:
                    idEntity = queryID_Nutrition(conn, inputEntity.get())
                    if idEntity:
                        deleteRowTable_dinh_duong(conn, idEntity)
                        delete_idDD_dd_vs_bl(conn, idEntity)
                        delete_idDD_tp_vs_dd(conn, idEntity)
                        textOutput_2.delete(1.0, END)
                        textOutput_2.insert(INSERT, inputEntity.get() + ' đã bị xóa khỏi cơ sở dữ liệu')
                    else:
                        messagebox.showwarning("Không thể xóa","Tên này không phải chất dinh dưỡng hoặc chưa có trong cơ sở dữ liệu")
                else :
                    if i == 3:
                        idEntity = queryID_Pathology(conn, inputEntity.get())
                        if idEntity:
                            deleteRowTable_benh_ly(conn, idEntity)
                            delete_idBL_dd_vs_bl(conn, idEntity)
                            delete_idBL_tp_vs_bl(conn, idEntity)
                            textOutput_2.delete(1.0, END)
                            textOutput_2.insert(INSERT, inputEntity.get() + ' đã bị xóa khỏi cơ sở dữ liệu')
                        else:
                            messagebox.showwarning("Không thể xóa","Tên này không phải tên bệnh lý hoặc chưa có trong cơ sở dữ liệu")

    click = Button(GUI, text = 'Thêm cơ sở dữ liệu', command = clickHandle_1)
    click.grid(row = 9, column = 3, sticky = N)

    click_2 = Button(GUI, text = 'Tìm kiếm', width = 20, command = clickHandle_2)
    click_2.grid(row = 18, column = 1, columnspan = 1, sticky = S)

    click_3 = Button(GUI, text = 'Thêm/cập nhật đối tượng', width = 20, command = clickHandle_3)
    click_3.grid(row = 18, column = 2, columnspan = 1, sticky = S)

    click_4 = Button(GUI, text = 'Xóa đối tượng', width = 20, command = clickHandle_4)
    click_4.grid(row = 18, column = 3, columnspan = 1, sticky = S)

    print('hello world')
    GUI.mainloop()
    print('over the world')
if __name__ == '__main__':
    designGUI()
    print('PP world')