from telethon.sync import TelegramClient

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

client = TelegramClient('session_name', api_id, api_hash)

client.start()  # logs in as USER account

for dialog in client.iter_dialogs():
 try:
    print(dialog.name)
    print(f"Deleting: {dialog.name}")

    client.delete_dialog(
        dialog.id,
        revoke=True
    )

    print("Deleted ✅")
 except Exception as e:
    print(f"Failed: {e}")
