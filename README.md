# Palo-Alto-NGFW-CIS-compliance-check
This repo demo how to use python to parse xml config file and check if the configuration complies to CIS.  
In the cis.py I just check first 4 points of CIS:  
  1.1.1 Ensure 'Login Banner' is set  
  1.1.2 Ensure 'Enable Log on High DP Load' is enabled  
  1.2.1 Ensure 'Permitted IP Addresses' is set to those necessary for device management  
  1.2.2 Ensure 'Permitted IP Addresses' is set for all management profiles where SSH, HTTPS, or SNMP is enabled  
For the remaining checks, you can add your own code using similar lines of code above.  
You can find the name of tag you want to check by go to https://firewall-ip/debug, then go to https://firewall-ip/ and modify config as needed then switch to https://firewall-ip/debug to see which tag is modified.  

