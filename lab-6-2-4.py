s = tuple(input('Write names students: ').split())
 
print( *tuple(i for i in s if 'ва' in i) )

# Асан Вова Елена Ева Лена Нұр Олжас

