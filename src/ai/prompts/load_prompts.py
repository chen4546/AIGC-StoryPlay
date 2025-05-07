import os


def load_prompts(prompts_class):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建完整的文件路径
    if prompts_class=="act_game":
        file_path = os.path.join(current_dir, 'act_game_prompts.txt')
        with open(file_path, 'r', encoding='utf-8') as f:
            read_data = f.readlines()
            return read_data[0]
    elif prompts_class=="start":
        file_path = os.path.join(current_dir, 'start_prompts.txt')
        with open(file_path, 'r', encoding='utf-8') as f:
            read_data = f.readlines()
            return read_data[0]
    elif prompts_class=="images":
        file_path = os.path.join(current_dir, 'images_prompts.txt')
        with open(file_path, 'r', encoding='utf-8') as f:
            read_data = f.readlines()
            return read_data[0]
    elif prompts_class=="wuxia":
        file_path = os.path.join(current_dir, 'martial_arts_prompts.txt')
        with open(file_path, 'r', encoding='utf-8') as f:
            read_data = f.readlines()
            return read_data[0]
