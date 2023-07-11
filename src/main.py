import pandas as pd
import pyshark
from extractFlow import extract_flow_info
from FlowDirection import flow_direction
from extractTimeStamps import Time_main
from extract_size import packet_length, segment_length
from extract_window_size import init_window_size, actual_pkt_fwd
from extract_flags import extractFlags
from predict_model import predict_output


def main():
    #define columns in the dataframe
    columns = [' Bwd IAT Max', ' Bwd URG Flags', ' Total Backward Packets',
       ' Fwd IAT Max', ' Active Max', ' URG Flag Count',
       ' Bwd Packet Length Mean', ' act_data_pkt_fwd',
       ' Bwd Packet Length Std', ' PSH Flag Count',
       ' ACK Flag Count', ' Avg Fwd Segment Size', 'Flow Bytes/s',
       ' Fwd Avg Bulk Rate', 'Active Mean',
       'Bwd Packet Length Max', 'Init_Win_bytes_forward', 'Idle Mean','dummy']
    
    try:
        packet_df = pd.DataFrame(columns=columns)

        pcap = pyshark.FileCapture('pcap_files/example.pcap')
        flow_dictionary, features_df = extract_flow_info(pcap)
        flow_with_direction = flow_direction(flow_dictionary)
        Time_main(flow_with_direction, packet_df)
        packet_length(flow_with_direction, packet_df)
        segment_length(flow_with_direction, packet_df)
        init_window_size(flow_with_direction,packet_df)
        actual_pkt_fwd(flow_with_direction,packet_df)
        extractFlags(flow_with_direction,packet_df)

        #drop extra columns from the dataframe !!
        packet_df.drop(['dummy',18],axis = 1,inplace=True)
        # print(packet_df)

        predict_output(packet_df, features_df)

        mapping_dict = {0:"BENIGN",4:"DoS Hulk",2:"DDoS", 10:"PortScan",3:"DoS GoldenEye",5:"DoS Slowhttptest",
                        6:"DoS slowloris", 7:"FTP-Patator",11:"SSH-Patator",1:"Bot",12:"Web Attack � Brute Force",
                        8:"Heartbleed ", 9:"Infiltration",13:"Web Attack � Sql Injection",14:"Web Attack � XSS"}     

        features_df['result'] = features_df['result'].replace(mapping_dict)   
                          
        """----------------------saving to csv file------------------------"""
        features_df.to_csv("ansDF.csv",index=False)
    except Exception as e:
        print("An error occured: ", e.args[0])
    
    return

"""---------------------------------------------------------------------------------------------"""
#code entry point 

if __name__ == "__main__":
    main()


