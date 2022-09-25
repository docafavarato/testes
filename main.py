import random

class tools:
    
    def __init__(self):
        pass
    
    def teste(data):
        alphabet = ['a','b','c','d','e','f', 'g', 'h', 'i',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                    'z', ' ']
        
        a = ''
        for letter in data:
            if letter == 'z':
                letter = 'a'
            else:
                next = alphabet[alphabet.index(letter) + 1]
            a += next
        print(a)

    def encript(data):
        random_chars = ['1', '2', '3', '4', '5', '6', '7',
                        '8', '9', '0', 'a', 'b', 'c', 'd',
                        'e', 'f', 'g', 'h', 'i', 'j', 'k',
                        'l', 'm', 'n', 'o', 'p', 'q', 'r',
                        's', 's', 't', 'u', 'v', 'w', 'x',
                        'y', 'z', '!', '@', '#', '$', '%',
                        '¨', '&', '*', '(', ')', '_', '-',
                        '+', '=', '{', '}', '[', '],', '^']
        
        key = {}
        a = ''
        for letter in data:
            rand = random.choice(random_chars)
            a += rand
            key[letter] = rand
        
        with open('keys.txt', 'a') as output:
            output.write(f'{key}\n')
        print(key)
        print(a)


    def decrypt(key):
        with open('keys.txt') as output:
            lines = output.readlines()
            for line in lines:
                if key in line:
                    print(line)
                    
    def increasing(list):
        '''Organiza a lista em ordem crescente'''
        new_list = [] # cria uma lista nova
        for i in range(len(list)): # define um loop com a duração da quantidade de elementos
            new_list.append(min(list)) # insere o menor valor na nova lista
            list.pop(list.index(min(list))) # remove esse valor da lista
        
        return new_list
    
    def decreasing(list):
        '''Organiza a lista em ordem decrescente'''
        new_list = [] # cria uma lista nova
        for i in range(len(list)): # define um loop com a duração da quantidade de elementos
            new_list.append(max(list)) # insere o maior valor na nova lista
            list.pop(list.index(max(list))) # remove esse valor da lista
            
        return new_list
            
    def even(num):
        '''Verifica se um número é par'''
        if num % 2 == 0:
            return True
        else:
            return False
    
    def odd(num):
        '''Verifica se um número é ímpar'''
        if num % 2 != 0:
            return True
        else:
            return False
        
    def random_strings(amount, infinite=False):
        '''Gera strings aleatórias'''
        amount+=1
        random_chars = ['1', '2', '3', '4', '5', '6', '7',
                        '8', '9', '0', 'a', 'b', 'c', 'd',
                        'e', 'f', 'g', 'h', 'i', 'j', 'k',
                        'l', 'm', 'n', 'o', 'p', 'q', 'r',
                        's', 's', 't', 'u', 'v', 'w', 'x',
                        'y', 'z', '!', '@', '#', '$', '%',
                        '¨', '&', '*', '(', ')', '_', '-',
                        '+', '=', '{', '}', '[', '],', '^']
        
        if infinite:
            while True:
                print(f'{random.choice(random_chars)}{random.choice(random_chars)}{random.choice(random_chars)}{random.choice(random_chars)}{random.choice(random_chars)}{random.choice(random_chars)}')
        else:
            for i in range(amount):
                print(f'{random.choice(random_chars)}{random.choice(random_chars)}{random.choice(random_chars)}{random.choice(random_chars)}{random.choice(random_chars)}{random.choice(random_chars)}')
                
    def fibonacci(amount):
        sequence = [1, 1] # cria uma lista com os dois valores inicias da sequência de Fibonacci
        
        for i in range(amount): # retorna a quantidade de números da sequência desejada 
            sequence.append(sequence[-1] + sequence[-2]) # adiciona na lista a soma entre os dois últimos elementos
        
        return sequence 
    
print(tools.decreasing([7, 1, 8, 3]))


        
        
        
