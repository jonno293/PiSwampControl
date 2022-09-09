objective of this repo is to use a raspberry pi as a thermostat with a swamp cooler.

<<<<<<< HEAD
It is configurable to multiple configurations

Trade study notes: https://cloud.roberts10.com/index.php/s/x88f4QdMDEXwFCK
=======
It is configurable to multiple configurations defined by config parameter in "swampcontrolsample.py"
Primary configuration (config = 1) Relay Board of 4x relays
  4 Hi/Low (0-5V) parameters (Fan Hi, Fan Lo, Water pump, purge pump (optional)) are controlled and commanded out over individual pins. These pins are connected to   relays which then pass 120V AC to the component
Secondary configuration (config = 2) Masterstat
  This configuration will pass an array of 4 boolean values to the masterstat.py which then computes the PWM wave to be sent out over a single pin. the connection points in this config is simply GND, and Signal.
  
 The goal for temperature sensing is to use either the DHT11 or DHT22 temp/humidity sensors. DHT22 is better and has more accuracy but DHT11 is an option as well.
 
 
>>>>>>> 3507f497768b35f2f4ae2ec897bb5db091dfb32a
