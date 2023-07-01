# pm2aqi

Console program to print out PM2.5 (μg/m³) to AQI values

The AQI values we're becoming familiar with in north-east and north central parts 
of America are actually based on various polutant factors that register on certain
sensing devices as PM μg/m³.

To determine the AQI rating based on the particulate matter some value of μg/m³, 
we need to convert the concentration into a range that corresponds to the 
Air Quality Index (AQI). The AQI scale is divided into six categories: 
Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy, and Hazardous.

However, it's important to note that the conversion from particulate matter concentration 
to AQI can vary depending on the specific country or region's air quality standards. 

The following conversion is based on the United States Environmental Protection Agency (EPA) standards for PM2.5:

AQI Conversion Formula:  
>
`AQI = (AQI_high - AQI_low) * (Cp - BP_low) / (BP_high - BP_low) + AQI_low`

Where:
- AQI is the Air Quality Index
- AQI_high and AQI_low are the upper and lower bounds of the AQI category
- Cp is the particulate matter concentration in μg/m³
- BP_low and BP_high are the upper and lower bounds of the particulate matter concentration 
in μg/m³ for the corresponding AQI category

For PM2.5, the following conversion table can be used:


|AQI Category | PM2.5 (μg/m³) Range|
| ---: | ---: |
|Good         | 0 - 12 |
|Moderate     | 12.1 - 35.4 |
|Unhealthy for Sensitive Groups | 35.5 - 55.4 |
|Unhealthy    | 55.5 - 150.4 |
|Very Unhealthy | 150.5 - 250.4 |
|Hazardous    | 250.5 - 500 |

Using the conversion formula and the PM2.5 range for each AQI category, 
we can determine the corresponding AQI rating for a particulate matter value of 2 μg/m³.

END