immutable_var=('book', 99.8, 10, ['table', 'chair', 2])
print(immutable_var)
print(immutable_var[0])
immutable_var[3][2]='sofa'
print(immutable_var)
#tuple- неизменяемый, упорядоченный тип данных, включает различные типы данных, но изменять элементы внутри кортежа нельзя, т.к. кортежи не поддерживают обращение по элементам. Но може внутри хранить изменяемые объекты, например списки.
mutable_list=['manager', 'expert', 'specialist', [0,0,0]]
print(mutable_list)
mutable_list[3]='top_manager'
print(mutable_list)





