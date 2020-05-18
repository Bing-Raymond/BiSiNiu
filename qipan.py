#Bing.L want made a game for little man.
from grid import Grid
#print()
#print('0  N-----------N    ')
#print('   |\         /     ')
#print('   |  \     /       ')
#print('   |    \ /         ')
#print('1  |     X    (  )  ')
#print('   |    / \         ')
#print('   |  /     \       ')
#print('   |/         \     ')
#print('2  R-----------R    ')
#print('                    ')
#print('   0     1     2    ')
#print('====================')
# 初始化棋盘
class QiPan(object):
    def __init__(self):
        self._data = Grid(3,3,'-')
        self._data.__setpos__(0,0,'N')
        self._data.__setpos__(0,2,'N')
        self._data.__setpos__(1,0,'|')
        self._data.__setpos__(1,1,'x')
        self._data.__setpos__(1,2,'#')
        self._data.__setpos__(2,0,'R')
        self._data.__setpos__(2,2,'R')
    # 从 1 -> 2
    def __moveR__(self,row_1,column_1,row_2,column_2):
        if self._data.__getpos__(row_1,column_1) != 'R' :
            print('只能挪动 R 棋子，请重新选择。')
            return
        else:
            self._data.__remove__(row_1,column_1)
            self._data.__setpos__(row_2,column_2,'R')
    # 计算机自己走 N
    def __moveN__(self):
        print(self.__shaomiao__(self))
    
    def __show__(self):
        print('  0 1 2')
        #print()
        print(self._data)
        #print('0 1 2')
    
    def __shaomiao__(self):
        self._data.__shaomiao__()


        