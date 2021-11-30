s=[]
x=0
y=0
f = open("dict_a.txt","r",encoding='utf-8')
f1 = open("output.txt","w",encoding='utf-8')
line=f.readline()

for i in range(0,60480):
      for line in f.readline():#這邊是readline
            # print(x)
            if y==0:
                  if x==0:
                        if line!= ',':
                              s.append(line)
                              f1.write(line)
                        elif line == ',':
                              f1.write('   ')
                              x=1
                  elif x==1:
                        if line == ',':
                              x=2
                  elif x==2:
                        if line == ',':
                              x=0
                              y=1
                  
            elif y==1:
                  if line =='"':
                        continue
                  elif x==0:
                        if line!= ',':
                              s.append(line)
                              f1.write(line)
                        elif line == ',':
                              f1.write('   ')
                              x=1

                  elif line == '\n':
                        x=0
                        y=0
                        f1.write(line)
                        
f.close()
f1.close()