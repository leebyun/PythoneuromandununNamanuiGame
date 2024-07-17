def fire(kind, n):
    for i in range(0, n):
        if kind == 'machine_gun':
            print("기관총 발사!")
        elif kind == 'missile':
            print("미사일 발사!")
        elif kind == 'bomb':
            print("폭탄 발사!")
        else:
            print("무기 없음")

fire('machine_gun', 3)
fire('missile', 2)
fire('bomb', 1)