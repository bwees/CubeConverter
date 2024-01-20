#include <Arduino.h>


// #define CONTROL_TYPE_LOADED_ANIMATION
#define CONTROL_TYPE_SERIAL

#ifdef CONTROL_TYPE_SERIAL
    #include <QuadrumSerial.h>
    QuadrumSerial cube(8, 1, 1, 500);
#endif

#ifdef CONTROL_TYPE_LOADED_ANIMATION
    #include <QuadrumCode.h>
    #include <animation.h>

    QuadrumCode cube(animation, 256);
#endif

bool cubeData[512];


void setup() {
    Serial.begin(115200);
    Serial2.begin(250000);

    cube.start(); // must be the last call inside setup function
}

void loop() {


    // // load frame into cubeData
    for (int y = 0; y < 8; y++) {
        for (int x = 0; x < 8; x++) {

            char rowByte = 0;

            for (int z = 0; z < 8; z++) {
                bool state = cube.getVoxelState(x, y, z); // returns true if voxel at x, y and z is on, otherwise returns false
                rowByte |= (state << z);
            }

            Serial2.write(rowByte);
        }
    }
    // delay(1000);

    // // // load frame into cubeData
    // for (int y = 0; y < 8; y++) {
    //     for (int x = 0; x < 8; x++) {

    //         char rowByte = 0;

    //         for (int z = 0; z < 8; z++) {
    //             bool state = cube.getVoxelState(x, y, z); // returns true if voxel at x, y and z is on, otherwise returns false
    //             rowByte |= (state << z);
    //         }

    //         Serial2.write(0x00);
    //     }
    // }
    // delay(1000);
}
