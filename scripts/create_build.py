#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Amadeus Wizard - Build Generator
Creates the initial 'full' build ZIP file from the repository contents.
"""

import os
import shutil
import zipfile
import argparse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_DIR = os.path.join(REPO_ROOT, 'build_temp')
RELEASES_DIR = os.path.join(REPO_ROOT, 'releases')

def create_base_build(version='1.0.0'):
    """Create a base build ZIP containing critical addons and settings."""
    print(f'[INFO] Creating base build v{version}...')
    
    # 1. Prepare structure
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    
    addons_dir = os.path.join(BUILD_DIR, 'addons')
    userdata_dir = os.path.join(BUILD_DIR, 'userdata')
    os.makedirs(addons_dir)
    os.makedirs(userdata_dir)
    
    # 2. Copy Addons
    print('[INFO] Copying addons...')
    # Copy Wizard
    shutil.copytree(
        os.path.join(REPO_ROOT, 'plugin.program.amadeuswizard'),
        os.path.join(addons_dir, 'plugin.program.amadeuswizard'),
        ignore=shutil.ignore_patterns('*.pyc', '__pycache__', '.git*')
    )
    # Copy Repo
    shutil.copytree(
        os.path.join(REPO_ROOT, 'repository.amadeuswizard'),
        os.path.join(addons_dir, 'repository.amadeuswizard'),
        ignore=shutil.ignore_patterns('*.pyc', '__pycache__', '.git*')
    )
    
    # 3. Copy Userdata/Settings
    print('[INFO] Configuring userdata...')
    
    # Copy guisettings.xml
    src_gui = os.path.join(REPO_ROOT, 'plugin.program.amadeuswizard', 'guisettings', 'guisettings.xml')
    if os.path.exists(src_gui):
        shutil.copy(src_gui, os.path.join(userdata_dir, 'guisettings.xml'))
        
    # Copy advancedsettings.xml
    src_adv = os.path.join(REPO_ROOT, 'plugin.program.amadeuswizard', 'resources', 'advancedsettings.xml')
    if os.path.exists(src_adv):
        shutil.copy(src_adv, os.path.join(userdata_dir, 'advancedsettings.xml'))
        
    # 4. Zip it up
    os.makedirs(RELEASES_DIR, exist_ok=True)
    zip_name = f'israel-full-build-{version}.zip'
    zip_path = os.path.join(RELEASES_DIR, zip_name)
    
    print(f'[INFO] Zipping to {zip_name}...')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(BUILD_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                # Keep structure relative to BUILD_DIR (so zip starts with addons/ and userdata/)
                arcname = os.path.relpath(file_path, BUILD_DIR)
                zf.write(file_path, arcname)
                
    # Cleanup
    shutil.rmtree(BUILD_DIR)
    print(f'[OK] Build created: {zip_path}')
    return zip_path

if __name__ == '__main__':
    create_base_build()
