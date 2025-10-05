import os
import sys
import subprocess
from shutil import which
from pathlib import Path
import platform
import zipfile

def find_pyinstaller():
    """查找nuitka可执行文件的完整路径"""
    pyinstaller_path = which('pyinstaller')
    if pyinstaller_path:
        return [pyinstaller_path]
    return [sys.executable, '-m', 'pyinstaller']

def setup_build_directory():
    build_dir = Path('ling')
    try:
        build_dir.mkdir(exist_ok=True)
        # 确保将 ling_settings.json 复制到构建目录（若不存在则创建默认模板）
        try:
            cfg_src = Path('ling_settings.json')
            cfg_dst = build_dir / 'ling_settings.json'
            if cfg_src.exists():
                import shutil as _shutil
                _shutil.copy2(cfg_src, cfg_dst)
                print(f":: COPY OK : {cfg_src} -> {cfg_dst}")
            else:
                import json as _json
                cfg_dst.write_text(_json.dumps({"exe_path": "", "theme": "LIGHT"}, ensure_ascii=False, indent=2), encoding='utf-8')
                print(f":: CREATE DEFAULT : {cfg_dst}")
        except Exception as _e:
            print(f":: COPY ling_settings.json WARN: {_e}")
        
    except Exception as e:
        print(f"\n:: RESOURCE COPY ERROR: {str(e)}")
        if not os.getenv('CI'):  # CI环境中忽略资源错误
            sys.exit(1)

    # Create zip archive
    system = platform.system().lower()
    arch = platform.machine().lower()
    zip_filename = f"ling-{system}-{arch}.zip"
    
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in build_dir.rglob('*'):
                if file.is_file():
                    arcname = file.relative_to(build_dir.parent)
                    zipf.write(file, arcname)
        
        print(f"\n:: CREAT SUCCESS : {zip_filename}")
        return True
    
    except Exception as e:
        print(f"\n:: RESOURCE ZIP ERROR: {e}")
        return False

def build():
    pyinstaller_cmd = find_pyinstaller()
    
    # 基础编译参数
    base_args = [
        '-F',
        '-w', 
        '--icon=doc/logo.png',
        '--distpath=ling',
        '--add-data=doc/logo.png:doc',
        '--add-data=dark.qss:.',
        '--add-data=ling_settings.json:.',
    ]
    pyinstaller_cmd.extend(base_args)

    pyinstaller_cmd.append('ling.py')
    # 在CI环境中显示完整命令
    if os.getenv('CI'):
        print('\n:: PYINSTALLER COMMAND :', ' '.join(pyinstaller_cmd))
    
    try:
        subprocess.run(pyinstaller_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f'\n:: BUILD FAILED (CODE {e.returncode})')
        sys.exit(1)

if __name__ == '__main__':
    try:
        build()
        setup_build_directory()
        print("\n:: BUILD SUCCESS ::")
    except KeyboardInterrupt:
        print("\n:: BUILD INTERRUPTED ::")
        sys.exit(1)
