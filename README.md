# Translation App

A machine learning application that translates text between several languages. 

## Installation

### 1. Install Streamlit

**For Windows**
- Install Anaconda. See Anaconda's [installation page](https://docs.anaconda.com/free/anaconda/install/windows/).
- Click on "Environments" from the left side menu.
- Select the "▶" icon that appears in the base(root) environment (or create a new environment). Then select "Open terminal".
- In the terminal that appears, type: 


    pip3 install streamlit

**For macOS/Linux**

- You'll need Python version 3.6 or above. 
- Install pip. See pip [documentation](https://pip.pypa.io/en/stable/installation/#supported-methods).



**For macOS**

    python3 -m ensurepip --upgrade

**For Ubuntu with Python 3**

    sudo apt-get install python3-pip


- **For macOS** also install Xcode command line tools


    xcode-select --install


- Install Streamlit 


    pip3 install streamlit


Read more on Streamlit [documentation](https://docs.streamlit.io/library/get-started/installation).

### 2. Install requirements 

- In the terminal (or Anaconda's terminal for Windows, step 1) navigate to the project's folder

- Inside the folder, you'll find the requirements.txt file. Type:

    
    pip3 install -r requirements.txt


- Then type 


    streamlit run translator-ui.py

- And the translation app will show up in your browser.

