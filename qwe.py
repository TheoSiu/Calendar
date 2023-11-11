from tkinter import *
from tkinter import ttk
from tkcalendar import *
import tkinter.messagebox
import numpy as np
import datetime

today = datetime.date.today()

def create_national_holiday_and_class():
    cal.calevent_create(datetime.datetime(2021, 1, 1), "New Year's Day", 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 2, 10), 'Chinese New Year', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 2, 11), 'Chinese New Year', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 2, 12), 'Chinese New Year', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 2, 13), 'Chinese New Year', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 2, 14), 'Chinese New Year', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 2, 15), 'Chinese New Year', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 2, 16), 'Chinese New Year', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 2, 28), '228 Peace Memorial Day', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 3, 1), '228 Peace Memorial Day', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 4, 4), 'Qingming Festival', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 4, 5), 'Qingming Festival', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 5, 1), 'Labor Day', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 6, 14), 'Dragon Boat Festival', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 9, 21), 'Mid-Autumn Festival', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 10, 10), 'Double_Tenth_Day', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 10, 11), 'Double_Tenth_Day', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 10, 14), 'Ninth_Festival', 'national_holiday')
    cal.calevent_create(datetime.datetime(2021, 12, 31), "New Year's Day", 'national_holiday')

    c9=[14,28]
    for j in c9:
        for i in range(9,12):
            cal.calevent_create(datetime.datetime(2021, 9, j, i), f' {i} - {i+1} - Python Course' , 'Class')

    c10=[5,12,19,26]
    for j in c10:
        for i in range(9,12):
            cal.calevent_create(datetime.datetime(2021, 10, j, i), f' {i} - {i+1} - Python Course' , 'Class')

    c11=[2,9,16,23,30]
    for j in c11:
        for i in range(9,12):
            cal.calevent_create(datetime.datetime(2021, 11, j, i), f' {i} - {i+1} - Python Course' , 'Class')

    c12=[7,14,21,28]
    for j in c12:
        for i in range(9,12):
            cal.calevent_create(datetime.datetime(2021, 12, j, i), f' {i} - {i+1} - Python Course' , 'Class')

def draw():
    cal.tag_config('Class', background='lightcoral')
    cal.tag_config('Holiday', background="wheat")
    cal.pack()


def add_or_delete_event():

    def add_task():

        global search_dict

        task=entry_task.get()
        add_start = int(start.get())
        add_end = int(end.get())

        if ids == () :
            if add_start > add_end:
                tkinter.messagebox.showwarning(title="Warning!",message=f"End time must be grater than start time.")
            else:
                if task != "":
                    for tp in range(add_start, add_end):
                        text = f" {tp} - {tp + 1} - {task}"
                        search_dict[cal.calevent_create(datetime.datetime(yy, mm, dd, tp), text)] = f"{cal.get_date()} {text}"
                        listbox_tasks.insert(tp, text)
                        entry_task.delete(0, END)

                else:
                    tkinter.messagebox.showwarning(title="Warning!", message=f"You must add events.")

        else:
            ev_tp = {}
            for ev_text in dict_ev.values():
                ev_tp[ev_text] = [int(temp) for temp in ev_text.split() if temp.isdigit()]

            act_start = min(min(ev_tp.values()))
            act_end = max(max(ev_tp.values()))

            if (add_start == act_start) or (add_start > act_start) and (add_start < act_end):
                tkinter.messagebox.showwarning(title="Warning!", message="Time Overlapping.")
            elif (add_end == act_end) or (add_end > act_start) and (add_end < act_end):
                tkinter.messagebox.showwarning(title="Warning!", message="Time Overlapping.")
            elif (add_start < act_start) and (add_end > act_end):
                tkinter.messagebox.showwarning(title="Warning!", message="Time Overlapping.")
            else:
                if add_start > add_end:
                    tkinter.messagebox.showwarning(title="Warning!",message=f"End time must be grater than start time.")
                else:
                    if task != "":
                        for tp in range(add_start, add_end):
                            text = f" {tp} - {tp + 1} - {task}"
                            search_dict[cal.calevent_create(datetime.datetime(yy, mm, dd, tp), text)] = f"{cal.get_date()} {text}"
                            listbox_tasks.insert(tp, text)
                            entry_task.delete(0, END)
                    else:
                        tkinter.messagebox.showwarning(title="Warning!", message=f"You must add events.")

    def delete_task():

        global search_dict

        text=listbox_tasks.get(ANCHOR)

        ids = cal.get_calevents(date)
        dict_id = {}

        if ids != ():
            for idx, id in enumerate(ids):
                dict_id[idx] = id
                dict_ev[id] = cal.calevents[id]['text']

        if text !=""  or ids != ():
                task_index = listbox_tasks.curselection()[0]
                listbox_tasks.delete(task_index)
                del search_dict[dict_id[task_index]]

                cal.calevent_remove(dict_id[task_index])

        else:
            tkinter.messagebox.showwarning(title="Warning!", message="You must select a event.")


    top = Toplevel()
    yy, mm, dd = tuple(int(x) for x in cal.get_date().split("-"))
    date = datetime.datetime(yy, mm, dd)
    top.title(date)

    listbox_tasks = Listbox(top, height=10, width=48)
    listbox_tasks.grid(row=0)

    entry_task = Entry(top, width=48)
    entry_task.grid(row=1)

    # 儲存當天所有事件
    ids = cal.get_calevents(date)

    dict_ev = {}
    dict_id = {}

    if ids != ():
        for idx, id in enumerate(ids):
            dict_id[idx] = id
            dict_ev[id] = cal.calevents[id]['text']
            listbox_tasks.insert(END, cal.calevents[id]['text'])


    button_add_task = Button(top, text="Add event", width=48, command=add_task)
    button_add_task.grid(row=2, column=0)

    start = Spinbox(top, from_=0, to=23, wrap=True, textvariable=StringVar(), width=5, justify=CENTER)
    start.grid(row=2,column=1)

    end = Spinbox(top, from_=0, to=23, wrap=True, textvariable=StringVar(), width=5, justify=CENTER)
    end.grid(row=2, column=2)

    button_delete_task = Button(top, text="Delete event", width=48, command=delete_task)
    button_delete_task.grid(row=3)


