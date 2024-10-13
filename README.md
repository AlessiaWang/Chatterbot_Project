### Please <span style="color:red"> read this file </span> before opening or running the Python files in this folder.

# Chatbot_Project
This folder contains files and codes that were used for developing and training the two chatbots which exposed participants in the online experiment of this study to certain predetermined stimulus materials.

## Project description

All the files in this folder were created/edited by **Yilan Wang** (Student Number: 12813168), research master of Communication Science (September 2022 - July 2024) at the University of Amsterdam, for the master thesis - **Give An Option, or Give A Solution? The Role of Scepticism and Conversational Agents’ Decisional Guidance in Consumer Decision Making**. 

The thesis investigated how different types of **decisional guidance** (informative vs. suggestive) provided in a chatbot's output messages containing brief descriptions about certain products and services, together with the level of **consumer scepticism** (low vs. high) towards chatbots as a general concept, affected consumer's **purchase intention** towards those products and services, in the context of leisure consumption. Additionally, the research studied the mediation role of consumer's attitude towards the content about those products and services in the relationship between decisional guidance and purchase intention. 

### Explanation of key terms
- **Decisional guidance**: a kind of system that provides relevant information to assist the consumer's decision making process.
- **Informative guidance**: providing the content about some products/services without making recommendations on which purchase decision consumers should make (i.e., what products/services they should buy).
- **Suggestive guidance**: providing the content including explicit recommendations on which purchase decision consumers should make.
- **Consumer scepticism**: consumer's degree of distrust towards chatbots on the whole, regardless of the diversity in chatbots' classifications and usages.
- **Purchase intention**: consumer's willingness to buy certain products or services.
- **Attitude towards the content**: consumer's attitude towards the content of the output messages in which certain products and services are briefly described.

