import secrets

for i in range(1, 6):
    sid = secrets.token_hex(16)
    print(f"ID {i}: {sid} | Length: {len(sid)} | Charset: hex (0-9, a-f)")
