from arrays import Array

class Grid(object):
    def __init__(self, rows, columns, fill_value=None):
        self._pos = [(0,0),(0,2),(1,1),(2,0),(2,2)]
        self._nullpos = (1,1)
        self._npos = (0,0)
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fill_value)

    def get_height(self):
        return len(self._data)

    def get_width(self):
        return len(self._data[0])
    # 拿到一整行的值。
    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            result +=  str(row) + " "
            for col in range(self.get_width()):
                result += str(self._data[row][col]) +" "
            result += "\n"
        return result
    # 计算点之间的距离。
    def __distance__(self,npoint,nullpos):
        if npoint == (0,2) and nullpos == (2,2):
            return 4
        if npoint == (2,2) and nullpos == (0,2):
            return 4
        else:
            return abs(npoint[0]-nullpos[0]) + abs(npoint[1] - nullpos[1])

    # 拿到某个点的值。
    def __getpos__(self,row,column):
        #result ``= ""
        return self._data[row][column]
    # 给某个点赋值。
    def __setpos__(self,row,column,fill_value ='x' ):
        self._data[row].__setitem__(column,fill_value)
    def __remove__(self,row,column):
        self._data[row].__setitem__(column,'-')

    # 新版本扫描棋盘，看看可以落子。
    def __shaomiao__(self):  
        for point in self._pos:
            if self.__getpos__(point[0],point[1]) != 'N' and self.__getpos__(point[0],point[1]) != 'R' :
                print('move N to: ' + str(point))
                #if self.__distance__(point)
                self._nullpos = point #self.__setpos__(point[0],point[1],'N')
                #print(self._nullpos)
        for npoint in self._pos:
            if self.__getpos__(npoint[0],npoint[1]) == 'N' : 
                #if self.__distance__(npoint,self._nullpos) < 3 :
                    print('from: ' + str(npoint))
                    self._npos = npoint
                    break
                # else:
                #     print('No more move, YOU WIN!!!')
                    #return
        self.__check__()

    def __check__(self):
        if self.__distance__(self._npos,self._nullpos) < 3:
            self.__removeN__(self._npos,self._nullpos)
        else:
            print('can move this step. lost?')


                #return (point)# point[0]

    def __removeN__(self,npoint,nullpos):
        self.__remove__(npoint[0],npoint[1])
        self.__setpos__(nullpos[0],nullpos[1],'N')
        print('Hello world')

