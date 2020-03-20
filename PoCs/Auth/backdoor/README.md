# Info
**Device:** Tenda AC10U AC-1200 router\
**Tested verison:** US_AC10UV1.0RTL_V15.03.06.48_multi_TDE01\
**By:** hnh49 of VCS
# Vulnerability
* The router employs 2 account for user to manage its web interface. However, user can only control 'admin' account using provided UI. The other account - 'baseuser' has username and password defaulted to user:user. Despite being named user, this account have full control over web functionalites as normal admin account.
* As this account is normally untouched by user, attacker can log in or use its password as cookies (Cookies: password=user) in requests to bypass httpd access control.
* httpd provided a function to change this account detail, but not exposed to the UI.
# Payload
* View common.py python script for detail.
