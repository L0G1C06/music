import os
from pydub import AudioSegment

# Defina a pasta onde estão os arquivos .wav
input_folder = "./albums/original"
output_folder = "./albums/convertedMP3"  # Salvar na mesma pasta
album_name = input("Digite o nome do album: ")
# Percorre todos os arquivos da pasta
for index, filename in enumerate(os.listdir(input_folder)):
    if filename.endswith(".wav"):  # Filtra apenas os arquivos .wav
        new_filename = f"{album_name}_{index + 1}.mp3"
        src = os.path.join(input_folder, filename)
        dst = os.path.join(output_folder, new_filename)
        
        # Converte wav para mp3
        sound = AudioSegment.from_wav(src)
        sound.export(dst, format="mp3")
        
        print(f"Convertido: {filename} -> {new_filename}")

print("Conversão concluída!")
