import pandas as pd
import argparse
import pyshark
import os
from tqdm import tqdm
from alive_progress import alive_bar
from extractFlow import extract_flow_info
from FlowDirection import flow_direction
from extractTimeStamps import Time_main
from extract_size import packet_length, segment_length
from extract_window_size import init_window_size, actual_pkt_fwd
from extract_flags import extractFlags
from predict_model import predict_output

def print_welcome_message():
   welcome = r"""
  
 _   _      _  ______                       _      
| \ | |    | | |  ___|                     (_)     
|  \| | ___| |_| |_ ___  _ __ ___ _ __  ___ ___  __
| . ` |/ _ \ __|  _/ _ \| '__/ _ \ '_ \/ __| \ \/ /
| |\  |  __/ |_| || (_) | | |  __/ | | \__ \ |>  < 
\_| \_/\___|\__\_| \___/|_|  \___|_| |_|___/_/_/\_\
                                                   
                                                                                                                                                                                                             

    """
   print(welcome)

def run_function_with_progress(function, function_name, *args):
    with alive_bar(1, title=function_name, bar='blocks') as bar:
        result = function(*args)
        bar()
    return result

def flow_file(pcap_file, flag):
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

        pcap = pyshark.FileCapture(pcap_file)
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

        if flag == "flow":
            print("Output generated Successfully\n", packet_df.describe())

            flow_csv_path = 'flow.csv'

            packet_df.to_csv(flow_csv_path, index=False)
            print(f"Flow CSV file generated: {flow_csv_path}")

    except Exception as e:
        print("An error occured: ", e.args[0])
    
    return packet_df,features_df

def result_file(packet_df, features_df):
    # print(packet_df)
        try:
            predict_output(packet_df, features_df)

            mapping_dict = {0:"BENIGN",4:"DoS Hulk",2:"DDoS", 10:"PortScan",3:"DoS GoldenEye",5:"DoS Slowhttptest",
                            6:"DoS slowloris", 7:"FTP-Patator",11:"SSH-Patator",1:"Bot",12:"Web Attack � Brute Force",
                            8:"Heartbleed ", 9:"Infiltration",13:"Web Attack � Sql Injection",14:"Web Attack � XSS"}     

            features_df['result'] = features_df['result'].replace(mapping_dict)   
                            
            """----------------------saving to csv file------------------------"""

            print("Output generated Successfully\n",features_df['result'].value_counts())

            flow_csv_path = 'result.csv'

            features_df.to_csv(flow_csv_path, index=False)
            print(f"Result CSV file generated: {flow_csv_path}")
        
        except Exception as e:
            print("An error occured: ", e.args[0])

def main():
    parser = argparse.ArgumentParser(description="Network Intrusion Tool/flanker-toolX")
    parser.add_argument('-f', '--flow', action='store_true', help="Generate flow.csv file")
    parser.add_argument('-r', '--result', action='store_true', help="Get result")
    parser.add_argument('--pcap', type=str, help="Path to the uploaded pcap/pcapng file")

    args = parser.parse_args()
    print_welcome_message()

    if args.flow and args.pcap:
        print_welcome_message()
        if os.path.isfile(args.pcap) and (args.pcap.endswith('.pcap') or args.pcap.endswith('.pcapng')):
            pkt_df, ft_df = run_function_with_progress(flow_file, "flow_file", args.pcap, "flow")
        else:
            print("Invalid pcap file. Please provide a valid path to a .pcap file.")
    elif args.result and args.pcap:
        print_welcome_message()
        if os.path.isfile(args.pcap) and (args.pcap.endswith('.pcap') or args.pcap.endswith('.pcapng')):
            pkt_df, ft_df = run_function_with_progress(flow_file, "flow_file", args.pcap, "res")
            run_function_with_progress(result_file, "result_file", pkt_df, ft_df)
        else:
            print("Invalid pcap file. Please provide a valid path to a .pcap/.pcapng file.")
    else:
        print("Invalid option. Please choose either --flow(-f) or --result(-r), and provide a valid --pcap file path.\nuse --help for more information")

if __name__ == "__main__":
    main()
