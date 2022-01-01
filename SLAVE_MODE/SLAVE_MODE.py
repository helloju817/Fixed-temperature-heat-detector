from Arduino import Arduino
import time

#�� ��ǰ�� ������ ������ �� ��ȣ�� �Ƴ��α� �� ��ȣ�� �Ҵ�

Rled = 10
Gled = 9
buzzerPin = 13                                                
tempPin = 0
BLED = 8
PIR = 12

#�µ������� ����� ���� ��ȯ�Ͽ� �����µ��� ��Ÿ���µ� �ʿ��� ���� ����

TEMP = 0
val = 0

board = Arduino("9600", port="COM3")
board.pinMode(Rled, "OUTPUT")
board.pinMode(Gled, "OUTPUT")
board.pinMode(buzzerPin, "OUTPUT")
board.pinMode(BLED, "OUTPUT")
board.pinMode(PIR, "INPUT")


while True:
#��ü ���� ������ ���� �ڵ�
    
    ifIsHuman=board.digitalRead(PIR)
    if ifIsHuman == "HIGH":
        board.digitalWrite(BLED,"HIGH")
    else :
        board.digitalWrite(BLED,"LOW")   


#�µ� ������ ������ ���� ������ �Ҵ��� ��, �������� ���� �� �ٽ� �����µ��� ��ȯ
    val = board.analogRead(tempPin)
    voltageTemp =  val * 5.0 / 1024.0;
    
    cTemp = (voltageTemp - 0.5)* 100.0
    print "temp: ", cTemp
    time.sleep(0.5)

#�µ��� �ö󰡸� LED, ������ �����ϴ� �ڵ�
#���� �µ��� 37���� ū�� Ȯ��
    
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

 
