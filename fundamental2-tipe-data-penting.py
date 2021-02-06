# tipe data list
anak = ['aka', 'azy', 'agy', 'aga']
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
    print(f'{a + 1}. hai {anak[a]}!')

"""
tipe data dict menggunakan kvp ( Key Value Pair)
"""

kamus = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print('\nmenampilkan tipe data dict')
print(kamus);

print('\nmenampilkan ayah')
print(kamus['ayah'])

print('\ncontoh dari server Gojek dengan tipe data dict')
data_dari_server_gojek = {
    'tanggal': '2021-02-06',
    'driver_list': [
        {'nama': 'aka', 'jarak': 10},
        {'nama': 'azy', 'jarak': 20},
        {'nama': 'agy', 'jarak': 30},
        {'nama': 'aga', 'jarak': 40},
        {'nama': 'axa', 'jarak': 50}
    ]
}

print('driver Gojek')
print(f"tanggal : {data_dari_server_gojek['tanggal']}")
print(f"driver : {data_dari_server_gojek['driver_list']}")
print(f"driver ke #1 : {data_dari_server_gojek['driver_list'][0]}")
print(f"driver ke #3 : {data_dari_server_gojek['driver_list'][2]}")
print('\nJarak Driver 3')
print(f"jaraknya : {data_dari_server_gojek['driver_list'][2]['jarak']}")