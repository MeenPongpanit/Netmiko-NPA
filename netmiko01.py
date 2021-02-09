from netmiko import ConnectHandler

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
    with ConnectHandler(**device_params) as ssh:
        print(f'Configuring {device}...')
        ssh.send_config_from_file(f'./config/{device}.txt')
        # print(ssh.send_command('sh ip int br'))
