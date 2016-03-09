
lst = [x for x in 'abcdefghijklmnopqrstuvwxyz']
output = []

for each in lst:
            output.append("".join([each.upper(),each.upper(),each.upper(),each,each.upper(),each.upper(),each.upper()]))

print (output)
f = open("links1.html",'w')

f.write('<html>')
f.write('\n')
for each in output:
    f.write("<a href = \'http://www.pythonchallenge.com/pc/def/"+each+'.html\'>'+each)
    f.write('</a>')
    f.write('\n')

f.write('</html>')

f.close()
    
