from tkinter import messagebox
from tkinter import *
from tkinter import Tk
from tkinter import ttk
import sqlite3


window = Tk()

con = sqlite3.connect("Daro.db")
cur = con.cursor()


# --------------------------------------------------------------------------تابع ها---


def namayesh_esm():

    cur.execute("SELECT esm FROM user ORDER BY id DESC LIMIT 1")
    result = cur.fetchone()

    if result:
        return result[0]
    else:
        return ""


#تابع ثبت اسم خوشامدگویی
def sabt_esm():
    esm = txt1.get().strip()

    if esm == "":
        messagebox.showwarning("خطا", "لطفاً اسمت را وارد کن.")
    else:

        cur.execute(
            "INSERT INTO user (esm) VALUES (?)",
            (esm,)
        )

        con.commit()

        messagebox.showinfo("ثبت اطلاعات", esm + " عزیز، با موفقیت اسمت ثبت شد.")
        top_khoshamad.destroy()

# پنجره اسم گرفتن
top_khoshamad = Toplevel(window)
top_khoshamad.title("خوش آمدید")
top_khoshamad.geometry("500x230")
top_khoshamad.resizable(False, False)
top_khoshamad.configure(bg="#DCEDC8")
top_khoshamad.transient(window)
top_khoshamad.grab_set()

lb1 = Label(top_khoshamad, text="😍💊 به برنامه یادآور دارو خوش اومدی", bg="#DCEDC8", font=("Arial",16,"bold"))
lb1.pack(pady=15)

lb2 = Label(top_khoshamad, text="لطفا اسمتو بگو تا زمان مصرف داروهات رو بهت یادآوری کنم.", bg="#DCEDC8", font=("Arial",12))
lb2.pack(pady=5)

txt1 = Entry(top_khoshamad, font=("Arial",12), width=25)
txt1.pack(pady=10)

btn1 = Button(top_khoshamad, text="بزن بریم", font=("Arial",11), bg="#B5C896", fg="black", command=sabt_esm)
btn1.pack(pady=15)

#---------------------------------------------------------------------------------------

def afzoodan_daro():

    top_afzoodan = Toplevel(window)
    top_afzoodan.title("افزودن دارو")
    top_afzoodan.geometry("500x390")
    top_afzoodan.resizable(False, False)
    top_afzoodan.configure(bg="#CFE8FF")
    top_afzoodan.transient(window)
    top_afzoodan.grab_set()

    def sabt_daro():
        if txt_daro.get() == "" or cmb_meghdar.get() == "" or cmb_tedad.get() == "":
            messagebox.showwarning("خطا", "لطفاً تمام اطلاعات را وارد کنید.")
        else:
            cur.execute(
                "INSERT INTO afzodan_daroha (name_daro, meghdar, tedad, tozihat) VALUES (?, ?, ?, ?)",
                (txt_daro.get(), cmb_meghdar.get(), cmb_tedad.get(), txt_tozih.get())
            )

            con.commit()
            messagebox.showinfo("ثبت دارو", "دارو با موفقیت ثبت شد.")

            txt_daro.delete(0, END)
            cmb_meghdar.set("")
            cmb_tedad.set("")
            txt_tozih.delete(0, END)
            txt_daro.focus()

    lb1 = Label(top_afzoodan, text="💊 افزودن دارو", bg="#CFE8FF", font=("Arial",16,"bold"))
    lb1.grid(row=0, column=0, columnspan=2, pady=15)

    lb2 = Label(top_afzoodan, text="نام دارو:", bg="#CFE8FF", font=("Arial",12))
    lb2.grid(row=1, column=0, padx=10, pady=8, sticky="e")

    txt_daro = Entry(top_afzoodan, width=30, font=("Arial",12))
    txt_daro.grid(row=1, column=1, padx=10, pady=8)

    lb3 = Label(top_afzoodan, text="مقدار مصرف:", bg="#CFE8FF", font=("Arial",12))
    lb3.grid(row=2, column=0, padx=10, pady=8, sticky="e")

    cmb_meghdar = ttk.Combobox(top_afzoodan, width=28, state="readonly")
    cmb_meghdar["values"] = ("نصف","1 عدد","2 عدد","1 قاشق سوپ خوری","2 قاشق سوپ خوری","1 قاشق غذاخوری","2 قاشق غذاخوری")
    cmb_meghdar.grid(row=2, column=1, padx=10, pady=8)

    lb4 = Label(top_afzoodan, text="تعداد دفعات مصرف در روز:", bg="#CFE8FF", font=("Arial",12))
    lb4.grid(row=3, column=0, padx=10, pady=8, sticky="e")

    cmb_tedad = ttk.Combobox(top_afzoodan, width=28, state="readonly")
    cmb_tedad["values"] = ("1 بار","2 بار","3 بار","4 بار","5 بار")
    cmb_tedad.grid(row=3, column=1, padx=10, pady=8)

    lb5 = Label(top_afzoodan, text="توضیحات:", bg="#CFE8FF", font=("Arial",12))
    lb5.grid(row=4, column=0, padx=10, pady=8, sticky="e")

    txt_tozih = Entry(top_afzoodan, width=30, font=("Arial",12))
    txt_tozih.grid(row=4, column=1, padx=10, pady=8)

    btn1 = Button(top_afzoodan, text="ثبت دارو", bg="#A8CAEB", font=("Arial",11), command=sabt_daro)
    btn1.grid(row=5, column=0, columnspan=2, pady=20)

