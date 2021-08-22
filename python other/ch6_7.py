import os

### ch 7 p 856
def main():
    scores = get_scores()
    total = get_total(scores)
    total -= min(scores)
    print(total/(len(scores)-1))

def get_total(s):
    tot = 0.0
    for score in s:
        tot += score
    return tot

def get_scores():
    test_scores = []
    again = 'y'
    while again == 'y':
        score = float(input('enter score: '))
        test_scores.append(score)
        again = input('again? ')
    return test_scores

main()

####### ch 7 p 845
'''
NUM_EMP = 3
def main():
    hrs_worked = [0] * NUM_EMP
    for emp in range(NUM_EMP):
        print('hrs worked by emp ', emp+1)
        hrs_worked[emp] = int(input())

    pay_rate = float(input('enter pay rate '))
    for index in range(NUM_EMP):
        pay = hrs_worked[index] * pay_rate
        print('emp ', index+1, 'gross pay: ', pay)
main()
'''


####### ch 6 p735-751
# write out
'''
def main():
    coffee_file = open('coffee.txt', 'a')
    keepGoing = 'y'
    while keepGoing == 'y':
        description = input('enter name of coffee ')
        quantity = float(input('enter amt in inventory '))
        coffee_file.write(description + '\n')
        coffee_file.write(str(quantity) + '\n')
        keepGoing = input('keep going? ')
    coffee_file.close()
main()
'''
# read in
'''
def main():
    coffee_file = open('coffee.txt', 'r')
    description = coffee_file.readline()

    while description != '':
        quantity = float(coffee_file.readline())
        #quantity = quantity.rstrip()
        description = description.rstrip()

        print('Description: ',description)
        print('quantity', quantity)
        description = coffee_file.readline()
    coffee_file.close()
main()
'''
# search for a record
'''
def main():
    found = False
    coffee_file = open('coffee.txt', 'r')
    search_item = input('item to search for: ')
    description = coffee_file.readline()

    while description != '':
        quantity = float(coffee_file.readline())
        description = description.rstrip('\n')

        if description == search_item:
            print(description, '\t', quantity)
            found = True
        description = coffee_file.readline()
    coffee_file.close()
    if not found:
        print('not found')
main()
'''
# modifying records     # have to create a temp file
'''
def main():
    found = False
    coffee_file = open('coffee.txt', 'r')
    coffee_new = open('coffee2.txt','w')
    description_change = input('which coffee to change ')
    qty_change = float(input('new quantity = '))

    description = coffee_file.readline()

    while description != '':
        qty = float(coffee_file.readline())
        description = description.rstrip('\n')
        if description == description_change:
            coffee_new.write(description + '\n')
            coffee_new.write(str(qty_change) + '\n')
            found = True
        else:
            coffee_new.write(description + '\n')
            coffee_new.write(str(qty) + '\n')
        description = coffee_file.readline()
    coffee_file.close()
    coffee_new.close()
#    os.remove('coffee.txt')
#    os.rename('coffee2.txt', 'coffee.txt')
    if found:
        print('file updated')
    else:
        print('item not found')
main()
'''
# deleting records      $ have to create a temp file
'''
def main():
    delete_record = input('what record to delete? ')
    c_file = open('coffee.txt', 'r')
    c_temp = open('coffee2.txt', 'w')
    descr = c_file.readline()
    found = False
    while descr != '':
        qty = float(c_file.readline())
        descr = descr.rstrip('\n')
        if descr != delete_record:
            c_temp.write(descr + '\n')
            c_temp.write(str(qty))
        else:
            found = True
        descr = c_file.readline()
    c_temp.close()
    c_file.close()
    #os.remove('coffee.txt')
    #os.rename('coffee2.txt', 'coffee.txt')
    if found:
       print('file uodated')
    else:
       print('item not found')
main()
'''

###### ch6, p 722
'''
def main():
    num_videos = int(input('enter num videos '))
    outfile = open('videos.txt','w')
    for video in range(1, num_videos + 1):
        run_time = float(input('video run time #' + str(video) + ': ' ))
        outfile.write(str(run_time) + '\n')
    outfile.close()
main()
'''
'''
def main():
    running_times = 0 #count
    total_runtimes = 0 #accumulator
    infile = open('videos.txt', 'r')
    for video in infile:
        line = float(video)
        total_runtimes += line
        print(line)
        running_times += 1
    infile.close()
    print(running_times)
    print(total_runtimes)
main()
'''

