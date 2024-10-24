import random



class Car:
    def __init__(self, registration_number, max_speed, current_speed, travelled_distance):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def display_info(self):
        return f"{self.registration_number:<10}{self.max_speed:<15}{self.current_speed:<15}{self.travelled_distance:<20}"

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance


def main():
    car = Car("ABC-123", 142, 0, 0)
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print(f'the current speed is {car.current_speed} km/h.')

    car.accelerate(-200)
    print(f'the current speed is {car.current_speed} km/h.')

    car_2 = Car("ABC-123", 142, 60, 2000)
    car_2.drive(1.5)
    print(f'the travelled distance is {car_2.travelled_distance} km.')

    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        car = Car(f"ABC-{i}", max_speed, 0, 0)
        cars.append(car)

    race_over = False
    hours = 0

    while not race_over:
        hours += 1

        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

            if car.travelled_distance >= 10000:
                race_over = True

    print(f"{'Car':<10}{'Max Speed (km/h)':<15}{'Current Speed (km/h)':<20}{'Travelled Distance (km)':<25}")
    print("=" * 70)
    for car in cars:
        print(car.display_info())


if __name__ == "__main__":
    main()
