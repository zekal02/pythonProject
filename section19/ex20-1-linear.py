'''

'''

 class LinearList():
     def __init__(self):
         self.linear = [] # 빈 리스트

    # 리스트에 데이터 추가
    def add_data(self, data):
        linear = self.linear
        linear.append(None)
        lLen = len(linear)
        linear[lLen - 1] = data

    def insert_data(self, position, data):
        linear = self.linear

# 실행코드
linear = LinearList()
linear.add_data(3)
linear.add_data(5)
linear.add_data(4)
linear.add_data(2)
linear.add_data(6)