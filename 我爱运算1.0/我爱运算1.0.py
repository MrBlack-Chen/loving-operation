import pyinputplus as pyip
import random as rd
import sys
import pyautogui as pg

def menu():
    ans1=int(pg.prompt("======  1.加减运算    2.乘除运算  ======\n=======           3.四则运算          =======",title="我爱运算"))
    ans2=int(pg.prompt("======= 1.10以内运算      2.50以内运算    =======\n======= 3.100以内运算    4.1000以内运算 =======",title="我爱运算"))
    pg.alert("  提示：结果为小数请小数点后保留两位!","我爱运算")
    return ans1,ans2

def main(res):
    symbol={1:"+-",2:"*/",3:"+-*/"}
    number={1:10,2:50,3:100,4:1000}
    num=0
    while True:
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
        tmp=round(eval(''.join(lis)),2)
        try:
            if eval(pg.prompt(''.join(lis)+'=',title="我爱运算"))==tmp:
                pg.alert("         答对了!","我爱运算")
            else:
                pg.alert(f"   答错了,正确答案是：{tmp}","我爱运算")
            num+=1
            if num==10:
                if pg.confirm("是否继续？","我爱运算")=="OK":
                    num=0
                else:
                    break
        except:
            sys.exit()

if __name__ == "__main__":
    while True:
        res=menu()
        main(res)
