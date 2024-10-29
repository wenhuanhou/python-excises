###123###
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Floor {target_floor} is out of bounds.")
            return

        print(f"Moving to floor {target_floor} from floor {self.current_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Going up: Now on floor {self.current_floor}")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Going down: Now on floor {self.current_floor}")
        else:
            print("Already at the bottom floor.")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destination_floor):
        if 0 <= elevator_num < len(self.elevators):
            print(f"\nRunning elevator {elevator_num} to floor {destination_floor}")
            self.elevators[elevator_num].go_to_floor(destination_floor)
        else:
            print(f"Elevator {elevator_num} does not exist in this building.")

    def fire_alarm(self):
        print("\nFire alarm activated! Moving all elevators to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"\nElevator {i} returning to the bottom floor:")
            elevator.go_to_floor(self.bottom_floor)


# Testing the Building and Elevator classes with fire alarm functionality
if __name__ == "__main__":

    building = Building(0, 10, 3)

    building.run_elevator(0, 5)
    building.run_elevator(1, 8)
    building.run_elevator(2, 10)

    building.fire_alarm()

###4###
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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'Car':<10}{'Max Speed (km/h)':<15}{'Current Speed (km/h)':<15}{'Travelled Distance (km)':<20}")
        print("=" * 70)
        for car in self.cars:
            print(car.display_info())
        print("\n")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


def main():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        car = Car(f"ABC-{i}", max_speed, 0, 0)
        cars.append(car)

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        hours += 1
        race.hour_passes()

        if hours % 10 == 0:
            print(f"Hour {hours}")
            race.print_status()

    print("Race finished!")
    print(f"The race lasted for {hours} hours.")
    race.print_status()


if __name__ == "__main__":
    main()
