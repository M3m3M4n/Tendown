# Info
**Device:** Tenda AC10U AC-1200 router\
**Tested verison:** US_AC10UV1.0RTL_V15.03.06.48_multi_TDE01\
**By:** hnh49 of VCS
# Vulnerability
* Vulnerability exist in /goform/addressNat handling module, 'mitInterface' parameter get parsed with sprintf lead to overflow\
![cause1](./bof4_addressNat_cause.jpg)
# Payload
* This payload crashes the device with $pc == 0x626262
![payload](./bof4_addressNat_payload.png)
