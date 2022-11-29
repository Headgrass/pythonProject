import mod_dictionary
import mod_search
import data

def start():
      print("Вас приветствует БД Работников. \n"
            "Здесь вы можете: \n"
            "1. Посмотреть всех сотрудников командой: all\n"
            "2. Добавлять нового работника командой: new\n"
            "3. Удалить сотрудника командой: del\n"
            "4. Выполнить поиск сотрудника в диапазоне года рождения sb\n"
            "5. Выполнить поиск сотрудника в диапазоне заработной платы ss\n"
            "6. Выполнить поиск сотрудника по специальности, например: sm")

start()
x = str(input("Введите ваш запрос: "))


def action_b (action):
      match action:
            case "all":
                  data.all_views()
            case "new":
                  new_e = str(input("Введите данные в таком формате:"
                                  "Павлов Павел Павлович Мужчина 13,6,1989 89153571232 Грузчик 30000:\n"))
                  data.new_employe(new_e)
                  print("У вас всё получилось")
                  start()
            case "del":
                  del_e = str(input("Введите del и ID сотрудника, например del 10002"))
                  data.deleteemloye(del_e)
                  print(f"Сотрудник с ID{del_e} успешно удален")
                  start()
            case "sb":
                  sb_e = str(input("Введите диапазон дат, например: 1985 1999"))
                  print(mod_search.search_by_bd(sb_e))
                  start()
            case "ss":
                  ss_e = str(input("Введите диапазон зарплат для поиска, например 30000 50000"))
                  mod_search.search_by_salary(ss_e)
                  start()
            case "sm":
                  sm_e = str(input("Введите специальности, например: Слесарь"))
                  mod_search.search_by_major(sm_e)
                  start()

action_b(x)