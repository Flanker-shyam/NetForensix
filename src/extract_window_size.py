
"""This file contains functions to extract following given features from the flow
Init_Win_bytes_forward(Intial window bytes size in forward direction)
act_data_pkt_fwd (actual data packets in forward direction)
"""
def init_window_size(flow_with_direction, packet_df):
    row = 0
    for key in flow_with_direction:
        forward_flow = flow_with_direction[key]['forward']
        init_win_length = 0
        for pkt in forward_flow:
            if 'tcp' in pkt:
                if pkt.tcp.flags_syn.int_value == 1:
                    init_win_length = pkt.tcp.window_size_value
                    break
        packet_df.iloc[row,packet_df.columns.get_loc('Init_Win_bytes_forward')] = init_win_length
        row +=1

    return

"""---------------------------------------------------------------------------------------"""
def actual_pkt_fwd(flow_with_direction, packet_df):
    row = 0
    for key in flow_with_direction:
        forward_flow = flow_with_direction[key]['forward']
        actual_pkt_count = 0
        for pkt in forward_flow:
            if "tcp" in pkt:
                if hasattr(pkt.tcp, 'payload'):
                    actual_pkt_count += 1

            elif "udp" in pkt:
                if hasattr(pkt.udp, 'payload'):
                    actual_pkt_count += 1

        packet_df.iloc[row,packet_df.columns.get_loc(' act_data_pkt_fwd')] = actual_pkt_count
        row += 1
    return

"""----------------------------------------------------------------------------------------------------"""



