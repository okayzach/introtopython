def hello():
    print('Hello user')

def pack(arg1, arg2, arg3):
    packlist = [arg1, arg2, arg3]
    print(packlist)
    return packlist

def eat_lunch(list):
    print(f"First I eat {list[0]}")
    i = 1
    while i < len(list):
        print(f"Next I eat {list[i]}")
        i += 1
    print("There's nothing left in my lunchbox")

hello()

pack('fruit', 'veggies', 'milk')

my_list = ['apple', 'banana', 'salmon', 'rootbeer']

eat_lunch(my_list)