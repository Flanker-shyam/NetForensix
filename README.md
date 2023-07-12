# Network_Intrusion_detection_system
A smart Network Intrusion detection tool to perform forensics on your network to discover various network attacks like Brute Force FTP, Brute Force SSH, DoS, Web Attack, Botnet, DDoS, etc, by analysing the flow behaviour of the network. This project is using CICIDS2017 dataset form kaggle.
This Project is still under develpment and an UI needs to be build!!

Feel free to contribute.

Project Flow Chart:
![diagram drawio](https://github.com/Flanker-shyam/Network-Intrusion-detection-system/assets/85950516/842c3670-cf43-4aa1-9701-868639c75504)


**What this tool is about**
1. You can generate a csv file that will contain various flow based features extracted from the entered file.
2. You can perform the forensic on the file to find the Intrusions and get the file in output.

**How to setup:**
1. Create a fork of this repo and clone into your local environment
2. Create a new branch
3. Install all dependencies by following command:
```bash
pip install -r requirements.txt
```
4. Open deploy_model.ipynb file in ML_model folder and run each cell one by one. This will do a minor preprocessing,
    train, test your model and save it into a file using joblib that it will use later.
5. All done !!

**How to use**
```bash
python src/main.py <options> <file>
```
1. After above given setup you can interact with the tool
2. Use follwing command to see all the options and how to use:
```bash
python src/main.py --help
```
3. To generate flow file use the follwing command:
```bash
python src/main.py -f --pcap <file_path>
```
4. To generate result of detected intrusions use the following command:
```bash
python src/main.py -r --pcap <file_path>
```

You will see the result on your cli and a file will be generated based on the chosen option.
