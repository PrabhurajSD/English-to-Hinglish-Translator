import openai
from Secret_Key import openai_key


openai.api_key = openai_key

def translate(text):
    prompt = get_prompt_Description() + text

    # Request translation from English to Hinglish using chat-based completions
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Choose the appropriate chat model
        messages=[
            {"role": "system", "content": prompt},

        ]
    )

    # Extract and print the Hinglish translation from the response
    hinglish_translation = response['choices'][0]['message']['content'].strip()
    return hinglish_translation

def get_prompt_Description():
    return '''  I want you to translate English sentences into  Hinglish but in a particular format which is mentioned below.

Format :
I want the translated sentence as a combination of Hindi Devanagari Script as well as English Script. This means  
If the word in the translated sentence belongs to the Hindi language then it should be written in the Hindi Warnamala 
Devanagari script and if it belongs to the English language then it should be written using the English Alphabetical script. 
Take reference from below 30 examples below to ready yourself for accurate translation in the required format. Also maintain the integrity 
and reading/speaking flueny of sentence after translation


Examples:
English: "I am going to the park."
Hinglish Translation : "मैं  park जा रहा हूँ।"
English: "She is reading a book."
            Hinglish Translation :  "वह एक book पढ़ रही है।"
English: "Can you please pass me the water?"
Hinglish Translation:  "क्या आप please मुझे  water दे सकते हैं?"
English: "They are watching a cricket match."
Hinglish Translation:  "वे एक cricket match देख रहे हैं।"
English: "My favorite color is blue."
Hinglish Translation: "मेरा favourite color blue है।"
English: "What time does the movie start?"
Hinglish Translation:  "movie कब शुरू होती है?"
English: "I like to eat pizza."
Hinglish Translation: "मुझे pizza खाना पसंद है।"
English: "She is a talented singer."
Hinglish Translation:  "वह एक talented singer है।"
English: "The weather is beautiful today."
Hinglish Translation :  "आज का  weather बहुत  beautiful है।"
English: "Let's go for a long drive."
Hinglish Translation:  "चलो long drive पे चलते हैं।"
English: "I can't find my keys."
Hinglish Translation : "मैं अपनी keys नहीं ढूँढ़ पा रहा हूँ।"
English: "They are playing cricket in the park."
Hinglish translation:  "वे park में cricket खेल रहे हैं।"
English: "She loves to dance."
Hinglish Translation:  "उसको dance करने का बहुत शौक है।"
English: "I need to buy some groceries."
Hinglish Translation: "मुझे कुछ groceries का  सामान खरीदना है।
English: "The traffic is terrible during rush hour."
Hinglish Translation:  "traffic office hour में बहुत खराब होता है।"
English: "I'm excited about the upcoming concert."
Hinglish Translation:  "मैं आने वाले concert के बारे में exicted हूँ।"
English: "Her new dress looks beautiful on her."
Hinglish Translation:  "उसकी नई dress उस पर बहुत सुंदर लग रही है।"
English: "Could you please help me find my glasses?"
Hinglish Translation: "क्या आप please मेरी glasses ढूँढ़ने में help कर सकते हैं?"
English: "I enjoy listening to classical music."
Hinglish Translation : "मैं classical music सुनने का आनंद लेता हूँ।"
English: "The sunset at the beach was breathtaking."
Hinglish Translation : "Beach  पे sunset देखकर तो सांस रुक गई।"
English:"The scientific community is excited about the breakthrough discovery."
Hinglish Translation :"Scientific community breakthrough discovery के लिए excited है।"
English: "She is pursuing a Ph.D. in neuroscience"
            Hinglish Translation :  "वह neuroscience में Ph.D कर रही है।"
English: "The historical artifacts in the museum are priceless"
Hinglish Translation:  "museum में ऐतिहासिक artifacts अनमोल हैं।"
English: "The government has announced a new economic policy."
Hinglish Translation:  "सरकार ने एक नई economic policy की announcement की है।"
English: "The chef prepared a gourmet meal for the special occasion."
Hinglish Translation:  "Chef ने  special occasion के लिए एक gourmet meal  तैयार किया।"
English: "The negotiations between the two countries are ongoing."
Hinglish Translation:  "दोनों countries के बीच negotiations अभी भी जारी है।"
English: "The art exhibition featured avant-garde pieces from around the world."
Hinglish Translation: "Art  exhibition में दुनिया भर से avant-grade कलाकृतियाँ featured की गईं।"
English:"The conference attracted renowned scholars and experts."
Hinglish Translation:"Conferene  में renowned scholars और experts attract हुए।"
English: "The legal proceedings in the courtroom were intense."
Hinglish Translation : "Coutroom में कानूनी प्रक्रिया intense थी।"
English:"The documentary sheds light on pressing social issues."
Hinglish Translation: "Doumentary  संवेदनशील social मुद्दों पर रोशनी डालती है।"



Please go through the above examples carefully because I want translation in the above format only.
Now translate the following sentence:


    '''
if __name__ == '__main__':
    english_text = " Definitely share your feedback in the comment section"
    df = translate(english_text)
    print("Hinglish Translation:", df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
