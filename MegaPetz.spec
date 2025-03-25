# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\\\MegaPetz\\\\View\\\\BackEnd\\\\Back_Principal.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\\\MegaPetz\\\\Model', 'Model'), ('C:\\\\MegaPetz\\\\View', 'View'), ('C:\\\\MegaPetz\\\\View\\\\FontEnd', 'View\\\\FontEnd'), ('C:\\\\MegaPetz\\\\View\\\\BackEnd', 'View\\\\BackEnd'), ('C:\\\\MegaPetz\\\\Controller', 'Controller'), ('C:\\\\MegaPetz\\\\UI', 'UI'), ('C:\\\\MegaPetz\\\\DataBase', 'DataBase'), ('C:\\\\MegaPetz\\\\Model\\\\DAO\\\\FuncoesAuxiliares', 'Model\\\\DAO\\\\FuncoesAuxiliares'), ('C:\\\\MegaPetz\\\\Model\\\\DAO\\\\FuncoesFormularios\\\\FuncoesFormAnimal', 'Model\\\\DAO\\\\FuncoesFormularios\\\\FuncoesFormAnimal'), ('C:\\\\MegaPetz\\\\Model\\\\DAO\\\\FuncoesFormularios\\\\FuncoesFormCliente', 'Model\\\\DAO\\\\FuncoesFormularios\\\\FuncoesFormCliente'), ('C:\\\\MegaPetz\\\\Model\\\\DAO\\\\FuncoesFormularios\\\\FuncoesFormServico', 'Model\\\\DAO\\\\FuncoesFormularios\\\\FuncoesFormServico'), ('C:\\\\MegaPetz\\\\Model\\\\DTO', 'Model\\\\DTO')],
    hiddenimports=['requests', 'sqlite3', 'cv2'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MegaPetz',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
