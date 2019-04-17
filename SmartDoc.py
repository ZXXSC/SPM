def lines(file):
    for line in file:yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
           block.append(' '+line+'<br>')
        elif block:
           yield ''.join(block).strip()
           block=[]
import sys,re


print ('<html><body>')

for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    print('<p>')
    print(block)
    print('</p>')

print('</body></html>')