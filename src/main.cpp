#include <Arduino.h>
/* first argument specifies cube side (in this case it is a 4x4x4 cube),
second the number of channels (colors for each LED)
third the resolution of each color (in this case 1 is just on/off)
last argument sets the speed at which the loop function is called

for debugging reasons the last argument is set to 256, a quite low setting, increase
it as much as possible while still being able to stream frames to the cube */

// #define CONTROL_TYPE_LOADED_ANIMATION
#define CONTROL_TYPE_SERIAL

#ifdef CONTROL_TYPE_SERIAL
    #include <QuadrumSerial.h>
    QuadrumSerial cube(8, 1, 1, 256);
#endif

#ifdef CONTROL_TYPE_LOADED_ANIMATION
    #include <QuadrumCode.h>
    #include <animation.h>

    QuadrumCode cube(animation, 256);
#endif

bool cubeData[512];

void setup() {
    Serial.begin(115200);
    Serial1.begin(250000);

    cube.start(); // must be the last call inside setup function
}

int y = 0;
void loop() {
    // load frame into cubeData
    for (int y = 0; y < 8; y++) {
        for (int x = 0; x < 8; x++) {
            for (int z = 0; z < 8; z++) {
                int index = (y * 64) + (z * 8) + x;
                cubeData[index] = cube.getVoxelState(x, y, z); // returns true if voxel at x, y and z is on, otherwise returns false
            }
        }
    }

    // send frame to cube
}
