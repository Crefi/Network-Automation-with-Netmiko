from netmiko import ConnectHandler

def ip_validation(address):
    parts = address.split(".")

    if len(parts) != 4:
        print("IP address {} is not valid".format(address))
        return False

    for part in address.split("."):
        if int(part) < 0 or int(part) > 255:
            print("IP address {} is not valid".format(address))
            return False
    return True

try:
    with open('ip.txt') as f:
        lines = []
        for line in f:
            lines.append(line)
    if ip_validation(line) == True:
        print("All the ip address are good")
    else:
        print("Some ip address in not good ")
    f.close()
except Exception as exc:
    print("The file cannot be open :")




def ConfigExtract():
    IP_LIST = open('ip.txt')
    for IP in IP_LIST:
        device = {
            'ip': IP,
            'username': 'admin',
            'password': 'cisco',
            'device_type': 'cisco_ios',
        }

        print('Connecting to device' + IP)
        net_connect = ConnectHandler(**device)

        output = net_connect.send_command('show run', delay_factor=False)
        print(output)

def ConfigSend():
    IP_LIST = open('ip.txt')
    for IP in IP_LIST:
        device = {
            'ip': IP,
            'username': 'admin',
            'password': 'cisco',
            'device_type': 'cisco_ios',
        }

        print('Connecting to device' + IP)
        net_connect = ConnectHandler(**device)

        output = net_connect.send_config_from_file(config_file='config_file')
        print(output)

        print('\n Saving the Configuration' + '\n')
        output = net_connect.send_command('wr', delay_factor=False)
        print(output)

def print_menu():
    print ('1 = Extract the config from devices' )
    print ('2 = Send config from file' )
    print ('3 = Exit' )

while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
           ConfigExtract()
        elif option == 2:
            ConfigSend()
        elif option == 3:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

