# sentence2pinyin

Python 包：将中文句子转换为拼音，支持多音字和 Ruby 注音格式（可用于 Anki）。

## 安装

```bash
pip install git+https://github.com/你的用户名/sentence2pinyin.git


使用示例
```python
from spinyin import SPinyin

sp = SPinyin()  # 默认音调符号
sentence = "海水淹没了城市"

# 普通拼音
print(sp.text(sentence))  
# hǎi shuǐ yān mò le chéng shì

# Ruby 注音
print(sp.ruby(sentence))  
# <ruby>海<rt>hǎi</rt></ruby><ruby>水<rt>shuǐ</rt></ruby>...

# 临时切换数字声调
print(sp.text(sentence, style='tone3'))  
# hai3 shui3 yan1 mo4 le cheng2 shi4
```


