import json


def main(file_name: str):
    with open(f"data/{file_name}") as json_file:
        input = json.load(json_file)

    r = input["r"]
    days = input["days"]

    # print(input)

    max_day = 0
    max_hour = 0
    max_employees = 0

    hour_counts = {day_number: [0] * r for day_number in range(1, r)}

    for day in days:
        day_number = day["day"]
        shifts = day["shifts"]

        for shift in shifts:
            start, end = map(int, shift.split("-"))
            if end < start:
                duration = (r - start) + end
            else:
                duration = end - start

            if start == end or duration > r:
                continue

            if end < start:
                for i in range(start, r):
                    hour_counts[day_number][i] += 1
                for i in range(0, end):
                    hour_counts[day_number + 1][i] += 1
            else:
                for i in range(start, end):
                    hour_counts[day_number][i] += 1

    # Find max hour with the most employees
    for day, hours in hour_counts.items():
        for hour, employees in enumerate(hours):
            if employees > max_employees:
                max_day = day
                max_hour = hour
                max_employees = employees

    print(f"Day {max_day} at hour {max_hour} has {max_employees} employees")


if __name__ == "__main__":
    for i in range(1, 8):
        print(f"Running instance {i}")
        main(f"instance{i}.json")
