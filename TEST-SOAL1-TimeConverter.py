import datetime                    # Mengimport atau memasukkan module datetime, module ini akan digunakan untuk mengubah hours, minutes, dan second ke dalam format time

def timeConverter(seconds):                 # Membuat suatu function dengan nama timeConverter dengan parameter seconds    
    if not type(seconds) == int :           # Jika type dari seconds bukan integer maka akan memunculkan ValueError = 'Invalid Input!'
        raise ValueError('Invalid Input!')
        
    if seconds <= 359999:               # jika seconds kurang dari 359999
        hours = (seconds) // (60*60)    # hours sama dengan seconds di-floor division dengan 60*60 (3600)
        seconds %= (60*60)              # kemudian seconds akan didefinisikan ulang dengan modulo 60*60 sehingga menghasilkan nilai sisa second
        minutes = seconds // 60         # minutes sama dengan nilai sisa seconds di-floor division dengan 60
        seconds %= 60                   # seconds sama dengan niali sisa seconds di-modulo dengan 60
        conversion = datetime.time(hours, minutes, seconds) # mengubah hours, minutes, seconds ke dalam format time

    else:                                   # lainnya:
        raise ValueError('Invalid Input!')  # apabila input lebih dari 359999 maka akan mengeluarkan 'Invalid Input!'

    return (f'Konversi : {conversion}')                       # Return conversion

print(timeConverter(3700))