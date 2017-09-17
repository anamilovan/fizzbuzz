y = int(raw_input("Vnesite stevilo med 1 in 100"))

for x in range(1,y+1):
        if x%3 == 0 and x%5 == 0 :
            print "fizzbuzz"
        elif x%3 == 0:
            print "fizz"
        elif x%5 == 0 :
            print "buzz"
        else:
            print x