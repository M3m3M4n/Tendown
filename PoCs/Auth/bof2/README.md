# Info
**Device:** Tenda AC10U AC-1200 router\
**Tested verison:** US_AC10UV1.0RTL_V15.03.06.48_multi_TDE01\
**By:** hnh49 of VCS
# Vulnerability
* Vulnerability exist in /goform/saveParentControlInfo handling module, 'time' parameter in request get parsed using sscanf lead to overflow.
![cause1](./bof2_saveParentControlInfo_cause_1.jpg)
![cause2](./bof2_saveParentControlInfo_cause_2.jpg)
# Payload
* This payload crashes the device with $pc == 0x626262
![payload](./bof2_saveParentControlInfo_payload.png)
