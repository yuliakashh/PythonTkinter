import tkinter as tk                      #внешний вид окна
window = tk.Tk()
window.title("Приложение ЭСМ-5")
window.geometry('900x800+10+10')
nazv=tk.Label(window,text='ЭСМ-5',font=('Arrial', 20,'bold'))
nazv.grid(row=0,column=0)
card=tk.Label(window,text='Карта №')
card.grid(row=2,column=0)
ecard=tk.Entry(window)
ecard.grid(row=2,column=1,stick='w')
naim=tk.Label(window,text='Машина')
naim.grid(row=3,column=0)
enaim=tk.Entry(window)
enaim.grid(row=3,column=1,stick='w')
mark=tk.Label(window,text='     Марка')
mark.grid(row=3,column=2,stick='w')
emark=tk.Entry(window)
emark.grid(row=3,column=3,stick='w')
invnom=tk.Label(window,text='Инвентарный номер')
invnom.grid(row=4,column=0)
einvnom=tk.Entry(window)
einvnom.grid(row=4,column=1,stick='w')
zavnom=tk.Label(window,text='     Заводской номер')
zavnom.grid(row=4,column=2,stick='w')
ezavnom=tk.Entry(window)
ezavnom.grid(row=4,column=3,stick='w')
god=tk.Label(window,text='Год выпуска')
god.grid(row=4,column=4,stick='w')
egod=tk.Entry(window)
egod.grid(row=4,column=5,stick='w')
god=tk.Label(window,text='Период работы')
god.grid(row=5,column=0)
c=tk.Label(window,text='c')
c.grid(row=6,column=0)
ec=tk.Entry(window)
ec.grid(row=6,column=1,stick='e')
po=tk.Label(window,text='по')
po.grid(row=6,column=2)
epo=tk.Entry(window)
epo.grid(row=6,column=3,stick='e')
nomrap=tk.Label(window,text='Номер рапорта')
nomrap.grid(row=7,column=0)
enomrap=tk.Entry(window)
enomrap.grid(row=7,column=1,stick='e')
smen=tk.Label(window,text='Сменность')
smen.grid(row=8,column=0)
smenrad=tk.IntVar()
def radio():
    level=smenrad.get()
tk.Radiobutton(window,text='1', variable=smenrad,value=1,command=radio).grid(row=9,column=0)
tk.Radiobutton(window,text='2', variable=smenrad,value=2,command=radio).grid(row=9,column=1)
tk.Radiobutton(window,text='3', variable=smenrad,value=3,command=radio).grid(row=9,column=2)
tk.Radiobutton(window,text='4', variable=smenrad,value=4,command=radio).grid(row=9,column=3)
kold=tk.Label(window,text='Количество дней:')
kold.grid(row=10,column=0)
prebhoz=tk.Label(window,text='Пребывания в хозяйстве')
prebhoz.grid(row=11,column=0)
eprebhoz=tk.Entry(window)
eprebhoz.grid(row=11,column=1,stick='e')
vrab=tk.Label(window,text='В работе')
vrab.grid(row=11,column=2)
evrab=tk.Entry(window)
evrab.grid(row=11,column=3,stick='e')
vyh=tk.Label(window,text='Выходных и праздничных')
vyh.grid(row=11,column=4)
evyh=tk.Entry(window)
evyh.grid(row=11,column=5)
otrab=tk.Label(window,text='Отработано машиночасов')
otrab.grid(row=12,column=0)
eotrab=tk.Entry(window)
eotrab.grid(row=12,column=1)
reasonp=tk.Label(window,text='Простои по причинам, ч')
reasonp.grid(row=13,column=0)
reason=('Неисправность машины','Техническое обслуживание','Внеплановый ремонт','Отсутствие горюче-смазочных материалов','Перебазирование и переоборудование машины','Отсутствие машиниста','Отсутствия материалов и конструкций','Необеспеченность подъездных путей','Отсутствие силовой энергии и освещения','Прочие')
from tkinter import ttk
cbreason1=ttk.Combobox(window,state="readonly",values=reason)
cbreason1.current(0)
cbreason1.grid(row=15,column=0)
cbreason2=ttk.Combobox(window,state="readonly",values=reason)
cbreason2.current(0)
cbreason2.grid(row=15,column=3)
ereasonh1=tk.Entry(window)
ereasonh1.grid(row=15,column=2)
ereasonh2=tk.Entry(window)
ereasonh2.grid(row=15,column=5)
reasonh=tk.Label(window,text='Продолжительность, ч')
reasonh.grid(row=15,column=1)
reasonh2=tk.Label(window,text='Продолжительность, ч')
reasonh2.grid(row=15,column=4)
ereasonh=tk.Entry(window)
vrrab=tk.Label(window,text='Время работы двигателя, ч')
vrrab.grid(row=17,column=0)
evrrab=tk.Entry(window)
evrrab.grid(row=17,column=1)
prob=tk.Label(window,text='Пробег, км')
prob.grid(row=18,column=0)
eprob=tk.Entry(window)
eprob.grid(row=18, column=1)
#def get_entry():
    #numcard = ecard.get()
