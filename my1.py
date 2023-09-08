from tkinter import*  # установили модуль для работы с окном

window = Tk()  # создали окно

window.title("Кормушка")  # задали название окну
window.geometry("1280x1080")  # задали размер

currently_page = None


def show_page(page: Frame):#?
    global currently_page#?
    currently_page = page#?
    glavnoemenu.place(x=1120, y=20)
    menuframe.forget()
    page.place(x=0, y=0)

def call_back():
    currently_page.place_forget()#?
    glavnoemenu.place(x=1120, y=20)#?
    menuframe.place(x=0, y=0)
    mecac_entry.delete(0,END)
    chislo_entry.delete(0, END)
    tem_entry.delete(0, END)
    chas_entry.delete(0, END)
    minyta_entry.delete(0, END)
    god_entry.delete(0, END)

    image_result.place_forget()

def frame_menu():  # создали функцию для frame меню
    menu = Frame(width=1280, height=1080, background="light blue")  # создали фрейм
    button = Button(menu, text="Вид кормушки", font=("Arial", 20, "bold"), command=lambda: show_page(page1))  # создали кнопку( Вид кормушки )
    button.place(x=520, y=255, width=250, height=40)  # располажили кнопку и задали размер
    button2 = Button(menu, text="Работа кормушки", font=("Arial", 20, "bold"), command=lambda: show_page(page2))  # создали кнопку(Работа кормушки)
    button2.place(x=520, y=305, width=250, height=40)
    button3 = Button(menu, text="Cостояние", font=("Arial", 20, "bold"), command=lambda: show_page(page3))  # создали кнопку(Состаяние)
    button3.place(x=520, y=355, width=250, height=40, )
    button4 = Button(menu, text="ВЫХОД", font=("Arial", 20, "bold"), command=window.quit)  # создали кнопку(ВЫХОД)
    button4.place(x=520, y=405, width=250, height=40, )
    info = PhotoImage(file="picture/POGPIS.png")
    infolabel = Label(menu, image=info, background="light blue")
    infolabel.image = info
    infolabel.place(x=930, y=370)


    return menu#?


def frame_button1():
    bud = Frame(width=1280, height=1080, background="light blue")#создали фрейм для фотографии кормушки

    # Загрузка изображений и сохранение ссылок
    photo1 = PhotoImage(file="picture/zad_st .png")
    label1 = Label(bud, image=photo1)
    label1.image = photo1
    label1.place(x=80, y=20)

    photo2 = PhotoImage(file="picture/bok_st .png")
    label2 = Label(bud, image=photo2)
    label2.image = photo2
    label2.place(x=580, y=20)

    photo3 = PhotoImage(file="picture/zad_st .png")
    label3 = Label(bud, image=photo3)
    label3.image = photo3
    label3.place(x=80, y=392)

    photo4 = PhotoImage(file="picture/lico_st .png")
    label4 = Label(bud, image=photo4)
    label4.image = photo4
    label4.place(x=580, y=392)

    return bud




def frame_button2():
    textframe = Frame(width=1280, height=1080, background="light blue")#создали фрейм о работе кормуки
    phototext = PhotoImage(file="picture/workrorm.png")#загрузили фото с текстом
    textlabel = Label(textframe, image=phototext)#сохранили фото
    textlabel.image = phototext#
    textlabel.place(x=280, y=0)#


    return textframe



image_result = Label(text="")# переменная для картинки с ответом

#функция для фрейма"Состояние" кормушки
def frame_button3():
    sostoframe = Frame(width=1280, height=1080, background="light blue")#cоздали фрейм

    global chislo_entry

    global mecac_entry#сделали переменую глобальной



    global tem_entry

    global chas_entry

    global minyta_entry

    global god_entry

    chislo = Label(sostoframe, text="Введите текущее число: ", font=15)# создали надпись
    chislo.place(x=140, y=65)# разместили надпись

    mecac = Label(sostoframe, text="Введите текущий месяц:", font=15)# создали надпись
    mecac.place(x=140, y=90)# разместили надпись

    mecac_entry = Entry(sostoframe, width=20)#создали полеввода для ЧИСЛА
    mecac_entry.place(x=370, y=90)#разместили полеввода

    chislo_entry = Entry(sostoframe, width=20)#создали полеввода для ЧИСЛА
    chislo_entry.place(x=370, y=65)#разместили полеввода

    temperatyra = Label(sostoframe, text="Введите температуру: ", font=15)# создали надпись
    temperatyra.place(x=140, y=190)# разместили надпись

    tem_entry = Entry(sostoframe, width=22)#создали полеввода для ЧИСЛА
    tem_entry.place(x=355, y=190)#разместили полеввода

    chas = Label(sostoframe, text="Cколько часов:", font=15)# создали надпись
    chas.place(x=140, y=140)# разместили надпись

    chas_entry = Entry(sostoframe, width=34)#создали полеввода для ЧИСЛА
    chas_entry.place(x=285, y=140)#разместили полеввода

    minyta = Label(sostoframe, text="Сколько минут:", font=15)# создали надпись
    minyta.place(x=140, y=165)# разместили надпись

    minyta_entry = Entry(sostoframe, width=34)#создали полеввода для ЧИСЛА
    minyta_entry.place(x=285, y=165)#разместили полеввода

    god = Label(sostoframe, text="Введите текущий год: ", font=15)# создали надпись
    god.place(x=140, y=115)# разместили надпись

    god_entry = Entry(sostoframe, width=23)#создали полеввода для ЧИСЛА
    god_entry.place(x=350, y=115)#разместили полеввода