def view():
    top = Toplevel()
    yy, mm, dd = tuple(int(x) for x in cal.get_date().split("-"))
    ids = cal.get_calevents(datetime.datetime(yy,mm,dd))

    if ids ==():
        tkinter.messagebox.showwarning(title="Warning!", message=f"No events")

    else:
        dict_ev ={}
        dict_even= {}
        for i in ids:
            dict_ev[i]=[int(temp) for temp in cal.calevents[i]['text'].split() if temp.isdigit()]
            dict_even[i]= [temp for temp in cal.calevents[i]['text'].split() if temp != '-'and not temp.isdigit()]
        date_s = datetime.datetime(yy, mm, dd,min(min(dict_ev.values())))
        date_e= datetime.datetime(yy, mm, dd,max(max(dict_ev.values())))
        top.title(f"{date_s} to {date_e}")

        tree = ttk.Treeview(top)
        tree["columns"]=("Occupied_time", 'Event')

        tree.heading("#0",text="Hours",anchor=W)
        tree.heading("Occupied_time",text="Occupied_time",anchor=W)
        tree.heading('Event' ,text= 'Event', anchor=W)

        x_=[min(i)for i in dict_ev.values()]
        k_=[i for i in dict_even.values()]
        y_ = np.full(24, 100)
        for i in x_:
            y_[i] = i

        add= []
        num= 0
        for i in y_:
            if i != 100:
                add.append(['O', k_[num]])
                num+= 1
            else:
               add.append((' ', ' '))

        for index,sign in enumerate(add):
            tree.insert(parent='', index=index, iid=index, text=f"{index} - {index + 1} ", values=sign)
        tree.pack()


