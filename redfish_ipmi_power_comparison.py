import csv
import time
from datetime import datetime
from pyghmi.ipmi import command
from pyghmi.redfish.command import Command

csv_filename = "bmc_power_data.csv"

# Replace with your BMC IP, username, and password
bmc_ip = ''
username = ''
password = ''


with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Timestamp", "Power Redfish PowerWatts (W)", "Power Redfish PowerConsummedWatts (W)", "Power IPMI DCMI (W)", "Power IPIMI Sensor (W)"])

    # IPMI
    ipmi_cmd = command.Command(bmc=bmc_ip, userid=username, password=password)

    try:
        while True:
            # REDFISH EnvironmentMetrics PowerWatts
            client = Command(bmc=bmc_ip, userid=username, password=password, verifycallback=lambda x: True)

            try:
                redfish_power = client.get_system_power_watts()
                print("Power Redfish:", redfish_power)
            except Exception as e:
                print("Error retrieving power data:", e)

            # REDFISH Chassis Power PowerConsumedWatts
            try:
                power_data = client.wc.grab_json_response('/redfish/v1/Chassis/System.Embedded.1/Power')

                power_control = power_data.get("PowerControl", [])
                if power_control:
                    redfish_power_consumed = power_control[0].get("PowerConsumedWatts", None)
                    if redfish_power_consumed is not None:
                        print("PowerConsumedWatts:", redfish_power_consumed)
                    else:
                        print("PowerConsumedWatts not found in the response.")
                else:
                    print("No PowerControl data found in the response.")

            except Exception as e:
                print("Error retrieving power data:", e)

            ## IPMI DCMI
            try:
                dcmi_power = ipmi_cmd.get_system_power_watts()
                print("Power DCMI:", dcmi_power)
            except Exception as e:
                print("Error retrieving Power:", e)

            ## IPMI Sensor
            try:
                sensor = ipmi_cmd.get_sensor_reading("Pwr Consumption")
                print(f"{sensor.name}: {sensor.value} {sensor.units}")
                #print(f"Imprecision: {sensor.imprecision}")
            except Exception as e:
                print("Error retrieving sensor data:", e)

            # CSV
            writer.writerow([datetime.now(), redfish_power, redfish_power_consumed, dcmi_power, sensor.value])
            time.sleep(1)
            print("########")

    except KeyboardInterrupt:
        print("\nLogging stopped.")
