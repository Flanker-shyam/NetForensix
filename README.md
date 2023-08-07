<h1>NetForensix: Smart Network Intrusion Detection Tool</h1>

<b>NetForensix</b> is a powerful and intelligent network intrusion detection tool designed to bolster your network's security by identifying various network attacks. By analyzing network flow behavior, this tool can detect and provide insights into attacks such as Brute Force FTP, Brute Force SSH, DoS, Web Attacks, Botnets, DDoS, and more. Leveraging the CICIDS2017 dataset from Kaggle, NetForensix offers a robust solution for network forensics and intrusion detection.

Feel free to contribute.

<ul><li><h3>Project Flow Chart</h3></li></ul>

For a visual representation of NetForensix's architecture and operation, please refer to the 
![diagram drawio](https://github.com/Flanker-shyam/Network-Intrusion-detection-system/assets/85950516/842c3670-cf43-4aa1-9701-868639c75504)

<ul><li><h3>Features:</h3></li></ul>
Advanced Intrusion Detection: Utilize machine learning techniques to uncover and report a wide range of network attacks.
Flow-based Analysis: NetForensix focuses on analyzing the flow behavior of network traffic, providing a deeper understanding of potential threats.
Effortless Setup: Follow the simple setup steps outlined in the How to Setup section to get NetForensix up and running quickly.
Automated Reporting: Generate detailed CSV files containing flow-based features extracted from input data files.
Forensic Analysis: Conduct forensic analysis on input files to identify and categorize network intrusions, and retrieve the output files.
User-friendly CLI: Interact with NetForensix using a command-line interface, making it accessible to both beginners and experts.

<ul><li><h3>How to setup:</h3></li></ul>

1. Create a fork of this repo and clone into your local environment
2. Create a new branch
3. Install all dependencies by following command:
```bash
pip install -r requirements.txt
```
4. Open deploy_model.ipynb file in ML_model folder and run each cell one by one. This will do a minor preprocessing,
    train, test your model and save it into a file using joblib that it will use later.
5. All done !!

<ul><li><h3>How to use:</h3></li></ul>

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

<ul><li><h3>How to Contribute:</h3></li></ul>

We welcome contributions from the community to enhance NetForensix's capabilities. Follow these steps to contribute:

Fork the repositor
Create a new branch for your feature or improvement.
Commit your changes and push to your branch.
Open a pull request to merge your changes.

<ul><li><h3>License:</h3></li></ul>
NetForensix is open-source software licensed under the MIT License.

<ul><li><h3>Contact:</h3></li></ul>
For questions, feedback, or collaborations, please feel free to reach out:
<div>Developer: <a href="https://in.linkedin.com/in/shyam-sunder19">Flanker</a></div>

<ul><li><h3>Acknowledgements:</h3></li></ul>
NetForensix appreciates the following resources:
<ul>
<li>CICIDS2017 Dataset</li>
<li>Joblib</li>
<li>pyshark</li>
<li>Pandas</li>
<li>Scikit-Learn</li>
</ul>

<em>Protect your network with NetForensix: Your Smart Network Intrusion Detection Tool. 🛡️🌐</em>