#--------------------------------------------------------------------------------------------

def virayesh_daro():

    top_virayesh = Toplevel(window)
    top_virayesh.title("ویرایش دارو")
    top_virayesh.geometry("500x420")
    top_virayesh.resizable(False, False)
    top_virayesh.configure(bg="#CFE8FF")
    top_virayesh.transient(window)
    top_virayesh.grab_set()

    def virayesh():

        if cmb_daro.get() == "" or txt_new.get() == "":
            messagebox.showwarning("خطا", "لطفاً نام دارو را وارد کنید.")
        else:
            cur.execute(
                "UPDATE afzodan_daroha SET name_daro=?, meghdar=?, tedad=?, tozihat=? WHERE name_daro=?",
                (txt_new.get(), cmb_meghdar.get(), cmb_tedad.get(), txt_tozih.get(), cmb_daro.get())
            )

            con.commit()

            messagebox.showinfo("ویرایش دارو", "دارو با موفقیت ویرایش شد.")

            txt_new.delete(0, END)
            cmb_daro.set("")
            cmb_meghdar.set("")
            cmb_tedad.set("")
            txt_tozih.delete(0, END)

    lb1 = Label(top_virayesh, text="✏ ویرایش دارو", bg="#CFE8FF", font=("Arial",16,"bold"))
    lb1.grid(row=0, column=0, columnspan=2, pady=15)

    lb2 = Label(top_virayesh, text="نام دارو:", bg="#CFE8FF", font=("Arial",12))
    lb2.grid(row=1, column=0, padx=10, pady=8, sticky="e")

    cur.execute("SELECT name_daro FROM afzodan_daroha")
    cmb_daro = ttk.Combobox(top_virayesh, width=28, state="readonly")
    cmb_daro["values"] = [i[0] for i in cur.fetchall()]
    cmb_daro.grid(row=1, column=1, padx=10, pady=8)

    lb3 = Label(top_virayesh, text="نام جدید:", bg="#CFE8FF", font=("Arial",12))
    lb3.grid(row=2, column=0, padx=10, pady=8, sticky="e")

    txt_new = Entry(top_virayesh, width=30, font=("Arial",12))
    txt_new.grid(row=2, column=1, padx=10, pady=8)

    lb4 = Label(top_virayesh, text="مقدار مصرف:", bg="#CFE8FF", font=("Arial",12))
    lb4.grid(row=3, column=0, padx=10, pady=8, sticky="e")

    cmb_meghdar = ttk.Combobox(top_virayesh, width=28, state="readonly")
    cmb_meghdar["values"] = ("نصف","1 عدد","2 عدد","1 قاشق سوپ خوری","2 قاشق سوپ خوری","1 قاشق غذاخوری","2 قاشق غذاخوری")
    cmb_meghdar.grid(row=3, column=1, padx=10, pady=8)

    lb5 = Label(top_virayesh, text="تعداد دفعات مصرف در روز:", bg="#CFE8FF", font=("Arial",12))
    lb5.grid(row=4, column=0, padx=10, pady=8, sticky="e")

    cmb_tedad = ttk.Combobox(top_virayesh, width=28, state="readonly")
    cmb_tedad["values"] = ("1 بار","2 بار","3 بار","4 بار","5 بار")
    cmb_tedad.grid(row=4, column=1, padx=10, pady=8)

    lb6 = Label(top_virayesh, text="توضیحات:", bg="#CFE8FF", font=("Arial",12))
    lb6.grid(row=5, column=0, padx=10, pady=8, sticky="e")

    txt_tozih = Entry(top_virayesh, width=30, font=("Arial",12))
    txt_tozih.grid(row=5, column=1, padx=10, pady=8)

    btn1 = Button(top_virayesh, text="ذخیره تغییرات", bg="#A8CAEB", font=("Arial",11), command=virayesh)
    btn1.grid(row=6, column=0, columnspan=2, pady=20)

