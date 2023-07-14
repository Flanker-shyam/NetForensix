**Contributing to Network Intrusion Detection Tool**

Thank you for considering contributing to the Network Intrusion Detection Tool! We welcome your contributions and appreciate your support in enhancing the tool's capabilities.

**a. How to Contribute**

To contribute to this project, please follow these steps:

1. Fork the repository and clone it to your local environment.
2. Create a new branch for your contributions.
3. Install all dependencies by running the following command:
```bash
pip install -r requirements.txt
```
4. Open the deploy_model.ipynb file in the ML_model folder and execute each cell sequentially. This notebook performs preprocessing, trains, and tests the model, saving it using joblib for later use.
You're all set!

**b. Project Flow Chart**
![diagram drawio](https://github.com/Flanker-shyam/Network-Intrusion-detection-system/assets/85950516/e9f23634-c888-484f-ab45-4e0ac183aa56)

**c. How to Use the Tool**

To interact with the tool, follow these steps:
1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Use the following command to see all available options and usage instructions:
For help:
```bash
python src/main.py --help
```
To generate a flow file containing extracted flow-based features from a specific file, use the following command:
```bash
python src/main.py -f --pcap <file_path>
```
To generate the results of detected intrusions based on the flow file, use the following command:
```bash
python src/main.py -r --pcap <file_path>
```
This will display the results on the command line and generate a file based on the chosen option.

**d. Submitting Changes**

When you're ready to submit your changes, please follow these steps:
1. Commit your changes to your branch.
2. Push your branch to your forked repository.
3. Open a pull request (PR) against the main repository.
4. Provide a clear and descriptive title and description for your PR, explaining the purpose and details of your contribution.
   
**Code of Conduct**

We expect all contributors to adhere to the Code of Conduct to ensure a respectful and inclusive community environment.

Thank you again for your interest in contributing to the Network Intrusion Detection Tool. We appreciate your time and efforts, and we look forward to your contributions!

For any further assistance or questions, please reach out to the project maintainers.

Happy contributing!
