from mod import Mod

a =  Mod(Mod(8146798528947,17),17)
b = Mod(Mod(11,6),6)

print ('Here is the flag')
print (min(11%6, 8146798528947%17))
#if a < b:
#    print (str(a).split('%')[0])
#else:
#    print (str(b).split('%')[0])
