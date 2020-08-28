#!/usr/bin/env python3
import time
import asyncio
import sys

from telethon import TelegramClient, events, utils, Button

api_id = 1629605
api_hash = '6a71c14abfb7e99a89dfc9a1b772e869'
sesi_file = 'tanamguild'

hasil = '11'

bot = 'KampungMaifamX4Bot'   


with TelegramClient(sesi_file, api_id, api_hash) as client:
   client.loop.run_until_complete(client.send_message(bot, '11'))
    
@client.on(events.NewMessage(from_users=bot))

async def handler(event):
        pesan = event.raw_text


        if  '_Siram' in pesan: 
            await event.respond('1')
            print('tanam')
            return

        if '/kebun' in pesan:
            await event.respond('/KebunGuild_Siram')
            return

        if 'EXP+4710' in pesan:
            await event.respond('/siram')
            print('siram')
            return

        if 'EXP+1600' in pesan:
            time.sleep(152)
            await event.respond('/kebunGuild_AmbilPanen')
            return

        if 'Berhasil memanen dari guild' in pesan:
            await event.respond('/ambilPanen')
            print('panen')
            return

        if 'Kamu berhasil memanen' in pesan:
            await event.respond('/levelup')
            return

        if 'tidak mencukupi' in pesan:
            await event.respond(hasil)
            return

        if 'menjadi petani level' in pesan:
            print('naik level')
            time.sleep(1)
            await event.respond(hasil)
            return
        
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')