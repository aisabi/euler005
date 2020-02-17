def smallestMult(n):
    # Counter method to count the number of times I got the same occurence
    from collections import Counter 
    liste = []
    listesmallestMult = []
    # for performance reason, the test is limited to 9999, change 10000 number to enlarge the limit
    # loop until it reaches the 'n' parameter. If 'n' parameter == 5 it loops from 1 to 5
    # put all numbers with remainder == zero in a list 
    x = range(1,10000) 
    tour = 1
    while tour <= n:
        for i in x:
            print(i)
            if i%tour == 0:
                print('match', i , tour)
                liste.append(i)
        tour = tour + 1
        #print('LALISTE',liste)
    # classify each number according to the number of times it gets a remainder ==0
    # Example : 7020 is an integer and can be divided from 1 to 5 and get a remainder == 0 each time
    listeNombre = Counter(liste) # 
    #print('listeNombre :',listeNombre)
    # for the 2 items, number is called 'c' and each loop is called 'd'
    for c,d in listeNombre.items():
        #if loop item from listeNombre == loop item from 'n'
        #append the data in 'listesmallestMult'
        if d == tour-1:
            print(d)
            print('Answer :',c)
            listesmallestMult.append(c)
        
    # use min() method to get the smallest positive number that is evenly divisible by all of the numbers from 1 to n
    print(listesmallestMult)# final list
    minimal = min(listesmallestMult)
    print('The smallest Multiple for', n, 'is', minimal)
            
        
smallestMult(10)