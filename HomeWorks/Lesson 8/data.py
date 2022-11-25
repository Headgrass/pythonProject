
def new_employe(object):
    with open("bd_emloyees.txt", 'a') as fo:
        fo.write(str(object))
        print("Новый работник внесен в БД.")
        fo.close()

def all_views():
    with open("bd_emloyees.txt", 'r') as fo:
        fo.read()
        return fo

def deleteemloye(id):
    with open("bd_emloyees.txt", 'a') as fo:
        fo.__delattr__(id)
        print("Новый работник внесен в БД.")
