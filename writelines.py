file=open('sreelekha.txt','a')
l1='I have completed graduation in acharya nagarjuna university\n'
l2='I was completed my intermediate in balaji college\n'
l3='Thank you'
# file.writelines([l1,l2,l3])
a=[l1,l2,l3]
file.writelines(a[1:])
