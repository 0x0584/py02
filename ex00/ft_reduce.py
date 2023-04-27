# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/02 07:09:36 by archid-           #+#    #+#              #
#    Updated: 2023/04/27 15:37:43 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from functools import reduce

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """

    prev = None
    for val in iter(iterable):
        if prev is None:
            prev = val
        else:
            prev = function_to_apply(prev, val)
    return prev
    
    
if __name__ == '__main__':
    def reduce_test(func, arr):
        assert reduce(func, arr) == ft_reduce(func, arr)
        
    reduce_test(lambda x, y: x ** y, [1, 2, 3, 3, 4])
    reduce_test(lambda x, y: x + y, "abcdef")
    reduce_test(lambda x, y: x - y, [10, 9, 8, 7])
    print(">>> All tests passed")