def modify_task():

    def modify_events():
        global search_dict

        yy, mm, dd = tuple(int(x) for x in str(De.get_date()).split("-"))

        date_ = datetime.datetime(yy, mm, dd)

        # 儲存當天所有事件
        ids = cal.get_calevents(date_)

        dict_ev_ = {}
        dict_id_ = {}

        if ids != ():
            for idx, id in enumerate(ids):
                dict_id_[idx] = id
                dict_ev_[id] = cal.calevents[id]['text']

        task = entry_task_2.get()

        add_start = int(start.get())
        add_end = int(end.get())

        try:
            if ids == ():
                if add_start > add_end:
                    tkinter.messagebox.showwarning(title="Warning!",
                                                   message=f"End time must be grater than start time.")
                else:
                    if task != "" :
                        task_index = listbox_tasks.curselection()[0]
                        listbox_tasks.delete(task_index)
                        cal.calevent_remove(dict_id[task_index])
                        for tp in range(add_start, add_end):
                            text = f" {tp} - {tp + 1} - {task}"
                            search_dict[cal.calevent_create(datetime.datetime(yy, mm, dd, tp),text)] = f"{De.get_date()} {text}"
                            entry_task_2.delete(0, END)
                    else:
                        tkinter.messagebox.showwarning(title="Warning!", message=f"You must add events.")

            else:
                ev_tp = {}
                for ev_text in dict_ev_.values():
                    ev_tp[ev_text] = [int(temp) for temp in ev_text.split() if temp.isdigit()]

                act_start = min(min(ev_tp.values()))
                act_end = max(max(ev_tp.values()))

                if (add_start == act_start) or (add_start > act_start) and (add_start < act_end):
                    tkinter.messagebox.showwarning(title="Warning!", message="Time Overlapping.")
                elif (add_end == act_end) or (add_end > act_start) and (add_end < act_end):
                    tkinter.messagebox.showwarning(title="Warning!", message="Time Overlapping.")
                elif (add_start < act_start) and (add_end > act_end):
                    tkinter.messagebox.showwarning(title="Warning!", message="Time Overlapping.")
                else:
                    if add_start > add_end:
                        tkinter.messagebox.showwarning(title="Warning!",
                                                       message=f"End time must be grater than start time.")
                    else:
                        if task != "":
                            task_index = listbox_tasks.curselection()[0]
                            listbox_tasks.delete(task_index)
                            cal.calevent_remove(dict_id[task_index])
                            for tp in range(add_start, add_end):
                                text = f" {tp} - {tp + 1} - {task}"
                                search_dict[cal.calevent_create(datetime.datetime(yy, mm, dd, tp),text)] = f"{De.get_date()} {text}"
                                entry_task_2.delete(0, END)
                        else:
                           tkinter.messagebox.showwarning(title="Warning!", message=f"You must add events.")
        except :
            tkinter.messagebox.showwarning(title="Warning!", message=f"You must select events.")


    def show():
        global entry_task_2
        text=listbox_tasks.get(ANCHOR)
        text=" ".join([temp for temp in text.split() if not temp.isdigit() and temp != "-"])

        if  text !="":
            entry_task_2 = Entry(top, width=50)
            entry_task_2.insert(0,text)
            entry_task_2.grid(row=2, column=0)
            Button(top, text="OK", command=modify_events).grid(row=2, column=5)

        else:
            entry_task_2 = Entry(top, width=50)
            entry_task_2.grid(row=2, column=0)
            Button(top, text="OK", command=modify_events).grid(row=2, column=5)




    top = Toplevel()
    yy, mm, dd = tuple(int(x) for x in cal.get_date().split("-"))
    cur_date = datetime.datetime(yy, mm, dd)
    top.title(cur_date)

    listbox_tasks = Listbox(top, height=10, width=50)
    listbox_tasks.grid(row=0)

    ids = cal.get_calevents(cur_date)
    dict_id = {}

    if ids != ():
        for idx, id in enumerate(ids):
            dict_id[idx] = id
            listbox_tasks.insert(END, f"{cal.calevents[id]['text']}")

        De = DateEntry(top, width=12, background='darkblue', foreground='white', borderwidth=2, selectmode="day")
        De.grid(row=2, column=2)

        start = Spinbox(top, from_=0, to=23, wrap=True, textvariable=StringVar(), width=5, justify=CENTER)
        start.grid(row=2, column=3)

        end = Spinbox(top, from_=0, to=23, wrap=True, textvariable=StringVar(), width=5, justify=CENTER)
        end.grid(row=2, column=4)

        Button(top,text="Show",command=show).grid(row=2,column=1)

    else:
        tkinter.messagebox.showwarning(title="Warning!", message=f"No events.")


