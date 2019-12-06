import re
str = ""




# regular expression

print(re.search(r"flag{[0-9a-zA-Z_]+}", "flag{1f65as1f461as6f1AJOI546__s1f}") )# <_sre.SRE_Match object; span=(12, 15), match='cat'>
print(re.search(r"flag{[0-9a-zA-Z_]+}", "flag{{}}") )# <_sre.SRE_Match object; span=(12, 15), match='cat'>
print(re.search(r"^flag{[0-9a-zA-Z_]*$}", "flag{1f65as1f461as6f1AJOI546__s1f}") )# <_sre.SRE_Match object; span=(12, 15), match='cat'>
print(re.search(r"flag{[0-9a-zA-Z_]+}", "flag{646df}a{s56{fsadf4646}494a{}sdf}") )
print(re.search(r"flag{[0-9a-zA-Z_{}]*}", "flag{{}}") )# <_sre.SRE_Match object; span=(12, 15), match='cat'>
print(re.search(r"^[A-Z]+[1-2]+[0-9]{8}","H123456289"))



