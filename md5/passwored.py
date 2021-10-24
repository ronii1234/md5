my="aaaaaa"
print(my)
bit=0
for i in range(97,123):
    my=my[:0]+chr(i)+my[1:]
    for j in range(97,123):
        my=my[:1]+chr(j)+my[2:]
        for k in range(97,123):
            my=my[:2]+chr(k)+my[3:]
            for x in range(97,123):
                my=my[:3]+chr(x)+my[4:]
                for y in range(97,123):
                    my=my[:4]+chr(y)+my[5:]
                    for z in range(97,123):
                       my=my[:5]+chr(z)+my[6:]
                       print(my)
                       
