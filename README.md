# 🌡️ 프로젝트: 아두이노 기반 열감지시스템

## 목적
본 프로젝트는 코로나 19의 재확산이 우려되는 만큼 철저하게 온도를 측정하여 경보음과 LED빛을 발산해 주의를 주는 시스템을 구현하는 것이 목적입니다.

### 설명
인체가 인식되면 Blue LED가 켜집니다. 그 후, 온도 센서를 통해 열을 측정하며 36도 이하인 경우 Green LED가 켜집니다.  
반대로, 37도 이상일 경우 Red LED와 부저를 이용해 빛과 경보음으로 위험성을 알립니다.

#### 구성
* 온도센서
* LED 3개 (RLED, GLED, BLED)
* 부저
* 인체 감지 센서

## 🛠️ 구성 요소

### 온도센서
TMP36 온도 센서가 출력하는 ADC 전압 값을 1~1023 사이 값으로 변환해 출력합니다.  
섭씨/화씨 온도 계산을 위해 아두이노에서 측정한 ADC값을 다시 전압으로 변환합니다.  

[변환 공식]  
- 전압(mV) = (ADC값 / 1024.0) x 센서에 공급되는 전압(mV)  
- 섭씨온도 = (전압(mV) - 500.0) / 10.0

## 📊 순서도
![sssssss](https://user-images.githubusercontent.com/76280200/147851193-422206af-a079-4d56-a4ce-f8081c2f7bae.PNG)

## 📅 개인프로젝트
(2020/09 ~ 2020/12)
