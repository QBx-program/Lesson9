class TrafficLight:
    __color = [['красный', 7], ['желтый', 2], ['зеленый', 5]]

    def running(self):
        import time
        i = 0
        print(self.__color[i][0])
        while True:
            local_time = self.__color[i][1]
            if i == 2:
                i = 0
            else:
                i += 1
            time.sleep(local_time)
            print(self.__color[i][0])


a = TrafficLight()
a.running()
