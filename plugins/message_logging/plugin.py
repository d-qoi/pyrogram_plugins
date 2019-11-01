import logging
from pyrogram import Client, MessageHandler, Filters

log = logging.getLogger("plugins.logging")

@Client.on_raw_update(group=-999)
def raw(client, update, users, chats):
    log.debug("Update: " + str(update))
    log.debug("Users:  " + str(users))
    log.debug("Chats:  " + str(chats))
