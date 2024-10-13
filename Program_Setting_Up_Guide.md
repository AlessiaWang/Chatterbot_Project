#### **Notice: <span style="color:red">Read this file</span>** before running the Python scripts `app1.py` and `app2.py` on local computers.

#### Please make sure to read the content in [README](./README.html) before reading the following file.

# Program Setting Up Guide

## 1. File description
This markdown file is written by **Yilan Wang** (Student Number: 12813168), research master of Communication Science (September 2022 - July 2024) at the University of Amsterdam, to enable that the Python library [Chatterbot](https://chatterbot.readthedocs.io/en/stable/index.html) runs successfully on local laptops or personal computers. 

`Chatterbot` is a Python library which was used to develop chatbots that were able to provide users with messages containing the stimulus materials used in the experimental research - **Give An Option, or Give A Solution? The Role of Scepticism and Conversational Agents’ Decisional Guidance in Consumer Decision Making**. 

## 2. Step-by-step guide for Chatterbot installations
This guide is written for the sake of installing the Python library `Chatterbot` for building and training chatbots as well as other libraries/modules on local laptops or personal computers which operate on `Mac OS systems` (version: Mac OS Sonoma 14.4.). Those computers operating on Windows systems will require different codes to realise such a goal.

After having run all the codes written in this file, and having modified the Python scripts on local laptops or computers based on the instructions given in this file, one will be able to download, import, and use the modules in the `Chatterbot` library to run the scripts `app1.py` and `app2.py` which build and train the two chatbots developed for this study and operate these chatbots on local ports.


### 2.1 Check if the environment is ready
Before installing the `Chatterbot` library on local computers, one needs to ensure that certain versions of `Python` and `Git` have already been installed.

#### 2.1.1. Commands to install Python packages

   **`python3 --install`**

   **`pip3 --install`** 


#### 2.1.2. Check the version of Python installed on the computer

```
python3 --version
```

The version should not be older than Python 3.12.3.

#### 2.1.3. Check if the version of pip is the latest one

The `Python Package Index` [PyPI](https://pypi.org/) should have already been installed so that `pip3` can be enabled to run for the sake of installing other Python packages via the command lines in terminal. 

It's necessary to ensure that pip, setuptools, and wheel are all up to date.

```
python3 -m pip install --upgrade pip setuptools wheel
```

An example of the output in the terminal after having executed this command: `Successfully installed setuptools-69.5.1 wheel-0.43.0`

For more detailed instructions on how to use `python3` and `pip`, please read the online tutorial: [How to install Python packages](https://packaging.python.org/en/latest/tutorials/installing-packages/). This tutorial also reveals some equavalents commands which can be used within the Windows systems.

#### 2.1.4. Check the version of Github's git

```
git --version
```

An example of the output in the terminal: `git version 2.39.3 (Apple Git-146)`

### 2.2 Install Chatterbot

#### 2.2.1. Select the appropriate version of Chatterbot to install

According to the issue NO.2305 reported and solved on the [Chatterbot's Github Page of Reporting Issues](https://github.com/gunthercox/ChatterBot/issues/2305), there will be an error that prevents `Chatterbot` from being installed successfuly while the following command `pip3 install chatterbot` is running. 

This is due to the **incompatibility** between the `Chatterbot library` which requires the version of Python to be older than 3.8.0 and the latest updates in the modules of `Python 3.12.3`. 

To avoid raising such an error, it's not a good idea to install an older version of Python on local computers, because there will still be incompatibility issues if the old version of Python does not match with other newly-upgraded Python packages. 

In this case, an available solution is to install `Chatterbot` with specifying its version as **1.0.4**.

```
pip3 install chatterbot==1.0.4
```

Example of the output in the terminal after having successfully installed Chatterbot:
`Successfully installed PyYAML-3.13 chatterbot-1.0.4 chatterbot-corpus-1.2.0 click-8.1.7 joblib-1.4.0 mathparse-0.1.2 nltk-3.8.1 pint-0.23 pymongo-3.13.0 python-dateutil-2.7.5 regex-2024.4.28 sqlalchemy-1.2.19 tqdm-4.66.2 typing-extensions-4.11.0
Note: you may need to restart the kernel to use updated packages.`

#### Relevant sources about Chatterbot:
 - [Chatterbot's documentation](https://chatterbot.readthedocs.io/en/stable/setup.html)
 - [Chatterbot's Github page](https://github.com/gunthercox/ChatterBot/tree/master/chatterbot)

### 2.2.2. Optional: Install Python packages inside a virtual environment

It's possible to install Python libraries in a virtual environment in the path of this folder `Chatbot_Project`.

An example of the commands using a virtual environment:

```
python3 -m venv myvenv
source /myvenv/bin/activate

python3 -m pip install --upgrade pip

```

Now, Python libraries can be installed in the directory `xxx.../Chatbot_Project/myvenv/lib`.

#### Relevant sources about virtual environment: 
[Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)

### 2.3 Install the other Python packages that Chatterbot requires

#### 2.3.1. Install pytz

To successfully import and run Chatterbot without errors, the [pytz library](https://pypi.org/project/pytz/) which allows accurate and cross platform timezone calculations needs to be installed.

```
pip3 install pytz
```

Example of the output in the terminal after having successfully installed pytz: `Successfully installed pytz-2024.1`

#### 2.3.2. Upgrade PyYAML

`.yml` files are used to train chatbots with the corpus data in these files. 

It's necessary to upgrade the [PyYAML library](https://pypi.org/project/PyYAML/) first to ensure that the version of PyYAML installed on a local computer matches with Python 3.12.3: 

```
pip3 install --upgrade PyYaml
```

Example of the output in the terminal after having successfully upgraded PyYAML: `Successfully installed PyYaml-6.0.1`

After this step, there will still be dependency issues between Chatterbot and the current PyYAML packages: `chatterbot-corpus 1.2.0 requires PyYAML<4.0,>=3.12, but the PyYAML has just been upgraded to version 6.0.1.` 

The following section `3. Modify specific scripts in certain Python libraries on local computers` in this file elaborates more on how to solve these dependency issues.

#### 2.3.3. Install Flask

The `Flask` framework [Flask 3.0](https://flask.palletsprojects.com/en/3.0.x/) is needed to build and run the applications of a chatbot. With Flask, users are able to interact with the chatbot through accessing its html front-end on web browsers.

```
pip3 install Flask
```

Example of the output in the terminal after having successfully installed Flask: `Successfully installed Flask-3.0.3 Werkzeug-3.0.2 blinker-1.8.1 itsdangerous-2.2.0`


#### Relevant sources about how to use Flask:
- [Using Flask to build a chatbot (in Chinese)](https://learnku.com/python/t/38853)
- [Github project: Candice-YourPersonalChatBot](https://github.com/sahil-rajput/Candice-YourPersonalChatBot/blob/master/templates/home.html)
- [A flask app for Chatterbot](https://github.com/chamkank/flask-chatterbot/blob/master/templates/index.html#L20-L23)

## 3. Modify specific scripts in certain Python libraries on local computers
This section is written to solve the incompatibility issues that the researcher encountered during the procedure of developing the two chatbots used in this study. These issues have been explained together with the researcher's solutions. 

<span style="color:red">**Notice:**</span> **There's no need to manually modify the Python scripts** in the Python libraries installed on local computers based on the instructions given in the section `5. Optional information: How to manually modify certain Python scripts`. Just replace them with the modified Python scripts stored in the folder [myscripts](./myscripts).

### 3.1 How to replace the Python scripts

#### 3.1.1. Replace constructor.py in PyYAML

- Find the following Python script `constructor.py` in the user directory (path of the folder in which the `PyYAML` packages are installed) on the local computer.

- An example of the path of this file: `File /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-pac kages/yaml/constructor.py`

- Open the folder [myscripts](./myscripts) in the folder "Chatbot_Project" in which this guide is located, find the modified version of the file `constructor.py`, and replace the original file with this modified file.

#### 3.1.2. Replace corpus.py in Chatterbot

- Find the following Python script `corpus.py` in the library of `chatterbot` in the user directory.

- An example of the path of this file: `/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-pac kages/chatterbot/corpus.py`

- Open the folder [myscripts](./myscripts) in the folder "Chatbot_Project" in which this guide is located, find the modified version of the file `corpus.py`, and replace the original file with this modified file.

#### 3.1.3. Replace app.py in Flask

- Find the following Python script `app.py` in `Flask` in the user directory.

- An example of the path of this file: `/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/flask/sansio/app.py`

Open the folder [myscripts](./myscripts) in the folder "Chatbot_Project" in which this guide is located, find the modified version of the file `app.py`, and replace the original file with this modified file.

## 4. Language data that were used to train the chatbots in this study

### 4.1 Everyday conversations in English
Some conversations selected from the book [Everyday Conversations: Learning American English](https://americanenglish.state.gov/files/ae/resource_files/b_dialogues_everyday_conversations_english_lo_0.pdf) were added to the .yml files in the folder [Corpus](./Corpus).

### 4.2 Short jokes in English
English jokes published on the following websites were added to the .yml files in the folder [Corpus](./Corpus) for the sake of enabling the chatbots to chat in a more natural manner. 
- [Short Jokes in English 1](https://parade.com/1287449/marynliles/short-jokes/)
- [Short Jokes in English 2](https://www.rd.com/list/short-jokes/)

However, because the researcher needed to have sufficient control in the experiment, participants were not exposed to any of those conversations or jokes during their participation.

————————————————————————————————————————————————————————————————

## 5. Optional information: How to manually modify certain Python scripts

<span style="color:red">**Notice:**</span> Please immediately save the modified Python scripts without making a copy of them and restart the kernel once the adjustments on the following scripts are made.

### 5.1 Modify constructor.py in PyYAML

**Issue:**

The module `collections` has no attribute `Hashable` when the version of Python ≥ 3.0. 

**Solution:** 

Use `collections.abc` to call the attribute `Hashable`.

- First, find the Python script `constructor.py` in the user directory (path of the folder in which the PyYAML package is installed). 

- An example of the path of this file: `File /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-pac kages/yaml/constructor.py`

- Then, open the script, and find the following line of codes: `in BaseConstructor.construct_mapping(self, node, deep)`

- Find the following line `if not isinstance(key, collections.Hashable):`, 
    - change `collections.Hashable` to `collections.abc.Hashable`, and save the file

Source: https://stackoverflow.com/questions/71618317/importing-tronweb-shows-import-error-cannot-import-name-hashable-from-collec 

### 5.2 Modify corpus.py in Chatterbot

**Issue:**

The method `yaml.load(file)` raises errors. 

As indicated in the section `2.3.2 Upgrade PyYAML`, PyYAML versions ≥ 6.0 are required for successfully using Chatterbot. However, these versions of PyYAML are neither compatible with the newer versions of Python (i.e., Python 3.12.3) nor the older versions of the Chatterbot library (i.e., Chatterbot 1.0.4). 

It's therefore necessary to make adjustments on certain scripts stored in the Chatterbot library. 

**Solution:** 

The new PyYAML versions ≥ 5.1 require positional argument: `'Loader' for the method yaml.load(input)`. This method should be modified to `yaml.load(input, Loader=yaml.FullLoader)`.

- Find the Python script `corpus.py` in the Chatterbot library in the user directory. 

- An example of the path of this file: `/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-pac kages/chatterbot/corpus.py`

- Find the following line: `in read_corpus(file_name)`,
    - change the method `return yaml.load(data_file)` to `yaml.load(data_file, Loader=yaml.FullLoader)` or `yaml.safe_load(data_file)`, and save the file

Source: https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation 

### 5.3 Modify app.py in Flask

**Issue:**

After having run the chatbot on a local port (i.e., 3000) for once, this port becomes unavailable for running the chatbot on it again.

**Solution:** 

To be able to run multiple Flask apps at the same time and to use the same ports repeatedly, one has to avoid raising the `AssertionError()` statement. This can be achieved through removing certain codes from the Python script `app.py` in the Flask package. 

If this step is not completed, it will be impossible to reuse the functions written for running a Flask App which were executed once in the past. And this issue can be very annoying: Whenever the researcher runs the Python scripts `app1.py` and `app2.py`, a new name has to be given to the functions such as `home1()`, `home2()`, `get_bot_response1()`, `get_bot_response2()`, etc.

- Find the Python script `app.py` in the Flask package in the user directory.

- An example of the path of this file: `/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/flask/sansio/app.py)`:

- Find the line (i.e., line No.657) which contains the codes `old_func = self.view_functions.get(endpoint)`, and remove the following codes:

```
(​​if old_func is not None and old_func != view_func:
                raise AssertionError(
                    "View function mapping is overwriting an existing"
                    f" endpoint function: {endpoint}"
              )
```

Source: https://github.com/megvii-research/CADDM/issues/36

              
Finally, restart the kernel after all the scripts have been modified and saved.
