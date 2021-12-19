from item import Item
from doList import DoList


def walcome():
    print('*****< Walcome to Do list >***** ')
    print('*' * 32)
    print()

def help():
    print("""*COMMANDS:
           * HELP   : list all commads.
                      ['HELLP', 'help','H','h']

           * SHOW   : show the items lis.
                      ['SHOW', 'show', 'S', 's']

           * CLEAR  : clear the list.
                      ['CLEAR','clear','C','c']

           * ADD    : to add a new item.
                      ['ADD','add', 'A','a']

           * LENGTH : to show list length.
                      ['LENGHT', 'length', 'L', 'l']

           * DELETE : to delete an item.
                      ['DELETE', 'delete', 'D', 'd']

           * STOP   : to qouit.
                      ['-1', 'STOP', 'stop', 'Q','q']

           * TOTAL  : the sum of items in the list.
                      ['TOTAL', 'total', 'T', 't']

           * FIND   : to find an item.
                      ['FIND', 'find', 'F', 'f']
            
           """)


def newItem(name, count = 0):
    new_item = Item(name, count)
    return new_item


def userInput():
    item_name = str(input('Enter the item name: '))
    item_count = int(input('Enter how many you need: ') or 0)
    return item_name, item_count 

def loopOver(lst, n):
    for i in lst:
        if i.getName() == n :
            return True  , i
    
    return False , n



def main():
    new_lst = DoList()

    walcome()
  

    while True:

        userCommand = input('> ')
        print()
          
        if userCommand in ['-1', 'STOP', 'stop', 'Q','q']:
            del new_lst
            print('Goodbye, See you later.')
            break
        
        elif userCommand in ['HELLP', 'help','H','h']:
            help()

        elif userCommand in ['ADD','add', 'A','a']:

            input_name, input_count = userInput()
            item_n = newItem(input_name, input_count)
            new_lst.add(item_n)
            print(f'{new_lst.length()} been added to the list.')

        elif userCommand in ['DELETE', 'delete', 'D', 'd']:
            userDelete = input('Enter the item name: ')
        
            funcReturn = loopOver(new_lst, userDelete)
            if funcReturn[0] :
                print(f'{funcReturn[1]} been deleted')
                new_lst.delete(funcReturn[1])
                print(f'{new_lst.length()} item(s) still in the list.')

            else:
                print(f'{userDelete} Not in the list. Try again!')
            
        elif userCommand in ['TOTAL', 'total', 'T', 't']:
            print(f'the total of the list items is {sum(new_lst)}')

        elif userCommand in ['FIND', 'find', 'F', 'f']:
            userFind = input('Enter what are you looking for: ')
            findReturn = loopOver(new_lst, userFind)
            if findReturn[0]:
                print(f'{findReturn[1]} been found')
            else:
                print(f'{findReturn[1]} not found.')

        elif userCommand in ['LENGHT', 'length', 'L', 'l']:

            print(f'The length of the list is: {new_lst.length()}')

        elif userCommand in ['SHOW', 'show', 'S', 's']:

            for l_item in new_lst:
                print(l_item)
        
        elif userCommand in ['CLEAR','clear','C','c']:

            new_lst.clearAll()
            print('All items been deleted from the list.')

    
main()