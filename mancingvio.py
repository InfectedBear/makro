#!/usr/bin/env python3
import time
import asyncio
import sys

from telethon import TelegramClient, events, utils

api_id = 1529569
api_hash = '4a079214fc8f272f6d82fa70b4fc983f'
sesi_file = 'VioMancing'


#mesej = 'Prisoner\'s Lake'
#mesej = 'Mimi River'
#mesej = 'Badabu River'
mesej = 'Danau Soprano'
#mesej = 'Bay of Bulari'
#mesej = 'Sungai Badabu'
#mesej = 'Laut Gabagaba'
#mesej = 'Ancient Sea'
#mesej = 'Haunted Sea'
#mese = 'Sungai Mimi'
#abis = 0

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('KampungMaifamBot', mesej))

    @client.on(events.NewMessage(from_users='KampungMaifamBot'))
    async def handler(event):
        #if 'the prisoners' in event.raw_text:
        #if 'Legend said' in event.raw_text:
        #if 'Only big fish' in event.raw_text:
        #if 'little sea creature' in event.raw_text:
        if 'Ikan langka' in event.raw_text:
        #if 'perempuan' in event.raw_text:
            mezo = await client.get_messages('KampungMaifamBot', ids=event.message.id)
            time.sleep(2)
#            await mezo.click(text='Pull The Net')
            await mezo.click(text='Tarik Jala')
            print(event.message.id)
            return

        if 'Kamu berhasil' in event.raw_text:
            time.sleep(3)
            await event.respond(mesej)
            print(event.message.id)
            return

        if 'Kamu tidak memiliki cukup' in event.raw_text:
           await event.respond("/restore")
           time.sleep(3)
           #await client.disconnect() 
           return

#        if 'No no no' in event.raw_text:
#           await event.respond("/restore") 
           #await client.disconnect() 
#           return

        if "Yummy" or "Energi berhasil" in event.raw_text:
           await event.respond(mesej) 
           #await client.disconnect() 
           return

#        if 'not fishing' in event.raw_text:
#           time.sleep(1)
#           await event.respond(mesej) 
#           return
#           abis += 1
    
#    client.run_until_disconnected()

    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Berhenti')
    
#if abis == 2 :
#    client.disconnect()
#    clien.disconnect()
