nome = 'RENATO ALVES SOARES'

print(nome[:: -1])

print(nome.lower())

# Strings - formatting v1
"Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
"Cisco model: %s, %d WAN slots, IOS %.f" % ("2600XM", 2, 12.4)
"Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM", 2, 12.4)
model = '2600XM'
slots = 2
ios = 12.4

nome1 = f"Cisco model: {model}, {slots} WAN SLOTS, IOS VERSION {ios}"

print(nome1)
print(pow(2, 11))

# Lists
list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]  # creating a list

len(list)  # returns the number of elements in the list

list1[0]  # returns "Cisco" which is the first element in the list (index 0)

list1[0] = "HP"  # replacing the first element in the list with another value
