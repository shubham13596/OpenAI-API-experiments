import openai
import gradio

openai.api_key = "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"

messages = [{"role":"system", "content": "You are a Danish langauge tutor"}]

def CustomChatGPT():
    messages.append({"role":"user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant", "content": ChatGPT_reply})
    return ChatGPT_reply    
    
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Danish Language Tutor")

demo.launch(share = True)