import os
from openai import OpenAI
import sys
from tqdm import tqdm

# @author: Danilo Basanta
# @author-linkedin: https://www.linkedin.com/in/danilobasanta/
# @author-github: https://github.com/dabasanta

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def translate_text(text, target_language="es"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"Translate the following text to {target_language}.",
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        model="gpt-4o-mini",
    )
    translation = chat_completion.choices[0].message.content.strip()
    return translation

def count_subtitles(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file if line.strip().isdigit())

def translate_srt(file_path, target_language="es"):
    total_subtitles = count_subtitles(file_path)
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    output_file_path = file_path.replace('.srt', f'_translated_{target_language}.srt')
    
    with open(output_file_path, 'w') as output_file, tqdm(total=total_subtitles, desc="Translating", unit="subtitle") as pbar:
        text_to_translate = ""
        subtitle_block = []
        subtitle_number = 0

        for line in lines:
            if line.strip().isdigit():
                if subtitle_block:
                    subtitle_number += 1
                    timestamp = subtitle_block[1].strip()
                    translated_text = translate_text(text_to_translate, target_language)
                    output_file.writelines(subtitle_block[:-1])
                    output_file.write(translated_text + '\n')
                    output_file.write('\n')
                    output_file.flush()
                    pbar.update(1)
                subtitle_block = [line]
                text_to_translate = ""
            elif '-->' in line:
                subtitle_block.append(line)
            elif line.strip():
                text_to_translate += line.strip() + " "
            else:
                subtitle_block.append(line)
        
        if subtitle_block:
            subtitle_number += 1
            timestamp = subtitle_block[1].strip()
            translated_text = translate_text(text_to_translate, target_language)
            output_file.writelines(subtitle_block[:-1])
            output_file.write(translated_text + '\n')
            output_file.write('\n')
            output_file.flush()
            pbar.update(1)
    
    print(f'Translation completed. Output file: {output_file_path}')

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python translate_srt.py <path_to_srt_file> [<target_language>]")
    else:
        file_path = sys.argv[1]
        target_language = sys.argv[2] if len(sys.argv) == 3 else "es"
        translate_srt(file_path, target_language)

