import docx
import os


def read_docx(path, goal_path):
    file = docx.Document(path)  # Document对象

    paragraphs = file.paragraphs  # 段落对象

    with open('%s' % goal_path, 'a', encoding='utf-8') as f:
        for para in paragraphs:
            para_text = para.text
            f.write(para_text)


if __name__ == '__main__':
    # GAI歌词读取
    GAI_path = '歌词/GAI的原创歌词2.0.docx'
    GAI_goal_path = 'GAI_lyric.txt'
    read_docx(GAI_path, GAI_goal_path)

    # 汪峰歌词读取
    wf_fl_list = os.listdir('歌词/汪峰专辑歌词')
    for wf_fl in wf_fl_list:
        if wf_fl == '.DS_Store':
            pass
        else:
            wf_path = '歌词/汪峰专辑歌词/%s' % wf_fl
            wf_goal_path = 'wf_lyric.txt'
            read_docx(wf_path, wf_goal_path)

    # 李圣杰歌词读取
    lsj_fl_list = os.listdir('歌词/李圣杰歌词')
    for lsj_fl in lsj_fl_list:
        if lsj_fl == '.DS_Store':
            pass
        else:
            lsj_path = '歌词/李圣杰歌词/%s' % lsj_fl
            lsj_goal_path = 'lsj_lyric.txt'
            read_docx(lsj_path, lsj_goal_path)

    # 张韶涵歌词读取
    zsh_fl_list = os.listdir('歌词/张韶涵歌词')
    for zsh_fl in zsh_fl_list:
        if zsh_fl == '.DS_Store':
            pass
        else:
            zsh_path = '歌词/张韶涵歌词/%s' % zsh_fl
            zsh_goal_path = 'zsh_lyric.txt'
            read_docx(zsh_path, zsh_goal_path)