import logging

from pyrogram import Client

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Client("CustClient", config_file="config.ini")
app.run()
