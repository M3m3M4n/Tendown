# Info
**Device:** Tenda AC10U AC-1200 router\
**Tested verison:** US_AC10UV1.0RTL_V15.03.06.48_multi_TDE01\
**By:** hnh49 of VCS
# Vulnerability
* Vulnerability exists in /goform/SetSambaCfg handling module, 'usbName' parameter is used directly in a system command\
![cause1](./cmdinject2_SetSambaCfg_cause.jpg)
# Payload
![payload](./cmdinject2_SetSambaCfg_payload.png)