#--------------------------------------------------------------------------------------------

def hazf_daro():

    top_hazf = Toplevel(window)
    top_hazf.title("حذف دارو")
    top_hazf.geometry("500x220")
    top_hazf.resizable(False, False)
    top_hazf.configure(bg="#CFE8FF")
    top_hazf.transient(window)
    top_hazf.grab_set()

    def hazf():

        if cmb_daro.get() == "":
            messagebox.showwarning("خطا", "لطفاً نام دارو را انتخاب کنید.")
        else:
            cur.execute(
                "DELETE FROM afzodan_daroha WHERE name_daro=?",
                (cmb_daro.get(),)
            )

            con.commit()

            messagebox.showinfo("حذف دارو", "دارو با موفقیت حذف شد.")

            cur.execute("SELECT name_daro FROM afzodan_daroha")
            cmb_daro["values"] = [i[0] for i in cur.fetchall()]
            cmb_daro.set("")

    lb1 = Label(top_hazf, text="🗑 حذف دارو", bg="#CFE8FF", font=("Arial",16,"bold"))
    lb1.grid(row=0, column=0, columnspan=2, pady=15)

    lb2 = Label(top_hazf, text="نام دارو:", bg="#CFE8FF", font=("Arial",12))
    lb2.grid(row=1, column=0, padx=10, pady=15, sticky="e")

    cur.execute("SELECT name_daro FROM afzodan_daroha")
    cmb_daro = ttk.Combobox(top_hazf, width=28, state="readonly")
    cmb_daro["values"] = [i[0] for i in cur.fetchall()]
    cmb_daro.grid(row=1, column=1, padx=10, pady=15)

    btn1 = Button(top_hazf, text="حذف دارو", bg="#A8CAEB", font=("Arial",11), command=hazf)
    btn1.grid(row=2, column=0, columnspan=2, pady=20)


#------------------------------------------------------------------------------------------

def list_daroha():

    top_list = Toplevel(window)
    top_list.title("لیست داروها")
    top_list.geometry("750x350")
    top_list.resizable(False, False)
    top_list.configure(bg="#CFE8FF")
    top_list.transient(window)
    top_list.grab_set()

    lb1 = Label(top_list, text="📋 لیست داروها", bg="#CFE8FF", font=("Arial",16,"bold"))
    lb1.pack(pady=10)

    txt_list = Text(top_list, width=80, height=12, font=("Arial", 11))
    txt_list.pack(pady=10)

    cur.execute("SELECT name_daro, meghdar, tedad, tozihat FROM afzodan_daroha")

    for row in cur.fetchall():
        txt_list.insert(
            END,
            f"نام دارو: {row[0]}   |  مقدار مصرف: {row[1]}   |    دفعات مصرف: {row[2]}   |    توضیحات: {row[3]}\n"
        )
        txt_list.insert(END, "-" * 127 + "\n")

    txt_list.config(state="disabled")   # این یعنی کاربر نتونه چیزی داخلش تایپ کنه
    
