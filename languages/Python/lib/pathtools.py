def get_path(relative_path: str) -> str:
    """通过将当前脚本的目录与提供的相对路径组合来获取绝对路径。
    Args:
        relative_path (str): 要与当前目录连接的文件名或相对路径
    Returns:
        str: 文件或目录的绝对路径
    """
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, relative_path)
