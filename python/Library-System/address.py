class Address():
    def __init__(self, city, state, country):
        self.__city = city
        self.__state = state
        self.__country = country

    @property
    def get_city(self):
        return self.__city
    
    @property
    def get_state(self):
        return self.__state

    @property
    def get_country(self):
        return self.__country
    