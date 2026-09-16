message = input("message: ").strip()
print(len(message))
print(f"first: {message[:1]}")
print(f"last: {message[:-1]}")
print(f"first 3: {message[:1]}")
print(f"last 3: {message[:-1]}")
print(f"every second character: {message[::2]}") 
print(f"revered: {message[::-1]}")



