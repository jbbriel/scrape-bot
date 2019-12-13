class popularCities:

    def inUS(self, numOfPlaces=None):
        arry = []
        i = 0
        with open('popularCities.txt', 'r') as file:
            for line in file:
                place = line.split(',')
                city = place[1]
                state = place[2]
                arry.append(str(city) + ', ' + str(state))
                i += 1
                if numOfPlaces == i:
                    break
            file.close()
        return arry

# output = popularCities().inUS()
# print zip(output)