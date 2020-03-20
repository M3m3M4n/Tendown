# Info
**Device:** Tenda AC10U AC-1200 router\
**Tested verison:** US_AC10UV1.0RTL_V15.03.06.48_multi_TDE01\
**By:** hnh49 of VCS
# Vulnerability
* Vulnerability exists in /goform/SetClientState handling module, 'limitSpeed' parameter get parsed using sprintf, lead to overflow\
![cause1](./bof6_SetClientState_cause_1.JPG)\
![cause2](./bof6_SetClientState_cause_2.JPG)
# Payload
* This payload crashes the device with $pc == 0x61616161
![payload](./bof6_SetClientState_payload.PNG)
