#include <WiFi.h>

const char* ssid = "ESP32_SoftAP";
const char* password = "12345678";

WiFiServer server(80); // 웹 서버를 위한 포트

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  server.begin();
  
  Serial.println("SoftAP started");
  Serial.print("SSID: ");
  Serial.println(ssid);
  Serial.print("Password: ");
  Serial.println(password);
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        Serial.println(c);
      }
    }
    client.stop();
    Serial.println("Client disconnected");
  }
}
