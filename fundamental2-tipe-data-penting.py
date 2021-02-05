# tipe data list
anak = ['aka','azy','agy','aga']
print(anak)

anak.append('axa')
print(anak)

print('')
print('sapa anak ke-2')
print(f'hai {anak[1]}')

print('')
print('sapa semua anak')
print(f'hai {anak}')

print('')
print('sapa semua anak dengan looping')
for anak_aink in anak:
    print(f'hai {anak_aink}')

print('\nsapa semua anak cara ke-2')
for a in range(0, len(anak)):
    print(f'{a+1}. hai {anak[a]}!')