#------------------------------------------------------------------------------------------

def sabt_zaman():

    top_zaman = Toplevel(window)
    top_zaman.title("ثبت زمان مصرف")
    top_zaman.geometry("500x350")
    top_zaman.resizable(False, False)
    top_zaman.configure(bg="#CFE8FF")
    top_zaman.transient(window)
    top_zaman.grab_set()

    def sabt():

        if cmb_daro.get() == "" or cmb_saat.get() == "" or cmb_daghighe.get() == "" or txt_tarikh.get() == "":
            messagebox.showwarning("خطا", "لطفاً تمام اطلاعات را وارد کنید.")

        else:

            zaman = cmb_saat.get() + ":" + cmb_daghighe.get()

            cur.execute(
                "INSERT INTO yadavari(name_daro, zaman, tarikh) VALUES(?,?,?)",
                (cmb_daro.get(), zaman, txt_tarikh.get())
            )

            con.commit()

            messagebox.showinfo("ثبت", "زمان مصرف با موفقیت ثبت شد.")

            cmb_daro.set("")
            cmb_saat.set("")
            cmb_daghighe.set("")
            txt_tarikh.delete(0, END)

    lb1 = Label(top_zaman, text="⏰ ثبت زمان مصرف", bg="#CFE8FF", font=("Arial",16,"bold"))
    lb1.grid(row=0, column=0, columnspan=2, pady=15)

    lb2 = Label(top_zaman, text="نام دارو:", bg="#CFE8FF", font=("Arial",12))
    lb2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    cur.execute("SELECT name_daro FROM afzodan_daroha")

    cmb_daro = ttk.Combobox(top_zaman, width=28, state="readonly")
    cmb_daro["values"] = [i[0] for i in cur.fetchall()]
    cmb_daro.grid(row=1, column=1, padx=10, pady=10)

    lb3 = Label(top_zaman, text="ساعت مصرف:", bg="#CFE8FF", font=("Arial",12))
    lb3.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    frame_zaman = Frame(top_zaman, bg="#CFE8FF")
    frame_zaman.grid(row=2, column=1, padx=10, pady=10)

    cmb_saat = ttk.Combobox(frame_zaman, width=8, state="readonly")
    cmb_saat["values"] = (
        "00","01","02","03","04","05","06","07","08","09","10","11",
        "12","13","14","15","16","17","18","19","20","21","22","23"
    )
    cmb_saat.grid(row=0, column=0)

    lb4 = Label(frame_zaman, text=":", bg="#CFE8FF", font=("Arial",12,"bold"))
    lb4.grid(row=0, column=1)

    cmb_daghighe = ttk.Combobox(frame_zaman, width=8, state="readonly")
    cmb_daghighe["values"] = (
        "00","05","10","15","20","25","30","35","40","45","50","55"
    )
    cmb_daghighe.grid(row=0, column=2)

    lb5 = Label(top_zaman, text="تاریخ شروع:", bg="#CFE8FF", font=("Arial",12))
    lb5.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    txt_tarikh = Entry(top_zaman, width=30, font=("Arial",12))
    txt_tarikh.grid(row=3, column=1, padx=10, pady=10)

    btn1 = Button(top_zaman, text="ثبت", bg="#A8CAEB", font=("Arial",11), command=sabt)
    btn1.grid(row=4, column=0, columnspan=2, pady=20)

#------------------------------------------------------------------------------------------

