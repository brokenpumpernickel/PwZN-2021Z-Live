# def my_super_generator():
#     yield 'Hello'
#     yield 'World'

# for e in my_super_generator():
#     print(e)

def lame_range(max_number):
    for i in range(max_number):
        if i > 5:
            return
        yield i

for i in lame_range(10):
    print(i)
