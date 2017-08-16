import requests
import json
import base64
import wave
from pydub import AudioSegment 
import io

class BaiduRest:
    def __init__(self, cu_id, api_key, api_secert):
        self.token_url = "https://openapi.baidu.com/oauth/2.0/token"
        self.getvoice_url = "http://tsn.baidu.com/text2audio"
        self.upvoice_url = 'http://vop.baidu.com/server_api'
        self.cu_id = cu_id
        self.getToken(api_key, api_secert)
        return

    def getToken(self, api_key, api_secert):
        data={'grant_type':'client_credentials','client_id':api_key,'client_secret':api_secert}
        r=requests.post(self.token_url,data=data)
        Token=json.loads(r.text)
        self.token_str = Token['access_token']


    def getVoice(self, text, filename):
        data={'tex':text,'lan':'zh','cuid':self.cu_id,'ctp':1,'tok':self.token_str}
        r=requests.post(self.getvoice_url,data=data,stream=True)
        voice_fp = open(filename,'wb')
        voice_fp.write(r.raw.read())
        # for chunk in r.iter_content(chunk_size=1024):
            # voice_fp.write(chunk)
        voice_fp.close()


    def getText(self, filename):
        data = {"format":"wav","rate":16000, "channel":1,"token":self.token_str,"cuid":self.cu_id,"lan":"zh"}
        wav_fp = open(filename,'rb')
        voice_data = wav_fp.read()
        data['len'] = len(voice_data)
        data['speech'] = base64.b64encode(voice_data).decode('utf-8')
        post_data = json.dumps(data)
        r=requests.post(self.upvoice_url,data=bytes(post_data,encoding="utf-8"))
        return r.text

    def ConvertToWav(self,filename,wavfilename):
        fp=open("out.mp3",'rb')
        data=fp.read()
        fp.close()
        aud=io.BytesIO(data)
        format='mp3'.encode('utf-8')
        sound=AudioSegment.from_file(aud,format.decode('utf-8'))
        raw_data = sound._data
        l=len(raw_data)
        f=wave.open(wavfilename,'wb')
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(16000)
        f.setnframes(l)
        f.writeframes(raw_data)
        f.close()
        return wavfilename

if __name__ == "__main__":
    api_key = "Dle3ghve9A5rdKBp3o2SsCSFA0hBgUY1" 
    api_secert = "Op6NXcFcj7Hu0xlwAe3HuMsyyPVhko2o"
    bdr = BaiduRest("test_python", api_key, api_secert)
    bdr.getVoice(u'问题,作为开发人员,你的职责是什么,答按照工作进度和编程工作规范编写系统中的关键模块,设计编写详细设计,配合测试员修改相应的程序,提供软件的后期技术支持,进行编码实现,代码走查,单元测试,产品交付,', "out.mp3")
    print(bdr.getText(bdr.ConvertToWav("out.mp3","test.wav")))