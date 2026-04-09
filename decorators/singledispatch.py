from functools import singledispatch


@singledispatch
def count_down(data_type):
    raise ValueError(f"Unsupported data type: {type(data_type)}")

@count_down.register(int)
@count_down.register(float)
@count_down.register(str)
def _(data_type):
    data = str(data_type)
    for c in data:
        print(data)
        data = data.replace(data[-1], '')
        

@count_down.register(dict)
def _(data_type):
    all_keys = data_type.keys()
    new_str = ""
    for k in all_keys:
        new_str += str(k)
    count_down(new_str)
    
@count_down.register(list)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(range)
def _(data_type):
    new_arr = "".join([str(i) for i in data_type])
    count_down(new_arr)



# count_down(1234)
# count_down(12.5)
# count_down('12345')
# count_down(12345)
# count_down(12.345)
count_down((1,2,3))
# count_down([1,2,3,4])