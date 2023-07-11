
def custom_sort(packet): #a custome function to sort the packets w.r.t to their timestamp
    if 'tcp' in packet:
        return float(packet.tcp.time_relative)  #to access time stamp
    elif 'udp' in packet:
        return float(packet.udp.time_relative)
    else:
        return float(0)  # or any default value you prefer
    
""""---------------------------------------------------------------------------------------------------"""

# Sort the packets based on the relative time attribute

def sort_TimeStamps(flow_with_direction): 
    # Extract the timestamps from a flow with direction.
    for key in flow_with_direction:  #extract a key from the dictionary
        forward_flow = flow_with_direction[key]['forward'] #now correspond to that key, extract the flow forward
        backward_flow = flow_with_direction[key]['backward'] #extract the flow backward
        forward_flow = sorted(forward_flow, key=lambda pkt: custom_sort(pkt))   #sort forward flow of packets
        backward_flow = sorted(backward_flow, key=lambda pkt: custom_sort(pkt))  #sort backward flow of packets
        flow_with_direction[key]['forward'] = forward_flow  #update the values
        flow_with_direction[key]['backward'] = backward_flow
    return


"""--------------------------------------------------------------------------------------------"""
#function to extract Inter arrival time max and Idle time mean
def IAT_MAX_Idle_mean(flow_with_direction,packet_df):
    row = 0    #to keep track of the row in the dataframe
  
    for key in flow_with_direction:
        forward_flow = flow_with_direction[key]['forward']   #extract forward list
        backward_flow = flow_with_direction[key]['backward']   #extract baclward list 
        maxIatForward = 0          #variable to store maxIAT in forward direction
        maxIatBackward = 0             #variable to store maxIAT in backward direction
        Idle_time = 0          #variable to store Idle time total..

        for i in range(0,len(forward_flow)-1, 2):       #iterate and compare two packets at a time.. 
            time1 = 0                       
            time2 = 0                 

            #extract time from pkt1 of forward flow        
            if "tcp" in forward_flow[i]:
                time1 = float(forward_flow[i].tcp.time_relative)
            elif "udp" in forward_flow[i]:
                time1 = float(forward_flow[i].udp.time_relative)

            #extract time from pkt2 of forward flow
            if "tcp" in forward_flow[i+1]:
                time2 = float(forward_flow[i+1].tcp.time_relative)
            elif "udp" in forward_flow[i+1]:
                time2 = float(forward_flow[i+1].udp.time_relative)

            #take difference of time1-time2 and compare it with maxIat and assign as per the condition
            maxIatForward = abs(time1 - time2) if abs(time1 - time2) > maxIatForward else maxIatForward
            #calclate total IDLE time ---> it is the difference between time of first and second packet 
            Idle_time += abs(time1-time2)

        #similar in backward direction    
        for i in range(0,len(backward_flow)-1, 2):
            time1 = 0
            time2 = 0
            if "tcp" in backward_flow[i]:
                time1 = float(backward_flow[i].tcp.time_relative)
            elif "udp" in backward_flow[i]:
                time1 = float(backward_flow[i].udp.time_relative)

            if "tcp" in backward_flow[i+1]:
                time2 = float(backward_flow[i+1].tcp.time_relative)
            elif "udp" in backward_flow[i+1]:
                time2 = float(backward_flow[i+1].udp.time_relative)

            maxIatBackward = abs(time1 - time2) if abs(time1 - time2) > maxIatBackward else maxIatBackward
            Idle_time += abs(time1-time2)
        
        #Idle time mean = total Idle time / total number of packets..
        Idle_time_Mean = 0
        if(len(forward_flow)+len(backward_flow))>0:
            Idle_time_Mean = Idle_time/(len(forward_flow)+len(backward_flow)) 

        #insert a dummy row initially

        packet_df.loc[row, packet_df.columns.get_loc('dummy')] = 0
        #insert into dataframe at the respective row and col --> row is updated by 1 after each iteration

        packet_df.iloc[row, packet_df.columns.get_loc(' Fwd IAT Max')] = maxIatForward
        packet_df.iloc[row, packet_df.columns.get_loc(' Bwd IAT Max')] = maxIatBackward
        packet_df.iloc[row, packet_df.columns.get_loc('Idle Mean')] = Idle_time_Mean

        row += 1
    return

""""---------------------------------------------------------------------------------------------------------"""
#this function will extract active time and flow rate fromm the dataframe

