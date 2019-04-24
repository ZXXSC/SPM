def lines(file):
    for line in file:yield line
    yield '\n'

import sys,re

print ('<html><body>')

for line in lines(sys.stdin):
    line = re.sub(r'\*(.+?)\*',r'<em>\1</em>',line)
    if line.startswith('@Requirement [id=rq1]'):
        print('<pre><a href="Word_Frequency.html#def1" name="rq1" target="_blank">'+line+'</a></pre>')
    elif line.startswith('@Requirement [id=rq2]'):
        print('<pre><a href="Word_Frequency.html#def2" name="rq2" target="_blank">'+line+'</a></pre>')
    elif line.startswith('@Requirement [id=rq3]'):
        print('<pre><a href="Word_Frequency.html#def3" name="rq3" target="_blank">'+line+'</a></pre>')
    elif line.startswith('@Requirement [id=rq4]'):
        print('<pre><a href="Word_Frequency.html#def4" name="rq4" target="_blank">'+line+'</a></pre>')
    elif line.startswith('#{see rq1}'):
        print('<pre><a href="SmartDocSRS.html#rq1" name="def1" target="_blank">'+line+'</a></pre>')
    elif line.startswith('#{see rq2}'):
        print('<pre><a href="SmartDocSRS.html#rq2" name="def2" target="_blank">'+line+'</a></pre>')
    elif line.startswith('#{see rq3}'):
        print('<pre><a href="SmartDocSRS.html#rq3" name="def3" target="_blank">'+line+'</a></pre>')
    elif line.startswith('#{see rq4}'):
        print('<pre><a href="SmartDocSRS.html#rq4" name="def4" target="_blank">'+line+'</a></pre>')
    else:
        print('<pre>'+line+'</pre>')

print('</body></html>')
