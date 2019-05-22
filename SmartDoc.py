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



j=1
file2=open(code_file,"r")
for line in file2:
    m=str(j)
    str1="#{see rq"+m+"}"
    if str1 in line:
        message = """
        <pre><a href="srs.html#rq%d" name="rq%d">%s</a></pre>
        """%(j,j,line)
        j+=1
    elif "#{see rq1}" in line:
        if not line.startswith("#"):
	        message = """
            <pre><a href="srs.html#rq%d" name="rq11">%s</a></pre>
           """%(n,line)
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
