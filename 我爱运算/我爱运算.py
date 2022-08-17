import pyinputplus as pyip
import random as rd
import sys

def menu():
    print('='*40)
    print('='*12+"    我爱运算    "+'='*12)
    print("======= 1.加减运算    2.乘除运算 =======")
    print("=======        3.四则运算        =======")
    print('='*40)

def choice():
    ans1=eval(input("请选择："))
    print("======= 1.10以内运算     2.50以内运算   =======")
    print("======= 3.100以内运算    4.1000以内运算 =======")
    ans2=eval(input("请选择："))
    return ans1,ans2

def main(res):
    while True:
        symbol={1:"+-",2:"*/",3:"+-*/"}
        number={1:10,2:50,3:100,4:1000}
        int_num=rd.randint(2,5)
        flo_num=rd.randint(0,2)
        lis=[]
        for i in range(int_num):
            lis.append(str(rd.randint(1,number[res[1]])))
            lis.append(rd.choice(symbol[res[0]]))
        if flo_num:
            lis.append(str(round(rd.uniform(0,number[res[1]]),1)))
        if lis[-1] in "+-*/":
            lis.pop()
        for item in lis:
            print(item,end=' ')
        print('=')
        tmp=eval(''.join(lis))
        if pyip.inputNum()==tmp:
            print("答对了")
        else:
            print("答错了")
            print(f"正确答案是:{tmp}")
        cho=pyip.inputChoice(['y','n','e'],prompt="是否继续：(y/n/e)")
        if cho=='n':
            break
        elif cho=='e':
            sys.exit()

if __name__ == "__main__":
    while True:
        menu()
        res=choice()
        main(res)
