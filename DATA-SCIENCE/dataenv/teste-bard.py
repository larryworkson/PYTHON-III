from bardapi import Bard
import os
os.environ['_BARD_API_KEY']="eQgc-4afBExf65kzgzjPN-oF60l_K1BnbpBtQsxBl7nhJiJZt6yZHLR-bU6K1L90MCvoWQ."
input_text = 'Qual melhor LLM do mercado?'
bard_output = Bard().get_answer(input_text)['content']
print(bard_output)

# python teste-bard.py