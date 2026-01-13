# Basic approach - reading entire file
with open('wheater.txt', 'r') as file:
    content = file.read()
    # Split by semicolon across entire file
    items = content.split(';')
    print(f"Total items: {len(items)}")
    for i, item in enumerate(items):
        print(f"{i}: {item.strip()}")
