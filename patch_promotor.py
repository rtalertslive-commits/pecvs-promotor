import sys
import os

path = r'C:\Users\Franco\.gemini\antigravity\scratch\pecvs-promotor\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Bitácora Panel
if 'id="tab-bitacora"' in content:
    import re
    # Match the entire div block for tab-bitacora
    # Since we don't know exactly the structure, we use a simple regex that finds the div start and looks for a balanced closer or just a large chunk
    # But wait, I know the line numbers roughly.
    lines = content.splitlines()
    new_lines = []
    skip = False
    for line in lines:
        if 'id="tab-bitacora"' in line:
            skip = True
            new_lines.append('        <!-- TAB BITACORA REMOVED -->')
            continue
        if skip and 'id="tab-leaderboard"' in line:
            skip = False
        if not skip:
            new_lines.append(line)
    content = '\n'.join(new_lines)

# 2. Remove Bitácora Log Modal
if 'id="modal-bitacora-log"' in content:
    lines = content.splitlines()
    new_lines = []
    skip = False
    for line in lines:
        if 'id="modal-bitacora-log"' in line:
            skip = True
            new_lines.append('    <div id="modal-bitacora-log" style="display:none"></div>')
            continue
        if skip and 'id="modal-reporte-log"' in line:
            skip = False
        if not skip:
            new_lines.append(line)
    content = '\n'.join(new_lines)

# 3. Final Header fix check
content = content.replace('PECVS$ Analytics', 'Promotor Hub')
content = content.replace('v1.3.6', 'v1.0.0')
content = content.replace('id="coach-display">Coach:', 'id="promotor-display">Promotor:')
content = content.replace('id="team-display"', 'id="promocode-display"')
content = content.replace('Equipo: Sin Código', 'Código: —')

# 4. Save Config Fix
content = content.replace('onclick="saveConfig()"', 'onclick="saveConfigPromotor()"')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleanup complete.")
