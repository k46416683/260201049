zaman='23.49'
times='40'
zamanlar=zaman.split('.')
dakika=(int(zaman[:-2])+int(times))%60
saat=(int(zaman[:2])+(int(zaman[:-2])+int(times))//60)%24
yeni_zaman=str(saat)+'.'+str(dakika)
print(yeni_zaman)