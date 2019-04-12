/*****************************************************************************
* | Description :	BitWear extension for micro:bit
* | Developer   :   CH MAKER Ed
* | More Info   :	http://chmakered.com/
******************************************************************************/

/**
 * Provides access to BitWear blocks for micro: bit functionality.
 */
//% color=190 icon="\uf126" block= "BitWear"
//% groups="['Analog', 'Digital', 'I2C', 'Grove Modules']"
namespace BitWear {
    /**
    * turn on of off the vibration motor
    */
    //% blockId=SetMotor
    //% block="motor $on|"
    //% on.shadow="toggleOnOff"
    //% on.defl="true"
    //% weight=45
    export function SetMotor(on: boolean) {
        if (on) {
            pins.digitalWritePin(DigitalPin.P2, 1);
        }else{
            pins.digitalWritePin(DigitalPin.P2, 0);
        }
    }
}