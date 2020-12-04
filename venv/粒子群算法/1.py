class Stu:
    def __init__(self,name,yw,sx,yy):
        self.name=name
        self.yw=yw
        self.sx=sx
        self.yy=yy

    def score_sum(self):
        return self.yw+self.sx+self.yy

    def print_score(self):
        msg="{name}的成绩是：语文：{yw_score},数学：{sx_score},英语：{yy_score}".format(name=self.name,yw_score=self.yw,sx_score=self.sx,yy_score=self.yy)

        print(msg)
        msg1="{name}的总成绩是：{score}".format(name=self.name,score=self.score_sum())
        print(msg1)

stus=[]
with open('成绩单','r',encoding='utf-8') as file:
    lines=file.readlines()
    print('lines:',lines)
    print(type(lines))
    for i in range(1,len(lines)):
        line=lines[i]
        print('line:',line)
        print('line 的type',type(line))
        arrs=line.split()
        print('arrs de type',type(arrs))
        print(arrs)
        s = Stu(arrs[0],int(arrs[1]),int(arrs[2]),int(arrs[3]))
        print('s de type',type(s))
        stus.append(s)

for stu in stus:
    stu.print_score()

