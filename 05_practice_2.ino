void setup()
{
  pinMode(7, OUTPUT);
}

void loop()
{
  int i = 1;

  digitalWrite(7, HIGH);
  delay(1000);
  digitalWrite(7, LOW);
  delay(1000);
  
  while(i<=5){
    digitalWrite(7, LOW);
    delay(100);
    
    digitalWrite(7, HIGH);
    delay(100);

    i++;  
  }
  
  while(1) {
 
  }
}
