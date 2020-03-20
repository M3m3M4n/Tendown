# Info
**Device:** Tenda AC10U AC-1200 router\
**Tested verison:** US_AC10UV1.0RTL_V15.03.06.48_multi_TDE01\
**By:** hnh49 of VCS
# Vulnerability
* Vulnerability exist in /goform/PowerSaveSet handling module, 'time' parameter in request get parsed using sscanf and sprintf to stack. Lead to buffer overflow.
![cause](./bof1_PowerSaveSet_cause.jpg)
# Payload
* This payload crashes the device with $pc == 0x626262
![payload](./bof1_PowerSaveSet_payload.png)
