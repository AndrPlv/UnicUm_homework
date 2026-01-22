#include <iarduino_DHT.h>
#include <LiquidCrystal_I2C.h> // Библиотека для LCD


#define POMP 7 // пин для помпы
#define SYS 13 // сигнальнальный пин 
#define DHTPIN 2     // Пин, к которому подключен датчик
#define SIG_POMP 12


iarduino_DHT sensor(DHTPIN);
LiquidCrystal_I2C lcd(0x27, 16, 2); // Адрес 0x27, дисплей 16x2
bool water = 0;

void up(int t,int h, int t_need, int h_need) {
  lcd.clear();
  lcd.setCursor(0, 0); // Установка курсора в 0-ю колонку, 0-ю строку
  lcd.print("T:"); // Печать первой строки
  lcd.setCursor(0, 1); // Установка курсора во 2-ю строку
  lcd.print("H:"); // Печать второй строки

  lcd.setCursor(9, 0);
  lcd.print("T:");
  lcd.setCursor(9, 1);
  lcd.print("H:");

  lcd.setCursor(3, 0);
  lcd.print(t);
  lcd.setCursor(3, 1);
  lcd.print(h);   

  lcd.setCursor(6, 0);
  lcd.print("C");
  lcd.setCursor(6, 1);
  lcd.print("%");

  lcd.setCursor(12, 0);
  lcd.print(t_need);
  lcd.setCursor(12, 1);
  lcd.print(h_need);   

  lcd.setCursor(15, 0);
  lcd.print("C");
  lcd.setCursor(15, 1);
  lcd.print("%");       

  lcd.setCursor(7, 0);
  lcd.print("|"); 
  lcd.setCursor(7, 1); 
  lcd.print("|");
}

void setup() {
  lcd.init();        // Инициализация дисплея
  lcd.backlight();   // Включение подсветки
  up(0,0,0,0);
  pinMode(POMP, OUTPUT); // Пин для помпы
  pinMode(SIG_POMP, OUTPUT); // Пин для помпы  
  pinMode(SYS, OUTPUT); // Пин для помпы  
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
}

void loop() {
    if (sensor.read() == DHT_OK) {
         int t_need = map(analogRead(A0), 0, 1023, 0, 80);
         int h_need = map(analogRead(A1), 0, 1023, 0, 100);

         int t = sensor.tem;
         int h = sensor.hum;

         
         up(t,h,t_need,h_need);

         if (t >= t_need or h <= h_need) {
              water = true;
         }   
         else {
          water = false;
         }
    
    
        if (water) {
          digitalWrite(SIG_POMP, HIGH);
          delay(500);
          digitalWrite(SIG_POMP, LOW);
          digitalWrite(POMP, HIGH);     
        }
        if (not(water)) {
          digitalWrite(POMP, LOW);
          digitalWrite(SYS, HIGH);
          delay(500);
          digitalWrite(SYS, LOW);          
          }
        delay(500);
    }
}
