# Info
**Device:** Tenda AC10U AC-1200 router\
**Tested verison:** US_AC10UV1.0RTL_V15.03.06.48_multi_TDE01\
**By:** hnh49 of VCS
# Vulnerability
* Vulnerability exists in /goform/SetOnlineDevName handling module, 'devName' parameter get parsed with sprintf lead to overflow.\
![cause1](./bof7_SetOnlineDevName_cause_1.JPG)\
![cause2](./bof7_SetOnlineDevName_cause_2.JPG)
# Payload
* This payload crashes the device with $pc == 0x61616161
![payload](./bof7_SetOnlineDevName_payload.PNG)
