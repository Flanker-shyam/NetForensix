import pandas as pd

def extract_flow_info(pcap):
    flow_dictionary = dict()
    columns = ['key','TimeStamp', 'srcIp', 'dstIp','srcPort', 'dstPort']
    features_df = pd.DataFrame(columns=columns)

    srcIp = ""
    dstIp = ""
    srcPort = ""
    dstPort = ""

    for pkt in pcap:
        timestamp = pkt.sniff_time
        if "tcp" in pkt:
            srcPort = pkt.tcp.srcport
            dstPort = pkt.tcp.dstport
        elif "udp" in pkt:
            srcPort = pkt.udp.srcport
            dstPort = pkt.udp.dstport

        if "ip" in pkt:
            srcIp = pkt.ip.src
            dstIp = pkt.ip.dst
        elif "ipv6" in pkt:
            srcIp = pkt.ipv6.src
            dstIp = pkt.ipv6.dst

        key_string = srcIp + ":" + srcPort + "-" + dstIp + ":" + dstPort

        flow_dictionary.setdefault(key_string, []).append(pkt)
        if not key_string in features_df['key'].values:
            features_df = features_df._append({'key':key_string,'TimeStamp':f'{timestamp}','srcIp': f'{srcIp}', 'dstIp':f'{dstIp}', 'srcPort':f'{srcPort}', 'dstport':f'{dstPort}'},ignore_index = True)

    return flow_dictionary, features_df

