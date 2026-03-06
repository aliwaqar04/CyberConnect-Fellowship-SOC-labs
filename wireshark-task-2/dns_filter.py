import pyshark

def analyze_dns(pcap_file):
    cap = pyshark.FileCapture(pcap_file, display_filter='dns')

    print("=" * 55)
    print(f"{'DNS TRAFFIC ANALYSIS':^55}")
    print(f"File: {pcap_file}")
    print("=" * 55)
    print(f"{'#':<5} {'SOURCE IP':<20} {'QUERIED DOMAIN'}")
    print("-" * 55)

    packet_count = 0
    query_count = 0

    for packet in cap:
        packet_count += 1
        try:
            if hasattr(packet, 'dns'):
                dns_layer = packet.dns
                qry_name = None

                if hasattr(dns_layer, 'qry_name'):
                    qry_name = dns_layer.qry_name
                elif hasattr(dns_layer, 'dns_qry_name'):
                    qry_name = dns_layer.dns_qry_name

                if qry_name:
                    src_ip = packet.ip.src
                    query_count += 1
                    print(f"{query_count:<5} {src_ip:<20} {qry_name}")

        except AttributeError:
            pass

    cap.close()
    print("-" * 55)
    print(f"Total packets analyzed : {packet_count}")
    print(f"DNS queries found      : {query_count}")
    print("=" * 55)

if __name__ == "__main__":
    PCAP_FILE = "capture.pcap"
    analyze_dns(PCAP_FILE)