from random import randint
lostnumber=0
x = 1001
factor=0.2
x2 = 0
xptotal = 0
a=2.6
for xRound in range(20):
    a = a+0.1
    print(a)
    x = x + 1
    xa = x
    win = 0
    lose = 0
    for Round in range(5000):
        state = "lose"
        x1 = x
        f = 1
        f1 = 1
        f2=0
        counter = 1
        l = 0
        high = 0
        low = x
        #   print("Round++++++++++++=",Round)

        while (x1 > (xa / 2)) & (f2 < (factor * xa)):
            i = (randint(0, 100))
            #     print ("---------------------------")
            counter = counter + 1

            if i < 45:

                state = "win"
                x1 = x1 + f1
                f2 = f2+f1

                ##                if (high <x1):
                ##                    high=x1
                if (x1 <= (xa / 2)) | (f2 >= (factor * xa)):
                    ##                    print ("winwinwinwinwinwinwinwinwin")
                    ##                    print ("counter=", counter)
                    ##                    print ("Random=",i)
                    ##                    print ("capital=",x1)
                    ##                    print ("next bet=",f1)
                    ##                    print ("high=",high)
                    ##                    print ("low", low)
                    win = win + 1

                f1 = f
                l = 0

            else:

                state = "lose"
                x1 = x1 - f1
                l = l + 1
                f2 = f2 - f1
                f1 = a * f1


                ##                if (low>x1):
                ##                    low=x1
                if (x1 <= (xa / 2)) | (f2 >= (factor * xa)):
                    ##                    print ("lose")
                    ##                    print ("Random=",i)
                    ##                    print ("lose in a row==============================", l)
                    ##                    print ("capital=",x1)
                    ##                    print ("next bet=",f1)
                    ##                    print ("high=",high)
                    ##                    print ("low", low)
                    lose = lose + 1

        total = win + lose
        ##    print("total win number=", win)
        ##    print("total lose number=", lose)
        ##    print("total number of rounds=",total)
        ##    print("win percentage", (win*100)/total,"%")
    xptotal = ((win * 100) / total)
    if xptotal > 70:
        print("related x=", x)
        print("best result=", xptotal)






print("lostnumber=", lostnumber)
#
#         x2 = x
# print("best result=", xptotal)
# print("related x=", x2)
