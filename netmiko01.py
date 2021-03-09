# from netmiko import ConnectHandler
import netmiko

username = 'admin'
password = 'cisco'

device_params = {
    'device_type': 'cisco_ios',
    # 'ip': device_ip,
    'username': username,
    'password': password,
}

devices_ip = {
    'R0': '172.31.171.1',
    'S0': '172.31.171.2',
    'S1': '172.31.171.3',
    'R1': '172.31.171.4',
    'R2': '172.31.171.5',
    'R3': '172.31.171.6',
    'R4': '172.31.171.7',
    'S2': '172.31.171.8',
    'R5': '172.31.171.9',
}

for device in devices_ip:
    device_params['ip'] = devices_ip[device]
    with netmiko.ConnectHandler(**device_params) as ssh:
        # print(f'Configuring {device}...')
        # ssh.send_config_from_file(f'./loopback/{device}.txt')
        if device in [f'R{i}' for i in range(1, 6)]:
            print(f'Configuring {device}...')
            ssh.send_config_from_file('/accesslist_tnssh/task4.txt')
            # ssh.send_config_from_file(f'./datacontrol/{device}.txt')
            # ssh.send_config_from_file(f'./accesslist/{device}.txt')
        ssh.send_command('wr')
        print(ssh.send_command('sh ip int br'))
