#coding:utf-8 
#输出的内容
str="a string to  122  print to file"
#路径（生成文件）（w代表写，r是只读）
f=open('0out.txt','w')
#将输出的内容写入文件
print >>f,str
#关闭文件，一定要关
f.close()