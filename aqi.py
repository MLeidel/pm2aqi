'''
aqi.py is a console program to calculate
AQI based on PM μg/m³ values

AQI = (AQI_high - AQI_low) * (Cp - BP_low) / (BP_high - BP_low) + AQI_low
 or
Ip =  [(Ihi-Ilow)/(BPhi-BPlow)] (Cp-BPlow)+Ilow

1. find the correct range based on PM (Cp) -> Given
2. Plug in the formula values to get AQI
'''

PMrange = {  # PM μg/m³ ranges
    "good": [0.0, 12.0],
    "moderate": [12.1, 35.4],
    "sensitive groups": [35.5, 55.4],
    "unhealthy": [55.5, 150.4],
    "very unhealthy": [150.5, 250.4],
    "hazerdous": [250.5, 500.0]
}

AQIcats = {  # AQI ranges
    "good": [0, 50],
    "moderate": [51, 100],
    "sensitive groups": [101, 150],
    "unhealthy": [151, 200],
    "very unhealthy": [201, 250],
    "hazerdous": [251, 300]
}

print("  Conversion of estimated PM2.5 to American AQI\n")
print("  (PM μg/m³)", "\t\tAQI")

for Cp in range(1, 330):
    # find the correct category using the given PM μg/m³ value Cp
    for cat, bounds in PMrange.items():
        if Cp < bounds[1]:
            c = cat  # category name
            break
    AQI = (AQIcats[c][1] - AQIcats[c][0]) * \
          (Cp - PMrange[c][0]) / (PMrange[c][1] - PMrange[c][0]) + AQIcats[c][0]

    print(f"  {Cp}", f"\t\t\t{AQI:.2f}", c)

print("\t. . .")
