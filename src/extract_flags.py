"""This file extracts information regarding the flags in the packets
# ACK Flag Count
# Bwd URG Flags
# PSH Flag Count
# URG Flag Count
"""

#extract all flags from the packets; 

def extractFlags(flow_with_direction, packet_df):
    row = 0
    for key in flow_with_direction:
        forward_flow = flow_with_direction[key]['forward']
        backward_flow = flow_with_direction[key]['backward']     #extract forward and backward flow of packets 

        ack_flags = 0
        bwd_urg_flags = 0
        psh_flag_count = 0
        urg_flag_count = 0

        for pkt in forward_flow:
            if 'tcp' in pkt:
                ack_flags += 1 if pkt.tcp.flags_ack.int_value == 1 else 0
                psh_flag_count += 1 if pkt.tcp.flags_push.int_value == 1 else 0
                urg_flag_count += 1 if pkt.tcp.flags_urg.int_value == 1 else 0

        for pkt in backward_flow:
            if 'tcp' in pkt:
                ack_flags += 1 if pkt.tcp.flags_ack.int_value == 1 else 0
                bwd_urg_flags += 1 if pkt.tcp.flags_urg.int_value == 1 else 0
                psh_flag_count += 1 if pkt.tcp.flags_push.int_value == 1 else 0
                urg_flag_count += 1 if pkt.tcp.flags_urg.int_value == 1 else 0

        packet_df.iloc[row,packet_df.columns.get_loc(' ACK Flag Count')] = ack_flags
        packet_df.iloc[row,packet_df.columns.get_loc(' PSH Flag Count')] = psh_flag_count
        packet_df.iloc[row,packet_df.columns.get_loc(' URG Flag Count')] = urg_flag_count
        packet_df.iloc[row,packet_df.columns.get_loc(' Bwd URG Flags')] = bwd_urg_flags
        row += 1

    return 