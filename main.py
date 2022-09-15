from importlib.resources import contents
import os
import cv2 
import librosa

from io import BytesIO
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from src.audio_analysis import AudioAnalysis

app = FastAPI()

@app.post("/Audio Sampling Rate & length/")
async def upload_audio_file(file: UploadFile = File(...)):
    try:
        if file.filename[-3:] in ['mp3', 'wav']:
            contents = file.file.read()
            filepath = f'static/audio/{file.filename}'
            with open(filepath, 'wb') as f:
                f.write(contents)
                
        audio = AudioAnalysis(filepath)
        sr, l = audio.y_sr()
        return {"Sampling rate(Hz)": sr, 'length(sec)': l}
        
    except Exception:
        return {"Message": "There was an error uploading the file. :)"}
    finally:
        file.file.close()
        os.remove(f'static/audio/{file.filename}')
        
        
@app.post("/Audio 2D Graph/")
async def upload_audio_file(file: UploadFile = File(...)):
    try:
        if file.filename[-3:] in ['mp3', 'wav']:
            contents = file.file.read()
            filepath = f'static/audio/{file.filename}'
            with open(filepath, 'wb') as f:
                f.write(contents)
                
        audio = AudioAnalysis(filepath)
        audio.music_2d_graph()
        graph_image = cv2.imread('result/2D_music_graph.jpg')
        _, buf = cv2.imencode('.jpeg', graph_image)
        return StreamingResponse(BytesIO(buf.tobytes()), media_type="image/jpeg")
        
    except Exception:
        return {"Message": "There was an error uploading the file. :)"}
    finally:
        file.file.close()
        os.remove(f'static/audio/{file.filename}')
     
        
@app.post("/Audio Fourier Transform Graph/")
async def upload_audio_file(file: UploadFile = File(...)):
    try:
        if file.filename[-3:] in ['mp3', 'wav']:
            contents = file.file.read()
            filepath = f'static/audio/{file.filename}'
            with open(filepath, 'wb') as f:
                f.write(contents)
                
        audio = AudioAnalysis(filepath)
        audio.fourier_transform_graph()
        graph_image = cv2.imread('result/fourier_transform_graph.jpg')
        _, buf = cv2.imencode('.jpeg', graph_image)
        return StreamingResponse(BytesIO(buf.tobytes()), media_type="image/jpeg")
        
    except Exception:
        return {"Message": "There was an error uploading the file. :)"}
    finally:
        file.file.close()
        os.remove(f'static/audio/{file.filename}')
        

@app.post("/Audio Spectogram Graph/")
async def upload_audio_file(file: UploadFile = File(...)):
    try:
        if file.filename[-3:] in ['mp3', 'wav']:
            contents = file.file.read()
            filepath = f'static/audio/{file.filename}'
            with open(filepath, 'wb') as f:
                f.write(contents)
                
        audio = AudioAnalysis(filepath)
        audio.spectogram_graph()
        graph_image = cv2.imread('result/spectogram_graph.jpg')
        _, buf = cv2.imencode('.jpeg', graph_image)
        return StreamingResponse(BytesIO(buf.tobytes()), media_type="image/jpeg")
        
    except Exception:
        return {"Message": "There was an error uploading the file. :)"}
    finally:
        file.file.close()
        os.remove(f'static/audio/{file.filename}')
        

@app.post("/Audio Mel Spectogram Graph/")
async def upload_audio_file(file: UploadFile = File(...)):
    try:
        if file.filename[-3:] in ['mp3', 'wav']:
            contents = file.file.read()
            filepath = f'static/audio/{file.filename}'
            with open(filepath, 'wb') as f:
                f.write(contents)
                
        audio = AudioAnalysis(filepath)
        audio.mel_spectogram_graph()
        graph_image = cv2.imread('result/mel_spectogram_graph.jpg')
        _, buf = cv2.imencode('.jpeg', graph_image)
        return StreamingResponse(BytesIO(buf.tobytes()), media_type="image/jpeg")
        
    except Exception:
        return {"Message": "There was an error uploading the file. :)"}
    finally:
        file.file.close()
        os.remove(f'static/audio/{file.filename}')
        
        