#делаем запись в сsv файл
main_lst=[]

def Add():                       #запись функция для создания списка из списков
   lst=['Карта №',ecard.get()]         #для записи в csv
   main_lst.append(lst)
   lst2=['Машина',enaim.get()]
   main_lst.append(lst2)
   lst3 = ['Марка', emark.get()]
   main_lst.append(lst3)
   lst4 = ['Инвентарный номер', einvnom.get()]
   main_lst.append(lst4)
   lst5 = ['Заводской номер', ezavnom.get()]
   main_lst.append(lst5)
   lst6 = ['Год выпуска', egod.get()]
   main_lst.append(lst6)
   lst7 = ['Период работы']
   main_lst.append(lst7)
   lst8 = ['C', ec.get(),'По',epo.get()]
   main_lst.append(lst8)
   lst9 = ['Номер рапорта', enomrap.get()]
   main_lst.append(lst9)
   lst10 = ['Сменность', smenrad.get()]
   main_lst.append(lst10)
   lst11 = ['Количество дней']
   main_lst.append(lst11)
   lst12 = ['Пребывания в хозяйстве',eprebhoz.get(),'В работе',evrab.get(),'Выходных и праздничных',evyh.get()]
   main_lst.append(lst12)
   lst13 = ['Отработано машиночасов',eotrab.get()]
   main_lst.append(lst13)
   lst14 = ['Простои по причинам:']
   main_lst.append(lst14)
   with open('data_entry.csv', newline='') as csvfile:   #работа со справочником и чтение из него
      reader = csv.DictReader(csvfile, delimiter=';')
      for row in reader:
         # print(row['Причина'],'|',row['Значение'])
         if row['Причина'] == cbreason1.get():
            cbresult1 = row['Значение']
         if row['Причина'] == cbreason2.get():
            cbresult2 = row['Значение']
   lst15 = [cbresult1,'Продолжительность, ч',ereasonh1.get(),cbresult2,'Продолжительность, ч',ereasonh2.get()]
   main_lst.append(lst15)
   lst16 = ['Время работы двигателя', evrrab.get()]
   main_lst.append(lst16)
   lst17 = ['Пробег, км',eprob.get()]
   main_lst.append(lst17)
   lst18 = ['Всего часов простоя', int(ereasonh1.get())+int(ereasonh2.get())]  #расчет общего времени простоя
   main_lst.append(lst18)
   machinehour=eotrab.get()
   dvig=evrrab.get()
   if (int(machinehour)) > (int(dvig)):
      messagebox.showerror('Форматно-логический контроль','Ошибка! Проверьте корректность данных')
   else:
      pass


from tkinter import messagebox

import csv

def Save():                      #функция для записи в csv
   myfile=open('t.csv','w')
   with myfile:
      writer=csv.writer(myfile)
      writer.writerows(main_lst)
   #with open("t.csv","w") as file:
      #Writer=writer(file)
      #Writer.writerows(main_lst)
add=tk.Button(window,text="Add",command=Add)
save=tk.Button(window,text="Save",command=Save)
add.grid(row=19, column=2)
save.grid(row=20, column=2)

#формантно-лоический контроль


window.mainloop()