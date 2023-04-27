# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/02 06:36:10 by archid-           #+#    #+#              #
#    Updated: 2023/04/26 21:01:42 by archid-          ###   ########.fr        #
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
    def map_test(func, arr):
        assert list(map(func, arr)) == list(ft_map(func, arr))

    map_test(lambda foo: not (foo % 2), [1, 2, 3, 4, 5])
    map_test(lambda foo: not (foo % 2), [1, 3, 5])
    map_test(lambda foo: not (foo % 2), [2, 4])
    map_test(lambda foo: (foo % 2), [1, 2, 3, 4, 5])
    map_test(lambda foo: (foo % 2), [1, 3, 5])
    map_test(lambda foo: (foo % 2), [2, 4])
    map_test(lambda foo: foo, [])
    # map_test(lambda foo: foo, None)
    # map_test(lambda foo: foo, 1)
    map_test(lambda foo: foo, {1, 2, 3, 4, 5})
    map_test(lambda foo: foo, {"0": 1, "1": 2, "3": 2})
    print(">>> All tests passed!")