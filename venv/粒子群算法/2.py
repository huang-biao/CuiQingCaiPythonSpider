class Stu:
    def __init__(self, name, yw, sx, en):
        self.name = name
        self.yw = yw
        self.sx = sx
        self.en = en

    def score_sum(self):
        return self.yw + self.sx + self.en

    def print_score(self):
        msg = "{name}的各科成绩如下: 语文:{yw_score}, 数学:{sx_score}, 英语:{en_score}".format(name=self.name, yw_score = self.yw,sx_score = self.sx,en_score = self.en
                                                )
        print(msg)
        msg = "{name}的总成绩是{score}".format(name=self.name, score=self.score_sum())
        print(msg)

stus = []
with open('成绩单', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(1, len(lines)):
        line = lines[i]
        arrs = line.split()
        s = Stu(arrs[0], int(arrs[1]), int(arrs[2]), int(arrs[3]))
        stus.append(s)

for stu in stus:
    stu.print_score()