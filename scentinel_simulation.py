import random
import time

print("=" * 55)
print("              SCENTINEL AI")
print("          DIGITAL NOSE SIMULATOR")
print("=" * 55)

print("\nInitializing virtual sensors...")
time.sleep(1)

print("MQ-2 Sensor       : READY")
print("MQ-135 Sensor     : READY")
print("BME680 VOC Sensor : READY")
print("Temperature       : READY")
print("Humidity          : READY")

print("\nScentinel is ready to detect odours!")

print("\nSelect an odour/environment to simulate:")
print("1. Normal Air")
print("2. Smoke")
print("3. Gas Leak")
print("4. Spoiled Food")
print("5. Coffee")
print("6. Flower")

choice = input("\nEnter your choice (1-6): ")

# Simulated sensor values
if choice == "1":
    odour = "Normal Air"
    mq2 = random.randint(80, 150)
    mq135 = random.randint(100, 180)
    voc = random.randint(50, 120)
    temperature = random.randint(24, 28)
    humidity = random.randint(40, 60)

elif choice == "2":
    odour = "Smoke"
    mq2 = random.randint(700, 950)
    mq135 = random.randint(500, 800)
    voc = random.randint(400, 700)
    temperature = random.randint(30, 40)
    humidity = random.randint(30, 50)

elif choice == "3":
    odour = "Gas Leak"
    mq2 = random.randint(600, 900)
    mq135 = random.randint(500, 850)
    voc = random.randint(350, 650)
    temperature = random.randint(25, 35)
    humidity = random.randint(35, 55)

elif choice == "4":
    odour = "Spoiled Food"
    mq2 = random.randint(250, 450)
    mq135 = random.randint(500, 750)
    voc = random.randint(450, 800)
    temperature = random.randint(25, 32)
    humidity = random.randint(55, 80)

elif choice == "5":
    odour = "Coffee"
    mq2 = random.randint(150, 300)
    mq135 = random.randint(250, 450)
    voc = random.randint(250, 500)
    temperature = random.randint(24, 30)
    humidity = random.randint(40, 65)

elif choice == "6":
    odour = "Flower"
    mq2 = random.randint(100, 220)
    mq135 = random.randint(200, 400)
    voc = random.randint(180, 350)
    temperature = random.randint(23, 29)
    humidity = random.randint(45, 70)

else:
    print("\nInvalid choice!")
    exit()

print("\n" + "-" * 55)
print("           SIMULATED SENSOR READINGS")
print("-" * 55)

print(f"MQ-2 Gas/Smoke     : {mq2}")
print(f"MQ-135 Air Quality : {mq135}")
print(f"BME680 VOC         : {voc}")
print(f"Temperature        : {temperature} °C")
print(f"Humidity           : {humidity} %")

print("\nAnalyzing sensor pattern...")
time.sleep(2)

print("\n" + "=" * 55)
print("              SCENT DETECTED")
print("=" * 55)

print(f"Detected condition : {odour}")

if odour == "Normal Air":
    print("Status              : SAFE")
    print("Voice Alert         : No abnormal odour detected.")

elif odour == "Smoke":
    print("Status              : DANGER")
    print("Voice Alert         : Warning! Smoke detected.")

elif odour == "Gas Leak":
    print("Status              : CRITICAL")
    print("Voice Alert         : Warning! Possible gas leak detected.")

elif odour == "Spoiled Food":
    print("Status              : WARNING")
    print("Voice Alert         : Spoiled food odour detected.")

elif odour == "Coffee":
    print("Status              : IDENTIFIED")
    print("Voice Alert         : Coffee-like odour detected.")

elif odour == "Flower":
    print("Status              : IDENTIFIED")
    print("Voice Alert         : Flower-like odour detected.")

print("=" * 55)
print("Scentinel analysis completed.")