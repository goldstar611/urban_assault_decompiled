# -*- mode: python -*-

block_cipher = None


a = Analysis(['bastoolsgui3.py'],
             pathex=['.'],
             binaries=[],
             datas=[('QMainWin.ui', '.'),
                    ('1452462960_file.png', '.'),
                    ('1452464202_folder_empty.png', '.'),
                    ('1452464741_shoppingcart.png', '.'),
                    ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='bastoolsgui3',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
