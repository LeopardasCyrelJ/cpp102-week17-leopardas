# THERMOGUARD: Smart Environmental Monitoring and Early-Warning System
# Python version

def is_whole_number(text):
    if text == "":
        return False
    for character in text:
        if character < "0" or character > "9":
            return False
    return True


def get_number(prompt, minimum, maximum):
    while True:
        text = input(prompt)
        if is_whole_number(text):
            number = int(text)
            if minimum <= number <= maximum:
                return number
        print(f"Invalid input. Enter a whole number from {minimum} to {maximum}.")


def enter_initial_readings():
    readings = []
    amount = get_number("How many devices will be monitored? ", 1, 1000)

    for index in range(amount):
        reading = get_number(
            f"Enter temperature for Device TG-{index + 1:03}: ", 0, 100
        )
        readings.append(reading)

    return readings


def classify_temperature(temperature):
    if temperature < 30:
        return "NORMAL"
    elif temperature <= 35:
        return "WARNING"
    return "CRITICAL"


def display_banner():
    print("=" * 54)
    print("             THERMOGUARD SYSTEM")
    print("     Smart Environmental Monitoring & Alerts")
    print("=" * 54)


def display_menu():
    print("\n---------------- CONTROL PANEL ----------------")
    print("[1] View Device Dashboard")
    print("[2] Register New Reading")
    print("[3] Run Diagnostic Scan")
    print("[4] Generate Engineering Report")
    print("[5] Shut Down System")


def view_dashboard(readings):
    print("\n================ DEVICE DASHBOARD ================")
    if len(readings) == 0:
        print("No devices have been registered.")
        return

    for index in range(len(readings)):
        temperature = readings[index]
        status = classify_temperature(temperature)
        print(
            f"TG-{index + 1:03} | {temperature:>3} °C | "
            f"{status}"
        )


def add_reading(readings):
    device_number = len(readings) + 1
    temperature = get_number(
        f"Enter temperature for new device TG-{device_number:03}: ",
        0, 100
    )
    readings.append(temperature)
    print(f"Reading stored for TG-{device_number:03}.")


def count_status(readings, target_status):
    count = 0
    for temperature in readings:
        if classify_temperature(temperature) == target_status:
            count += 1
    return count


def calculate_total(readings):
    total = 0
    for temperature in readings:
        total += temperature
    return total


def calculate_average(readings):
    if len(readings) == 0:
        return 0.0
    return calculate_total(readings) / len(readings)


def find_extreme(readings, find_highest):
    extreme = readings[0]
    for temperature in readings:
        if find_highest and temperature > extreme:
            extreme = temperature
        elif not find_highest and temperature < extreme:
            extreme = temperature
    return extreme


def run_diagnostic_scan(readings):
    print("\n================ DIAGNOSTIC SCAN ================")
    normal = count_status(readings, "NORMAL")
    warning = count_status(readings, "WARNING")
    critical = count_status(readings, "CRITICAL")

    if len(readings) == 0:
        print("SCAN RESULT: No readings available.")
        return

    print(f"Devices scanned : {len(readings)}")
    print(f"NORMAL          : {normal}")
    print(f"WARNING         : {warning}")
    print(f"CRITICAL        : {critical}")

    if critical > 0:
        print("SYSTEM ALERT: CRITICAL TEMPERATURE DETECTED.")
        for index in range(len(readings)):
            if classify_temperature(readings[index]) == "CRITICAL":
                print(
                    f"  -> Inspect TG-{index + 1:03}: "
                    f"{readings[index]} °C"
                )
    elif warning > 0:
        print("SYSTEM NOTICE: WARNING RANGE DETECTED.")
        print("Recommendation: Continue monitoring affected devices.")
    else:
        print("SYSTEM CLEAR: All monitored devices are normal.")


def overall_status(warning, critical):
    if critical > 0:
        return "RED ALERT - ATTENTION REQUIRED"
    elif warning > 0:
        return "YELLOW NOTICE - MONITOR"
    return "GREEN STATUS - NORMAL"


def generate_report(readings):
    if len(readings) == 0:
        print("No readings available for the report.")
        return

    normal = count_status(readings, "NORMAL")
    warning = count_status(readings, "WARNING")
    critical = count_status(readings, "CRITICAL")
    total = calculate_total(readings)
    amount = len(readings)

    print("\n=============== ENGINEERING REPORT ===============")
    print(f"Registered devices : {amount}")
    print(f"Combined readings  : {total} °C")
    print(f"Average temperature: {calculate_average(readings):.2f} °C")
    print(f"Lowest temperature : {find_extreme(readings, False)} °C")
    print(f"Highest temperature: {find_extreme(readings, True)} °C")

    print("\nSTATUS DISTRIBUTION")
    print(f"NORMAL   : {normal} ({normal / amount * 100:.1f}%)")
    print(f"WARNING  : {warning} ({warning / amount * 100:.1f}%)")
    print(f"CRITICAL : {critical} ({critical / amount * 100:.1f}%)")

    print("\nFINAL SYSTEM ASSESSMENT")
    print(overall_status(warning, critical))


def main():
    display_banner()
    readings = enter_initial_readings()

    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == "1":
            view_dashboard(readings)
        elif choice == "2":
            add_reading(readings)
        elif choice == "3":
            run_diagnostic_scan(readings)
        elif choice == "4":
            generate_report(readings)
        elif choice == "5":
            print("\nTHERMOGUARD shutting down. Stay safe!")
            break
        else:
            print("Invalid selection. Choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
