#!/usr/bin/env python3
import time
import asyncio
import sys
import random
import re

from telethon import TelegramClient, events, utils, Button

api_id = 1629605
api_hash = '6a71c14abfb7e99a89dfc9a1b772e869'
sesi_file = 'malinguang'

hasil = '/rumah_curiUang'



bot = 'KampungMaifamX4Bot'   


with TelegramClient(sesi_file, api_id, api_hash) as client:
   client.loop.run_until_complete(client.send_message(bot, '/rumah_curiUang'))
    
@client.on(events.NewMessage(from_users=bot))
async def handler(event):
        pesan = event.raw_text

        file = open("malinguang.txt","a+")
        if  'Rumah Warga' in pesan: 
            print('kunjungi rumah warga')
            time.sleep(2)
            #await event.respond('masuk')

            hasil = pesan.split(' ')
            
            print(hasil)
            count = 0
            
            for i in range(3,32,3):
                await event.respond(hasil[i])
                print('kirim')
                file.write(hasil[i]+'\n')
                print('maling alamat ke-'+str(i))  
                count+= 1
                #number+=4
            
                if count%10==0:
                    time.sleep(3)
                    await event.respond('/makan_KudapanSuci_1')
                    print('hapus buronan')
                time.sleep(3)
            await event.respond('/rumah_curiUang')
            file.close()
            return

        if 'Kamu terkurung dalam penjara menjijikkan' in pesan:
            print('kena polisi')
            time.sleep(60)
            await event.respond('/release')
            print('nyogok polisi')
            time.sleep(5)
            await event.respond('/rumah_curiUang')
            return

        if 'Kamu tidak memiliki cukup' in event.raw_text:
           await event.respond("/makan_RujakKeramat_1")
           time.sleep(3)
           #await client.disconnect() 
           return

        if 'Tidak tidak' in event.raw_text:
           await event.respond("/restore")
           time.sleep(3)
           #await client.disconnect() 
           return


        if "Yummy" or "Energi berhasil" in event.raw_text:
           await event.respond(hasil) 
           #await client.disconnect() 
           return

        
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')

       
