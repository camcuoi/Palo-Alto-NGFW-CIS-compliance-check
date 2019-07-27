import xml.etree.ElementTree as ET
def main():
    
    tree = ET.parse("running-config.xml")
    root = tree.getroot()
    #1.1.1 Ensure 'Login Banner' is set (Scored)
    children = root.getchildren()
    #ch1 is element <devices> (children[2])
    ch1 = children[2]
    # ch2 start from <devices>
    ch2 = ch1.getchildren()
    #/entry/deviceconfig/system 0/1/1
    ch3 = ch2[0][1][1]
    # check if login-banner is set
    # chk = ch3.find('login-banner')
    if ch3.find('login-banner')==None:
        print('Login banner is not set')
        print('Checking CIS 1.1.1 failed')
    else:
        print('login banner is set as following:')
        print ch3.find('login-banner').text
    
    # 1.1.2 Ensure 'Enable Log on High DP Load' is enabled (Scored)
    #/entry/deviceconfig/setting/management 0/1/0/1
    ch4 = ch2[0][1][0][1]
    if ch4.find('enable-log-high-dp-load')==None:
        print('log high dp load is not enable')
        print('Checking CIS 1.1.2 failed')
    else:
        print('log high dp load is enable')
        print ch4.find('enable-log-high-dp-load').text
        
    #1.2.1 Ensure 'Permitted IP Addresses' is set to those necessary for device management (Scored)
    #/entry/deviceconfig/system 0/1/1
    if ch3.find('permitted-ip')==None:
        print('Permitted IP Addresses is not set for device management')
        print('Checking CIS 1.2.1 failed')
    else:
        tvar = ch3.find('permitted-ip')
        print('Permitted IP Addresses is set to those necessary for device management')
        for ele in tvar:
            print ele.attrib
    
    #1.2.2 Ensure 'Permitted IP Addresses' is set for all management profiles where SSH, HTTPS, or SNMP is enabled (Scored)
    #/entry/network/profiles/interface-mnageent-profile
    ch5 = ch2[0][0][1][1]
    # no interface management profile
    p=0
    if ch5.text == None:
        print(' You dont have interface management profile')
    else:
        for tvar1 in ch5.findall('entry'):
            if tvar1.find('permitted-ip')==None:
                print('you dont have permitted ip on following profile:')
                print tvar1.attrib
                print('Checking CIS 1.2.2 failed')
                p = p+1
            else:
                tvar2 = tvar1.find('permitted-ip')
                print('this profile', tvar1.attrib,'has folloing permitted ip')
                for ele in tvar2:
                    print ele.attrib
    if p==0 :
        print('Checking CIS 1.2.2 PASS')
    else:
        print('since one of profile does not has permitted ip, Checking CIS 1.2.2 failed')
# khi structure has only 1 element, then we can not use indice [0], must use getchildren()
# for example <config> and <devices>
if __name__ == '__main__': 
    main()