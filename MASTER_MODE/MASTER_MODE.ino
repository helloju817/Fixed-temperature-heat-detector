  // 아두이노 보드의 핀 모드를 설정합니다.
const int temperature = A0;
const int Rled = 10;//빨간색 LED를 10번핀에 연결합니다. 
const int Gled = 9;//녹색 LED를 9번핀에 연결합니다.
const int buzzerPin = 13; //부저를 13번 핀에 연결합니다. 
int PIR = 12;   // 인체감지센서를 12번 핀에 연결합니다.
int BLED = 8;    // LED를 8번 핀에 연결합니다.



void setup() {
  //부저와 LED를 연결한 핀을 출력모드로 설정합니다. 
  Serial.begin(9600);
  pinMode(Rled,OUTPUT);
  pinMode(Gled,OUTPUT);
  pinMode(buzzerPin,OUTPUT);
  pinMode(PIR, INPUT);      // 아두이노의 12번핀을 입력으로 사용합니다.
  pinMode(BLED, OUTPUT);   

}
void loop() {
  int ifIsHuman = digitalRead(PIR);   // 인체감지센서의 센서값을 ifIsHuman 변수에 저장합니다.
  if(ifIsHuman == HIGH){                    // 센서값이 HIGH이면(인체가 감지되면)
    digitalWrite(BLED, HIGH);          // LED를 작동합니다.
    Serial.println("인체 감지 성공");
    delay(5000);                            // 이후 5초간 기다립니다.
  } else {                                  // 센서값이 HIGH가 아니라면, (인체가 감지되지 않는다면)
    digitalWrite(BLED, LOW);             // LED 작동을 멈춥니다. 
  }  
  
  //온도센서가 측정한 값을 섭씨온도로 변환합니다.
  int value = analogRead(temperature);
  float volt = value * 5.0 / 1024.0;
  float tempC = (volt -0.5)*100;
  Serial.print(tempC);
  Serial.println("C");
  
  // 37도 미만의 경우 정상체온으로 측정하여 Green LED가 동작하도록 설정합니다. 
  if(tempC < 37.0){
    noTone(buzzerPin);
    digitalWrite(Rled,LOW);
    digitalWrite(Gled,HIGH);
  } 

  // 사람의 정상 체온 범위를 고려하여 37도 이상인 경우 LED와 부저가 동작하도록 설정합니다. 
  else{
    tone(buzzerPin,294);
    digitalWrite(Gled,LOW);
    digitalWrite(Rled,HIGH);
  }
  delay(500);
}