def virayesh_zaman():

    top_virayesh = Toplevel(window)
    top_virayesh.title("ویرایش زمان مصرف")
    top_virayesh.geometry("500x350")
    top_virayesh.resizable(False, False)
    top_virayesh.configure(bg="#CFE8FF")
    top_virayesh.transient(window)
    top_virayesh.grab_set()

    def virayesh():

        if cmb_daro.get() == "" or cmb_saat.get() == "" or cmb_daghighe.get() == "":
            messagebox.showwarning("خطا", "لطفاً نام دارو و ساعت را وارد کنید.")

        else:

            zaman = cmb_saat.get() + ":" + cmb_daghighe.get()

            if txt_tarikh.get() == "":

                cur.execute(
                    "UPDATE yadavari SET zaman=? WHERE name_daro=?",
                    (zaman, cmb_daro.get())
                )

            else:

                cur.execute(
                    "UPDATE yadavari SET zaman=?, tarikh=? WHERE name_daro=?",
                    (zaman, txt_tarikh.get(), cmb_daro.get())
                )

            con.commit()

            messagebox.showinfo("ویرایش", "زمان مصرف با موفقیت ویرایش شد.")

            cmb_daro.set("")
            cmb_saat.set("")
            cmb_daghighe.set("")
            txt_tarikh.delete(0, END)

    lb1 = Label(top_virayesh, text="✏ ویرایش زمان مصرف", bg="#CFE8FF", font=("Arial",16,"bold"))
    lb1.grid(row=0, column=0, columnspan=2, pady=15)

    lb2 = Label(top_virayesh, text="نام دارو:", bg="#CFE8FF", font=("Arial",12))
    lb2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    cur.execute("SELECT name_daro FROM yadavari")

    cmb_daro = ttk.Combobox(top_virayesh, width=28, state="readonly")
    cmb_daro["values"] = [i[0] for i in cur.fetchall()]
    cmb_daro.grid(row=1, column=1, padx=10, pady=10)

    lb3 = Label(top_virayesh, text="ساعت جدید:", bg="#CFE8FF", font=("Arial",12))
    lb3.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    frame_zaman = Frame(top_virayesh, bg="#CFE8FF")
    frame_zaman.grid(row=2, column=1, padx=10, pady=10)

    cmb_saat = ttk.Combobox(frame_zaman, width=8, state="readonly")
    cmb_saat["values"] = (
        "00","01","02","03","04","05","06","07","08","09","10","11",
        "12","13","14","15","16","17","18","19","20","21","22","23"
    )
    cmb_saat.grid(row=0, column=0)

    Label(frame_zaman, text=":", bg="#CFE8FF", font=("Arial",12,"bold")).grid(row=0, column=1)

    cmb_daghighe = ttk.Combobox(frame_zaman, width=8, state="readonly")
    cmb_daghighe["values"] = (
        "00","05","10","15","20","25","30","35","40","45","50","55"
    )
    cmb_daghighe.grid(row=0, column=2)

    lb4 = Label(top_virayesh, text="تاریخ جدید:", bg="#CFE8FF", font=("Arial",12))
    lb4.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    txt_tarikh = Entry(top_virayesh, width=30, font=("Arial",12))
    txt_tarikh.grid(row=3, column=1, padx=10, pady=10)

    btn1 = Button(top_virayesh, text="ذخیره تغییرات", bg="#A8CAEB", font=("Arial",11), command=virayesh)
    btn1.grid(row=4, column=0, columnspan=2, pady=20)

#------------------------------------------------------------------------------------------

