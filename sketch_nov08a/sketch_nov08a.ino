String testString = "123.45";

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
while (Serial.available()) {
testString = Serial.readString();
float testFloat = testString.toFloat();

Serial.println(testFloat);
}
}
