#from scapy.all import Ether, Dot1Q, IP, sendp, sniff
#import threading
#
## 송신 함수
#def send_vlan_packet():
#    pkt = Ether(src="18:c0:4D:72:c5:e3", dst="00:08:dc:78:91:71") / Dot1Q(vlan=100) / IP(dst="192.168.100.15") / "Hello, VLAN!"
#    print("Sending VLAN packet...")
#    sendp(pkt, iface="이더넷")  # 'eth0'을 적절한 인터페이스 이름으로 변경하세요.
#
## 수신 함수
#def receive_vlan_packets():
#    def handle_packet(packet):
#        if packet.haslayer(Dot1Q):  # VLAN 태그가 있는지 확인
#            print("VLAN Packet Received:")
#            packet.show()
#
#    print("Listening for VLAN packets...")
#    sniff(iface="이더넷", prn=handle_packet, filter="ether proto 0x8100", count=5)
#
## 메인 함수
#if __name__ == "__main__":
#    # 스레드를 사용하여 송신과 수신을 동시에 수행
#    send_thread = threading.Thread(target=send_vlan_packet)
#    receive_thread = threading.Thread(target=receive_vlan_packets)
#
#    # 수신 스레드 시작
#    receive_thread.start()
#
#    # 잠시 대기 후 송신 스레드 시작 (필요시 시간 조정)
#    send_thread.start()
#
#    # 스레드가 종료될 때까지 대기
#    send_thread.join()
#    receive_thread.join()
from scapy.all import Ether, Dot1Q, IP, sendp, sniff

# 송신 함수
def send_vlan_packet():
    pkt = Ether(src="18:c0:4D:72:c5:e3", dst="00:08:dc:78:91:71") / Dot1Q(vlan=100) / IP(dst="192.168.0.15") / "Hello, VLAN!"
    print("Sending initial VLAN packet...")
    sendp(pkt, iface="이더넷")  # 'eth0'은 네트워크 인터페이스 이름입니다. 환경에 맞게 변경하세요.

# 수신 함수
def receive_and_respond_vlan_packets(timeout=2):
    def handle_packet(packet):
        if packet.haslayer(Dot1Q):
            print("VLAN Packet Received:")
            packet.show()

            # 수신 후 응답 송신
            response_pkt = Ether(src=packet[Ether].dst, dst=packet[Ether].src) / Dot1Q(vlan=200) / IP(dst=packet[IP].src) / "Response VLAN Packet"
            print("Sending response VLAN packet...")
            sendp(response_pkt, iface="이더넷")

    print("Waiting for VLAN packets...")
    #sniff(iface="이더넷", prn=handle_packet, filter="ether proto 0x8100", count=1,timeout=timeout)  # 첫 번째 패킷 수신 후 응답
    sniff(iface="이더넷", prn=handle_packet,  count=1,timeout=timeout)  # 첫 번째 패킷 수신 후 응답

# 메인 함수
if __name__ == "__main__":
    # 초기 송신
    send_vlan_packet()

    # 수신 후 응답
    receive_and_respond_vlan_packets()
    try:
        while True:
            input("Press Enter to send a VLAN packet...")  # 엔터키 입력 대기
            send_vlan_packet()  # 송신
            receive_and_respond_vlan_packets(5)  # 수신 대기 (최대 2초)
    except KeyboardInterrupt:
        print("\nProgram terminated.")
    
    