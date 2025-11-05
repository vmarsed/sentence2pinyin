# spinyin/spinyin.py
"""
SPinyin 类
默认输出音调符号，可切换数字声调
支持普通拼音和 Ruby 注音（用于 Anki）
"""
import jieba
from pypinyin import pinyin, Style, load_phrases_dict
from pypinyin_dict.phrase_pinyin_data import cc_cedict

class SPinyin:
    def __init__(self, style='tone'):
        """
        style:
            'tone'  -> 音调符号，例如 hǎo
            'tone3' -> 数字声调，例如 hao3
        """
        self.style = Style.TONE if style=='tone' else Style.TONE3
        # 只加载一次词库
        cc_cedict.load()
    
    def text(self, sentence, style=None):
        """
        返回拼音字符串，用空格分隔
        style 可临时切换 'tone' 或 'tone3'
        """
        style_to_use = self.style if style is None else (Style.TONE if style=='tone' else Style.TONE3)
        words = jieba.lcut(sentence)
        result = []
        for word in words:
            pys = pinyin(word, style=style_to_use, heteronym=False)
            for char, py in zip(word, pys):
                result.append(py[0])
        return " ".join(result)
    
    def ruby(self, sentence, style=None):
        """
        返回带 <ruby> 注音字符串，用于 Anki
        style 可临时切换 'tone' 或 'tone3'
        """
        style_to_use = self.style if style is None else (Style.TONE if style=='tone' else Style.TONE3)
        words = list(sentence)
        pys = pinyin(words, style=style_to_use, heteronym=False)
        ruby_list = [f"<ruby>{char}<rt>{py[0]}</rt></ruby>" for char, py in zip(words, pys)]
        return "".join(ruby_list)
