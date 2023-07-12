"""This function divide packets into forward and backward direction to understand flow pattern"""

def flow_direction(flow_dict):
    flow_with_direction = dict()
    for key in flow_dict:
        forward = []
        backward = []
        packets = flow_dict[key]
        for pkt in packets:
            if 'tcp' in pkt:
                ack_flag = pkt.tcp.flags_ack
                syn_flag = pkt.tcp.flags_syn

                if ack_flag.int_value == 1 and syn_flag.int_value == 1:
                    #backward traffic (ack and syn both flags are set)
                    backward.append(pkt)
                else:
                    # Backward Traffic
                    forward.append(pkt)
            
            elif 'udp' in pkt:
                srcPort = pkt.udp.srcport
                dstPort = pkt.udp.dstport

                if int(srcPort) > int(dstPort):
                    # Forward Traffic (Source Port is less than Destination port)
                    forward.append(pkt)
                else:
                    # Backward Traffic
                    backward.append(pkt)
        flow = dict()
        flow['forward'] = forward
        flow['backward'] = backward
        flow_with_direction[key] = flow
    
    return flow_with_direction   
