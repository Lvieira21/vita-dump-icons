# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/lucasvieira/Documents/Programação/PythonWorkspace/VitaIconDump'],
             binaries=[],
             datas=[('/Users/lucasvieira/.local/share/virtualenvs/VitaIconDump-Kjry_sym/lib/python3.8/site-packages/eel/eel.js', 'eel'), ('_view', '_view')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Vita Icon Downloader',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='/Users/lucasvieira/Documents/Programação/PythonWorkspace/VitaIconDump/_view/_icons/psv.icns')
app = BUNDLE(exe,
             name='Vita Icon Downloader.app',
             icon='/Users/lucasvieira/Documents/Programação/PythonWorkspace/VitaIconDump/_view/_icons/psv.icns',
             bundle_identifier=None)
