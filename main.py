from qipan import QiPan
qipan = QiPan

qipan.__init__(qipan)    # 打印出棋盘

#qipan.__moveR__(qipan,2,0,1,1)
#qipan.__show__(qipan)
qipan.__show__(qipan)
while True:
    print('You are use R key, show you move: AABB, like: 20(positon) -> 11(position) @exit to close')
    N = input()
    if N == 'exit':
        break
    print('R ' + N[:2] + ' Move -> ' + N[2:])
    #print(N[0])
    qipan.__moveR__(qipan,int(N[0]),int(N[1]),int(N[2]),int(N[3]))
    qipan.__show__(qipan)
    # 让计算机自己控制’N‘
    print('走N')
    qipan.__shaomiao__(qipan)
    qipan.__show__(qipan)



