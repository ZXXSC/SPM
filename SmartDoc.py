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

def lookup(fname):
    result=[]
    d={}
    f = open(fname)
    for line in f:
        if line.find("see rq")>=0:
            pattern = re.compile(r'rq\d+')
            rq=pattern.findall(line)
            result.append(rq[0])
            if rq[0] in result:
                if not rq[0] in d:
                    d[rq[0]]=1
                else:
                    d[rq[0]]+=1
    return d
        	
d=lookup(code_file)
key=list(d.keys())
value=list(d.values())

f1.write("<html><head></head><body>")
for line in file1:
    if "@Requirement" in line:
        pattern=re.compile(r"id=rq\d+")
        id=pattern.findall(line)
        idno=id[0][5:]
        idno1=int(idno)
        if value[idno1-1]==1:
            str1='<a href="code.html#rq'+idno+'" name="rq'+idno+'">'+id[0].replace('=',': ')+"</a>"
            message = """
		    <pre>%s</pre>
		    """%(line.replace('=',': ').replace('[',' ').replace(']',' ').replace(id[0].replace('=',': '),str1)) 
            f1.write(message)			
        elif value[idno1-1]>1:
            ss='<select name="'+key[idno1-1]+'"" onchange="self.location.href=options[selectedIndex].value"><option>'+key[idno1-1]+'</option>'
            s=[] 			
            for i in range(0,value[idno1-1]):
                s.append('<option value="code.html#'+key[idno1-1]+str(i+1)+'">'+key[idno1-1]+str(i+1)+'</option>')
                ss+=s[i]
                i+=1
            ss+="</select>"
            message="""
            <pre>%s</pre>
		    """%(line.replace('=',': ').replace('[',' ').replace(']',' ').replace(id[0].replace('=',': '),ss))
            f1.write(message)
    else:
        message = """
        <pre>%s</pre>
        """%(line.replace('=',': ').replace('[',' ').replace(']',' '))
        f1.write(message) 
    f1.write("</html></body>")
f1.close()

i=1
f2.write("<html><head></head><body>")
for line in file2:   
    if line.find("see rq")>=0:
        pattern=re.compile(r"#{see rq\d+")
        id=pattern.findall(line)
        idno=id[0][8:]
        idno1=int(idno)
        if value[idno1-1]==1:
            str2='<a href="srs.html#rq'+idno+'" name="rq'+idno+'">'+id[0]+'}</a>'
            message = """
		    <pre>%s</pre>
		    """%(line.replace(id[0]+"}",str2)) 
            f2.write(message)		
        elif value[idno1-1]>1:      
            str3='<a href="srs.html#'+key[idno1-1]+'" name="'+key[idno1-1]+str(i)+'">#{see '+key[idno1-1]+'}'+'</a>'             
            i+=1
            message="""
            <pre>%s</pre>
		    """%(line.replace(id[0]+"}",str3))
            f2.write(message)
    else:
        message = """
        <pre>%s</pre>
        """%(line)
        f2.write(message) 
    f2.write("</html></body>")
f2.close()
webbrowser.open(GEN_HTML1,new = 1) 
webbrowser.open(GEN_HTML2,new = 1) 