# функция для сохранения данных для которых ввёл пользователь
    def save_info():
        global image_result # сделали переменную глобальной (видимую для функции)

        entered_chislo = chislo_entry.get()# команда get(сохраняет введёное число в переменую)
        entered_mecac = mecac_entry.get()#сохранили месяц в переменую
        entered_mecac = int(entered_mecac)
        entered_temperatyry = tem_entry.get()
        entered_temperatyry = int(entered_temperatyry)
        entered_chas = chas_entry.get()
        entered_chas = int(entered_chas)
        entered_minyta = minyta_entry.get()
        entered_minyta = int(entered_minyta)
        entered_god = god_entry.get()
        # сохранение других значений

        print("Введенное число:", type(entered_chislo))
        print("Введенный месяц:", type(entered_mecac))
        print("Введённая температуру:", entered_temperatyry)
        print("Введённый час:", entered_chas)
        print("Введённая минута:", entered_minyta)
        print("Введённый год:", entered_god)
        # вывод других значений

# создаем условия

        if entered_mecac > 3 and entered_mecac < 10:#условие
            photo = PhotoImage(file="picture/not_work.png")#загрузили фото
            image_result = Label(sostoframe, image=photo)#сохранили фото
            image_result.image = photo
            image_result.place(x=140, y=330)#разместили фото

        elif ((entered_mecac>=10 and entered_mecac<=12) or #условие
             (entered_mecac>=1 and entered_mecac<=3)) and(
              entered_chas == 9 and entered_minyta ==0):
            photo02 = PhotoImage(file="picture/nine_zero.png")#загрузили фото
            image_result = Label(sostoframe, image=photo02)#сохранили фото
            image_result.image = photo02
            image_result.place(x=140, y=300)#разместили фото

        elif ((entered_mecac>=10 and entered_mecac<=12) or#условие
             (entered_mecac>=1 and entered_mecac<=3)) and(
              entered_chas == 12 and entered_minyta ==0) and(
              entered_temperatyry <= -15):
            photo03 = PhotoImage(file="picture/cold.png")#загрузили фото
            image_result = Label(sostoframe, image=photo03)#сохранили фото
            image_result.image = photo03
            image_result.place(x=140, y=300)#разместили фото


        elif ((entered_mecac>=10 and entered_mecac<=12) or#условие
        (entered_mecac>=1 and entered_mecac<=3)) and (
        entered_chas == 12 and entered_minyta ==0) and (
        entered_temperatyry >= -15):
            photo04 = PhotoImage(file="picture/notworktwelve.png")#загрузили фото
            image_result = Label(sostoframe, image=photo04)#сохранили фото
            image_result.image = photo04
            image_result.place(x=140, y=300)#разместили фото


        elif ((entered_mecac >= 10 and entered_mecac <= 12) or#условие
          (entered_mecac >= 1 and entered_mecac <= 3)) and (
                 entered_chas >= 12 and entered_minyta ==1):
            photo05 = PhotoImage(file="picture/zavtra.png")#загрузили фото
            image_result = Label(sostoframe, image=photo05)#сохранили фото
            image_result.image = photo05
            image_result.place(x=140, y=300)#разместили фото

        elif ((entered_mecac>=10 and entered_mecac<=12) or#условие
        (entered_mecac>=1 and entered_mecac<=3)) and (
        entered_chas >= 9 or entered_chas<=11 and entered_minyta ==1) and (
        entered_temperatyry >= -15):
            photo06 = PhotoImage(file="picture/notnine.png")#загрузили фото
            image_result = Label(sostoframe, image=photo06)#сохранили фото
            image_result.image = photo06
            image_result.place(x=140, y=300)#разместили фото


    save_button = Button(sostoframe, text="Отправить", font=("Arial", 15), command=save_info)#создали кнопку "Отправить"
    save_button.place(x=140, y=260)#разместили кнопку"Отправить"


    return sostoframe


menuframe = frame_menu()  # сохранила фрейм в переменую menu
menuframe.place(x=0, y=0)  # разместили фрейм на главном экране

#переходы в другие окна
page1 = frame_button1()
page2 = frame_button2()
page3 = frame_button3()
glavnoemenu = Button(window, text="вернуться в меню", command=call_back)

mainloop()#конец программы