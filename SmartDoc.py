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

webbrowser.open(GEN_HTML1,new = 1) 
webbrowser.open(GEN_HTML2,new = 1) 
