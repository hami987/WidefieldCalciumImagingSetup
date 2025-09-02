#include <ax12.h>           // ArbotiX DYNAMIXEL library

#define SERVO_ID           254
#define SPEED_VALUE        432    // 0–1023. 432 ≃ 1 rev in ~2 s (no load)
#define RUN_TIME_MS        25000   // ~3 rev at SPEED_VALUE

void setup() {
  Serial.begin(9600);
  dxlInit(1000000);              // open bus at 1 Mbps
  pinMode(23, OUTPUT);           // direction‐pin for ArbotiX
  digitalWrite(23, HIGH);

  // ——— Wheel‐Mode (continuous) ———
  ax12SetRegister2(SERVO_ID, AX_GOAL_SPEED_L, 432);
  ax12SetRegister2(SERVO_ID, AX_CW_ANGLE_LIMIT_L,  0);
  ax12SetRegister2(SERVO_ID, AX_CCW_ANGLE_LIMIT_L, 0);

  // set a constant speed
  ax12SetRegister2(SERVO_ID, AX_GOAL_SPEED_L, SPEED_VALUE);

  Serial.println("Spinning…");
  delay(RUN_TIME_MS);            // run long enough for ~3 turns

  // stop
  ax12SetRegister2(SERVO_ID, AX_GOAL_SPEED_L, 0);
  Serial.println("Done.");
}

void loop() {
  // nothing else
}
