# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/02 10:02:37 by archid-           #+#    #+#              #
#    Updated: 2023/04/27 15:51:32 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class ObjectC(object):
    def __init__(self):
        pass

def what_are_the_vars(*args, **kwargs):
    c = ObjectC()
    var_i = 0
    for val in args:
        var_name = 'var_' + str(var_i)
        var_i += 1
        try:
            getattr(c, var_name)
        except:
            return None
        setattr(c, var_name, val)

    for var in kwargs.keys():
        try:
            getattr(c, var)
        except:
            return None
        setattr(c, var, kwargs[var])
    return c

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == '__main__':
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)