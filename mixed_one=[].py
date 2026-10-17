mixed_one=[]
mixed_two=[]
mixed_list=[10,"",20,"name2",30,"name3",40,"name4"]
for item in mixed_list:
    if isinstance(item, (int , float)):
        mixed_one.append(item)
    else:
        mixed_two.append(item)
print("Numbers (int/float):", mixed_one)
print("Other items (strings):", mixed_two)
 