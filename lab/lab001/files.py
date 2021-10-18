with open('data/pan-tadeusz.txt', encoding = 'utf8') as f:
    #f.read()
    for line in f:
        print(line.strip().split())
