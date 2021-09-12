def add(a,b):
    result=a+b
    return result
def minus(a,b):
    result=a-b
    if result<0:
        result=b-a
    return result
def cheng(a,b):
    result=a*b
    return result
def div(a,b):
    result=a/b
    return result
def biao(k,j):
    for i in range(1,k):
        for j in range(1,i+1):
            print(i,'*',j,'=',i*j,end='\t')
        print()
def encode(s):
    q =input('请选择编码方式：GBK or UTF-8')
    if q == 'GBK':
        byte=s.encode(encoding='GBK')
    else:byte=s.encode(encoding='UTF-8')
    return  byte
def decode(s):
    q = input('请选择解码方式：GBK or UTF-8')
    print('请输入对应的编码方式，否则报错')
    if q == 'GBK':
        byte = s.decode(encoding='GBK')
    else:
        byte = s.decode(encoding='UTF-8')
    return byte
def list():
    print('-------------')
    print('欢迎进入Bankrotteur个人Python程序展示')
    print('下面是temporary项目')
    print('1.加减乘除')
    print('2.乘法口诀表')
    print('3.文字编码解码')
    print('-------------')
def display(q):
    if q == '1':
        print('您选择的是1.加减乘除')
    elif q=='2':
        print('您选择的是2.乘法口决表')
    elif q=='3':
        print('您选择的是3.编码解码')



list();
q2=input('请选择是需要的程序：1 or 2 or 3')
display(q2)

if q2 == '1':
    a = int(input('请输入第一个数'))
    b = int(input('请输入第二个数'))
    q=input('请输入需要的操作：加减乘除')
    if q=='加':
        result=add(a,b)
    elif q=='减':
        result=minus(a,b)
    elif q=="乘":
        result=cheng(a,b)
    elif q=='除':
        result=div(a,b)
    print('结果是',result)
elif q2=='2':
    k=int(input('请输入您需要输出的行数'))
    j=int(input('请输入您需要输出的列数'))
    result=biao(k,j)
    print(result)
elif q2=='3':
    s=input('请输入需要编码的字符：')
    result=encode(s)
    print(result)
    result2=decode(result)
    print(result2)

