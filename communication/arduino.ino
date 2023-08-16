void setup() {
  Serial.begin(115200); // 시리얼 통신 속도 설정
}

void loop() {
  if (Serial.available()) { // 시리얼 버퍼에 데이터가 있는지 확인
    char receivedChar = Serial.read(); // 데이터를 읽음
    Serial.print("Received: ");
    Serial.println(receivedChar); // 수신된 데이터 출력
  }
}
