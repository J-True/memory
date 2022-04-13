import random
import numpy as np

def createMemory ():
    print('You choose create your own set. If your set is complete type in (c)omplete. ')
    original_memory = []
    memory = []
    while True:

        name = input(f'Please create your {(len(original_memory)+ 1)}.object. ')
        if name == 'c':
            print(f'Your set includes following objects: {(original_memory)}')
            copy_memory = original_memory.copy()
            memory = copy_memory + original_memory
            return shuffleMemory(memory)
            break

        set = []
        set.append(name)
        original_memory = original_memory + set
        print(f'Your set includes following objects: {(original_memory)}')



def shuffleMemory (memory):
    shuffle_memory = memory
    random.shuffle(shuffle_memory)
    return selectElement(shuffle_memory)


def selectElement (memory):
    memory = memory

    while True:
        print(f'Type in a number from 1 to {(len(memory))} for choosing the first object: ')
        try:
            indexA = int(input()) - 1
            first_element = memory[indexA]

            if first_element != 'c':
                print(f'Your first object is {(first_element)}.')
                break
            else:
                print('You already found this object')

        except ValueError:
            print(f'Give me a number between 1 to {(len(memory))}.')
        except IndexError:
            print(f'Give me a number between 1 to {(len(memory))}.')


    while True:
        print(f'Type in a number from 1 to {(len(memory))} for choosing the second object: ')
        try:
            indexB = int(input()) - 1
            second_element = memory[indexB]

            if indexB == indexA:
                print('You have choosen the same object.')
            elif first_element != 'c':
                print(f'Your second object is {(second_element)}.')
                break
            else:
                print('You already found this object')

        except ValueError:
            print(f'Give me a number between 1 to {(len(memory))}.')
        except IndexError:
            print(f'Give me a number between 1 to {(len(memory))}.')

    return compareElement(second_element, first_element, memory)


def compareElement (first_element, second_element, memory):
    first_elment = first_element
    second_element = second_element
    memory = memory
    last_pair = len(memory)/2
    pair_total= 0
    indexA = memory.index(first_element)
    indexB = memory.index(second_element)



    if first_element == second_element:
        memory[indexA] = 'c'
        indexB = memory.index(second_element)
        memory[indexB] = 'c'
        pair_total = pair_total + 1

        if pair_total < last_pair:
            return selectElement(memory)
        else:
            print('You have found all objects.')

    elif first_element != second_element:
       return selectElement(memory)

    """elif first_element == second_element:
        memory[indexA] = 'c'
        indexB = memory.index(second_element)
        memory[indexB] = 'c'
        print('You have found all objects.')"""







createMemory()


