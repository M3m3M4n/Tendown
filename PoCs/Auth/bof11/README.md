# Info
**Device:** Tenda AC10U AC-1200 router\
**Tested verison:** US_AC10UV1.0RTL_V15.03.06.48_multi_TDE01\
**By:** hnh49 of VCS
# Vulnerability
* Vulnerability exists in /goform/SetSysTimeCfg handling module, 'timezone' parameter get parsed with strcpy lead to overflow\
![cause1](./bof11_SetSysTimeCfg_cause.JPG)
# Payload
* This payload crashes the device with $pc == 0x626262
![payload](./bof11_SetSysTimeCfg_payload.PNG)
