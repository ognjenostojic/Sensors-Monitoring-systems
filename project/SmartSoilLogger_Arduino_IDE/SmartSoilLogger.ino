#include <Wire.h>
#include "RTClib.h"

RTC_DS3231 rtc;

const int sensorPin = A0;  // Soil moisture sensor connected to A0

void setup() {
  Serial.begin(9600);
  Wire.begin();

  // RTC Setup
  if (!rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);
  }

  // If RTC has lost power, set it to the date & time this sketch was compiled
  if (rtc.lostPower()) {
    Serial.println("RTC lost power, setting time!");
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  }

  Serial.println("Soil Moisture Logger Started");
}

void loop() {
  int moistureValue = analogRead(sensorPin);
  int moisturePercent = map(moistureValue, 1023, 300, 0, 100);  // Adjust based on your calibration
  moisturePercent = constrain(moisturePercent, 0, 100);         // Clamp to 0–100%

  DateTime now = rtc.now();

  Serial.print("[");
  Serial.print(now.year(), DEC);
  Serial.print("-");
  Serial.print(now.month(), DEC);
  Serial.print("-");
  Serial.print(now.day(), DEC);
  Serial.print(" ");
  Serial.print(now.hour(), DEC);
  Serial.print(":");
  Serial.print(now.minute(), DEC);
  Serial.print(":");
  Serial.print(now.second(), DEC);
  Serial.print("] ");

  Serial.print("Soil moisture: ");
  Serial.print(moisturePercent);
  Serial.println("%");

  delay(3000);  // Log every 3 seconds
}
