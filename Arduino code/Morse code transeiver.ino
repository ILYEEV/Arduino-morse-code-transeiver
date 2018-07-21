
//setting the pins 
int number;
int buz = A0;
const int dotLength = 50;
const int dashLength = 150;

void setup() {
  //starting serial
  Serial.begin(9600);
  pinMode(buz, OUTPUT);
  Serial.print('3');
}



void loop() {

  //Getting info from python
  if (Serial.available()) {
    number = Serial.read();
    if (number == '1') {
      dot();
    }

    if (number == '2') {
      dash();
    }

    if (number == '3') {
      delay(150);
    }
    
  }
}

// creating functions
void dot(){
  digitalWrite(13, HIGH);
  tone(buz, 196 , 1000);
  delay(dotLength);
  noTone(buz);
  digitalWrite(13, LOW);
  delay(dotLength);
  }



void dash(){
  digitalWrite(13, HIGH);
  tone(buz, 196 , 1000);
  delay(dashLength);
  noTone(buz);
  digitalWrite(13, LOW);
  delay(dashLength);

  }


