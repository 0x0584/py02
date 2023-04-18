# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/02 06:36:10 by archid-           #+#    #+#              #
#    Updated: 2023/04/18 13:36:24 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable. 
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return: 
        An iterable. None if the iterable can not be used by the function.
    """
    for val in iter(iterable):
        yield function_to_apply(val)

if __name__ == '__main__':
    l = list(ft_map(lambda x: x ** 2, [1, 2, 3]))
    for v in l:
        print(v)
    try:
        ft_map(lambda x: x, None)
        assert False
    except:
        assert True    
    try:
        ft_map(lambda x: x, 1)
        assert False
    except:
        assert True
