immutable_var = ( 1,"one",2,"apple","banan",[1,2,3,4],True)
print(immutable_var)
# immutable_var[0] = 2
#TypeError: 'tuple' object does not support item assignment
#Главное свойство кортежа - это невозможность изменить содержимое кортежа после его создания
mutable_list = [1,"one",2,[1,2,3,4],'banana','apple',True]
mutable_list[0] = 'two'
mutable_list[1] = 3
print(mutable_list)



