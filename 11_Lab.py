"""
Your module description
"""
v=" 1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed 61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"

v1=""
v2=""
v3=""
v4=""
v0=""
c=0
for i in v:
    if i!=v0:
        if 0<c<25:
            v1+=i
        elif 24<c<54:
            v2+=i
        
        
        elif 55<c<89:
            v3+=i
        
        else:
            v4+=i
        c+=1

print(v1)
print(v2)
print(v3)
print(v4)