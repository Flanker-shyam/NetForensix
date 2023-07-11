
def packet_length(flow_with_direction, packet_df):
    row = 0
    for key in flow_with_direction:  #extract a key from the dictionary
        backward_flow = flow_with_direction[key]['backward'] #extract the flow backward

        bwd_packet_lengths = []
        for pkt in backward_flow:
            if "ip" in pkt:
                bwd_packet_lengths.append(float(pkt.ip.len))
            elif "ipv6" in pkt:
                bwd_packet_lengths.append(float(pkt.ipv6.plen))

        max_length = 0    
        mean_length = 0
        std_length = 0
        if bwd_packet_lengths:
            max_length = max(bwd_packet_lengths)
            mean_length = sum(bwd_packet_lengths) / len(bwd_packet_lengths)
            std_length = (sum((x - mean_length) ** 2 for x in bwd_packet_lengths) / len(bwd_packet_lengths)) ** 0.5

        packet_df.iloc[row,packet_df.columns.get_loc('Bwd Packet Length Max')] = max_length
        packet_df.iloc[row,packet_df.columns.get_loc(' Bwd Packet Length Mean')] = mean_length
        packet_df.iloc[row,packet_df.columns.get_loc(' Bwd Packet Length Std')] = std_length
        packet_df.iloc[row,packet_df.columns.get_loc(' Total Backward Packets')] = len(backward_flow)

        row += 1
    return

"""------------------------------------------------------------------------------------------------------------"""

def segment_length(flow_with_direction, packet_df):
    row = 0
    for key in flow_with_direction:  #extract a key from the dictionary
        forward_flow = flow_with_direction[key]['forward'] #extract the flow backward

        total_segments = 0
        total_segment_size = 0
        for pkt in forward_flow:
            if "tcp" in pkt:
                total_segment_size += float(pkt.tcp.len)
            elif "udp" in pkt:
                total_segment_size += float(pkt.udp.length)
            total_segments += 1
            
        if total_segments > 0:
            avg_segment_size = total_segment_size / total_segments
        
        packet_df.iloc[row,packet_df.columns.get_loc(' Avg Fwd Segment Size')] = avg_segment_size
        row += 1
    return

"""-------------------------------------------------------------------------------------------------------------------"""
