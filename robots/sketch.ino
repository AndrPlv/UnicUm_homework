// Ширина базы 18
// формула pBa/360
#define H1 4
#define S1 5
#define S2 6
#define H2 7

#define pinA 2
#define pinB 3

const int trigPin = 12;
const int echoPin = 11;

int EncoderA = 0;
int EncoderB = 0;

int porog = 300;
int speed = 90;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for (int j = 4;j<=7;j++) {
    pinMode(j, OUTPUT);
  }
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(pinA, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(pinA), readEncoderA, CHANGE);
  attachInterrupt(digitalPinToInterrupt(pinB), readEncoderB, CHANGE);  
}

void loop() {
  // // put your main code here, to run repeatedly:
  // int line0 = analogRead(A0);
  // int line1 = analogRead(A1);
  // int distan = S();

  // Serial.print(line0);
  // Serial.print(' ');
  // Serial.println(line1);

  // if (line0 > porog and line1 > porog) {
  //   forward();
  // } 
  // else if (line0 > porog and line1 < porog) {
  //   left();
  // } 
  // else if (line0 < porog and line1 > porog) {
  //   right();
  // }   
  // else if (line0 < porog and line1 < porog){
  //   stops();    
  // }
  Serial.println(Encoder);
}
void forward() {
  digitalWrite(H1, LOW);
  digitalWrite(H2, LOW);

  analogWrite(S1, speed);
  analogWrite(S2, speed);  
}
void undo() {
  digitalWrite(H1, LOW);
  digitalWrite(H2, LOW);

  analogWrite(S1, speed);
  analogWrite(S2, speed);  
}
void left() {
  digitalWrite(H1, HIGH);
  digitalWrite(H2, LOW);

  analogWrite(S1, speed);
  analogWrite(S2, speed);  
}
void right() {
  digitalWrite(H1, LOW);
  digitalWrite(H2, HIGH);

  analogWrite(S1, speed);
  analogWrite(S2, speed);  
}
void stops() {
  digitalWrite(H1, HIGH);
  digitalWrite(H2, HIGH);

  analogWrite(S1, 0);
  analogWrite(S2, 0);  
}

float S() {
  long duration;

  // Очищаем пин Trig
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Подаем импульс High длительностью 10 мкс
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Считываем время возврата эха на пине Echo
  duration = pulseIn(echoPin, HIGH);

  // Вычисляем расстояние в сантиметрах
  return duration * 0.034 / 2; // или duration / 5
}
void readEncoderA() {
  EncoderA ++;
}
void readEncoderB() {
  EncoderA ++;
}
