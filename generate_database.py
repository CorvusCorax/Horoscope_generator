import torch
#from utils import sample_sequence
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from run_generation import sample_sequence
import datetime
import strtotime
import re

zodiacs=['Aquarius','Aries','Cancer','Capricorn','Gemini','Leo','Libra','Pisces','Sagittarius','Scorpio','Taurus','Virgo']

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_class, tokenizer_class = (GPT2LMHeadModel, GPT2Tokenizer)
tokenizer = tokenizer_class.from_pretrained('output')
model = model_class.from_pretrained('output')
model.to(device)
model.eval()

def generateHoro(raw_text):
  context_tokens = tokenizer.encode(raw_text, add_special_tokens=False)
  out = sample_sequence(
      model=model,
      context=context_tokens,
      num_samples=10,
      length=150,
      device=device)
  out = out[:, len(context_tokens):].tolist()
  text = [ raw_text + tokenizer.decode(x, clean_up_tokenization_spaces=True) for x in out ]
  text = [ x.replace('\n', '').replace('\xa0', '') for x in text ]
  return text

def main():
  i=0
  for day in range(366):
      for zodiac in zodiacs:
          d=strtotime.strtodatetime('Jan 1 2020 + '+str(day)+' day')
          s=d.strftime('%B %d')
          text=zodiac+'. '+s+'.'
          res=generateHoro(text)
          for line in res:
              line=re.sub(r'  *',' ',line)
              line=re.sub(r'.[^.]*$','.',line)
              line=re.sub(r'"','\'',line)
              line=str(i)+'|'+d.strftime('%m')+'|'+d.strftime('%d')+'|'+zodiac+'|"'+line+'"'
              print(line)
              i+=1
              
  
if __name__ == '__main__':
  main()
