

with open("fields.txt") as f:
    lines = f.read().splitlines()
print (lines)

op=[]

for each in lines:
    op.append("TRACE_LOG(MSG_LEVEL_ALWAYS,\"sizeof "+each+" is %d,0,0,TRC_DW_PARAM1(sizeof("+each+")));")

print(lines)
for each in op:
    print(each)
