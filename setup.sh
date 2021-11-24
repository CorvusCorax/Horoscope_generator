pip3 install -r requirements.txt
git clone https://github.com/huggingface/transformers.git
cd transformers/ && git checkout v2.2.0 && pip install -r requirements.txt && pip install .
cd ..
wget https://github.com/dsnam/markovscope/raw/master/data/horoscopes.csv
source prepare_data.sh
