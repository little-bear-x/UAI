# ai/__init__.py

import ollama
import toml

class Ai:
    messages_list = []
    models_list = []
    client = None
    def __init__(self):
        ollama_config = toml.load("ollama.toml")
        self.client = ollama.Client(
            host=ollama_config['server']['host'] + ':' + str(ollama_config['server']['port']),
        )
        
        self.get_model_list()

    def get_model_list(self):
        models = self.client.list()
        self.models_list = [model.model for model in models.models]
        return self.models_list

    def chat_text_stream(self, prompt: str, model: str):
        """
        使用文字流式生成结果, 通过迭代器返回文字
        prompt: 提示词
        model: 使用模型. 将会校验是否在可用模型内.
        """
        if model not in self.models_list:
            raise 'Model "' + model + '" not found'
        # add history
        self.messages_list.append({'role': 'user', 'content': prompt})
        response = self.client.chat(
            model=model,
            messages=self.messages_list,
            stream=True,
        )

        result = ""
        for chunk in response:
            result += chunk['message']['content']
            yield chunk['message']['content']
        
        self.messages_list.append({'role': 'assistant', 'content': result})
        yield ''
