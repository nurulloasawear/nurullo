from scapy.all import *

def sniff_devices():
    devices = set()

    def sniff_callback(packet):
        if packet.haslayer(Dot11):
            if packet.type == 0 and packet.subtype == 4:
                if packet.addr2 not in devices:
                    devices.add(packet.addr2)
                    print("New device detected: " + packet.addr2)

    sniff(prn=sniff_callback, iface="wlan0mon", store=0, timeout=60)

if __name__ == "__main__":
    sniff_devices()
