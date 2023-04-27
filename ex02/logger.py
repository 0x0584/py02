# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/02 10:25:17 by archid-           #+#    #+#              #
#    Updated: 2023/04/26 21:32:12 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from random import randint
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time.monotonic()
        ret = func(*args, **kwargs)
        en = time.monotonic()
        t = (en - st) * 1000
        suff = 'ms'
        if t > 1000:
            t /= 1000
            suff = 's'
        with open('machine.log', 'a+') as f:
            f.write('Running: {:16} {:.3f}{}\n'.format(
                ' '.join([part.capitalize() for part in func.__name__.split('_')]),
                t, suff))
        return ret
    return wrapper

class CoffeeMachine(): 
    water_level = 100
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    @log
    def boil_water(self): 
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print('Coffe is ready!')
            
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print('Blub Blub Blub...')
        
if __name__ == "__main__":
    machine = CoffeeMachine() 
    for i in range(0, 5):
        machine.make_coffee()
    
    machine.make_coffee()
    machine.add_water(70)