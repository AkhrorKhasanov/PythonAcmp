s1 = input()
s2 = input()
s3 = input()
if s1 == 'XXX' or s2 == 'XXX' or s3 == 'XXX':
    print('Win')
elif s1[0] + s2[0] + s3[0] == 'XXX':
    print('Win')
elif s1[1] + s2[1] + s3[1] == 'XXX':
    print('Win')
elif s1[2] + s2[2] + s3[2] == 'XXX':
    print('Win')
elif s1[0] + s2[1] + s3[2] == 'XXX':
    print('Win')
elif s1[2] + s2[1] + s3[0] == 'XXX':
    print('Win')
elif (s1 + s2 + s3).find('.') == -1:
    print('Draw')
else:
    print('Lose')