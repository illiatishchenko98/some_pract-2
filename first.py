
num =  [32, 2332, 2232, 2232, 353, 'hello']
print(num)
print(len(num))

new_num = num[:4]
print(new_num)

num[2] = 'Illia'

print(num)

new_num.append('OK')

new_num.insert(0, 'Its me')


new_num.pop(1) #by index

new_num.remove(2232) # exactly remove
print(new_num)



number_list = [32, 23, -23, 69]

letter_list = ['asd', 'adfa', 'gttt', 'bcvcb']


number_list.sort()
letter_list.sort()

print(number_list)
print(letter_list)


top = [32, 3243, 242]
top.pop(1)
print(top)