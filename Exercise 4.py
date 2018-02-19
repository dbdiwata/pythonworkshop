DNA=open("DNA.txt").read()
length=len(DNA)
sumc=0
sumg=0
for x in range(0,length):
    if DNA[x]=='G':
        letterG=len(DNA[x])
        sumg=sumg+letterG
    elif DNA[x]=='C':
        letterC=len(DNA[x])
        sumc=sumc+letterC

percent=((sumg+sumc)/18.0)*100
print "The percent of C and G is",percent, "%"

