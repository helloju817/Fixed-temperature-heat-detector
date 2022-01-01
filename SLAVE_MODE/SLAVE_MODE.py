from Arduino import Arduino
import time

#각 부품을 연결한 디지털 핀 번호와 아날로그 핀 번호를 할당

Rled = 10
Gled = 9
buzzerPin = 13                                                
tempPin = 0
BLED = 8
PIR = 12

#온도센서가 출력한 값을 변환하여 섭씨온도로 나타내는데 필요한 변수 선언

TEMP = 0
val = 0

board = Arduino("9600", port="COM3")
board.pinMode(Rled, "OUTPUT")
board.pinMode(Gled, "OUTPUT")
board.pinMode(buzzerPin, "OUTPUT")
board.pinMode(BLED, "OUTPUT")
board.pinMode(PIR, "INPUT")


while True:
#인체 감지 센서에 대한 코드
    
    ifIsHuman=board.digitalRead(PIR)
    if ifIsHuman == "HIGH":
        board.digitalWrite(BLED,"HIGH")
    else :
        board.digitalWrite(BLED,"LOW")   


#온도 센서가 측정한 값을 변수에 할당한 뒤, 전압으로 변경 후 다시 섭씨온도로 변환
    val = board.analogRead(tempPin)
    voltageTemp =  val * 5.0 / 1024.0;
    
    cTemp = (voltageTemp - 0.5)* 100.0
    print "temp: ", cTemp
    time.sleep(0.5)

#온도가 올라가면 LED, 부저를 제어하는 코드
#섭씨 온도가 37보다 큰지 확인
    
    if cTemp > 37:
        board.analogWrite(buzzerPin, 294)
        time.sleep(0.001911)
        board.digitalWrite(Rled, "HIGH")
        board.digitalWrite(Gled, "LOW")



    else:
        board.analogWrite(buzzerPin, 0)
        time.sleep(0.001911)
        board.digitalWrite(Rled, "LOW")
        board.digitalWrite(Gled, "HIGH")

 
