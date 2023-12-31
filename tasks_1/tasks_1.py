#функция чтения файла и возвращения пронумерованных строк
def read_file(file_txt):
    with open(file_txt, "r") as file:
        lines = file.readlines()
    modified_lines = [f"{n}: {line}" for n, line in enumerate(lines, start=1)]
    return "".join(modified_lines)

#Функция записи файла
def create_new_file(file_original,new_file):
  content=read_file(file_original)
  with open(new_file,"w") as file:
    file.write(content)

#Запрашиваем данные у пользователя
file_original = input("Введите имя исходного файла: ")
new_file = input("Введите имя нового файла: ")
create_new_file(file_original,new_file)
