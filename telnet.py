import telnetlib


string = "show run"
enter = "\n"
end = "end"

tn = telnetlib.Telnet("192.168.80.135",32771)

tn.write(enter.encode())
tn.write(string.encode())
tn.write(enter.encode())
#show_inter=tn.read_all().decode("ascii")

#tn.close()
show_inter=tn.read_until(b"line vty 0 4").decode('ascii')


f = open("/opt/running_info_R1","w",encoding="utf-8")
f.write(show_inter)
f.close()