def hazf_yadavari():

    top_hazf = Toplevel(window)
    top_hazf.title("حذف یادآوری")
    top_hazf.geometry("500x220")
    top_hazf.resizable(False, False)
    top_hazf.configure(bg="#CFE8FF")
    top_hazf.transient(window)
    top_hazf.grab_set()

    def hazf():

        if cmb_daro.get() == "":
            messagebox.showwarning("خطا", "لطفاً نام دارو را انتخاب کنید.")

        else:

            cur.execute(
                "DELETE FROM yadavari WHERE name_daro=?",
                (cmb_daro.get(),)
            )

            con.commit()

            messagebox.showinfo("حذف", "یادآوری با موفقیت حذف شد.")

            cur.execute("SELECT name_daro FROM yadavari")

            cmb_daro["values"] = [i[0] for i in cur.fetchall()]
            cmb_daro.set("")

    lb1 = Label(top_hazf, text="🗑 حذف یادآوری", bg="#CFE8FF", font=("Arial",16,"bold"))
    lb1.grid(row=0, column=0, columnspan=2, pady=15)

    lb2 = Label(top_hazf, text="نام دارو:", bg="#CFE8FF", font=("Arial",12))
    lb2.grid(row=1, column=0, padx=10, pady=15, sticky="e")

    cur.execute("SELECT name_daro FROM yadavari")

    cmb_daro = ttk.Combobox(top_hazf, width=28, state="readonly")
    cmb_daro["values"] = [i[0] for i in cur.fetchall()]
    cmb_daro.grid(row=1, column=1, padx=10, pady=15)

    btn1 = Button(top_hazf, text="حذف یادآوری", bg="#A8CAEB", font=("Arial",11), command=hazf)
    btn1.grid(row=2, column=0, columnspan=2, pady=20)

#------------------------------------------------------------------------------------------

def sabt_vaziyat():

    top_vaziyat = Toplevel(window)
    top_vaziyat.title("ثبت وضعیت مصرف")
    top_vaziyat.geometry("500x280")
    top_vaziyat.resizable(False, False)
    top_vaziyat.configure(bg="#CFE8FF")
    top_vaziyat.transient(window)
    top_vaziyat.grab_set()

    def sabt():

        if cmb_daro.get() == "":
            messagebox.showwarning("خطا", "لطفاً نام دارو را انتخاب کنید.")

        else:

            cur.execute(
                "INSERT INTO tarikheche(name_daro, vaziyat) VALUES(?,?)",
                (cmb_daro.get(), vaziyat.get())
            )

            con.commit()

            messagebox.showinfo("ثبت وضعیت", "وضعیت مصرف با موفقیت ثبت شد.")

            cmb_daro.set("")
            vaziyat.set("مصرف شده")

    lb1 = Label(top_vaziyat, text="📝 ثبت وضعیت مصرف", bg="#CFE8FF", font=("Arial",16,"bold"))
    lb1.grid(row=0, column=0, columnspan=3, pady=15)

    lb2 = Label(top_vaziyat, text="نام دارو:", bg="#CFE8FF", font=("Arial",12))
    lb2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    cur.execute("SELECT name_daro FROM afzodan_daroha")

    cmb_daro = ttk.Combobox(top_vaziyat, width=28, state="readonly")
    cmb_daro["values"] = [i[0] for i in cur.fetchall()]
    cmb_daro.grid(row=1, column=1, padx=10, pady=10)

    lb3 = Label(top_vaziyat, text="وضعیت:", bg="#CFE8FF", font=("Arial",12))
    lb3.grid(row=2, column=0, padx=10, pady=10, sticky="ne")

    vaziyat = StringVar()
    vaziyat.set("مصرف شده")

    rb1 = Radiobutton(top_vaziyat, text="مصرف شده",variable=vaziyat, value="مصرف شده", bg="#CFE8FF",font=("Arial",11))
    rb1.grid(row=2, column=1, sticky="w")

    rb2 = Radiobutton(top_vaziyat, text="مصرف نشده", variable=vaziyat,value="مصرف نشده", bg="#CFE8FF", font=("Arial",11))
    rb2.grid(row=3, column=1, sticky="w")

    btn1 = Button(top_vaziyat, text="ثبت وضعیت", bg="#A8CAEB", font=("Arial",11), command=sabt)
    btn1.grid(row=4, column=0, columnspan=2, pady=20)

#-----------------------------------------------------------------------------------------

