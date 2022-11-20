import time

start_time = time.time()

for i in range(1, 1000):
    n = i
    pro = 1
    dig: int = 1
    while n > 0:
        dig = n % 10
        n = n // 10
        pro *= dig

    for j in range(1001, 10000):
        no = j
        pros: int = 1
        digs = 1,
        while no > 0:
            digs = no % 10
            no = no // 10
            pros *= digs
        l = []
        m = []
        if pros > 100 and pro > 100:
            if pros == pro:
                n1 = i
                while n1 > 0:
                    x =  n1 % 10
                    n1 = n1//10
                    l.append(x)
                l=l[::-1]

                no1 = j
                while no1 > 0:
                    x =  no1 % 10
                    no1 = no1//10
                    m.append(x)
                m=m[::-1]




                if l[1] == l[0] + 1 and l[2] == l[1]+1 and m[1] == m[0] + 1 and m[2] == m[1]+1 :
                    print(f"****** {i} and {j} = {pro} *********")





print("time elapsed: {:.2f}s".format(time.time() - start_time))
