"""GitHub Pages에 올릴 화면 만들기: ../Index.html → index.html 복사  →  python build.py
이 web 폴더(index.html, manifest.json, sw.js, icon-*.png, .nojekyll)만 저장소에 올린다. 키·PIN은 넣지 않는다."""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
shutil.copyfile(os.path.join(HERE, '..', 'Index.html'), os.path.join(HERE, 'index.html'))
open(os.path.join(HERE, '.nojekyll'), 'w').close()
print('web/index.html 갱신 완료')
