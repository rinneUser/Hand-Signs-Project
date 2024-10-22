from tkinter import*
import webbrowser

class hand_sign:
    def __init__ (self):
        self.spec=str(input("Укажите специализацию техники: "))
        self.first=str(input("Укажите первую печать: "))
        self.second=str(input("Укажите вторую печать: "))
        self.third=str(input("Укажите третью печать: "))
        self.fourth=str(input("Укажите четвёртую печать: "))
        self.fifth=str(input("Укажите пятую печать: "))
        self.sixth=str(input("Укажите шестую печать: "))
        self.seventh=str(input("Укажите седьмую печать: "))
        self.eighth=str(input("Укажите восьмую печать: "))
        self.ninth=str(input("Укажите девятую печать: "))
        print("=================>")
    
    def info(self):
        print("Специализация: ",self.spec,"\nПервая печать: ",self.first,"\nВторая печать: ",self.second,"\nТретья печать: ",self.third,"\nЧетвёртая печать: ",self.fourth,"\nПятая печать: ",self.fifth,"\nШестая печать: ",self.sixth,"\nСедьмая печать: ",self.seventh,"\nВосьмая печать: ",self.eighth,"\nДевятая печать: ")
        print("=================>")
    def search(self):
        print("Определяем Технику под Ваш запрос...")
        if self.spec=="Нападение" and self.first=="собака" and self.second=="кролик" and self.third=="змея" and self.fourth=="птица" and self.fifth=="свинья" and self.sixth=="лошадь" and self.seventh=="тигр":
            print("Использована техника Простого Пламени")
            webbrowser.open_new("https://jut.su/technique/prostoe-ognennoe-plamya.html")
        elif self.spec=="Нападение" and self.first=="змея" and self.second=="овца" and self.third=="лошадь" and self.fourth=="кролик" and self.fifth=="овца" and self.sixth=="лошадь" and self.seventh=="кролик":
            print("Использована техника Водной Тюрьмы")
            webbrowser.open_new("https://jut.su/technique/vodnaya-tyurma.html")
        elif self.spec=="Нападение" and self.first=="бык" and self.second=="кролик" and self.third=="обезьяна":
            print("Использована техника Райкири")
            webbrowser.open_new("https://jut.su/technique/raykiri.html")
        elif self.spec=="Нападение" and self.first=="змея" and self.second=="дракон" and self.third=="тигр":
            print("Использована техника Простого Пламени Дракона")
            webbrowser.open_new("https://jut.su/technique/prostoe-plamya-drakona.html")
        elif self.spec=="Нападение" and self.first=="змея" and self.second=="овца" and self.third=="обезьяна" and self.fourth=="свинья" and self.fifth=="лошадь" and self.sixth=="тигр":
            print("Использована техника Струй Пламени")
            webbrowser.open_new("https://jut.su/technique/ognennoe-plamya.html")
        elif self.spec=="Нападение" and self.first=="тигр" and self.second=="дракон" and self.third=="крыса" and self.fourth=="тигр":
            print("Использована техника Сюрикена Черепицы")
            webbrowser.open_new("https://jut.su/technique/syuriken-cherepicy.html")
        elif self.spec=="Призыв" and self.first=="тигр" and self.second=="змея" and self.third=="дракон" and self.fourth=="собака":
            print("Использована техника Призыва Собачек")
            webbrowser.open_new("https://jut.su/technique/prizyv-sobachek.html")
        elif self.spec=="Призыв" and self.first=="змея" and self.second=="тигр":
            print("использована техника Рук-Змей")
            webbrowser.open_new("https://jut.su/technique/ruki-zmei.html")
        elif self.spec=="Нападение" and self.first=="тигр":
            print("Использована техника Дождя Сенбонов")
            webbrowser.open_new("https://jut.su/technique/dozhd-senbonov.html")
        elif self.spec=="Нападение" and self.first=="птица":
            print("Использована техника Песчаного Гроба")
            webbrowser.open_new("https://jut.su/technique/peschanyy-grob.html")
        elif self.spec=="Нападение" and self.first=="тигр":
            print("Использована техника Высасывания Чакры")
            webbrowser.open_new("https://jut.su/technique/vysasyvanie-chakry.html")
        elif self.spec=="Призыв" and self.first=="собака" and self.second=="свинья" and self.third=="птица" and self.fourth=="обезьяна" and self.fifth=="овца":
            print("Использована техника Призыва Жабы")
            webbrowser.open_new("https://jut.su/technique/prizyv-zhaby.html")
        elif self.spec=="Защита" and self.first=="змея":
            print("Использована техника Барьера Четырёх Фиолетовых Огней")
            webbrowser.open_new("https://jut.su/technique/ognennyy-barer.html")
        elif self.spec=="Клонирование" and self.first=="овца" and self.second=="крыса" and self.third=="птица" and self.fourth=="свинья" and self.fifth=="тигр":
            print("Использована техника Теневого Клонирования Сюрикенов")
            webbrowser.open_new("https://jut.su/technique/syuriken-teni-klona.html")
        elif self.spec=="Запретная" and self.first=="тигр" and self.second=="змея" and self.third=="собака" and self.fourth=="дракон":
            print("использована техника Нечестивого Воскрешения")
            webbrowser.open_new("https://jut.su/technique/prizyv-ozhivlenie-treh-hokage.html")
        elif self.spec=="Нападение" and self.first=="овца" and self.second=="лошадь" and self.third=="дракон" and self.fourth=="тигр" and self.fifth=="овца":
            print("Использована техника Стреляющего Грязью и Огнём Дракона")
            webbrowser.open_new("https://jut.su/technique/strelyayuschiy-gryazyu-i-ognem-drakon.html")
        elif self.spec=="Нападение" and self.first=="овца" and self.second=="лошадь" and self.third=="змея" and self.fourth=="дракон" and self.sixth=="крыса" and self.seventh=="бык" and self.eighth=="тигр":
            print("Использована техника Пламени Дракона")
            webbrowser.open_new("https://jut.su/technique/plamya-drakona.html")
        elif self.spec=="Универсальная" and self.first=="тигр" and self.second=="змея":
            print("Использована техника Сотворения Леса")
            webbrowser.open_new("https://jut.su/technique/sotvorenie-lesa.html")
        elif self.spec=="Нападение" and self.first=="крыса" and self.second=="тигр" and self.third=="собака" and self.fourth=="бык" and self.fifth=="кролик" and self.sixth=="тигр":
            print("Использована техника Цветов Феникса")
            webbrowser.open_new("https://jut.su/technique/cvety-feniksa.html")
        elif self.spec=="Нападение" and self.first=="змея" and self.second=="овца" and self.third=="обезьяна" and self.fourth=="свинья" and self.fifth=="лошадь" and self.sixth=="тигр":
            print("Использована техника Огненного Шара")
            webbrowser.open_new("https://jut.su/technique/ognennyy-shar.html")
        elif self.spec=="Призыв" and self.first=="свинья" and self.second=="собака" and self.third=="обезьяна" and self.fourth=="овца":
            print("Использована техника Призыва Короля Обезьян")
            webbrowser.open_new("https://jut.su/technique/prizyv-korolya-obezyan.html")
        elif self.spec=="Запретная" and self.first=="змея" and self.second=="свинья" and self.third=="овца" and self.fourth=="кролик" and self.fifth=="собака" and self.sixth=="крыса" and self.seventh=="птица" and self.eighth=="лошадь" and self.ninth=="змея":
            print("Использована техника Печати Бога Смерти")
            webbrowser.open_new("https://jut.su/technique/lico-pechat-smerti.html")
        elif self.spec=="Нападение" and self.first=="тигр":
            print("Использована техника Паучьей Сети")
            webbrowser.open_new("https://jut.su/technique/pauchya-set.html")
        elif self.spec=="Гендзюцу" and self.first=="собака" and self.second=="змея" and self.third=="обезьяна" and self.fourth=="бык" and self.fifth=="тигр":
            print("Использована техника Обхватывающих Деревьев")
            webbrowser.open_new("https://jut.su/technique/obhvatyvayuschie-derevya-gendzyucu.html")
        elif self.spec=="Защита" and self.first=="паук" and self.second=="тигр":
            print("Использована техника Быстрого Исцеления")
            webbrowser.open_new("https://jut.su/technique/bystroe-iscelenie.html")
        elif self.spec=="Универсальная" and self.first=="тигр" and self.second=="лошадь" and self.third=="кролик"and self.fourth=="крыса" and self.fifth=="собака":
            print("Использована техника Скальпеля Чакры")
            webbrowser.open_new("https://jut.su/technique/skalpel-chakry.html")
        elif self.spec=="Призыв" and self.first=="свинья" and self.second=="собака" and self.third=="птица" and self.fourth=="обезьяна" and self.fifth=="овца":
            print("Использована техника Призыва Змеи")
            webbrowser.open_new("https://jut.su/technique/prizyv-zmei.html")
        elif self.spec=="Нападение" and self.first=="свинья" and self.second=="тигр":
            print("Использована техника Топкого Болота")
            webbrowser.open_new("https://jut.su/technique/topkoe-boloto.html")
        elif self.spec=="Защита" and self.first=="тигр" and self.second=="лошадь" and self.third=="свинья" and self.fourth=="овца" and self.fifth=="крыса" and self.sixth=="змея":
            print("Использована техника Колючего Стража")
            webbrowser.open_new("https://jut.su/technique/kolyuchiy-strazh.html")
        elif self.spec=="Нападение" and self.first=="змея" and self.second=="овца" and self.third=="обезьяна" and self.fourth=="свинья" and self.fifth=="лошадь" and self.sixth=="тигр":
            print("Использована техника Зажигательного пламени")
            webbrowser.open_new("https://jut.su/technique/zazhigatelnoe-plamya.html")
        elif self.spec=="Защита" and self.first=="собака" and self.second=="бык" and self.third=="птица" and self.fourth=="свинья":
            print("Использована техника Исчезновения")
            webbrowser.open_new("https://jut.su/technique/nebolshoe-peremeschenie-ischeznovenie.html")
        elif self.spec=="Нападение" and self.first=="овца" and self.second=="змея" and self.third=="тигр":
            print("Использована техника Чёрного Дождя")
            webbrowser.open_new("https://jut.su/technique/chernyy-dozhd.html")
        elif self.spec=="Нападение" and self.first=="крыса" and self.second=="бык" and self.third=="тигр":
            print("использована техника Шипованного Мясного Танка")
            webbrowser.open_new("https://jut.su/technique/shipovannyy-myasnoy-tank.html")
        elif self.spec=="Универсальная" and self.first=="Слон":
            print("Использована техника Мега Роста")
            webbrowser.open_new("https://jut.su/technique/mega-rost.html")
        elif self.spec=="Призыв" and self.first=="свинья" and self.second=="собака" and self.third=="птица" and self.fourth=="обезьяна" and self.fifth=="овца":
            print("Использована техника Призыва Паука")
            webbrowser.open_new("https://jut.su/technique/prizyv-pauka.html")
        elif self.spec=="Призыв" and self.first=="змея":
            print("Использована техника Призыва Врат Рашомон")
            webbrowser.open_new("https://jut.su/technique/prizyv-vrat-rashomon.html")
        elif self.spec=="Нападение" and self.first=="свинья" and self.second=="обезьяна" and self.third=="крыса" and self.fourth=="обезьяна" and self.fifth=="лошадь" and self.sixth=="собака" and self.seventh=="овца" and self.eighth=="лошадь":
            print("Использована техника Песчаного Водопада")
            webbrowser.open_new("https://jut.su/technique/peschanyy-vodopad.html")
        elif self.spec=="Универсальная" and self.first=="овца" and self.second=="змея" and self.third=="тигр" and self.fourth=="овца":
            print("Использована техника Гарема")
            webbrowser.open_new("https://jut.su/technique/garem.html")
        elif self.spec=="Нападение" and self.first=="обезьяна" and self.second=="лошадь" and self.third=="собака" and self.fourth=="овца":
            print("Использована техника Квадрата Взрывных Свитков")
            webbrowser.open_new("https://jut.su/technique/kvadrat-vzryvnyh-svitkov.html")
        elif self.spec=="Поддержка" and self.first=="овца":
            print("Использована техника Сбора Насекомых")
            webbrowser.open_new("https://jut.su/technique/cbor-nasekomyh.html")
        elif self.spec=="Защита" and self.first=="свинья" and self.second=="обезьяна" and self.third=="дракон" and self.fourth=="овца" and self.fifth=="собака":
            print("Использована техника Защитной Сферы из Жуков")
            webbrowser.open_new("https://jut.su/technique/zaschitnaya-sfera-iz-zhukov.html")
        elif self.spec=="Нападение" and self.first=="тигр" and self.second=="крыса" and self.third=="бык" and self.fourth=="собака" and self.fifth=="лошадь" and self.sixth=="птица" and self.seventh=="тигр":
            print("Использована техника Тысяч Пчелиных Жал")
            webbrowser.open_new("https://jut.su/technique/tysyachi-pchelinyh-zhal.html")
        elif self.spec=="Нападение" and self.first=="змея" and self.second=="тигр":
            print("Использована техника Ветвистого Заряда Молнии")
            webbrowser.open_new("https://jut.su/technique/vetvistyy-zaryad-molnii.html")
        elif self.spec=="Клонирование" and self.first=="крыса" and self.second=="бык" and self.third=="тигр" and self.fourth=="кролик" and self.fifth=="дракон" and self.sixth=="змея" and self.seventh=="лошадь" and self.eighth=="овца":
            print("Использована техника Массового Теневого Лже-Клонирования")
            webbrowser.open_new("https://jut.su/technique/massovoe-tenevoe-lzhe-klonirovanie.html")
        elif self.spec=="Нападение" and self.first=="свинья" and self.second=="собака" and self.third=="птица" and self.fourth=="обезьяна" and self.fifth=="овца":
            print("Использована техника Водной Воронки")
            webbrowser.open_new("https://jut.su/technique/vodnaya-voronka.html")
        elif self.spec=="Призыв" and self.first=="свинья" and self.second=="собака" and self.third=="птица" and self.fourth=="обезьяна" and self.fifth=="овца":
            print("Использована техника Призыва Серебряной Змеи")
            webbrowser.open_new("https://jut.su/technique/prizyv-serebryanoy-zmei.html")
        elif self.spec=="Запретная" and self.first=="птица":
            print("Использована техника Мистического Искусства Павлина: Крылья")
            webbrowser.open_new("https://jut.su/technique/mistichiskiy-metod-pavlina.html")
        elif self.spec=="Запретная" and self.first=="обезьяна" and self.second=="свинья" and self.third=="овца" and self.fourth=="дракон" and self.fifth=="обезьяна" and self.sixth=="птица":
            print("Использована техника Звёздного Лассо")
            webbrowser.open_new("https://jut.su/technique/zvezdnoe-lasso.html")
        elif self.spec=="Универсальная" and self.first=="свинья" and self.second=="овца" and self.third=="овца" and self.fourth=="овца":
            print("Использована техника Цветочной Бури")
            webbrowser.open_new("https://jut.su/technique/cvetochnaya-burya.html")
        elif self.spec=="Нападение" and self.first=="овца" and self.second=="собака" and self.third=="свинья" and self.fourth=="бык" and self.fifth=="змея":
            print("Использована техника Водяного Пузыря")
            webbrowser.open_new("https://jut.su/technique/vodyanoy-puzyr.html")
        elif self.spec=="Нападение" and self.first=="кролик" and self.second=="свинья" and self.third=="овца":
            print("Использована техника Огненного Шквала")
            webbrowser.open_new("https://jut.su/technique/ognennyy-shkval.html")
        elif self.spec=="Призыв" and self.first=="свинья" and self.second=="собака" and self.third=="птица" and self.fourth=="обезьяна" and self.fifth=="овца":
            print("Использована техника Призыва Пираний")
            webbrowser.open_new("https://jut.su/technique/prizyv-piraniy.html")
        elif self.spec=="Универсальная" and self.first=="змея" and self.second=="лошадь" and self.third=="тигр":
            print("Использована техника Массы Водных Пузырей")
            webbrowser.open_new("https://jut.su/technique/massa-vodnyh-puzyrey.html")
        elif self.spec=="Универсальная" and self.first=="тигр":
            print("Использована техника Электромагнитного Миража")
            webbrowser.open_new("https://jut.su/technique/elektromagnitnyy-mirazh.html")
        elif self.spec=="Универсальная" and self.first=="змея" and self.second=="крыса" and self.third=="собака" and self.fourth=="овца":
            print("Использована техника Ледяных Дисков")
            webbrowser.open_new("https://jut.su/technique/ledyanye-diski.html")
        elif self.spec=="Универсальная" and self.first=="овца" and self.second=="свинья" and self.third=="собака":
            print("Использована техника Гусеницы Зеркал")
            webbrowser.open_new("https://jut.su/technique/gusenica-zerkal.html")
        elif self.spec=="Нападение" and self.first=="собака" and self.second=="кролик" and self.third=="свинья":
            print("Использована техника Острых Наконечников")
            webbrowser.open_new("https://jut.su/technique/ostrye-nakonechniki.html")
        elif self.spec=="Призыв" and self.first=="собака" and self.second=="овца" and self.third=="обезьяна":
            print("Использована техника Возведения-Призыва Столбов")
            webbrowser.open_new("https://jut.su/technique/vozvedenie-prizyv-stolbov.html")
        elif self.spec=="Гендзюцу" and self.first=="собака" and self.second=="змея" and self.third=="бык" and self.fourth=="птица" and self.fifth=="тигр":
            print("Использована техника Обратного Гипноза")
            webbrowser.open_new("https://jut.su/technique/obratnyy-gipnoz.html")
        elif self.spec=="Универсальная" and self.first=="овца":
            print("Использована техника Удаления Взрывных Печатей")
            webbrowser.open_new("https://jut.su/technique/udalenie-vzryvnyh-pechatey.html")
        elif self.spec=="Универсальная" and self.first=="свинья" and self.second=="собака" and self.third=="лошадь" and self.fourth=="тигр":
            print("Использована техника Столба Воды")
            webbrowser.open_new("https://jut.su/technique/vodnyy-stolb.html")
        elif self.spec=="Гендзюцу" and self.first=="тигр" and self.second=="свинья" and self.third=="тигр" and self.fourth=="лошадь" and self.fifth=="бык":
            print("Использована техника Цветочного Побега")
            webbrowser.open_new("https://jut.su/technique/cvetochnyy-pobeg.html")
        elif self.spec=="Гендзюцу" and self.first=="собака" and self.second=="кролик" and self.third=="змея" and self.fourth=="овца":
            print("Использована техника Связывающей Иллюзии")
            webbrowser.open_new("https://jut.su/technique/svyazyvayuschaya-illyuziya.html")
        elif self.spec=="Универсальная" and self.first=="тигр" and self.second=="змея" and self.third=="свинья":
            print("Использована техника Металлической Сферы")
            webbrowser.open_new("https://jut.su/technique/metallicheskaya-sfera.html")
        elif self.spec=="Запретная" and self.first=="крыса" and self.second=="собака" and self.third=="свинья" and self.fourth=="овца":
            print("Использована техника Ритуала Воскрешения")
            webbrowser.open_new("https://jut.su/technique/ritual-voskresheniya.html")
        elif self.spec=="Нападение" and self.first=="бык" and self.second=="свинья" and self.third=="крыса":
            print("Использована техника Кары Громом и Молнией")
            webbrowser.open_new("https://jut.su/technique/kara-gromom-i-molniey.html")
        elif self.spec=="Гендзюцу" and self.first=="крыса":
            print("Использована техника Миража Смерти")
            webbrowser.open_new("https://jut.su/technique/mirazh-smerti-gendzyucu.html")
        elif self.spec=="Клонирование" and self.first=="тигр":
            print("Использована техника Водяного Клона")
            webbrowser.open_new("https://jut.su/technique/vodyanoy-klon.html")
        elif self.spec=="Универсальная" and self.first=="собака" and self.second=="овца":
            print("Использована техника Увеличения Глиняной Фигуры")
            webbrowser.open_new("https://jut.su/technique/uvelichenie-glinyanoy-figury.html")
        elif self.spec=="Секретная" and self.first=="змея" and self.second=="тигр":
            print("Использована техника С1")
            webbrowser.open_new("https://jut.su/technique/c-si-1.html")
        elif self.spec=="Призыв" and self.first=="тигр":
            print("Использована техника Управления Марионетками")
            webbrowser.open_new("https://jut.su/technique/upravlenie-marionetkami.html")
        elif self.spec=="Призыв" and self.first=="овца" and self.second=="змея" and self.third=="крыса" and self.fourth=="бык" and self.fifth=="змея" and self.sixth=="собака" and self.seventh=="тигр":
            print("Использована техника Призыва Статуи Демона-Еретика")
            webbrowser.open_new("https://jut.su/technique/prizyv-demonicheskoy-statui-gedo-mazo.html")
        elif self.spec=="Групповое Дзюцу" and self.first=="тигр" and self.second=="змея" and self.third=="крыса" and self.fourth=="бык" and self.fifth=="собака" and self.sixth=="овца":
            print("Использована техника Запечатывания Девяти Призрачных Драконов")
            webbrowser.open_new("https://jut.su/technique/zapechatyvanie-devyati-prizrachnyh-drakonov.html")
        elif self.spec==""
        
        else:
            print("Такой техники нет.")
            webbrowser.open_new("https://jut.su/by-episodes/")

sign_first=hand_sign()

sign_first.info()

sign_first.search()