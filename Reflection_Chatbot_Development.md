
# Reflections on Chatbot Development

## Document Description
This file is about my personal reflections on the limitations of the chatbots that I built and trained for my experiment as well as the design of my experiment.

### 1. Perceived functionality: My Chatbots are NOT smart enough

Almost all the participants reflected that the chatbots were not very smart after the experiment ended. It was mainly because the researcher aimed to gurantee enough experimental control during the experimental procedure. Therefore, the two chatbots used in the experiment were not able to memorise and learn from their conversation with any participants that participated in this research, since the conversation was immediately deleted from the chatbots' databases whenever an experiment session was over. 

That's to say, even if the participants disclose their personal information (i.e., their names) to the chatbots during the experiment, these chatbots are not able to recall this information even when they're still in conversation with the same participants. 

Such a setting guranteed that the privacy of every participant was protected, but it also resulted in the fact that the chatbot functioned in a less "smart" way: the chatbots were not able to deeply understand what the participant was talking about. Consequently, responses that did not match the participant's expections over the chatbots' functionality were given. 

Nonetheless, my chatbots did not use `Logic Adapters`. Logic Adapters could help in determining the logic for how a chatbot selects the responses to a given user input so that the responses of my chatbot would seem to be more logical. Principally, the [best match adapter](https://chatterbot.readthedocs.io/en/latest/logic/index.html#best-match-adapter) should have been applied while building my chatbots. There should also be a default response (i.e., 'Sorry, I couldn't understand this') in the situation where all the responses stored in the chatbots' databases had a relatively low match score (i.e., less than 0.6) with the user input. 

However, it was not realistic to achieve this goal in my study:

- First, to be able to use Logic Adapters, I have to have some large databases which contain plenty of responses (from list data, Corpus data, and user's conversation). With a small database of responses, it is super difficult to find any response that can match a random user input with a high score.
  
  - However, in my study, I could only use a very small dataset in order to ensure control over the responses. And I wanted the chatbot to be 'professional' - it should be precise in providing answers. Therefore, I narrowed down the topics the chatbots could talk about a bit. I removed the Corpus data which allowed the chatbot to express emotions so that it would not elicit positive or negative emotions of the participants.

- Second, (Chatterbot)[https://github.com/gunthercox/ChatterBot], which I used for building and training my chatbots, is a relatively old Python library. Now the original codes that the developer of this library provided in the documentation cannot work very well, which was also the reason why I had to fix the codes in some scripts in its library. I have tried to add the Logic Adapters to my chatbot, only found that as a research master student in the field of Communication Science I had very limited time and knowledge to figure out how to achieve my goals without invoking errors.

### 2. Emotional feelings: My chatbots may raise emotional appeals by accident

Another problem that I encountered during the experimental procedure was that, the chatbots sometimes replied "weird" sentences to the participants. After the experiment, one of the participants reported that the chatbot the person chatted with suddenly called the person "a bad parent" even if I had removed the emotional expressions from my data used to train the chatbots. In my chatbot-training-and-testing process, I had also encountered similar cases. 

I have not yet figured out how to solve the problem yet. Maybe this problem was also related to the lack of use of the Logic Adapters. My chatbots are indeed selecting responses based on comparing the similiarity between the user input and the recorded input in the pre-determined list and corpus data, but without logic adapters we will never know how it makes a decision on providing a certain response instead of others. Maybe the chatbots just decide to provide a response that is used the most frequently in its database.

This problem could affect user's emotional feelings about the chatbot which they interacted with during the experiment. They may tend to like a chatbot more if it suddenly tells an interesting joke, and they may tend to dislike a chatbot if it says something that is somehow not logical and even a bit offensive. Thus, together with the perceived functionality ('smartness') of the chatbot, emotional feelings may cause that the participants have a higher degree of trust or distrust in the chatbot and its messages. This could in turn have confounded the effect of consumer scepticism on purchase intention in my study. 

### 3. My chatbots could not only learn from responses but also the user's inputs

This is also a major limitation of my chatbots. These chatbots learnt everything that were written in the list data and corpus data used to train them, including the pontential user inputs that are used to be compared with the actual user inputs in terms of similarity. 

For example:
- In my Corpus data, I set that: when a user asked "What is your name?" (user input), the chatbots will answer "My name is Alex" (chatbot response). But this means that the chatbots doe not only record "My name is Alex" but also "What is your name?" in their lists of responses. So, sometimes the chatbots will suddenly ask "What is your name?" during a conversation, and they are actually giving a response from its list of responses.
- Then the problem occurs:
  - In my list data, I set that: when a user asked "Find me cafés in Amsterdam", the chatbots will provide some specific, pre-determined responses. But this also means that the chatbots may suddenly ask the participants to "Find me cafés in Amsterdam". Although in my brief user's guide (How_to_chat_with_the_Chatbot.docx)[./How_to_chat_with_the_Chatbot.docx], I already told the participants, if the chatbots asked them something that you did not know how to answer or did not want to answer, they could just reply "I don't know" or throw the question back to the chatbots. But this problem still could have resulted in a lower degree of the perceived functionality of the chatbots, which could have confounded the effect of consumer scepticism on purchase intention.
 
Unfortuantely, I haven't found a solution to this problem.

### 4. My failures

In summary, I have met the following failures before and during my experiment process.

- 1) I didn't enable the chatbots to learn during their conversation with the participants.

Even though the conversation data was immediately deleted after the experiment ended, I should still have enabled the chatbots learn from chatting BEFORE every conversation ended. Therefore, the conversation will be more logical, natural, and accurate.
     
- 2) I didn't narrow down the topics to a larger extent.
    
To ensure the precision of the chatbot responses, I should furtherly limit the topics that my chatbot could talk about to merely chatbot profiles, daily conversations, and consumption-related topics. This will make my chatbots to be more like the professional chatbots that are used in real life conditions.

- 3) I didn't let the chatbot only learn from the pre-determined chatbot responses but not the potential user inputs. This is sometimes annoying because it may interrput the conversation between the chatbots and the users.
     
- 4) I didn't measure the participants' liking of the chatbots they chatted with, which is a limitation of my research design.
    
- 5) I didn't measure the participants' perceived functionality of the chatbots they chatted with, which is a limitation of my research design too. 
