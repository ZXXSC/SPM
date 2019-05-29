import webbrowser
import sys,re
from sys import argv

script,srs_file,code_file=argv
file1=open(srs_file,"r")
file2=open(code_file,"r")
GEN_HTML1 = "srs.html" 
GEN_HTML2 = "code.html"
f1 = open(GEN_HTML1,'w')
f2 = open(GEN_HTML2,'w')

f1.write("<html><head></head><body>")
f2.write("<html><head></head><body>")
i=0
for line in file1:
    if "@Requirement" in line:
        i+=1
        message = """
        <pre><a href="code.html#rq%d" name="rq%d">%s</a></pre>
        """%(i,i,line.replace('=',' ').replace('[',' ').replace(']',' '))
        if i==1:
            message = """
            <pre><a href="code.html#rq1" name="rq1">%s</a></pre>
	    <pre><a href="code.html#rq11" name="rq1">rq=11</a></pre>
	    """%(line.replace('=',' ').replace('[',' ').replace(']',' '))
    else:
         message = """
        <pre>%s</pre>
        """%(line.replace('=',' ').replace('[',' ').replace(']',' '))
    f1.write(message) 



result=[]
d={}
for line in file2:
    if line.find("see rq")>=0:
        pattern = re.compile(r'rq\d+')
        rq=pattern.findall(line)
        result.append(rq[0])
        if rq[0] in result:
            if not rq[0] in d:
                d[rq[0]]=1
            else:
                d[rq[0]]+=1

key=list(d.keys())
value=list(d.values())
i=0

for j in range(-1,len(d)-1):
    j+=1
    file2=open(code_file,"r")#待修改
    f2.write("<html><head></head><body>")
    for line in file2:    	
        if (line.find("see "+key[j])>0):
            print(j)
            if value[j]>1:
                i+=1
                message="""
                <pre><a href="srs.html#%s" name="%s%d">%s</a></pre>
                """%(key[j],key[j],i,line)
                message2="""
                <pre><a href="code.html#%s%d">%s%d</a></pre>
                """%(key[j],i,key[j],i)
                f1.write(message2)
                f2.write(message)
            print(value[j]==1)
            if value[j] is 1:
                print(value[j])
                message = """
                <pre><a href="srs.html#%s" name="%s">%s</a></pre>
                """%(key[j],key[j],line)
                f2.write(message)
            print(j)
        else:
            message = """
            <pre>%s</pre>
            """%(line)
            f2.write(message)

f1.write("</body></html>")
f2.write("</body></html>")
f1.close()
f2.close()
webbrowser.open(GEN_HTML1,new = 1) 
webbrowser.open(GEN_HTML2,new = 1) 
