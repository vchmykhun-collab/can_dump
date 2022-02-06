#include <SPI.h>
#include <mcp2515.h>

struct can_frame canMsg; // for reading

MCP2515 mcp2515(10);

void setup() {
  
  Serial.begin(115200);
  
  mcp2515.reset();

  //  mcp2515.setBitrate(CAN_500KBPS, MCP_8MHZ);
  mcp2515.setBitrate(CAN_100KBPS, MCP_8MHZ);

  mcp2515.setNormalMode();
}

void print_msg(can_frame canMsg) {
  if (canMsg.can_id <= 0xff) {
    Serial.print("0");
  }
  Serial.print(canMsg.can_id, HEX); // print ID
  Serial.print(" "); 
  Serial.print(canMsg.can_dlc, HEX); // print DLC
  Serial.print(" ");
  
  // print the data
  for (int i = 0; i<canMsg.can_dlc; i++)  {
    if (canMsg.data[i] <= 15) {
      Serial.print("0");
    }
    Serial.print(canMsg.data[i],HEX);
    Serial.print(" ");

  }
  Serial.println();
}

void loop() {
  if (mcp2515.readMessage(&canMsg) == MCP2515::ERROR_OK) {
    print_msg(canMsg);
// Filter messages from IDs
//    switch(canMsg.can_id) {
//      case 0x26E:
//      case 0x130:
//      case 0x202:
//      case 0x1f6:
//      case 0x21A:
//      case 0x5f2:
//        print_msg(canMsg);
//        return;
//    }
  }
}