### Experimental conditions
Two experimental conditions - (1) informative guidance and (2) suggestive guidance, were implemented in the online experiment of the research. The Python library [Chatterbot](https://chatterbot.readthedocs.io/en/stable/index.html) was used to build and train chatbots that could return fixed, predetermined responses to certain user inputs. The experimental manipulation was therefore enabled: participants were able to be exposed to certain stimulus materials while performing the same task, a.k.a., asking the chatbots the same question. After running the codes in the Python scripts [app1.py](./app1.py) and [app2.py](./app2.py), two chatbots, `Alex01` and `Alex02`, were built and trained separately. 

- 1. In the condition of informative guidance, when the participant typed "Find me cafés in Amsterdam" in the chatbot's message box, the chatbot would respond "I found some information about the cafés in Amsterdam" followed by the picture: ![Stimuli](https://github.com/AlessiaWang/myimage/blob/main/stimuli.png?raw=true)

- 2. In the condition of suggestive guidance, when the participant typed "Find me cafés in Amsterdam" in the chatbot's message box, the chatbot would respond "I’d love to recommend you to try the following cafés in Amsterdam" followed by the picture: ![Stimuli](https://github.com/AlessiaWang/myimage/blob/main/stimuli.png?raw=true)

Other materials and codes that were used for training both chatbots were precisely the same. 

Due to the properties of `Chatterbot`, the chatbots used in this study were unable to learn from their conversation with users. Hence, participants' privacy was protected, and there were no differences in each chatbot's responses to a certain question given by participants in the same experimental condition. While across the two conditions, the chatbot's responses only varied in their answers to the question "Find me cafés in Amsterdam".

- For more details about the development and training of the chatbots in this study, please read the section `Building and training the chatbots on local computers` below.
- For more details about the deployment of the chatbots in this study, please read the section `Deploying the chatbots online` below.
- For more details about the hypotheses, methods, and results of this research, please read the Word document [2024_SEM2_YilanWang_ZephMCvanBerlo_MasterThesis.docx].

## Structure of this folder and the files

- [app1.py](./app1.py)
- [app2.py](./app2.py)
- [Chatbot01.py](./Chatbot01.py)
- [Chatbot02.py](./Chatbot02.py)
- [Corpus](./Corpus)
  - [botprofile.yml](./Corpus/botprofile.yml)
  - [computers.yml](./Corpus/computers.yml)
  - [conversations.yml](./Corpus/conversations.yml)
  - [food.yml](./Corpus/food.yml)
  - [gossip.yml](./Corpus/gossip.yml)
  - [greetings.yml](./Corpus/greetings.yml)
  - [health.yml](./Corpus/health.yml)
  - [humor.yml](./Corpus/humor.yml)
  - [money.yml](./Corpus/money.yml)
  - [psychology.yml](./Corpus/psychology.yml)
  - [science.yml](./Corpus/science.yml)
  - [sports.yml](./Corpus/sports.yml)
- [Instructions_to_Use_the_Chatbot.docx](./Instructions_to_Use_the_Chatbot.docx)
- [LICENSE.txt](./LICENSE.txt)
- [myscripts](./myscripts)
  - [app.py](./myscripts/app.py)
  - [constructor.py](./myscripts/constructor.py)
  - [corpus.py](./myscripts/corpus.py)
- [Program_Setting_Up_Guide.html](./Program_Setting_Up_Guide.html)
- [Program_Setting_Up_Guide.md](./Program_Setting_Up_Guide.md)
- [README.html](./README.html)
- [README.md](./README.md)
- [stimuli](./stimuli)
  - [stimuli.png](./stimuli/stimuli.png)
  - [stimuli_condition_1.png](./stimuli/stimuli_condition_1.png)
  - [stimuli_condition_2.png](./stimuli/stimuli_condition_2.png)
- [templates](./templates)
  - [chatbot_icon.png](./templates/chatbot_icon.png)
  - [home01.html](./templates/home01.html)
  - [home02.html](./templates/home02.html)


## How to read and use the files in this folder

The content and usage of all the files in this folder are explained in the following section.

### 1. Requirements for the Hardwares, Softwares, and Environment to build and train chatbots on your local laptop/PC 

All the files in this folder have been written to be compatible with computers which use the **MacOS system** (`macOS Sonoma Version 14.4`) as the default operating system and the `Apple M3 Pro chip` for executing instructions of computer programs. The version of Python used for running all the scripts in this folder is **Python 3.12.3**. There will be variations in terminal commands as well as the versions of Python libraries and modules that are required to be installed in advance while running the scripts in this folder on those computers which only use the Windows systems instead of the MacOS systems.

Please make sure that you have downloaded and installed [Python (the latest version 3.12.4)](https://www.python.org/downloads/release/python-3124/) on your local computer (or in a virtual environment).

After having installed Python, please open the terminal window on your computer to run the following commands:

- Check Python and pip version: 

```
!python3 --version
```

```
python3 -m pip --version
```

- Install pip:

```
python3 -m ensurepip
```

- Upgrade pip:

```
pip3 install --upgrade pip
```


### 2. Setting up the Python libraries and installing necessary packages

First of all, please make sure that you carefully read the content and run the codes written in the Python file [**Program_Setting_Up_Guide.md**](./Program_Setting_Up_Guide.md). This file can help you with the installation of the [Chatterbot](https://github.com/gunthercox/ChatterBot) library as well as the [Flask](https://flask.palletsprojects.com/en/3.0.x/) framework and make sure that no incompatibility issues will occur between different Python libraries, modules, and packages while you are attempting to run the Python script [app1.py](./app1.py) or [app2.py](./app2.py). 

The three `.py` Python scripts saved in the folder [myscripts](./myscripts) were written to solve the errors the researcher has encountered during the chatbot training procedure. These errors were raised due to the incompatibility issues between old and new Python modules. You need to replace the scripts that share the same name with those modified Python scripts in the installed Python libraries on your computer. For the step-by-step instruction on how to replace the scripts, please read the file [Program_Setting_Up_Guide.md](./Program_Setting_Up_Guide.md).

### 3. Randomly assigning participants at the level of couples

While conducting true experiments, researchers must randomly assign each participant to one of the experimental conditions. In this study, the researcher ensured random assignment at the level of couples of individuals - the Qualtrics survey evenly presents the two experimental conditions among participants. 

Every two participants in this study were paired into one group. In each group, the first participant  was randomly assigned to one of the two experimental conditions, while the second participant was automatically assigned to the other experimental condition.

### 4. Building, training, and running chatbots on local computers

The Python scripts [Chatbot01.py](./Chatbot01.py) (used in experimental condition 1, informative guidance) and [Chatbot02.py](./Chatbot02.py) (used in experimental condition 2, suggestive guidance) contain the codes that are used to train the two chatbots. The codes in both scripts only differ in the predetermined text responses to the user input **"Find me cafés in Amsterdam"**. 

To build, train, and run the two chatbots on your local computer, you only need to run the Python scripts [app1.py](./app1.py) and [app2.py](./app2.py) directly inside your terminal window. While running these two scripts, your computer will automatically run the codes in the scripts [Chatbot01.py](./Chatbot01.py) and [Chatbot02.py](./Chatbot02.py).

The `.yml` files saved in the folder [Corpus](./Corpus) contain the language data used for training the chatbots. These language data were manually adapted by the researcher from the online open-access resources [the original English corpus for Chatterbot](https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/english).

The two `.html` files in the folder [templates](./templates), [home01.html](./templates/home01.html) and [home02.html](./templates/home02.html) are the templates used for building an html Front-End of the two chatbots on the local ports on your computer. The codes in these two html files only differ in the title of the two web pages - one is named as "Alex01" (used for the condition of informative guidance) while the other is named as "Alex02" (used for the condition of suggestive guidance). Therefore, the two chatbots can be accessed simultaneously via your browsers, and you will be able to distinguish which front end belongs to which chatbot through checking the page titles. 

The image [chatbot_icon.png](./templates/chatbot_icon.png) in the same folder is used to create an "appearance" for the chatbots so that participants will better recognise and understand the fact that they are chatting with a chatbot.

The visual stimulus material [stimuli.png](./stimuli.png) used in this study locates in the  folder [stimuli](./stimuli). Such a folder also contains two screenshots of the conversation between the two chatbots and their users, [stimuli_condition_1.png](./stimuli_condition_1.png) and [stimuli_condition_2.png](./stimuli_condition_2.png), which explain how the stimuli has been presented to the participants in each experimental condition.

The file [requirements.txt](./requirements.txt) was written to ask the cloud server to install certain required Python packages before starting the operation of the Flask applications.

### 5. SQLite files which store the generate data during the procedure of training and running of the chatbots

After the Python script [app1.py](./app1.py) has been run, the chatbot Alex01 will be able to chat with users through its html front-end (page title: [Alex01](./templates/home01.html)). During the procedure of training and running this chatbot, three SQLite databases will be created and stored in this folder. 
- The database `database1.db` stores the language data that were used to train the chatbot [Alex01](./templates/home01.html), which includes the data adapted from the [Chatterbot's English corpus data](https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/english) and some predetermined list data (See the codes in [Chatbot01.py](./Chatbot01.py)).
- The databases `database1.db-shm` and `database1.db-wal` temporarily store the language data in the messages that the chatbot receives from a user in their conversation. Data in these two databases will be automatically cleaned whenever the chatbot is shut down and restarted.
- To enable experimental control, the researcher also needs to manually delete the file `database1.db` whenever the terminal  restarts or the chatbot is trained again.

The same thing will happen after running the script [app2.py](./app2.py): the SQLite files `database2.db`, `database2.db-shm`, and `database2.db-wal` will be created in this folder.

### 6. Deploying and running the chatbots online

In order to conduct an online experiment, it is necessary to ensure that the participants are able to access the two chatbots used in this experiment from anywhere via links on any devices that are connected to the Internet. This required that:

- 1. Both chatbots need to be running on certain ports of a remote web server;
- 2. The public IP address of the remote server and the predetermined ports are accessible to external IP addresses;
- 3. The public IP address of the remote server is accessible through visiting a certain domain.

**(1) Purchase a remote server:**
First, a cloud server needs to be purchased. This can be done via any cloud computing services such as [Amazon Web Services](https://aws.amazon.com/), [Google Cloud](https://cloud.google.com/), [Heroku](https://www.heroku.com/). The researcher in this study bought a Tencent Cloud Server [Tencent Cloud Server](https://cloud.tencent.com/) which is located in Frankfurt. This server uses CentOS 7.6 64bit as the operating system and Docker as the server's template, because docker images need to be created for running the chatbots. After purchasing the server, its public IP address can be found in the server's information page. However, at this point, this IP address has not been linked to a public domain, nor can it be accessed by users from any external IP address.

**(2) Set up the server:**
The next step is to purchase a Cloud Drive and mount it on the cloud server. This Drive will be used to expand the space of the cloud server's storage and to read and write data of your cloud applications. Such a step can be directly completed via the Cloud computing services' platforms.

After the mounting process is done, a public domain name needs to be bought to link the domain to the Cloud server's public IP address. Thus, participants in this experiment do not have to access the chatbots via IP addresses - those online chatbot applications in real life are always accessed via domains. In this study, the researcher bought a domain from [DNSPOD](https://www.dnspod.cn/):
- Go to "**Record Management**" of the domain.
- Enter the public IP address of the cloud server in "**Record Value**".
- Select "A" for "**Record Type**".
- Select "@" and "www" for "**Host**".
- Confirm to save the changes.

Now, the public IP address is mapped to this domain.

Add two user-defined rules to the settings of the firewall of the Cloud server from dashboard:
- **Source**: 0.0.0.0/0
  - This setting allows the cloud server to listen on any available external IP addresses so that it will allow access from any users through visiting certain ports of the domain.
- **Protocol**: TCP
- **Policy**: Allow
- **Port**: Enter the ports on which your chatbot will be accessed by users. The ports used in this experiment were 3000 and 3004.

**(3) Upload files to the Cloud server and deploy the chatbots**

The chatbots in this experiment ran through `Flask applications`. Hence, it is necessary to first upload all the Python scripts used to build, train, and run these chatbots onto the Cloud server. Then, it's needed to build Docker images on the server, create containers inside those images, and run the Flask applications of the two chatbots separately inside the two containers.

First, log into `the root directory` of the Cloud server via `SSH key` in the local terminal window. Execute the following command at the command line:

```
ssh root@Enter.public.IP.address
```

Then, enter the login password of the SSH, and press the "Enter" key.

After successfully logging in, create two new folders in the root directory of the Cloud server, for example:

```
mkdir chatbot-app-1
mkdir chatbot-app-2
```

Next, upload all the files in this folder on your local computer to the folders `chatbot-app-1` (for deploying the first chatbot) and `chatbot-app-2` (for deploying the second chatbot) on the Cloud server.

Create a file named Dockerfile respectively in the folders `chatbot-app-1` and `chatbot-app-2`:

```
nano Dockerfile
```

The next step is very critical. As it is stated in the file [**Program_Setting_Up_Guide.md**](./Program_Setting_Up_Guide.md), there are cases where different versions of Python packages are not compatible with each other, which can cause errors when running the Flask Apps. The same issues can happen on the cloud server. Therefore, it is necessary to modify and replace certain Python scripts to avoid conflicts through writing certain commands in the Dockerfiles in advance of building the Docker images and running the containers.

Take the codes written by the researcher in the `Dockerfile` in the folder of `chatbot-app-1` as an example:

```
FROM python:3.12.3-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader punkt_tab
COPY myscripts/constructor.py /usr/local/lib/python3.12/site-packages/yaml/constructor.py
COPY myscripts/app.py /usr/local/lib/python3.12/site-packages/flask/sansio/app.py
EXPOSE 3004
CMD ["python", "app1.py"]
```
Once these steps are done, save and exit the Dockerfile, and go back to the directory of `chatbot-app-1`. Run the following command to build the image `app-1-image`:

```
docker build -t app-1-image .

```
Create the container `app1-container` in the Docker image `app-1-image`:

```
docker run -d -p 3004:3004 --name app1-container app-1-image
```

Run the container `app1-container` and check the logs:

```
docker logs app1-container
```

At this point, the Flask application of the first chatbot would have already started running on the Cloud server if no errors had occurred during the procedure. This chatbot will continue to run until the container is stopped or deleted, even if the researcher has logged out from the Cloud server and closed the terminal window on the local computer.

The operation to build, train, and run the second chatbot on the Cloud server works under the same principle, thus it will not be repeated here.


### 7. Running the online experiment

- The Qualtrics survey used in this study was published, and the link of the [survey](https://uva.fra1.qualtrics.com/jfe/form/SV_6Gr5MCu6tyOGldI) was pasted to the online experiment project in the Behavioural Science Lab's system: https://www.lab.uva.nl/lab/recruitment/.

- The research project was published onto the lab's page of "Ongoing Studies" to allow online participation: https://www.lab.uva.nl/lab/onderzoek/overzicht?language=eng

- The participants were rewarded with either 2 euros or 0.5 research credit through the lab's system. Participants who preferred to receive the monetary reward were asked to contact the researcher by sending an email in which their student email addresses linked with their student accounts were indicated. These emails were not recorded for analytical usage, and were destroyed as soon as the data collection was finished.
 
- The researcher determined whether the data collection process should terminate or not.

### 7. Providing instructions to participants

After having answered the questions about their age and gender identity in the Qualtrics survey, every participant was exposed to one of the two textual instructions on the next page of the survey. The instructions in the two experimental conditions could be found in the file [Instructions_to_Use_the_Chatbot.docx](./Instructions_to_Use_the_Chatbot.docx). 

The instructions briefly described how to access one of the chatbots, how to interact with the chatbot (i.e., sending and receiving messages via the chatbot's html front-end), questions which could be used to test the chatbot, the scenario that participants were facing in this study, and what they should ask the chatbot in order to receive the chatbot messages containing the stimulus materials.

### 8. Licence for use
This project has been licensed under GNU General Public License v3.0. For more details about the Licence, please check the file [LICENSE](./LICENSE) in the same folder.

## Reference list 
This listed all the online resources for developing the chatbots in this study.

[Build a Chatbot using Flask in 5 minutes](https://dev.to/sahilrajput/build-a-chatbot-using-flask-in-5-minutes-574i)

[Build your first ChatBot in 5 minutes](https://dev.to/sahilrajput/build-your-first-chatbot-in-5-minutes--15e3) 

[Candice-YourPersonalChatBot](https://github.com/sahil-rajput/Candice-YourPersonalChatBot)

[Can i train multiple answers to the same question ? #1587](https://github.com/gunthercox/ChatterBot/issues/1587)

[Chatterbot Installation Doc](https://chatterbot.readthedocs.io/en/stable/setup.html)

[Chatterbot on Github](https://github.com/gunthercox/ChatterBot/tree/master/chatterbot)

[Create a chatbot based on Chatterbot (in Chinese)](https://blog.51cto.com/u_10487107/4881132)

[Creating multiple bots on same server instance without sharing training data #1232](https://github.com/gunthercox/ChatterBot/issues/1232) 
[Datasets for Natural Language Processing](https://github.com/karthikncode/nlp-datasets) 

[How to train an Chatbot with Custom Datasets](https://medium.com/@shaikhrayyan123/how-to-train-an-chatbot-with-custom-datasets-107ce09f4326)
['pip install chatterbot' error #2305](https://github.com/gunthercox/ChatterBot/issues/2305)

[python chatterbot call function instead of providing a text response back](https://stackoverflow.com/questions/73421480/python-chatterbot-call-function-instead-of-providing-a-text-response-back)

[Random responses to same question #234](https://github.com/gunthercox/ChatterBot/issues/234) 

[Use Chatterbot to create chatbots (in Chinese)](https://www.biaodianfu.com/chatterbot.html)