@app.post("/Audio Harmonic And Percussive Components Graph/")
async def upload_audio_file(file: UploadFile = File(...)):
    try:
        if file.filename[-3:] in ['mp3', 'wav']:
            contents = file.file.read()
            filepath = f'static/audio/{file.filename}'
            with open(filepath, 'wb') as f:
                f.write(contents)
                
        audio = AudioAnalysis(filepath)
        audio.harmonic_and_percussive_components()
        graph_image = cv2.imread('result/harmonic_and_percussive_components.jpg')
        _, buf = cv2.imencode('.jpeg', graph_image)
        return StreamingResponse(BytesIO(buf.tobytes()), media_type="image/jpeg")
        
    except Exception:
        return {"Message": "There was an error uploading the file. :)"}
    finally:
        file.file.close()
        os.remove(f'static/audio/{file.filename}')
   
        
@app.post("/Audio Spectral Centroid Graph/")
async def upload_audio_file(file: UploadFile = File(...)):
    try:
        if file.filename[-3:] in ['mp3', 'wav']:
            contents = file.file.read()
            filepath = f'static/audio/{file.filename}'
            with open(filepath, 'wb') as f:
                f.write(contents)
                
        audio = AudioAnalysis(filepath)
        audio.spectral_centroid_graph()
        graph_image = cv2.imread('result/spectral_centroid_graph.jpg')
        _, buf = cv2.imencode('.jpeg', graph_image)
        return StreamingResponse(BytesIO(buf.tobytes()), media_type="image/jpeg")
        
    except Exception:
        return {"Message": "There was an error uploading the file. :)"}
    finally:
        file.file.close()
        os.remove(f'static/audio/{file.filename}')
        

@app.post("/Audio Spectral Rolloff Graph/")
async def upload_audio_file(file: UploadFile = File(...)):
    try:
        if file.filename[-3:] in ['mp3', 'wav']:
            contents = file.file.read()
            filepath = f'static/audio/{file.filename}'
            with open(filepath, 'wb') as f:
                f.write(contents)
                
        audio = AudioAnalysis(filepath)
        audio.spectral_rolloff_graph()
        graph_image = cv2.imread('result/spectral_rolloff_graph.jpg')
        _, buf = cv2.imencode('.jpeg', graph_image)
        return StreamingResponse(BytesIO(buf.tobytes()), media_type="image/jpeg")
        
    except Exception:
        return {"Message": "There was an error uploading the file. :)"}
    finally:
        file.file.close()
        os.remove(f'static/audio/{file.filename}')
        
        
@app.post("/Audio Mel Frequency Cepstral Coefficients Graph/")
async def upload_audio_file(file: UploadFile = File(...)):
    try:
        if file.filename[-3:] in ['mp3', 'wav']:
            contents = file.file.read()
            filepath = f'static/audio/{file.filename}'
            with open(filepath, 'wb') as f:
                f.write(contents)
                
        audio = AudioAnalysis(filepath)
        audio.mel_frequency_cepstral_coefficients_graph()
        graph_image = cv2.imread('result/mel_frequency_cepstral_coefficients_graph.jpg')
        _, buf = cv2.imencode('.jpeg', graph_image)
        return StreamingResponse(BytesIO(buf.tobytes()), media_type="image/jpeg")
        
    except Exception:
        return {"Message": "There was an error uploading the file. :)"}
    finally:
        file.file.close()
        os.remove(f'static/audio/{file.filename}')
        
        
@app.post("/Audio Chroma Frequencies Graph/")
async def upload_audio_file(file: UploadFile = File(...)):
    try:
        if file.filename[-3:] in ['mp3', 'wav']:
            contents = file.file.read()
            filepath = f'static/audio/{file.filename}'
            with open(filepath, 'wb') as f:
                f.write(contents)
                
        audio = AudioAnalysis(filepath)
        audio.chroma_frequencies_grapy()
        graph_image = cv2.imread('result/chroma_frequencies_graph.jpg')
        _, buf = cv2.imencode('.jpeg', graph_image)
        return StreamingResponse(BytesIO(buf.tobytes()), media_type="image/jpeg")
        
    except Exception:
        return {"Message": "There was an error uploading the file. :)"}
    finally:
        file.file.close()
        os.remove(f'static/audio/{file.filename}')