a = '0123456789'
if (not (a[::] == a)): raise Exception('Slice bug')
if (not (a[::2] == '02468')): raise Exception('Slice bug')
if (not (a[1::2] == '13579')): raise Exception('Slice bug')
if (not (a[::-1] =='9876543210')): raise Exception('Slice bug')
if (not (a[::-2] == '97531')): raise Exception('Slice bug')
if (not (a[3::-2] == '31')): raise Exception('Slice bug')
if (not (a[-100:100:] == a)): raise Exception('Slice bug')
if (not (a[100:-100:-1] == a[::-1])): raise Exception('Slice bug')
if (not (a[-100:100:2] == '02468')): raise Exception('Slice bug')
