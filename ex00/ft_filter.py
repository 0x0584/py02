# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/02 07:07:32 by archid-           #+#    #+#              #
#    Updated: 2023/04/26 20:59:30 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable. None if the iterable can not be used by the function.
    """
    
    for val in iter(iterable):
        if function_to_apply(val):
            yield val

if __name__ == '__main__':
    def filter_test(func, arr):
        assert list(filter(func, arr)) == list(ft_filter(func, arr))
    filter_test(lambda foo: not (foo % 2), [1, 2, 3, 4, 5])
    filter_test(lambda foo: not (foo % 2), [1, 3, 5])
    filter_test(lambda foo: not (foo % 2), [2, 4])
    filter_test(lambda foo: (foo % 2), [1, 2, 3, 4, 5])
    filter_test(lambda foo: (foo % 2), [1, 3, 5])
    filter_test(lambda foo: (foo % 2), [2, 4])
    filter_test(lambda foo: foo, [])
    # filter_test(lambda foo: foo, None)
    # filter_test(lambda foo: foo, 1)
    filter_test(lambda foo: foo, {1, 2, 3, 4, 5})
    filter_test(lambda foo: foo, {"0": 1, "1": 2, "3": 2})
    print(">>> All tests passed!")
