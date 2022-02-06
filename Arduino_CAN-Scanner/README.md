CAN Dump : Arduino CAN scanner part
===

Please assemble a circuit according to following diagram

![alt text](https://github.com/vchmykhun-collab/can_dump/blob/master/Arduino_CAN-Scanner/assets/MCP2515.png?raw=true)

Configuraton notes:

  `mcp2515.setBitrate(CAN_100KBPS, MCP_8MHZ);` - specify 100KBPS or 500KBPS for different versions of CANBUS

  Uncomment `Filter messages by IDs` codeblock to oversee only specific messages.