def active_Time_flow_rate(flow_with_direction, packet_df):
    row = 0
  
    for key in flow_with_direction:
        forward_flow = flow_with_direction[key]['forward']
        backward_flow = flow_with_direction[key]['backward']     #extract forward and backward flow of packets 

        active_total = 0
        active_time_max = 0
        for i in range(0,len(forward_flow)):    #iterate over each list with step size 1
            time1 = 0
            if "tcp" in forward_flow[i]:
                time1 = float(forward_flow[i].tcp.time_relative)
            elif "udp" in forward_flow[i]:
                time1 = float(forward_flow[i].udp.time_relative)

            active_time_max = (time1) if time1 > active_time_max else active_time_max
            active_total += time1

        for i in range(0,len(backward_flow)):
            time2 = 0
            if "tcp" in backward_flow[i]:
                time2 = float(backward_flow[i].tcp.time_relative)
            elif "udp" in backward_flow[i]:
                time2 = float(backward_flow[i].udp.time_relative)

            active_time_max = (time2) if time2 > active_time_max else active_time_max
            active_total += time2
       
        #active_time_mean is equal to total active time divide by the total number of packets in that flow.
        if (len(forward_flow)+len(backward_flow))>0:
            active_time_mean = active_total/(len(forward_flow)+len(backward_flow)) 

        #insert values in the dataframe at coresponding indexes
        packet_df.iloc[row, packet_df.columns.get_loc(' Active Max')] = active_time_max
        packet_df.iloc[row, packet_df.columns.get_loc('Active Mean')] = active_time_mean

        #calcuate flow rate
        mx_t1 = 0
        mx_t2 = 0

        #extract the time of last packets in forward and backward direction.. 
        if forward_flow:
            if "tcp" in forward_flow[len(forward_flow)-1]:
                mx_t1 = float(forward_flow[len(forward_flow)-1].tcp.time_relative)
            elif "udp" in forward_flow[len(forward_flow)-1]:
                mx_t1 = float(forward_flow[len(forward_flow)-1].udp.time_relative)
        if backward_flow:
            if "tcp" in backward_flow[len(backward_flow)-1]:
                mx_t2 = float(backward_flow[len(backward_flow)-1].tcp.time_relative)
            elif "udp" in backward_flow[len(backward_flow)-1]:
                mx_t2 = float(backward_flow[len(backward_flow)-1].udp.time_relative)

        #insert maximum of above calculates times divided bt total number of packets in the flow in the df ..
        flow_rate = 0
        if(len(forward_flow)+len(backward_flow))>0:
            flow_rate = (mx_t1 if mx_t1>mx_t2 else mx_t2)/(len(forward_flow)+len(backward_flow))
        packet_df.iloc[row,packet_df.columns.get_loc('Flow Bytes/s')] = flow_rate
        row += 1

    return

"""-----------------------------------------------------------------------------------------------------------------"""
#function to calculate bulk flow rate 

def bulk_Flow_rate(flow_with_direction, packet_df):
    row = 0
  
    for key in flow_with_direction:
        forward_flow = flow_with_direction[key]['forward']  #extract forward and backward flow of packets 
            
        Total_payload = 0
        for pkt in forward_flow:
            if "tcp" in pkt:
                Total_payload += float(pkt["tcp"].len)
            elif "udp" in pkt:
                Total_payload += float(pkt['udp'].length)

            if "ip" in pkt:
                Total_payload += float(pkt['ip'].len)
            elif "ipv6" in pkt:
                Total_payload += float(pkt['ipv6'].plen)

        Total_time = 0
        if forward_flow:
            if "tcp" in forward_flow[len(forward_flow)-1]:
                Total_time = float(forward_flow[len(forward_flow)-1].tcp.time_relative)
            elif "udp" in forward_flow[len(forward_flow)-1]:
                Total_time = float(forward_flow[len(forward_flow)-1].udp.time_relative)

        AvgBulkRate = 0
        if Total_time>0:
            AvgBulkRate = Total_payload/Total_time

        packet_df.iloc[row,packet_df.columns.get_loc(' Fwd Avg Bulk Rate')] = AvgBulkRate
        row +=1
    return
        

"""-------------------------------------------------------------------------------------------------------------"""
#Main function to Simulate each function from here !!

def Time_main(flow_with_direction, packet_df):
    sort_TimeStamps(flow_with_direction)
    IAT_MAX_Idle_mean(flow_with_direction, packet_df)
    active_Time_flow_rate(flow_with_direction, packet_df)
    bulk_Flow_rate(flow_with_direction, packet_df)
    return




    
