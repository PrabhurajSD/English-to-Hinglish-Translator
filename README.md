# English-to-Hinglish-Translator
Steps to Run the Model:
  1) Obtain your OpenAI API key and store it securely.
  2) Create a file named "Secret_Key.py" and store your API key as follows:
     python code:
     openai_key = "your-api-key-here"
  3) copy the code of translator.py in any Python compiler (e.g. - Jupyter Notebook, pyCharm, etc)
  4) Run the code

Evaluating Model Performance:

Evaluating the performance of a language translation model like the one using OpenAI's GPT-3.5 Turbo can be challenging 
since it's a pre-trained model that generates responses based on a vast amount of data. However, you can assess its performance in the following ways:
1) Manually review the translated sentences. Ensure that the translation sounds natural, maintains the meaning, and retains the original sentence's tone.
2) Compare the model's translations with your own knowledge of both languages (English and Hindi). Note any inaccuracies or instances where the translation
   deviates from the intended meaning.
3) Assess the fluency and coherence of the Hinglish sentences. Ensure that the translation flows well and is easy to understand for bilingual speakers.
4) Check if the script differentiation (Hindi in the Devanagari script and English in the English script) is correctly applied.
5) Gather feedback from users or stakeholders who are fluent in both languages to assess how well the translations meet their expectations.



Key Features:

1) Bilingual Script Preservation: The project maintains the integrity of the source text by accurately identifying and differentiating between English and Hindi words. 
It ensures that English words are written in the English script and Hindi words are presented in the Hindi Devanagari script.
2) Language Fusion: The translation seamlessly combines the two languages, creating a fluid Hinglish output that is easy to read and understand for speakers of both Hindi and English.
3) Language Fluency: The translated sentences are designed to sound natural and fluent in the Hinglish language, ensuring that the final output retains the original sentence's meaning and readability.
4) Chat-Based Model: The project leverages the OpenAI GPT-3.5 Turbo model for chat-based completions, making it capable of handling various translation requests and providing fast and accurate responses.
5) System Prompt: The translation process begins with a system prompt that sets the format expectations for the translation, ensuring consistency in the output.

Usage:

The project can be used for translating English sentences into Hinglish while maintaining script differentiation. It is versatile and can be applied in various contexts,
including content localization, communication with bilingual audiences, and more.

Examples:

Input: "I am going to the park."

Output: "मैं park जा रहा हूँ।"

Input: "She is reading a book."

Output: "वह एक book पढ़ रही है।"

Input: "Definitely share your feedback in the comment section."

Output: "Definitely comment section में अपनी feedback share करें।"

Input: "The scientific community is excited about the breakthrough discovery."

Output: "Scientific community breakthrough discovery के लिए excited है।"

Input: "The traffic is terrible during rush hour."

Output: "traffic office hour में बहुत खराब होता है।"

Input: "The art exhibition featured avant-garde pieces from around the world."

Output: "Art exhibition में दुनिया भर से avant-grade कलाकृतियाँ featured की गईं।"

Project Extension:
The project can be extended to support translation between other language pairs with script differentiation, offering a versatile solution for various linguistic needs. Additionally,
it can be integrated into applications, websites, or chatbots to provide real-time translation services to users.
