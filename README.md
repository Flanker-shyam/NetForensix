# Network_Intrusion_detection_system
A smart Network Intrusion detection tool to perform forensics on your network to discover various network attacks like Brute Force FTP, Brute Force SSH, DoS, Web Attack, Botnet, DDoS, etc, by analysing the flow behaviour of the network. This project is using CICIDS2017 dataset form kaggle.
This Project is still under develpment and an UI needs to be build!!

Feel free to contribute.

Project Flow Chart:
![chart drawio](https://github.com/Flanker-shyam/Network-Intrusion-detection-system/assets/85950516/d170900c-10d4-4fbb-8891-f8d8aca6fb06)


How to use setup:
1. Create a fork of this repo and clone into your local environment
2. Create a new branch
3. Install all dependencies by following command:
```bash
pip install -r requirements.txt

```
4. Open deploy_model.ipynb file in ML_model folder and run each cell one by one. This will do a minor preprocessing
   train, test your model and save it into a file using joblib that we will use later.
5. All done !!
6. Now simply run main.py by following command
 ```bash
 python src/main.py
 ```
7. You can also add your own test pcap file in main.py
8. Your output will be saved in a file named ansDF.csv (for now you can visualize your output by opening this file)
   (UI under development)---- Will finish it soon !!
