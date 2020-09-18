from flask import Flask, redirect
from flask_restful import Api
import nltk

nltk.download('punkt')

from resources.methods import TemSentenceTokenizer

from resources.methods import FrequencyDistribution
from resources.methods import TemSentenceTokenizer, PosTagging
from resources.mariam_kvantaliani.methods import GroupingMultiplePatters
from resources.chunk_CleanSentences import Chunk_CleanSentences
from resources.methods import SentenceTokenizer
from resources.frequencyReturner import FrequencyReturner
from resources.methods import sentTok
from resources.methods import SentTokenizer
from resources.methods import DepTreeSvgMaker

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return redirect('https://github.com/temurchichua/DemoApi')


api.add_resource(TemSentenceTokenizer, '/TemSenTok')
api.add_resource(FrequencyDistribution, '/FreqDist')
api.add_resource(SentTokenizer, '/SentTokenizer')
api.add_resource(GroupingMultiplePatters, '/GMultiplePatterns')
api.add_resource(Chunk_CleanSentences, '/Chunk')
api.add_resource(SentenceTokenizer, '/sentence')
api.add_resource(FrequencyReturner, '/FreqReturner')
api.add_resource(sentTok, '/SentTok')
api.add_resource(PosTagging, '/PosTag')
api.add_resource(DepTreeSvgMaker,"/DepTree")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
