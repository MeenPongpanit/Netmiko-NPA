from netmiko import ConnectHandler
import threading
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
def config(device):
    device_params['ip'] = devices_ip[device]
    with ConnectHandler(**device_params) as ssh:
        # print(f'Configuring {device}...')
        # ssh.send_config_from_file(f'./loopback/{device}.txt')
        # if device in [f'R{i}' for i in range(1, 6)]:
        print(f'Configuring {device}...')
        # ssh.send_config_from_file('accesslist_tnssh/task4.txt')

        # ssh.send_config_from_file(f'cdp_lldp/{device}.txt')

        # ssh.send_command('wr')
        cdp_nei = ssh.send_command('sh cdp nei')
        cdp_nei = [x for x in cdp_nei.split('\n') if 'npa.com' in x]
        for neighbour in cdp_nei:
            # descript(neighbour)
            ssh.send_config_set(descript(neighbour))
        if ssh.send_command('show ip int br'):
            print(device, 'success')

def descript(neighbourline):
    hostname, local_int, local_num, *temp, nei_int, nei_num = neighbourline.split()
    print(hostname, local_int, local_num, nei_int, nei_num)
    hostname = hostname.strip('.npa.com')
    return [f'int {local_int} {local_num}', f'des "connect to {nei_int} {nei_num} of {hostname}"']

def nat_config(device):
    device_params['ip'] = devices_ip[device]
    with ConnectHandler(**device_params) as ssh:
        ssh.send_config_set(['router ospf 1', 'default-information originate'])
        # ssh.send_config_set(['access-list 10 permit any', 'ip nat inside source list 10 interface gigabitEthernet 0/2 overload'])
        # ssh.send_config_set(['int g0/1', 'ip nat inside', 'int g0/2', 'ip nat outside'])
        print(ssh.send_command('show run'))



def test_connect(device):
    device_params['ip'] = devices_ip[device]
    with ConnectHandler(**device_params) as ssh:
        if ssh.send_command('show ip int br'):
            print(device, 'success')

for device in ['R5']:
    # threading.Thread(target=nat_config, args=(device, )).start()
    nat_config(device)
    # threading.Thread(target=test_connect, args=(device, )).start()

    
