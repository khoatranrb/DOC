#include<AFMotor.h>

AF_DCMotor motor1(3);
AF_DCMotor motor2(4);
char cmd = 2;

int trig = 8;
int echo = 7;

unsigned long duration;
int dist;

void setup(){
  Serial.begin(9600);
  motor1.setSpeed(255);
  motor2.setSpeed(255);
}

void loop(){
   if ( Serial.available() > 0 ){
    cmd = Serial.read();
   }
   
  if(cmd=='1'){
    digitalWrite(trig,0);
   delayMicroseconds(2);
   digitalWrite(trig,1);
   delayMicroseconds(5);
   digitalWrite(trig,0);

   duration = pulseIn(echo, HIGH);

   dist = int(duration/2/29.412);
   Serial.println(dist);

   if(dist>7){
    Stop();
   }
   else{
    forward();
   }
  }
  else if(cmd=='5'){
    right();
  }
  else if(cmd=='3'){
    backward();
  }
  else if(cmd=='4'){
    left();
  }
  else if(cmd=='2'){
    Stop();
  }
  else if(cmd=='9'){
    forward();;
  }
}

void forward(){
  motor1.run(FORWARD);
  motor2.run(FORWARD);
}

void backward(){
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
}

void left(){
  motor1.run(FORWARD);
  motor2.run(RELEASE);
}

void right(){
  motor1.run(RELEASE);
  motor2.run(FORWARD);
}

void Stop(){
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}
