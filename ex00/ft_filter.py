# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/02 07:07:32 by archid-           #+#    #+#              #
#    Updated: 2023/04/18 13:34:16 by archid-          ###   ########.fr        #
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
    arr = [1, 2, 3, 4, 5]
    func = lambda foo: not (foo % 2)
    assert list(filter(func, arr)) == list(ft_filter(func, arr))