class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """Always calculate cost using the formula, no guard needed."""
        price = (car.comfort_class *
                 (self.clean_power - car.clean_mark) *
                 self.average_rating /
                 self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        """Wash a single car if clean_power > clean_mark, update mark, return cost."""
        if car.clean_mark < self.clean_power:
            cost = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return cost
        return 0.0
