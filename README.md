### <span style="color:red">Please read this file</span> before opening the Jupyter Notebook files in this folder and running the codes there.

# Chatterbot_Project
This repository stores all the files that are used to build and train chatbots for my master's thesis.

## Project Description

All the files in this folder are created/edited by **Yilan Wang** (Student Number: 12813168), a student in the research master's programme of Communication Science (September 2022 - July 2024) at University of Amsterdam, for her master's thesis - **Give An Option, or Give A Solution? The Role of Scepticism and Conversational Agents’ Decisional Guidance in Consumer Decision Making**. 

The thesis investigated how different types of **decisional guidance** (Informative vs. Suggestive) in a chatbot's output messages and the level of **consumer scepticism** would influence a consumer's **purchase intention** of the products or services mentioned in the output. 

### Explanation of the terms
- **Informative guidance**: only giving information about some products/services that are asked by the consumers without making suggestions on what products/services they should purchase.
- **Suggestive guidance**: making explicit suggestions on which purchase decision consumers should make (i.e., what products/services they should purchase).
- **Consumer scepticism**: a consumer's distrust in a chatbot and its messages.
- **Purchase intention**: a consumer's willingness to buy certain products or services.

### Experimental conditions
Two experimental conditions - 1. informative guidance and 2. suggestive guidance, are manipulated in this study. To enable manipulation, the Python library [Chatterbot](https://chatterbot.readthedocs.io/en/stable/index.html) is used to build real chatbots that can provide certain messages as the stimulus materials during experiment. Two chatbots - Alex01 and Alex02, are trained through running the codes in [Chatbot01.ipynb](./Chatbot01.ipynb) and [Chatbot02.ipynb](./Chatbot02.ipynb).

In the condition of informative guidance, when the participant type in "Find me cafés in Amsterdam" in the chatbot's input area, the chatbot will respond "I found some information about the cafés in Amsterdam" followed by the picture: ![Stimuli](https://github.com/AlessiaWang/myimage/blob/main/stimuli.png?raw=true)

In the condition of suggestive guidance, when the participant type in "Find me cafés in Amsterdam" in the chatbot's input area, the chatbot will respond "I’d love to recommend you to try the following cafés in Amsterdam" followed by the picture: ![Stimuli](https://github.com/AlessiaWang/myimage/blob/main/stimuli.png?raw=true)

The other codes for training both chatbots are precisely the same. 

For more details about the experimental conditions, please read the section `Building and training your own chatbots` below. For more details about the research, please read the Word document [Master Thesis.docx].

## Files in this folder 

- Corpus
  - botprofile.yml
  - computers.yml
  - conversations.yml
  - food.yml
  - gossip.yml
  - greetings.yml
  - health.yml
  - humor.yml
  - money.yml
  - psychology.yml
  - science.yml
  - sports.yml
- myscripts
  - app.py
  - constructor.py
  - corpus.py
- templates
  - chatbot_icon.png
  - home01.html
  - home02.html
- Chatbot01.ipynb
- Chatbot02.ipynb
- Program_Setting_Up_Guide.ipynb
- Random_Number_Generator.ipynb
- README.md

## How to read and use these files

In this section, the content and usage of all the files in this folder are explained.

### 1. Requirements for Hardware, Software, and Environment 

All the files in this folder are written to fit with computers that are using the **Mac system** (`macOS Sonoma Version 14.4`) as their operation system and the `Apple M3 Pro chip` in executing instructions of computer programs. The Python version that I used for running all the codes here is **3.12.3**. For those computers that operate on the Windows system, there will be some variations in the versions of Python and Jupyter Notebook as well as the format of codes.

Please make sure that you have downloaded and installed [Python (the latest version 3.12.4)](https://www.python.org/downloads/release/python-3124/) and [Jupyter Lab](https://jupyter.org/install) on your computer.

If you have already installed Python on your laptop or personal computer, open the terminal on your computer to run the following commands.

Check Python and pip version: 

```
!python3 --version
```
```
python3 -m pip --version
```

Install pip:

```
python3 -m ensurepip
```

Upgrade pip:

```
pip3 install --upgrade pip
```

Install Jupyter lab:

```
pip3 install jupyterlab
```

Open Jupyter lab:

```
jupyter lab
```

### 2. Setting up the Python libraries and packages

After successfully installed Python, pip, and Jupyter Lab, you can open all the files in the Jupyter lab environment.

First of all, make sure that you read the content and run the codes in the Jupyter Notebook file [**Program_Setting_Up_Guide.ipynb**](./Program_Setting_Up_Guide.ipynb). This file is written to install the Chatterbot library as well as the flask framework and make sure that there will not be incompatibability issues between different libraries or packages when you attempt to run the codes in [Chatbot01.ipynb](./Chatbot01.ipynb) or [Chatbot02.ipynb](./Chatbot02.ipynb). 

The three `.py` Python scripts in the folder 'myscripts' are written to solve some program errors the research has encountered during the chatbot training procedure. You can replace the files that have the same name on your laptop with these edited scripts. For step-by-step instructions, please read the file [Program_Setting_Up_Guide.ipynb](./Program_Setting_Up_Guide.ipynb).

### 3. Randomly assigning participants to different conditions

To conduct true experiments, researchers must randomly assign each participants to certain experimental conditions. In this study, the researcher used the following file [Random_Number_Generator.ipynb](./Random_Number_Generator.ipynb) to ensure random assignments.

You do not need to run these codes unless you want to generate a new list of random numbers.

### 4. Building and training your own chatbots

The Jupyter notebook file [Chatbot01.ipynb](./Chatbot01.ipynb) and [Chatbot02.ipynb](./Chatbot02.ipynb) contain all the codes that you need to create and train your personal chatbots. 

[Chatbot01.ipynb](./Chatbot01.ipynb) is used in experimental condition 1, informative guidance; while [Chatbot02.ipynb](./Chatbot02.ipynb) is used in experimental condition 2, suggestive guidance.

The codes in both files only differ in the pre-determined text response to the user input **'Find me cafés in Amsterdam'**. 

The `.yml` files in the folder 'Corpus' are the corpus data that are used to train the personal chatbots. They are manually adapted by the research **Yilan Wang** based on [the original English corpus for Chatterbot](https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/english).

The two `.html` files in the folder 'templates', [home01.html](./templates/home01.html) and [home02.html](./templates/home02.html) are the templates that are used for building the web Front-End of your personal chatbots on your local port. The codes of these two files only differ in the page title - one is called 'Alex01' (informative guidance) and the other is called 'Alex02' (suggestive guidance). Therefore, the researcher will not confuse the two chatbots.

The image [chatbot_icon.png](./templates/chatbot_icon.png) in the same folder is used to create an 'appearance' for the chatbot so that participants can better understand that they are chatting with a bot.

### 5. Database after you trained your chatbots

After you run the codes in the file [Chatbot01.ipynb](./Chatbot01.ipynb), you will be able to chat with the chatbot Alex (html page title: Alex01). During this procedure three new databases will be created in this folder. 
- The file `database1.db` stores the English corpus data and the list data that you used to train the chatbot before you have interacted with it.
- The files `database1.db-shm` and `database1.db-wal` save the data which contains the messages that the chatbot receives while you are interacting with it.
- Every time when you restart the Kernel, `database1.db-shm` and `database1.db-wal` will be automatically deleted. To control the experiment, the researcher also needs to manually delete the file `database1.db` whenever Jupyter Lab restarts or the chatbot is trained again.

The same thing applies to the codes in the file [Chatbot02.ipynb](./Chatbot02.ipynb): After you run the codes in this file, `database2.db`, `database2.db-shm`, and `database2.db-wal` will appear in the folder.

### 6. Running the experiment

- Open the link of the Qualtrics questionnaire on a computer in the lab.
  - Refresh the web page if the computer has not been operated for a long time.
- Answer the first question of the questionnaire that indicates which experimental condition the participant is assigned to before she/he/they enters the room. Then, go to the next page of the questionnaire that displays the information letter and the informed consent.
- Place the printed version of [How_to_chat_with_the_Chatbot.docx](./How_to_chat_with_the_Chatbot.docx) on the computer desk.
- If the chatbot which is going to be used during the specific experiment session has already been trained, refresh the web page of the chatbot's Front End so that previous conversations will be removed.
- If the chatbot is not trained yet, run the codes in [Chatbot01.ipynb](./Chatbot01.ipynb) or [Chatbot02.ipynb](./Chatbot02.ipynb) to train the chatbot, and then open the Front End.
- Let the participant enter the room, explain the whole procedure of the experiment, ask the participant to sign the informed consent on paper, and then start the experiment.
- Wait outside of the room until the participant finishes/quits the study.
- Thank the participants for their participation and ask them whether they'd like to receive research credits or money reward. (Optional) Ask the participants how they feel about their experience.

### 7. Providing instructions to your participants

During the experiment, participants are able to read [How_to_chat_with_the_Chatbot.docx](./How_to_chat_with_the_Chatbot.docx) on a piece of paper at their right hand side. It gives some brief instructions to help them understand how to interact with the chatbots.

## References list
[Build a Chatbot using Flask in 5 minutes](https://dev.to/sahilrajput/build-a-chatbot-using-flask-in-5-minutes-574i)

[Build your first ChatBot in 5 minutes](https://dev.to/sahilrajput/build-your-first-chatbot-in-5-minutes--15e3) 

[Candice-YourPersonalChatBot](https://github.com/sahil-rajput/Candice-YourPersonalChatBot)

[Can i train multiple answers to the same question ? #1587](https://github.com/gunthercox/ChatterBot/issues/1587)

[Chatterbot Installation Doc](https://chatterbot.readthedocs.io/en/stable/setup.html)

[Chatterbot on Github](https://github.com/gunthercox/ChatterBot/tree/master/chatterbot)

[Create a chatbot based on Chatterbot (Chinese)](https://blog.51cto.com/u_10487107/4881132)

[Creating multiple bots on same server instance without sharing training data #1232](https://github.com/gunthercox/ChatterBot/issues/1232) 
[Datasets for Natural Language Processing](https://github.com/karthikncode/nlp-datasets) 

[How to train an Chatbot with Custom Datasets](https://medium.com/@shaikhrayyan123/how-to-train-an-chatbot-with-custom-datasets-107ce09f4326)
['pip install chatterbot' error #2305](https://github.com/gunthercox/ChatterBot/issues/2305)

[python chatterbot call function instead of providing a text response back](https://stackoverflow.com/questions/73421480/python-chatterbot-call-function-instead-of-providing-a-text-response-back)

[Random responses to same question #234](https://github.com/gunthercox/ChatterBot/issues/234) 

[Use Chatterbot to create chatbots (Chinese)](https://www.biaodianfu.com/chatterbot.html)