def masraf_shode():

    top_list = Toplevel(window)
    top_list.title("لیست مصرف شده ها")
    top_list.geometry("500x350")
    top_list.resizable(False, False)
    top_list.configure(bg="#CFE8FF")
    top_list.transient(window)
    top_list.grab_set()

    lb1 = Label(top_list, text="✅ لیست مصرف شده ها", bg="#CFE8FF", font=("Arial",16,"bold"))
    lb1.pack(pady=10)

    txt_list = Text(top_list, width=55, height=12, font=("Arial",11))
    txt_list.pack(pady=10)

    cur.execute("SELECT name_daro FROM tarikheche WHERE vaziyat='مصرف شده'")

    for row in cur.fetchall():
        txt_list.insert(END, row[0] + "\n")

    txt_list.config(state="disabled")

#-----------------------------------------------------------------------------------------

def masraf_nashode():

    top_list = Toplevel(window)
    top_list.title("لیست مصرف نشده ها")
    top_list.geometry("500x350")
    top_list.resizable(False, False)
    top_list.configure(bg="#CFE8FF")
    top_list.transient(window)
    top_list.grab_set()

    lb1 = Label(top_list, text="❌ لیست مصرف نشده ها", bg="#CFE8FF", font=("Arial",16,"bold"))
    lb1.pack(pady=10)

    txt_list = Text(top_list, width=55, height=12, font=("Arial",11))
    txt_list.pack(pady=10)

    cur.execute("SELECT name_daro FROM tarikheche WHERE vaziyat='مصرف نشده'")

    for row in cur.fetchall():
        txt_list.insert(END, row[0] + "\n")

    txt_list.config(state="disabled")

#-----------------------------------------------------------------------------------------

def aboutme():

    top_about = Toplevel(window)
    top_about.title("درباره ما")
    top_about.geometry("500x350")
    top_about.resizable(False, False)
    top_about.configure(bg="#CFE8FF")
    top_about.transient(window)
    top_about.grab_set()

    Label(top_about, text=" اپلیکیشن یاداور دارو ", bg="#CFE8FF", fg="#1565C0", font=("Arial", 20, "bold")).pack(pady=15)

    (Label(top_about, text="طراح و برنامه نویس: شهناز امیری ", bg="#CFE8FF", fg="black", font=("Arial", 12, "bold"))
    .pack( pady=3))

    (Label(top_about, text="رشته تحصیلی: مهندسی کامپیوتر", bg="#CFE8FF", fg="black", font=("Arial", 12, "bold"))
    .pack( pady=3))

    Label(top_about, text="دانشگاه: فنی و حرفه ای دختران کاشان ", bg="#CFE8FF", fg="black",
          font=("Arial", 12, "bold")).pack(pady=3)

    Label(top_about, text="درس: توسعه نرم افزار ", bg="#CFE8FF", fg="black", font=("Arial", 12, "bold")).pack(pady=3)

    Label(top_about, text="استاد: سرکار خانم دکتر نسرین اسدی ", bg="#CFE8FF", fg="black", font=("Arial", 12, "bold")).pack( pady=3)

    Label(top_about, text="( این برنامه جهت مدیریت و یادآوری زمان مصرف داروها طراحی شده است. )", bg="#CFE8FF", font=("Arial",12, "bold"), wraplength=420, justify="center").pack(pady=10)

    Label(top_about, text="نسخه: 1.0", bg="#CFE8FF", font=("Arial",12)).pack(pady=3)

    Button(top_about, text="بستن", bg="#A8CAEB", font=("Arial",11), command=top_about.destroy).pack(pady=15)

#-----------------------------------------------------------------------------------------

