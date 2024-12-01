test=open('test.txt','r').read()
new=open('test.txt','w')
new.write('python'+test+'python')
new.close()
#这么写是因为我发现所有的写入模式都会覆盖已有内容，所以干脆直接读取整个文件再头尾再相加两个串
