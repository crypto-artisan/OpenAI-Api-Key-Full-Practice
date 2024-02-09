from langchain_openai.llms import OpenAI
import dotenv
dotenv.load_dotenv()
# Before executing the following code, make sure to have
# your OpenAI key saved in the “OPENAI_API_KEY” environment variable.
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)
text = "Suggest a personalized workout routine for someone looking to improve cardiovascular endurance and prefers outdoor activities."
print(llm(text))
##################################image generation#####################################
# import openai
# from packaging import version

# required_version = version.parse("1.1.1")
# current_version = version.parse(openai.__version__)

# if current_version < required_version:
#     raise ValueError(f"Error: OpenAI version {openai.__version__}"
#                      " is less than the required version 1.1.1")
# else:
#     print("OpenAI version is compatible.")

# # -- Now we can get to it
# from openai import OpenAI
# client = OpenAI(api_key="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")  # should use env variable OPENAI_API_KEY
# response = client.images.generate(
#   model="dall-e-2",
#   prompt="a white siamese cat",
#   size="1024x1024",
#   quality="standard",
#   n=1,
# )

# image_url = response.data[0].url
# print(image_url)
#################################text-to-speech generation#####################################
# from pathlib import Path
# from openai import OpenAI
# client = OpenAI(api_key="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")

# speech_file_path = Path(__file__).parent / "speech.mp3"
# response = client.audio.speech.create(
#   model="tts-1",
#   voice="alloy",
#   input="Happy new year!"
# )

# response.stream_to_file(speech_file_path)

#################################speech-to-text generation#####################################
# from openai import OpenAI
# client = OpenAI(api_key="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")

# audio_file= open("./speech.mp3", "rb")
# transcript = client.audio.transcriptions.create(
#   model="whisper-1", 
#   file=audio_file
# )
# print(transcript)
#################################??????????vision#####################################
# from openai import OpenAI

# client = OpenAI(api_key="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")

# system_prompt = "You are an expert analyzing images."
# response = client.chat.completions.create(
#     model="gpt-4-vision-preview",
#     messages=[
#         {
#             "role": "system",
#             "content": [
#                 {"type": "text", "text": system_prompt},
#             ],
#         },
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url":"https://testimages-s3bucket.s3.amazonaws.com/testimage.png",
#                     }
#                 },
#             ],
#         },
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": "What do you see in this photo?"},
#             ],
#         }
#     ],
#     max_tokens=1000,
# )

# print(response.choices[0])

#################################moderation#####################################

# from openai import OpenAI
# client = OpenAI(api_key="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")

# response = client.moderations.create(input="Sample text goes here.")

# output = response.results[0]

# print(output)