def settings():
    def bg1():
        global bg_image

        bg_image = PhotoImage(file="bagmain.png")
        bg_label.config(image=bg_image)

    def bg2():
        global bg_image

        bg_image = PhotoImage(file="bag2.png")
        bg_label.config(image=bg_image)

    def bg3():
        global bg_image

        bg_image = PhotoImage(file="bag3.png")
        bg_label.config(image=bg_image)

    def bg4():
        global bg_image

        bg_image = PhotoImage(file="bag1.png")
        bg_label.config(image=bg_image)


    top_setting = Toplevel(window)
    top_setting.title("تنظیمات")
    top_setting.geometry("450x240")
    top_setting.resizable(False, False)
    top_setting.configure(bg="#CFE8FF")
    top_setting.transient(window)
    top_setting.grab_set()

    lb1 = Label(top_setting, text="⚙ تنظیمات", bg="#CFE8FF", fg="#1565C0", font=("Arial",16,"bold"))
    lb1.pack(pady=15)


    lb3 = Label(top_setting, text=" تغییر پس زمینه", bg="#CFE8FF", font=("Arial",12,"bold"))
    lb3.pack(pady=15)

    frame2 = Frame(top_setting, bg="#CFE8FF")
    frame2.pack()

    Button(frame2, text="پس زمینه ۱", bg="#A8CAEB", width=10, command=bg1).grid(row=0, column=0, padx=5)

    Button(frame2, text="پس زمینه ۲", bg="#A8CAEB", width=10, command=bg2).grid(row=0, column=1, padx=5)

    Button(frame2, text="پس زمینه ۳", bg="#A8CAEB", width=10, command=bg3).grid(row=0, column=2, padx=5)

    Button(frame2, text="پس زمینه ۴", bg="#A8CAEB", width=10, command=bg4).grid(row=0, column=3, padx=5)

    Button(top_setting, text="بستن", bg="#A8CAEB", font=("Arial",11), width=15,
           command=top_setting.destroy).pack(pady=20)

#-----------------------------------------------------------------------------------------

window.title("اپلیکیشن یادآور دارو")
window.geometry("800x500")
window.resizable(width=False, height=False)

# بگگراند اپ
bg_image = PhotoImage(file="bagmain.png")
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0)

esm_karbar = namayesh_esm()
lb_esm = Label( window, text="" + esm_karbar + " عزیز، خوش آمدی",bg="#F8BBD0",fg="black", font=("Arial",12,"bold")
)
lb_esm.place(x=520, y=40)

#---------------------------------------------------------------------------
# منو
menobar = Menu(window)
window.configure(menu=menobar)

menobar.add_cascade(label="صفحه اصلی")

#-----------------------------------------------------------------------------

daro_menu = Menu(menobar, tearoff=0)
daro_menu.add_command(label="افزودن دارو", command=afzoodan_daro)
daro_menu.add_command(label="ویرایش دارو", command=virayesh_daro)
daro_menu.add_command(label="حذف دارو", command=hazf_daro)
daro_menu.add_command(label="لیست داروها", command=list_daroha)
menobar.add_cascade(label="داروها", menu=daro_menu)



#---------------------------------------------------------------------------------

yadavar_menu = Menu(menobar, tearoff=0)
yadavar_menu.add_command(label="ثبت زمان مصرف", command=sabt_zaman)
yadavar_menu.add_command(label="ویرایش زمان", command=virayesh_zaman)
yadavar_menu.add_command(label="حذف یادآوری", command=hazf_yadavari)
menobar.add_cascade(label="یادآوری ها", menu=yadavar_menu)

#-----------------------------------------------------------------------------------

vaziyat_menu = Menu(menobar, tearoff=0)
vaziyat_menu.add_command(label="ثبت وضعیت مصرف", command=sabt_vaziyat)
vaziyat_menu.add_command(label="لیست مصرف شده ها", command=masraf_shode)
vaziyat_menu.add_command(label="لیست مصرف نشده ها", command=masraf_nashode)
menobar.add_cascade(label="وضعیت", menu=vaziyat_menu)

menobar.add_command(label="درباره ما", command=aboutme)
menobar.add_command(label=" تنظیمات", command=settings)
menobar.add_command(label="خروج", command=window.destroy)








window.mainloop()