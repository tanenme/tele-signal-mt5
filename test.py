from telethon.sync import TelegramClient, events
import MetaTrader5 as mt5

api_id = "17612509"
api_hash = "5d987f53b6ef5df97f05388828ba3f09"

# Inisialisasi Telegram Client
client =  TelegramClient('test', api_id, api_hash)

def mt5Order():
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()
 
    # display data on MetaTrader 5 version
    print(mt5.version())
    # connect to the trade account without specifying a password and a server
    account=17221085
    authorized=mt5.login(account)  # the terminal database password is applied if connection data is set to be remembered
    if authorized:
        print("connected to account #{}".format(account))
    else:
        print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
    
    # now connect to another trading account specifying the password
    account=25115284
    authorized=mt5.login(account, password="gqrtz0lbdm")
    if authorized:
        # display trading account data 'as is'
        print(mt5.account_info())
        # display trading account data in the form of a list
        print("Show account_info()._asdict():")
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))
    else:
        print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
    
    # shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()

# Mendefinisikan event handler untuk menangani pesan baru
@client.on(events.NewMessage(chats=['Soodtest']))  # Ganti dengan nama grup yang ingin Anda monitor
async def handle_new_message(event):
    data = {
        #"group": event.chat.title,
        #"sender": event.sender_id,
        "text": event.message.text,
        #"date": event.message.date
    }
    print(data)
    mt5Order()
    # Di sini Anda bisa menambahkan kode untuk menangani pesan baru, misalnya menyimpannya ke database

# Mulai menjalankan client
with client:
    # Perintah ini akan menjalankan client dan menunggu hingga terjadi peristiwa
    client.run_until_disconnected()