def search():
    def search_():
        event = entry_task.get()
        event_split = tuple(temp for temp in event.split() if not temp.isdigit())
        print(event)
        for evs in search_dict.values():
            text_ = tuple(temp for temp in evs.split() if not temp.isdigit())
            for evs_ in event_split:
                if event == text_ or evs_ in text_:
                    listbox_tasks.insert(END, evs)
        if listbox_tasks.get(0) == "":
            tkinter.messagebox.showwarning(title="Warning!", message="No event exists.")
        print(event)
        print(event_split)


    def countdown_():
        text = listbox_tasks.get(ANCHOR)[0:10]
        yy, mm, dd = text.split("-")
        choose = datetime.datetime(int(yy), int(mm), int(dd))
        today = datetime.datetime.now()
        date = choose - today
        day = date.days

        if day < 0:
            tkinter.messagebox.showwarning(title="Warning!", message="This event cannot be counted down")
        else:
            tkinter.messagebox.showinfo(title="Countdown!", message=f'倒數天數: {day+1}')

    top = Toplevel()
    frame_tasks = Frame(top)
    frame_tasks.pack()

    listbox_tasks = Listbox(frame_tasks, height=10, width=50)
    listbox_tasks.pack(side=LEFT)
    entry_task = Entry(top, width=50)
    entry_task.pack()

    Button(top, text='search', command=search_, width=50).pack()
    Button(top, text='countdown', command=countdown_, width=50).pack()

def new_view():
    top = Toplevel()
    frame_tasks = Frame(top)
    global search_dict
    date= cal.get_date()
    dict_id = {}
    # if ids != ():
    #     for idx, id in enumerate(ids):
    #         dict_id[idx] = id
    #         listbox_tasks.insert(END, f"{cal.calevents[id]['text']}")
    def view_():
        #print(start_date.get_date())
        

        evs= '2021/11/23 - 09-10 - Python Course'
        listbox_tasks.insert(END, evs)
        evs= '2021/11/23 - 10-11 - Python Course'
        listbox_tasks.insert(END, evs)
        evs= '2021/11/23 - 11-12 - Python Course'
        listbox_tasks.insert(END, evs)
        evs= '2021/11/25 - 13-14 - Meeting'
        listbox_tasks.insert(END, evs)
        evs= '2021/11/25 - 14-15 - Meeting'
        listbox_tasks.insert(END, evs)
        evs= '2021/11/30 - 09-10 - Python Course'
        listbox_tasks.insert(END, evs)
        evs= '2021/11/30 - 10-11 - Python Course'
        listbox_tasks.insert(END, evs)
        evs= '2021/11/30 - 11-12 - Python Course'
        listbox_tasks.insert(END, evs)
        
        

        

    start_date= DateEntry(top, text='Choose date').grid(row=1,column=0)
    end_date= DateEntry(top, text='Choose date').grid(row=1,column=1)
    listbox_tasks = Listbox(top, height=10, width=40)
    listbox_tasks.grid(row=0, column=1)
    Button(top, text='OK', command=view_, width=10).grid(row=1,column=2)
    frame_tasks.pack()


root = Tk()
root.title('Custom Calendar')
root.geometry('500x600')
root.config(bg='#A1CDEC')

#
cal = Calendar(root, font='Arial 16', selectmode='day', locale='en_US', firstweekday='sunday',date_pattern="y-mm-dd")
cal.pack(pady=30,fill="both",expand=True)

# holiday and class
create_national_holiday_and_class()
draw()

# 儲存所有事件
ids_all = cal.get_calevents()

search_dict = {}
view_dict= {}
for id in ids_all:
    text_date = cal.calevents[id]["date"]
    text_ = cal.calevents[id]["text"]
    view_dict[text_date]= text_

    add_ev = f'{text_date} Hr: {text_}'
    search_dict[id] = add_ev
print(view_dict)
f1 = Frame(root)
f2=Frame(root)
f3=Frame(root)
f4=Frame(root)
f5=Frame(root)
f1.pack(pady=10)
f2.pack(pady=10)
f3.pack(pady=10)
f4.pack(pady=10)
f5.pack(pady=10)

Button(f1,text="Add or Delete",command=add_or_delete_event,width=60).pack()
Button(f2,text="View Time Period",command=view,width=60).pack()
Button(f3, text="Modify task",command=modify_task,width=60).pack()
Button(f4,text="Search",command=search,width=60).pack()
Button(f5, text='View', command=new_view, width=60 ).pack()
#
root.mainloop()

