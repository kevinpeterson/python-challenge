"""
Exercise 1: Shifting array indexes to produce a decoded message.
"""

alpha = "abcdefghijklmnopqrstuvwxyz"

message = list('''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr 
amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr 
ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() 
gq pcamkkclbcb. lmu ynnjw ml rfc spj. 
''')

url = list('map')

def getRealIdx( idx ):
    if( idx < len(alpha) ):
        return idx
    else:
        return idx - len(alpha)
    
def translate( phrase ):
    for i in range( len( phrase ) ):
        char = phrase[i]
        if( alpha.find( char ) != -1):
            idx = alpha.index( char ) + 2
            phrase[i] = alpha[ getRealIdx( idx ) ]

translate( message )
translate( url )

print "".join( message )
print "".join( url )

