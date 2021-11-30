from prettytable import PrettyTable 

mytable = PrettyTable(['name', 'age,','gender'])


mytable.add_row(['uday','23','M'])
mytable.add_row(['ajay', '22', 'M'])


print(mytable)

for row in mytable:
    print(row.get_string(fields='Column[0]'))

