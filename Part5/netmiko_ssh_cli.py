from netmiko import ConnectHandler

print("Connecting via SSH => show interface status (brief)")
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.56.101",
    port="22",
    username="cisco",
    password="cisco123!"
    )

config_interface = (
    "interface loopback 15",
    "ip add 15.16.17.18 255.255.255.0",
    "no shut",
)

config_route = (
    "ip route 0.0.0.0 0.0.0.0 lo15",
)

output=sshCli.send_command("show ip interface brief")
print(output)
output=sshCli.send_command("show ip route")
print(output)

cfg = sshCli.send_config_set(config_interface)
print(cfg)
sshCli.send_config_set(config_route)
print(cfg)

output=sshCli.send_command("show ip interface brief")
print(output)
output=sshCli.send_command("show ip route")
print(output)
