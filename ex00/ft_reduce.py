# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/02 07:09:36 by archid-           #+#    #+#              #
#    Updated: 2023/04/02 07:12:19 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
            yield prev
